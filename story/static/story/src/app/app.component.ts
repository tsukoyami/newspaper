import { Component } from '@angular/core';
import { StoryService } from './story.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'story';
  constructor(private storyService: StoryService) { }

  logout() {
    this.storyService.redirectToLogout();
  }

  goToSource() {
    this.storyService.redirectToSource();
  }

  goToStory() {
    this.storyService.redirectToStory();
  }
}
