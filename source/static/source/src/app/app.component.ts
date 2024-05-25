import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SourceService } from './source.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'source';

  constructor(private sourceService: SourceService) { }

  logout() {
    this.sourceService.redirectToLogout();
  }

  goToSource() {
    this.sourceService.redirectToSource();
  }

  goToStory() {
    this.sourceService.redirectToStory();
  }
}
