import { LoginComponent } from './Vistas/login/login.component';
import { ModuleWithProviders, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PaginaPrincipalComponent } from './Vistas/pagina-principal/pagina-principal.component';
import { RegistroComponent } from './Vistas/registro/registro.component';

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

];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {  }
