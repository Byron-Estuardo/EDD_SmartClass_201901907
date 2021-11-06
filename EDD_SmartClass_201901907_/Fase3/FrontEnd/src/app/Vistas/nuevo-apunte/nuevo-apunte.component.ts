import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nuevo-apunte',
  templateUrl: './nuevo-apunte.component.html',
  styleUrls: ['./nuevo-apunte.component.css']
})
export class NuevoApunteComponent implements OnInit {

  constructor() { }
  Titulo:string = '';
  Contenido:string = '';
  ngOnInit(): void {
  }

  Agregar(Titulo: any, Contenido: any){

    if (Titulo !== "" && Contenido !== ""){
      var data = JSON.stringify({
      "Titulo": Titulo,
      "Contenido": Contenido
      });
      fetch('http://localhost:3000/Cliente/NuevoApunte', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
      })
        .then(response => response.json())
        .then(data => {
        console.log(data)
        alert(data.response)
        this.LimpiarValores()
        });
    }
    else {
      alert('Uno de los campos se encuentra vacio')
    }
  }

  LimpiarValores(){
    this.Titulo = '';
    this.Contenido = '';
  }
}
