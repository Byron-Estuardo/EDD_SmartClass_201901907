import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  form: FormGroup | undefined;
  constructor() {

  }
  currentVal = "";
  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }
  ngOnInit(): void {
  }
  private buildForm(){
    this.form = new FormGroup({

      Carnet: new FormControl('', [Validators.required]),
      DPI: new FormControl('', [Validators.required]),
      Nombre: new FormControl('', [Validators.required]),
      Carrera: new FormControl('', [Validators.required]),
      Correo: new FormControl('', [Validators.required]),
      Password: new FormControl('', [Validators.required]),
      Edad: new FormControl('', [Validators.required])
    });
    this.form.valueChanges.subscribe(value => console.log(value))
  }

}
