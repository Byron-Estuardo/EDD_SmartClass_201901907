import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

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
  Correo1: string= '';
  Edad1:string = '';
  LimpiarValores(){
    this.Carnet1 = '';
    this.DPI1 = '';
    this.Nombre1 = '';
    this.Carrera1 = '';
    this.Contra1 = '';
    this.Edad1 = '';
    this.Correo1 = '';
  }
  Registrar(Carnet: any, dpi: any, nombre: any, carrera: any, correo: any ,contra: any, Edad: any){
    console.warn(Carnet+ ' '+ dpi+ ' '+ nombre+ ' '+ carrera+ ' '+ contra+ ' '+Edad)
    if (Carnet !== "" && dpi !== "" && nombre !== "" && carrera !== "" && correo !== "" && contra !== "" && Edad !== ""){
      var data = JSON.stringify({
      "Carnet": Carnet,
      "DPI": dpi,
      "Nombre": nombre,
      "Carrera": carrera,
      "Correo": correo,
      "Contra": contra,
      "Edad": Edad
      });
      fetch('http://localhost:3000/Registro', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
      })
        .then(response => response.json())
        .then(data => {
        console.log(data)
        if (data.Existe === true){
          alert('El usuario Con el carnet "' + this.Carnet1 + '" Ya se encuentra registrado')
          this.LimpiarValores()
        }
        else{
          alert('Usuario registrado con Exito')
          this.LimpiarValores()
        }
        //alert(data.response)
        });
    }
    else {
      alert('Uno de los campos se encuentra vacio')
    }
  }
  ngOnInit(): void {
    this.title.setTitle('Registro');
  }

}
