
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatChipsModule } from '@angular/material/chips';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';

import { SourceListComponent } from './source-list/source-list.component';
import { SourceFormComponent } from './source-form/source-form.component';
import { SourceSearchComponent } from './source-search/source-search.component';

import { SourceService } from './source.service';

@NgModule({
  declarations: [
    AppComponent,
    SourceListComponent,
    SourceFormComponent,
    SourceSearchComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatChipsModule,
    MatAutocompleteModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule,
  ],
  providers: [
    provideAnimationsAsync(),
    SourceService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
