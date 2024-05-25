from django.db import IntegrityError
from django.test import TestCase
from .models import Story
from registereduser.models import RegisteredUser
from source.models import Source

class StoryTest(TestCase):
  """Tests for the Story model"""

  def test_create_story(self):
    """Tests creating a new Story object"""
    user = RegisteredUser.objects.create(
        username="test_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
            )
    source = Source.objects.create(
        source_user=user,
        source_name="Test Source",
        source_url="https://www.example.com/source",
    )
    story = Story.objects.create(
        created_by=user,
        source=source,
        title="Test Story Title",
        published_date="2023-05-26",  # Replace with a valid date
        body_text="This is a test story body.",
        url="https://www.example.com/story",
        tags="news,technology",
    )
    self.assertEqual(story.title, "Test Story Title")
    self.assertEqual(story.source.source_name, "Test Source")  # Check source association

  def test_unique_url_per_user(self):
    """Tests that a user cannot have duplicate stories with the same URL"""
    user = RegisteredUser.objects.create(
        username="test_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
    )
    story1 = Story.objects.create(
        created_by=user,
        title="Story 1",
        published_date="2023-05-26",  # Replace with a valid date
        body_text="This is story 1.",
        url="https://www.example.com/story",
        tags="news",
    )
    with self.assertRaises(IntegrityError):
        Story.objects.create(
            created_by=user,
            title="Story 2",
            published_date="2023-05-26",  # Replace with a valid date
            body_text="This is story 2.",
            url="https://www.example.com/story",  # Duplicate URL for user
            tags="science",
        )
