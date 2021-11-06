import { VerApuntesComponent } from './Vistas/ver-apuntes/ver-apuntes.component';
import { NuevoApunteComponent } from './Vistas/nuevo-apunte/nuevo-apunte.component';
import { GrafoPrerequisitosComponent } from './Vistas/grafo-prerequisitos/grafo-prerequisitos.component';
import { EstudianteVComponent } from './Vistas/estudiante-v/estudiante-v.component';
import { ReportesComponent } from './Vistas/reportes/reportes.component';
import { LoginComponent } from './Vistas/login/login.component';
import { ModuleWithProviders, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PaginaPrincipalComponent } from './Vistas/pagina-principal/pagina-principal.component';
import { RegistroComponent } from './Vistas/registro/registro.component';
import { ReportesCursosComponent } from './Vistas/reportes-cursos/reportes-cursos.component';

export const routes: Routes = [

  {
    path: '',
    component: LoginComponent
  },
  {
    path: 'Administrador',
    component: PaginaPrincipalComponent
  },
  {
    path: 'Registro',
    component: RegistroComponent
  },
  {
    path: 'Reportes',
    component: ReportesComponent
  },
  {
    path: 'Cliente',
    component: EstudianteVComponent
  },
  {
    path: 'GrafoPre',
    component: GrafoPrerequisitosComponent
  },
  {
    path: 'nuevoApunte',
    component: NuevoApunteComponent
  },
  {
    path: 'verApuntes',
    component: VerApuntesComponent
  },
  {
    path: 'ReporteCursos',
    component: ReportesCursosComponent
  },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {  }
