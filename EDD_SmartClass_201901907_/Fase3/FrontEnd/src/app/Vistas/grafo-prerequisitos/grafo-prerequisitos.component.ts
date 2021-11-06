import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-grafo-prerequisitos',
  templateUrl: './grafo-prerequisitos.component.html',
  styleUrls: ['./grafo-prerequisitos.component.css']
})
export class GrafoPrerequisitosComponent implements OnInit {

  constructor() { }

  year:string = '';
  semestre:string ='';
  codigo: string = '';

  ngOnInit(): void {
  }

  Agregar(codigo:any, year: any, semestre: any){

    if (year !== "" && semestre !== "" && codigo != ""){
      var data = JSON.stringify({
      "Year": year,
      "Semestre": semestre,
      "Codigo": codigo
      });
      fetch('http://localhost:3000/Cliente/AgregarCursoManual', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
      })
      .then(response => response.json())
      .then(data => {

        if(data.response == 'El Curso No se Encuentra en el Pensum'){
          alert(data.response)
          this.codigo = '';
        }
        else if (data.response == 'Curso Agregado con Exito'){
          alert(data.response)
          this.LimpiarValores()
        }


      });
    }
    else {
      alert('Uno de los campos se encuentra vacio')
    }
  }


  Grafico(codigo:any){

    if (codigo != ""){
      var data = JSON.stringify({
        "Codigo": codigo
      });
      fetch('http://localhost:3000/Cliente/GraficoPre', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
      })
      .then(response => response.json())
      .then(data => {

        if(data.response == 'El Codigo no Existe en el Pensum Actual'){
          alert(data.response)
          this.codigo = '';
        }
        else if (data.response == 'Grafo Realizado Con Exito'){
          alert(data.response)
          var img:any
          (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+data.Imagen+"\">"
          console.log(data.Imagen)
          this.LimpiarValores()
        }


      });
    }
    else {
      alert('Uno de los campos se encuentra vacio')
    }
  }

  LimpiarValores(){
    this.codigo = '';
    this.semestre = '';
    this.year = '';
  }

}
