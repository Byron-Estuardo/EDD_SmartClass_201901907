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
            console.log(data)
          alert(data.response)
          var img:any = data.img
          (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+img+"\">"
          console.log(img)
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
          alert(data.response)
          var img:any = data.img
          (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+img+"\">"
          console.log(img)
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
            alert(data.response)
            var img:any = data.img
            (<HTMLInputElement>document.getElementById("img")).innerHTML = "<img src=\"data:image/png;base64,"+img+"\">"
            console.log(img)
          });
        }
}
