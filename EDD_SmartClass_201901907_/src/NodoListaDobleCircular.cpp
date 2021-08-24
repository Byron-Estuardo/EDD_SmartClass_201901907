#include "NodoListaDobleCircular.h"
#include <string>

NodoListaDobleCircular::NodoListaDobleCircular(){
	this->carnet = "";
	this->dpi = "";
	this->nombre = "";
	this->carrera = "";
	this->contra = "";
	this->correo = "";
	this->creditos = 0;
	this->edad = 0;
	this->siguiente = NULL;
	this->anterior = NULL;
}

NodoListaDobleCircular::NodoListaDobleCircular(string carnet_, string dpi_, string nombre_, string carrera_, string contra_, int creditos_, int edad_, string correo_){
	this->carnet = carnet_;
	this->dpi = dpi_;
	this->nombre = nombre_;
	this->carrera = carrera_;
	this->contra = contra_;
	this->creditos = creditos_;
	this->correo = correo_;
	this->edad = edad_;
	this->siguiente = 0;
	this->anterior = 0;
}

NodoListaDobleCircular::NodoListaDobleCircular(string carnet_, string dpi_, string nombre_, string carrera_, string contra_, int creditos_, int edad_, string correo_, NodoListaDobleCircular *siguiente_, NodoListaDobleCircular *anterior_){
	this->carnet = carnet_;
	this->dpi = dpi_;
	this->nombre = nombre_;
	this->carrera = carrera_;
	this->contra = contra_;
	this->creditos = creditos_;
	this->edad = edad_;
	this->correo = correo_;
	this->siguiente = siguiente_;
	this->anterior = anterior_;
}

string NodoListaDobleCircular::getCarnet(){
	return this->carnet;
}

string NodoListaDobleCircular::getDpi(){
	return this->dpi;
}

string NodoListaDobleCircular::getNombre(){
	return this->nombre;
}

int NodoListaDobleCircular::getEdad(){
	return this->edad;
}

string NodoListaDobleCircular::getCorreo(){
	return this->correo;
}

string NodoListaDobleCircular::getContra(){
	return this->contra;
}

int NodoListaDobleCircular::getCreditos(){
	return this->creditos;
}

string NodoListaDobleCircular::getCarrera(){
	return this->carrera;
}
NodoListaDobleCircular *NodoListaDobleCircular::getSiguiente(){
	return this->siguiente;
}

NodoListaDobleCircular *NodoListaDobleCircular::getAnterior(){
	return this->anterior;
}

void NodoListaDobleCircular::setCarnet(string carnet_){
	this->carnet = carnet_;
}
void NodoListaDobleCircular::setDpi(string dpi_){
	this->dpi = dpi_;
}
void NodoListaDobleCircular::setNombre(string nombre_){
	this->nombre = nombre_;
}
void NodoListaDobleCircular::setContrasena(string contra_){
	this->contra = contra_;
}
void NodoListaDobleCircular::setCreditos(int creditos_){
	this->creditos = creditos_;
}
void NodoListaDobleCircular::setEdad(int edad_){
	this->edad = edad_;
}
void NodoListaDobleCircular::setCorreo(string correo_){
	this->correo = correo_;
}
void NodoListaDobleCircular::setCarrera(string carrera_){
	this->carrera = carrera_;
}
void NodoListaDobleCircular::setSiguiente(NodoListaDobleCircular *siguiente_){
	this->siguiente = siguiente_;
}
void NodoListaDobleCircular::setAnterior(NodoListaDobleCircular *anterior_){
	this->anterior = anterior_;
}
