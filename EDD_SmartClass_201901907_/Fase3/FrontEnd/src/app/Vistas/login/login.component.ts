import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private title: Title) { }
  currentVal = "";
  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }
  Carnet1:string = '';
  Contra1:string = '';
  LimpiarValores(){
    this.Carnet1 = '';
    this.Contra1 = '';
  }
  ngOnInit(): void {
    this.title.setTitle('Registro');
  }

}
