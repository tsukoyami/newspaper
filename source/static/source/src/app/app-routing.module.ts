import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SourceListComponent } from './source-list/source-list.component';
import { SourceFormComponent } from './source-form/source-form.component';

const routes: Routes = [
  { path: '', redirectTo: '/source', pathMatch: 'full' },
  { path: 'source', component: SourceListComponent },
  { path: 'create-source', component: SourceFormComponent },
  { path: 'edit-source/:id', component: SourceFormComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
