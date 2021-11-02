import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerApuntesComponent } from './ver-apuntes.component';

describe('VerApuntesComponent', () => {
  let component: VerApuntesComponent;
  let fixture: ComponentFixture<VerApuntesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VerApuntesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VerApuntesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
