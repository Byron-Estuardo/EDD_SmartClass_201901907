#include "NodoListaDobleEnlazada.h"

NodoListaDobleEnlazada::NodoListaDobleEnlazada()
{
    this->id = "";
    this->mes = "";
    this->dia = "";
    this->hora= "";
    this->carnet = "";
    this->nombre = "";
    this->descripcion = "";
    this->materia = "";
    this->fecha = "";
    this->estado = "";
    this->NextD = NULL;
    this->PrevD = NULL;
}

/*NodoListaDobleEnlazada::NodoListaDobleEnlazada(string id_,string mes_,string dia_,string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_)
{
    this->id = id_;
    this->mes = mes_;
    this->dia = dia_;
    this->hora = hora_;
    this->carnet = carnet_;
    this->nombre = nombre_;
    this->descripcion = descripcion_;
    this->materia = materia_;
    this->fecha = fecha_;
    this->estado = estado_;
    this->NextD = 0;
    this->PrevD = 0;
}*/

NodoListaDobleEnlazada::NodoListaDobleEnlazada(string id_,string mes_,string dia_,string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_, NodoListaDobleEnlazada *PrevD_, NodoListaDobleEnlazada *NextD_)
{
    this->id = id_;
    this->mes = mes_;
    this->dia = dia_;
    this->hora = hora_;
    this->carnet = carnet_;
    this->nombre = nombre_;
    this->descripcion = descripcion_;
    this->materia = materia_;
    this->fecha = fecha_;
    this->estado = estado_;
    this->NextD = NextD_;
    this->PrevD = PrevD_;
}

string NodoListaDobleEnlazada::getId()
{
    return this->id;
}

string NodoListaDobleEnlazada::getMes(){
    return this->mes;
}

string NodoListaDobleEnlazada::getDia(){
    return this->dia;
}

string NodoListaDobleEnlazada::getHora(){
    return this->hora;
}

string NodoListaDobleEnlazada::getCarnet()
{
    return this->carnet;
}

string NodoListaDobleEnlazada::getNombre(){
    return this->nombre;
}

string NodoListaDobleEnlazada::getDescripcion(){
    return this->descripcion;
}

string NodoListaDobleEnlazada::getMateria(){
    return this->materia;
}

string NodoListaDobleEnlazada::getFecha(){
    return this->fecha;
}

string NodoListaDobleEnlazada::getEstado(){
    return this->estado;
}

NodoListaDobleEnlazada *NodoListaDobleEnlazada::getNextD()
{
    return this->NextD;
}

NodoListaDobleEnlazada *NodoListaDobleEnlazada::getPrevD(){
    return this->PrevD;
}

void NodoListaDobleEnlazada::setId(string id_)
{
    this->id = id_;
}

void NodoListaDobleEnlazada::setMes(string mes_){
    this->mes = mes_;
}

void NodoListaDobleEnlazada::setDia(string dia_){
    this->dia = dia_;
}

void NodoListaDobleEnlazada::setHora(string hora_){
    this->hora = hora_;
}

void NodoListaDobleEnlazada::setCarnet(string carnet_){
    this->carnet = carnet_;
}

void NodoListaDobleEnlazada::setNombre(string nombre_){
    this->nombre = nombre_;
}

void NodoListaDobleEnlazada::setDescripcion(string descripcion_){
    this->descripcion = descripcion_;
}

void NodoListaDobleEnlazada::setMateria(string materia_){
    this->materia = materia_;
}

void NodoListaDobleEnlazada::setFecha(string fecha_){
    this->fecha = fecha_;
}


void NodoListaDobleEnlazada::setEstado(string estado_){
    this->estado = estado_;
}


void NodoListaDobleEnlazada::setNextD(NodoListaDobleEnlazada *NextD_){
    this->NextD = NextD_;
}

void NodoListaDobleEnlazada::setPrevD(NodoListaDobleEnlazada *PrevD_){
    this->PrevD = PrevD_;
}

