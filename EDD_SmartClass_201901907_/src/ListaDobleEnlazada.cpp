#include "ListaDobleEnlazada.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include<string>
#include <sstream>
using namespace std;

ListaDobleEnlazada::ListaDobleEnlazada(){
    this->First = NULL;
    this->Last = NULL;
}

int ListaDobleEnlazada::getSize(){
    NodoListaDobleEnlazada *aux = First;
    int contador = 0;
    while(aux != NULL){
        contador++;
        aux = aux->getNextD();
    }
    delete aux;
    return contador;
}

bool ListaDobleEnlazada::isEmpty(){
    return this->First == NULL;
}

void ListaDobleEnlazada::PrintList(){
    NodoListaDobleEnlazada *aux = First;
    while(aux != NULL){
        cout<<"Index: "<<aux->getId()<<endl;
        cout<<"Mes: "<<aux->getMes()<<endl;
        cout<<"Dia: "<<aux->getDia()<<endl;
        cout<<"Hora: "<<aux->getHora()<<endl;
        cout<<"Carnet: "<<aux->getCarnet()<<endl;
        cout<<"Nombre: "<<aux->getNombre()<<endl;
        cout<<"Descripcion: "<<aux->getDescripcion()<<endl;
        cout<<"Materia: "<<aux->getMateria()<<endl;
        cout<<"Fecha: "<<aux->getFecha()<<endl;
        cout<<"Estado: "<<aux->getEstado()<<endl;
        aux = aux->getNextD();
    }
    delete aux;
}

void ListaDobleEnlazada::Eliminar(string id){
    string SiNo;
    NodoListaDobleEnlazada *actual = new NodoListaDobleEnlazada();
    actual = this->First;
    bool encontrado = false;
    string nodoBuscado = id;
    if(this->First != NULL){

        while(actual != NULL && encontrado != true){
            if(actual->getId() == nodoBuscado){
                cout << "\n La Tarea con el ID:  ( " << nodoBuscado << " ) Fue Encontrado";
                cout <<"Esta Seguro que Desea Eliminar esta Tarea: (Y/N)"<<endl;
                cin>>SiNo;
                if(SiNo == "y"|| SiNo == "Y"){

                    actual->setCarnet("");
                    actual->setDescripcion("");
                    actual->setDia("");
                    actual->setEstado("");
                    actual->setFecha("");
                    actual->setHora("");
                    actual->setMateria("");
                    actual->setMes("");
                    actual->setNombre("");
                    cout << "\n Tarea Eliminada";
                    encontrado = true;
                }
                else{
                    cout<<"Opcion Cancelada, La Tarea no se Eliminara"<<endl;
                    encontrado=false;
                }
            }
            actual = actual->getNextD();
        }

        if(!encontrado){
            cout << "\nTarea No Encontrado\n\n";
        }

    }else{
        cout << "\n La listas se encuentra Vacia\n\n";
    }
}

