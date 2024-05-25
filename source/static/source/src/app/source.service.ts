import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// Define an interface for your source data (optional but improves type safety)
export interface Source {
  id: number;
  source_user: number;
  source_name: string;
  source_url: string;
  story_count: number;
  tags: string;
}

@Injectable({
  providedIn: 'root'
})
export class SourceService {

  constructor(private http: HttpClient) { }

  private baseUrl = 'http://127.0.0.1:8000/api/source/';
  private searchUrl = 'http://127.0.0.1:8000/api/search/';
  private filterUrl = 'http://127.0.0.1:8000/api/filter/';

  // Get all sources
  getSources(): Observable<Source[]> {
    return this.http.get<Source[]>(this.baseUrl)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Get a specific source by ID
  getSource(id: number): Observable<Source> {
    const url = `${this.baseUrl}${id}`;
    return this.http.get<Source>(url)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Create a new source
  createSource(source: Source): Observable<Source> {
    return this.http.post<Source>(this.baseUrl, source)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Update an existing source
  updateSource(source: Source): Observable<Source> {
    const url = `${this.baseUrl}${source.id}`;
    return this.http.put<Source>(url, source)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Delete a source
  deleteSource(id: number): Observable<{}> {
    const url = `${this.baseUrl}${id}`;
    return this.http.delete(url)
      .pipe(
        catchError(this.handleError)
      );
  }


  fetchStories(sourceId: number): Observable<any> {
    const url = `http://127.0.0.1:8000/api/fetch-stories/${sourceId}/`;
    return this.http.post(url, {})
      .pipe(
        catchError(this.handleError)
      );
  }


  // Search sources by name or URL
  searchSources(query: string): Observable<Source[]> {
    const params = new HttpParams().set('q', query);
    return this.http.get<Source[]>(this.searchUrl, { params })
      .pipe(
        catchError(this.handleError)
      );
  }

  // Filter sources by tag
  filterSourcesByTag(tag: string): Observable<Source[]> {
    const params = new HttpParams().set('tag', tag);
    return this.http.get<Source[]>(this.filterUrl, { params })
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
      errorMessage = `Error: ${error.error.message}`;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(errorMessage);
  }
}
