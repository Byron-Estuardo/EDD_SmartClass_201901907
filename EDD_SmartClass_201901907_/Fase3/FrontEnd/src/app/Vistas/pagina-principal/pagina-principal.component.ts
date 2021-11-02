import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pagina-principal',
  templateUrl: './pagina-principal.component.html',
  styleUrls: ['./pagina-principal.component.css']
})
export class PaginaPrincipalComponent implements OnInit {

  constructor(private title: Title, private router: Router) { }
  currentVal = "";
  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }

  RegistrarMasivoJson(ruta: any){
    console.warn(ruta)
    var data = JSON.stringify({
      "Ruta": ruta
    });

    fetch('http://localhost:3000/Administrador/MasivaEstudiantesJson', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data
    })

      .then(response => response.json())
      .then(data => {
        alert(data.response)
      });

  }

    RegistrarMasivoTxt(ruta: any){
      console.warn(ruta)

        var data = JSON.stringify({
          "Ruta": ruta
        });

        fetch('http://localhost:3000/Administrador/MasivaEstudiantesTxt', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: data
        })

          .then(response => response.json())
          .then(data => {
            console.log(data)
            //if (data.Ingreso === true){
              //this.router.navigate(['/Administrador']);
            //}
            //else{
             // alert(data.response)
            //}

            //alert(data.response)
        });

      }

    RegistrarMasivoJsonApuntes(ruta: any){
      console.warn(ruta)
      var data = JSON.stringify({
        "Ruta": ruta
      });

      fetch('http://localhost:3000/Administrador/MasivoApuntes', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: data
      })

      .then(response => response.json())
      .then(data => {
        alert(data.response)
      });

  }

  Ruta:string = '';
  DPI1:string = '';
  Nombre1:string = '';
  Carrera1:string = '';
  Correo1:string = '';
  Contra1:string = '';
  Edad1:string = '';
  LimpiarValores(){
    this.Ruta = '';
    this.DPI1 = '';
    this.Nombre1 = '';
    this.Carrera1 = '';
    this.Contra1 = '';
    this.Edad1 = '';
    this.Correo1 = '';
  }
  ngOnInit(): void {
    this.title.setTitle('Administrador');
  }
  code = '';
  array = [];
  texto="";
  lista = [];
  abrir(eve:any)
  {
    let a =eve.target.files[0]
    console.warn(a)

    let text=""
    if(a){
      console.log(a.name)
      this.RegistrarMasivoJson(a.name)
    }
  }

  abrir1(eve:any)
  {
    let a =eve.target.files[0]
    console.warn(a)

    let text=""
    if(a){
      console.log(a.name)
      this.RegistrarMasivoJsonApuntes(a.name)
    }
  }
}
