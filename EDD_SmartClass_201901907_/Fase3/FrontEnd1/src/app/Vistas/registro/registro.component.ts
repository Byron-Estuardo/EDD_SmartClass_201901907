import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

  constructor() { }
  currentVal = "";
  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }
  ngOnInit(): void {
  }

}
