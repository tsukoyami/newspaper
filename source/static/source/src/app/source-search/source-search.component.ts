import { Component, EventEmitter, Output } from '@angular/core';
import { SourceService } from '../source.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-source-search',
  templateUrl: './source-search.component.html',
  styleUrls: ['./source-search.component.css']
})
export class SourceSearchComponent {
  searchTerm: string = '';
  filteredOptions: string[] = [];
  @Output() search = new EventEmitter<string>();

  constructor(private sourceService: SourceService) { }

  onSearch(): void {
    if (this.searchTerm) {
      this.sourceService.searchSources(this.searchTerm).pipe(
        map(sources => sources.filter(source =>
          source.source_name.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          source.source_url.toLowerCase().includes(this.searchTerm.toLowerCase())
        ))
      ).subscribe(filteredSources => {
        this.filteredOptions = filteredSources.map(source => source.source_name);
        this.search.emit(this.searchTerm);
      });
    } else {
      this.filteredOptions = [];
      this.search.emit('');
    }
  }
}
