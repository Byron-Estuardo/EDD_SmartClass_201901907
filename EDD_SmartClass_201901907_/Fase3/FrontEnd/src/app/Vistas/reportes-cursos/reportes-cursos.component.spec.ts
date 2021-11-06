import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReportesCursosComponent } from './reportes-cursos.component';

describe('ReportesCursosComponent', () => {
  let component: ReportesCursosComponent;
  let fixture: ComponentFixture<ReportesCursosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReportesCursosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReportesCursosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
