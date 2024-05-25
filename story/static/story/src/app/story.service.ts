// src/app/story.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Router } from '@angular/router';
// Define an interface for your story data
export interface Story {
  id: number;
  created_by: number;
  source: number;
  title: string;
  published_date: string;
  body_text: string;
  url: string;
  tags: string;
}

@Injectable({
  providedIn: 'root'
})
export class StoryService {
  getTags() {
    throw new Error('Method not implemented.');
  }
  constructor(private http: HttpClient, private router: Router) { }

  private baseUrl = 'http://127.0.0.1:8000/api/story/';
  private searchUrl = 'http://127.0.0.1:8000/api/search_story/';
  private filterUrl = 'http://127.0.0.1:8000/api/filter_story/';



  // Get all stories
  getStories(): Observable<Story[]> {
    return this.http.get<Story[]>(this.baseUrl)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Get a specific story by ID
  getStory(id: number): Observable<Story> {
    const url = `${this.baseUrl}${id}/`;
    return this.http.get<Story>(url)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Create a new story
  createStory(story: Story): Observable<Story> {
    return this.http.post<Story>(this.baseUrl, story)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Update an existing story
  updateStory(story: Story): Observable<Story> {
    const url = `${this.baseUrl}${story.id}/`;
    return this.http.put<Story>(url, story)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Delete a story
  deleteStory(id: number): Observable<{}> {
    const url = `${this.baseUrl}${id}/`;
    return this.http.delete(url)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Search sources by name or URL
  searchStories(query: string): Observable<Story[]> {
    const params = new HttpParams().set('q', query);
    return this.http.get<Story[]>(this.searchUrl, { params })
      .pipe(
        catchError(this.handleError)
      );
  }

  // Filter sources by tag
  filterStoriesByTag(tag: string): Observable<Story[]> {
    const params = new HttpParams().set('tag', tag);
    return this.http.get<Story[]>(this.filterUrl, { params })
      .pipe(
        catchError(this.handleError)
      );
  }

  redirectToLogout() {
    window.location.href = 'http://127.0.0.1:8000/logout/';
  }

  redirectToSource() {
    window.location.href = 'http://127.0.0.1:8000/source/';
  }

  redirectToStory() {
    window.location.href = 'http://127.0.0.1:8000/story/';
  }

  // Error handling function
  private handleError(error: any) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Client-side or network error occurred. Handle it accordingly.
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // Backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(errorMessage);
  }
}
