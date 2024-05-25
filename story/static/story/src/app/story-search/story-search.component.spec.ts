import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StorySearchComponent } from './story-search.component';

describe('StorySearchComponent', () => {
  let component: StorySearchComponent;
  let fixture: ComponentFixture<StorySearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StorySearchComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(StorySearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
