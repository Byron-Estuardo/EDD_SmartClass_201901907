import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EstudianteVComponent } from './estudiante-v.component';

describe('EstudianteVComponent', () => {
  let component: EstudianteVComponent;
  let fixture: ComponentFixture<EstudianteVComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EstudianteVComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EstudianteVComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
