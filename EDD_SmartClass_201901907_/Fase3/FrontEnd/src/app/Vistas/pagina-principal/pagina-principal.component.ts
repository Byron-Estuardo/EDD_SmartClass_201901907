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
  Ruta:string = '';
  DPI1:string = '';
  Nombre1:string = '';
  Carrera1:string = '';
  Contra1:string = '';
  Edad1:string = '';
  LimpiarValores(){
    this.Ruta = '';
    this.DPI1 = '';
    this.Nombre1 = '';
    this.Carrera1 = '';
    this.Contra1 = '';
    this.Edad1 = '';
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
    console.log(a.name)
    let text=""
    if(a){
      /*
      let reader=new FileReader()
        reader.onload=ev=>{
        const resultado=ev.target?.result
        text=String(resultado)
        var data = JSON.parse(text);
        //data.nombre.forEach(elems => this.array.push(elems));

        this.array.forEach(el => this.lista.push(el)) // para ingresar los datos
        this.code=text.toString();

      }

      reader.readAsText(a)
      */
    }
  }
}
