import { RegistroComponent } from './../registro/registro.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reportes-cursos',
  templateUrl: './reportes-cursos.component.html',
  styleUrls: ['./reportes-cursos.component.css']
})
export class ReportesCursosComponent implements OnInit {

  constructor() { }
  year:string = '';
  semestre:string = '';
  ngOnInit(): void {
  }

  Agregar(year: any, semestre: any){

    if (year !== "" && semestre !== ""){
      var data = JSON.stringify({
      "Year": year,
      "Semestre": semestre
      });
      fetch('http://localhost:3000/Cliente/ReporteCursos', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
      })
      .then(response => response.json())
      .then(data => {

        if(data.response == 'El semestre no Existe'){
          alert(data.response)
          this.semestre = '';
        }
        else if (data.response == 'El Año no existe'){
          alert(data.response)
          this.year = '';
        }
        else if (data.response == 'Grafica Realizada'){
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
    this.year = '';
    this.semestre = '';
  }
}
