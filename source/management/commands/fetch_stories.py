
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
import feedparser
from datetime import datetime
from source.models import Source
from story.models import Story

class Command(BaseCommand):
    help = 'Fetch stories from a specific RSS feed source'

    def add_arguments(self, parser):
        parser.add_argument('source_id', type=int)

    def handle(self, *args, **options):
        source_id = options['source_id']
        # Fetch the source based on the provided source ID
        try:
            source = Source.objects.get(id=source_id)
        except Source.DoesNotExist:
            self.stdout.write(self.style.ERROR('Source does not exist'))
            return

        feed = feedparser.parse(source.source_url)
        new_stories_count = 0
        for entry in feed.entries:
            try:
                if not Story.objects.filter(url=entry.link).exists():
                    if all(field in entry and entry[field] for field in ['title', 'published', 'summary', 'link']):
                        datetime_formats = [
                            '%a, %d %b %Y %H:%M:%S %z',
                            '%Y-%m-%dT%H:%M:%S%z',
                            '%a, %d %b %Y %H:%M:%S %z',
                            '%Y-%m-%dT%H:%M:%S%z',
                            '%Y-%m-%dT%H:%M:%SZ',
                            '%a, %d %b %Y %H:%M:%S %Z',
                            '%Y-%m-%d %H:%M:%S',
                            '%Y-%m-%d %H:%M:%S.%f',
                        ]
                        published_date = None
                        for fmt in datetime_formats:
                            try:
                                published_date = datetime.strptime(entry.published, fmt)
                                break
                            except ValueError:
                                pass
                        
                        if published_date is None:
                            raise ValueError('Failed to parse datetime')

                        story = Story(
                            title=entry.title[:500],
                            published_date=published_date,
                            body_text=entry.summary[:2000],
                            url=entry.link[:200],
                            source=source,
                            tags=source.tags,
                            created_by=source.source_user,
                        )
                        story.full_clean()
                        story.save()
                        new_stories_count += 1
                        self.stdout.write(self.style.SUCCESS(f'Successfully created story: {story}'))
                    else:
                        self.stdout.write(self.style.WARNING('Missing or empty fields in RSS entry, skipping story creation'))
                else:
                    self.stdout.write(self.style.WARNING('Story with this URL already exists, skipping story creation'))
            except ValidationError as e:
                self.stdout.write(self.style.WARNING(f'Validation error: {e}'))
            except ValueError as e:
                self.stdout.write(self.style.WARNING(f'Failed to parse datetime: {e}'))
        # Update the story count in the source model
        source.story_count += new_stories_count
        source.save()
        self.stdout.write(self.style.SUCCESS(f'Updated story count for source: {source.source_name}'))