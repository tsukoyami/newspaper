import { Component, OnInit } from '@angular/core';
import { StoryService, Story } from '../story.service';
import { Observable, map, of } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-story-list',
  templateUrl: './story-list.component.html',
  styleUrl: './story-list.component.css'
})
export class StoryListComponent implements OnInit {
  [x: string]: any;
  isFormDisplayed = false;
  stories!: Observable<Story[]>;

  constructor(private storyService: StoryService, private router: Router) { }

  ngOnInit(): void {
    this.loadStories();
  }

  loadStories(): void{
    this.stories = this.storyService.getStories().pipe(
      map(stories => stories.sort((a, b) => new Date(b.published_date).getTime() - new Date(a.published_date).getTime()))
    );
  }

  editStory(id: number):void {
    this.router.navigate(['/edit-story', id]);
  }

  deleteStory(id: number): void {
    this.storyService.deleteStory(id).subscribe(() => this.loadStories());
  }

  filterByTag(tag: string): void {
    this.storyService.filterStoriesByTag(tag).subscribe(filteredStories => this.stories = of(filteredStories));
  }

  applyFilter(filterValue: string): void {
    this.storyService.searchStories(filterValue).subscribe(filteredStories => this.stories = of(filteredStories));
  }
  toggleFormDisplay() {
    this.isFormDisplayed = !this.isFormDisplayed;
    if (this.isFormDisplayed) {
      document.body.classList.add('blur-background');
    } else {
      document.body.classList.remove('blur-background');
    }
  }

}
