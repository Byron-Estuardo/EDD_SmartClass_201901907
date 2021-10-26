import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegistroComponent } from './Vistas/registro/registro.component';
import { PaginaPrincipalComponent } from './Vistas/pagina-principal/pagina-principal.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './Vistas/login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    RegistroComponent,
    PaginaPrincipalComponent,
    LoginComponent
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
