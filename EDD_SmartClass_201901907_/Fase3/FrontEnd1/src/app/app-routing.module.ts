import { PaginaPrincipalComponent } from './Vistas/pagina-principal/pagina-principal.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegistroComponent } from './Vistas/registro/registro.component';

const routes: Routes = [
  {
    path: '',
    component: PaginaPrincipalComponent
  },
  {
    path: 'Registro',
    component: RegistroComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
