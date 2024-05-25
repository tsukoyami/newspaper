import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StoryListComponent } from './story-list/story-list.component';
import { StoryFormComponent } from './story-form/story-form.component';
// import { AppComponent } from './app.component';

const routes: Routes = [
  { path: '', redirectTo: '/story', pathMatch: 'full' },
  { path: 'story', component: StoryListComponent },
  { path: 'create-story', component: StoryFormComponent },
  { path: 'edit-story/:id', component: StoryFormComponent },
  // { path: 'logout', component:  AppComponent},
  // { path: 'source', component: AppComponent },
  // { path: 'story', component: AppComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
