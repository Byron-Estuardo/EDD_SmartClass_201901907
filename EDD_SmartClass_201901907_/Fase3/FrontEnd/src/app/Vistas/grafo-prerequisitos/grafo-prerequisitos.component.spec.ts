import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GrafoPrerequisitosComponent } from './grafo-prerequisitos.component';

describe('GrafoPrerequisitosComponent', () => {
  let component: GrafoPrerequisitosComponent;
  let fixture: ComponentFixture<GrafoPrerequisitosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GrafoPrerequisitosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GrafoPrerequisitosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
