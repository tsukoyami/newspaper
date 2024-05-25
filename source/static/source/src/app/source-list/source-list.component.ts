import { Component, OnInit } from '@angular/core';
import { SourceService, Source } from '../source.service';
import { Observable, of } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-source-list',
  templateUrl: './source-list.component.html',
  styleUrls: ['./source-list.component.css']
})
export class SourceListComponent implements OnInit {
  [x: string]: any;
  isFormDisplayed = false;
  sources!: Observable<Source[]>;

  constructor(private sourceService: SourceService, private router: Router) { }

  ngOnInit(): void {
    this.loadSources();
  }

  loadSources(): void {
    this.sources = this.sourceService.getSources();
  }

  editSource(id: number): void {
    this.router.navigate(['/edit-source', id]);
  }

  deleteSource(id: number): void {
    this.sourceService.deleteSource(id).subscribe(() => this.loadSources());
  }

  fetchStories(id: number): void {
    this.sourceService.fetchStories(id).subscribe(() => this.loadSources());
  }

  viewStories(id: number): void {
    // Logic to navigate to the stories view
  }

  filterByTag(tag: string): void {
    this.sourceService.filterSourcesByTag(tag).subscribe(filteredSources => this.sources = of(filteredSources));
  }

  applyFilter(filterValue: string): void {
    this.sourceService.searchSources(filterValue).subscribe(filteredSources => this.sources = of(filteredSources));
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
