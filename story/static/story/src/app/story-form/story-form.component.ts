import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { StoryService, Story } from '../story.service';
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'app-story-form',
  templateUrl: './story-form.component.html',
  styleUrl: './story-form.component.css',
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
export class StoryFormComponent implements OnInit{
  isFormDisplayed = false;
  story: Story = {
    id: 0,
    created_by: 0,
    source: 0,
    title: '',
    published_date: '',
    body_text: '',
    url: '',
    tags: '',
  };
  isEditMode = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private storyService: StoryService
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if (id) {
      this.isEditMode = true;
      this.storyService.getStory(id).subscribe(story => this.story = story);
    }
  }
  onSubmit(): void {
    if (this.isEditMode) {
      this.storyService.updateStory(this.story).subscribe(() => this.router.navigate(['/story']));
    } else {
      this.storyService.createStory(this.story).subscribe(() => this.router.navigate(['/story']));
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