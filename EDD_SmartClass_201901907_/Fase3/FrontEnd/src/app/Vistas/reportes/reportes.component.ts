import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.css']
})
export class ReportesComponent implements OnInit {

  constructor(private title: Title) { }

  ngOnInit(): void {
  }
  graficar(){
    fetch('http://localhost:3000/Administrador/GraficoAvlEncriptado', {
        method: 'get',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => response.json())
        .then(data => {
          alert(data.response)
          var img:any
          (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+data.Imagen+"\">"
          console.log(data.Imagen)

        });
      }
    graficar2(){
    fetch('http://localhost:3000/Administrador/GraficoAvl', {
        method: 'get',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            console.log(data.Imagen)
            var img:any
            (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+data.Imagen+"\">"
            alert(data.response)
        });
    }
    graficar3(){
      fetch('http://localhost:3000/Administrador/GraficoApuntes', {
          method: 'get',
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(data => {
              console.log(data)
              console.log(data.Imagen)
              var img:any
              (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+data.Imagen+"\">"
              alert(data.response)
          });
        }
        graficar4(){
          fetch('http://localhost:3000/Administrador/GraficoGrafoPensum', {
              method: 'get',
              headers: {
                'Content-Type': 'application/json'
              }
            })
              .then(response => response.json())
              .then(data => {
                alert(data.response)
                var img:any
                (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+data.Imagen+"\">"
                console.log(data.Imagen)

              });
            }
}
