import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateSignersComponent } from './update-signers.component';

describe('UpdateSignersComponent', () => {
  let component: UpdateSignersComponent;
  let fixture: ComponentFixture<UpdateSignersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UpdateSignersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UpdateSignersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