void ListaDobleEnlazada::Modificar(string id){
    string SiNo;
    int menus0;
    NodoListaDobleEnlazada *actual = new NodoListaDobleEnlazada();
    actual = this->First;
    bool encontrado = false;
    string nodoBuscado = id;
    if(this->First != NULL){

        while(actual != NULL && encontrado != true){
            if(actual->getId() == nodoBuscado){
                do{
                                        cout << "**** Menu de Modificacion de Datos ***" << endl;
                                        cout << "*                                    *" << endl;
                                        cout << "*          1. Mes                    *" << endl;
                                        cout << "*          2. Hora                   *" << endl;
                                        cout << "*          3. Dia                    *" << endl;
                                        cout << "*          4. Carnet                 *" << endl;
                                        cout << "*          5. Nombre                 *" << endl;
                                        cout << "*          6. Descripcion            *" << endl;
                                        cout << "*          7. Materia                *" << endl;
                                        cout << "*          8. Fecha                  *" << endl;
                                        cout << "*          9. Estado                 *" << endl;
                                        cout << "*          10. Salir                 *" << endl;
                                        cout << "*                                    *" << endl;
                                        cout << "**************************************\n" << endl;
                                        cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
                                        cin >> menus0;

                                        switch (menus0)
                                        {
                                            case 1:
                                                {
                                                    string mes;
                                                    cout<<"Ingrese Nuevo Mes "<<endl;
                                                    cin>>mes;
                                                    actual->setMes(mes);
                                                    break;
                                                }
                                            case 2:
                                                {
                                                    string hora;
                                                    cout<<"Ingrese Nueva Hora "<<endl;
                                                    cin>>hora;
                                                    actual->setHora(hora);
                                                    break;
                                                }
                                            case 3:
                                                {
                                                    string dia;
                                                    cout<<"Ingrese Nuevo Dia "<<endl;
                                                    cin>>dia;
                                                    actual->setDia(dia);

                                                    break;
                                                }
                                            case 4:
                                                {
                                                    string carnet;
                                                    cout<<"Ingrese Nuevo Carnet "<<endl;
                                                    cin>>carnet;
                                                    actual->setCarnet(carnet);
                                                    break;
                                                }
                                            case 5:
                                                {
                                                    string nombre;
                                                    cout<<"Ingrese Nuevo Nombre "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, nombre);
                                                    actual->setNombre(nombre);
                                                    break;
                                                }
                                            case 6:
                                                {
                                                    string descri;
                                                    cout<<"Ingrese Nueva Descripcion "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, descri);
                                                    actual->setDescripcion(descri);
                                                    break;
                                                }
                                            case 7:
                                                {
                                                    string mate;
                                                    cout<<"Ingrese Nueva Materia "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, mate);
                                                    actual->setMateria(mate);
                                                    break;
                                                }
                                            case 8:
                                                {
                                                    string fecha;
                                                    cout<<"Ingrese Nueva Fecha "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, fecha);
                                                    actual->setFecha(fecha);
                                                    break;
                                                }
                                            case 9:
                                                {
                                                    string esta;
                                                    cout<<"Ingrese Nuevo Estado "<<endl;
                                                    cin >> esta;
                                                    actual->setEstado(esta);
                                                    break;
                                                }

                                        }
                                    } while (menus0 != 10);
            }
            actual = actual->getNextD();
        }

        if(!encontrado){
            cout << "\n Tarea no Encontrado\n\n";
        }

    }else{
        cout << "\n La listas se encuentra Vacia\n\n";
    }
}

void ListaDobleEnlazada::insertar(string id_, string mes_, string dia_, string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_)
{
    NodoListaDobleEnlazada *newNode = new NodoListaDobleEnlazada( id_, mes_, dia_, hora_, carnet_,  nombre_,  descripcion_,  materia_,  fecha_,  estado_, NULL, NULL);
    if(isEmpty()){
        this->First = newNode;
        this->Last = this->First;
    }
    else{
        this->Last->setNextD(newNode);
        newNode->setPrevD(this->Last);
        this->Last = newNode;
    }
}

void ListaDobleEnlazada::Grafico(){
    int contador = 0;
    ofstream archivo("Linealizado.dot");
    archivo << "digraph G {\n";
    archivo << "rankdir=LR;\n";
    archivo << "node[shape = record];\n ";
    NodoListaDobleEnlazada *aux = new NodoListaDobleEnlazada();
    aux = this->First;
    if (this->First != NULL)
    {
        do
        {
            int contador2 = contador + 1;

        	string str1 = std::to_string(contador);
            string str2 = std::to_string(contador2);
            archivo << "nodo" + str1 << "[label=\" id: "+ aux->getId() + "\n |Mes: " + aux->getMes() + "\n |Hora: "+ aux->getHora() +
            "\n |Dia: " + aux->getDia() + "\n |Carnet: " + aux->getCarnet()  + "\n |Nombre:" + aux->getNombre() +
            "\n |Descripcion: " + aux->getDescripcion() + "\n |Materia:" + aux->getMateria()  +"\n |Fecha: " + aux->getFecha() +"\n |Estado: " + aux->getEstado() +'\"'+ "]";
            if (aux->getNextD() == this->First)
            {
                archivo << "\n nodo" + str1 + "-> nodo0\n";
            }
            else
            {
                archivo << "\n nodo" + str1 + "->" + "nodo" + str2 + "\n";
            }
            contador++;
            aux = aux->getNextD();
        } while (aux != this->First);
        archivo << "}\n";
        archivo.close();
        string ej= "dot -Tpng Linealizado.dot -o Linealizado.png";
        char const *ejecutar = ej.c_str();
        system(ejecutar);
    }
    else
    {
        cout << "La lista esta vacia !!!\n";
    }
}
