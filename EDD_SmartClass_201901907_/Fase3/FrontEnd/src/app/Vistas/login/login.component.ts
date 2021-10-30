import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private title: Title, private router: Router) { }
  currentVal = "";

  agregar(usuario: any, contra: any){
    console.warn(usuario + ' ' + contra)
    if (usuario === "admin" && contra === "admin"){
      this.router.navigate(['/Administrador']);
    } else {
      var data = JSON.stringify({
        "Usuario": usuario,
        "Contra": contra
      });

      fetch('http://localhost:3000/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: data
      })
        .then(response => response.json())
        .then(data => {
          console.log(data)
          if (data.Ingreso === true){
            this.router.navigate(['/Administrador']);
          }
          else{
            if (data.Error === 'La contraseña es incorrecta'){
              alert(data.Error);
              this.Contra1 = '';
            }
            else{
              alert(data.Error);
              this.LimpiarValores();
            }

          }
          //alert(data.response)
      });
    }

  }

  getValue(val: any){
    console.warn(val)
    this.currentVal = val
  }
  Carnet1:string = '';
  Contra1:string = '';
  LimpiarValores(){
    this.Carnet1 = '';
    this.Contra1 = '';
  }
  ngOnInit(): void {
    this.title.setTitle('Registro');
  }

}
