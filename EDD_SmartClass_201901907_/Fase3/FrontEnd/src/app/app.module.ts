import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegistroComponent } from './Vistas/registro/registro.component';
import { PaginaPrincipalComponent } from './Vistas/pagina-principal/pagina-principal.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './Vistas/login/login.component';
import { ReportesComponent } from './Vistas/reportes/reportes.component';
import { EstudianteVComponent } from './Vistas/estudiante-v/estudiante-v.component';
import { NuevoApunteComponent } from './Vistas/nuevo-apunte/nuevo-apunte.component';
import { VerApuntesComponent } from './Vistas/ver-apuntes/ver-apuntes.component';
import { GrafoPrerequisitosComponent } from './Vistas/grafo-prerequisitos/grafo-prerequisitos.component';
import { ReportesCursosComponent } from './Vistas/reportes-cursos/reportes-cursos.component';

@NgModule({
  declarations: [
    AppComponent,
    RegistroComponent,
    PaginaPrincipalComponent,
    LoginComponent,
    ReportesComponent,
    EstudianteVComponent,
    NuevoApunteComponent,
    VerApuntesComponent,
    GrafoPrerequisitosComponent,
    ReportesCursosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
