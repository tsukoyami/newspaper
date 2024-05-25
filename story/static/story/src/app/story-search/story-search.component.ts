import { Component, EventEmitter, Output } from '@angular/core';
import { StoryService } from '../story.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-story-search',
  templateUrl: './story-search.component.html',
  styleUrl: './story-search.component.css'
})
export class StorySearchComponent {
  searchTerm: string = '';
  filteredOptions: string[] = [];
  @Output() search = new EventEmitter<string>();

  constructor(private storyService: StoryService) { }

  onSearch(): void {
    if (this.searchTerm) {
      this.storyService.searchStories(this.searchTerm).pipe(
        map(stories => stories.filter(story =>
          story.title.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          story.url.toLowerCase().includes(this.searchTerm.toLowerCase())
        ))
      ).subscribe(filteredStories => {
        this.filteredOptions = filteredStories.map(story => story.title);
        this.search.emit(this.searchTerm);
      });
    } else {
      this.filteredOptions = [];
      this.search.emit('');
    }
  }
}
