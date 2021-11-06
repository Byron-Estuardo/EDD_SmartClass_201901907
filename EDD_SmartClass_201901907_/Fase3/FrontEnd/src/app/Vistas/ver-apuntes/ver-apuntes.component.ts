import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ver-apuntes',
  templateUrl: './ver-apuntes.component.html',
  styleUrls: ['./ver-apuntes.component.css']
})
export class VerApuntesComponent implements OnInit {
apuntes: any
  CargarApuntes(){
    var data = JSON.stringify({
      "Ruta": "Hola"
    });

    fetch('http://localhost:3000/Cliente/VerApuntes', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
    })

    .then(response => response.json())
    .then(data => {
      if(data.Resresponse != "False"){
        this.apuntes = data
        console.log(this.apuntes)
      }
    });

}

  constructor() { }

  ngOnInit(): void {
    this.CargarApuntes();
  }

}
