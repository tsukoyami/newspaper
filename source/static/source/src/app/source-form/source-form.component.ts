import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { SourceService, Source } from '../source.service';
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'app-source-form',
  templateUrl: './source-form.component.html',
  styleUrls: ['./source-form.component.css'],
  animations: [
    trigger('formAnimation', [
      state('void', style({
        opacity: 0,
        transform: 'scale(0.8)'
      })),
      transition('void => *', [
        animate('300ms ease-out')
      ])
    ])
  ]
})
export class SourceFormComponent implements OnInit {
  isFormDisplayed = false;
  source: Source = {
    id: 0,
    source_user: 1,
    source_name: '',
    source_url: '',
    story_count: 22,
    tags: ''
  };
  isEditMode = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private sourceService: SourceService
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if (id) {
      this.isEditMode = true;
      this.sourceService.getSource(id).subscribe(source => this.source = source);
    }
  }

  onSubmit(): void {
    if (this.isEditMode) {
      this.sourceService.updateSource(this.source).subscribe(() => this.router.navigate(['/source']));
    } else {
      this.sourceService.createSource(this.source).subscribe(() => this.router.navigate(['/source']));
    }
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
