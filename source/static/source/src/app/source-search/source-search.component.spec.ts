import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SourceSearchComponent } from './source-search.component';

describe('SourceSearchComponent', () => {
  let component: SourceSearchComponent;
  let fixture: ComponentFixture<SourceSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SourceSearchComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SourceSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
