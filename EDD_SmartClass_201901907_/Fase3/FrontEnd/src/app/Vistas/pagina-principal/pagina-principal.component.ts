import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-pagina-principal',
  templateUrl: './pagina-principal.component.html',
  styleUrls: ['./pagina-principal.component.css']
})
export class PaginaPrincipalComponent implements OnInit {

  constructor(private title: Title) { }
  currentVal = "";
  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }
  Carnet1:string = '';
  DPI1:string = '';
  Nombre1:string = '';
  Carrera1:string = '';
  Contra1:string = '';
  Edad1:string = '';
  LimpiarValores(){
    this.Carnet1 = '';
    this.DPI1 = '';
    this.Nombre1 = '';
    this.Carrera1 = '';
    this.Contra1 = '';
    this.Edad1 = '';
  }
  ngOnInit(): void {
    this.title.setTitle('Registro');
  }

}
