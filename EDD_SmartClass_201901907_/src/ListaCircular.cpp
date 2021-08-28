#include "ListaCircular.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include<string>
#include <sstream>
using namespace std;

ListaCircular::ListaCircular()
{
	this->Primero = NULL;
	this->Ultimo = NULL;
}

bool ListaCircular::isEmpty()
{
	return this->Primero == NULL;
}

int ListaCircular::getSize()
{
	NodoListaDobleCircular *auxiliar = this->Primero;
	int contador = 0;
	do{
		contador++;
		auxiliar = auxiliar->getSiguiente();
	}while(auxiliar != this->Primero);
	return contador;
}

void ListaCircular::getListaC()
{
	NodoListaDobleCircular *auxiliar = this->Primero;
	do{
		cout<<" "<<auxiliar->getCarnet()<<" - "<<auxiliar->getDpi()<<" - "<<auxiliar->getNombre()<<" - "<<auxiliar->getCarrera()<<" - "<<auxiliar->getContra()<<" - "<<auxiliar->getCreditos()<<" - "<<auxiliar->getEdad()<<" - "<<auxiliar->getCorreo()<<endl;
		auxiliar = auxiliar->getSiguiente();
	}while(auxiliar!=this->Primero);
}

void ListaCircular::insertar(string carnet_, string dpi_, string nombre_, string carrera_, string contra_, int creditos_, int edad_, string correo_)
{
	NodoListaDobleCircular *newNode = new NodoListaDobleCircular(carnet_, dpi_, nombre_,  carrera_,  contra_, creditos_, edad_, correo_);
	if(isEmpty()){
		this->Primero = newNode;
		this->Ultimo = newNode;
		this->Primero->setSiguiente(this->Primero);
		this->Primero->setAnterior(this->Ultimo);
	}
	else{
		this->Ultimo->setSiguiente(newNode);
		newNode->setAnterior(this->Ultimo);
		newNode->setSiguiente(this->Primero);
		this->Ultimo = newNode;
		this->Primero->setAnterior(this->Ultimo);
	}
}

void ListaCircular::grafico()
{
    int contador = 0;
    ofstream archivo("estudiantes.dot");
    //archivo.open("estudiantes.dot", ios::out);
    archivo << "digraph G {\n";
    archivo << "rankdir=LR;\n";
    archivo << "node[shape = record];\n ";
    NodoListaDobleCircular *aux = new NodoListaDobleCircular();
    aux = this->Primero;
    if (this->Primero != NULL)
    {
        do
        {
            int contador2 = contador + 1;

        	string str1 = std::to_string(contador);
            string str2 = std::to_string(contador2);
            string cre = std::to_string(aux->getCreditos());
            string ed = std::to_string(aux->getEdad());
            archivo << "nodo" + str1 << "[label=\" Carnet: "+ aux->getCarnet() + "\n |DPI: " + aux->getDpi() + "\n |Nombre: "+ aux->getNombre() +
            "\n |Carrera: " + aux->getCarrera() + "\n |Correo: " + aux->getCorreo()  + "\n |Contrasena:" + aux->getContra() +
            "\n |Creditos: " + cre + "\n |Edad:" + ed  +'\"'+ "]";
            if (aux->getSiguiente() == this->Primero)
            {
                archivo << "\n nodo" + str1 + "-> nodo0\n";
            }
            else
            {
                archivo << "\n nodo" + str1 + "->" + "nodo" + str2 + "\n";
            }
            contador++;
            aux = aux->getSiguiente();
        } while (aux != this->Primero);
        archivo << "}\n";
        archivo.close();
        string ej= "dot -Tpng estudiantes.dot -o estudiantes.png";
        char const *ejecutar = ej.c_str();
        system(ejecutar);
    }
    else
    {
        cout << "La lista esta vacia !!!\n";
    }
}

void ListaCircular::mostrar()
{

	NodoListaDobleCircular *aux = new NodoListaDobleCircular();
    aux = this->Primero;
    if (this->Primero != NULL)
    {
        cout << "La lista de estudiantes actualmente es:\n";
        do
        {
            cout << aux->getNombre() << endl;
            aux = aux->getSiguiente();
        } while (aux != this->Primero);
    }
    else
    {
        cout << "La lista esta vacia !!!\n";
    }
}

void ListaCircular::modificar(string DPI){
    int menus0;
    string carnet, dpi, nombre, carrera, correo, contrasena, creditos, edad;
    NodoListaDobleCircular *actual = new NodoListaDobleCircular();
    actual = this->Primero;
    bool encontrado = false;
    string nodoBuscado;
    nodoBuscado = DPI;
    if(this->Primero!=NULL){
            do{

                if(actual->getDpi()==nodoBuscado){
                    cout << "Datos con el DPI: ( " << nodoBuscado << " ) Encontrado";

                    do{
                                        cout << "**** Menu de Modificacion de Datos ***" << endl;
                                        cout << "*                                    *" << endl;
                                        cout << "*          1. Carnet                 *" << endl;
                                        cout << "*          2. DPI                    *" << endl;
                                        cout << "*          3. Nombre                 *" << endl;
                                        cout << "*          4. Carrera                *" << endl;
                                        cout << "*          5. Contrasena             *" << endl;
                                        cout << "*          6. Creditos               *" << endl;
                                        cout << "*          7. Edad                   *" << endl;
                                        cout << "*          8. Correo                 *" << endl;
                                        cout << "*          9. Salir                  *" << endl;
                                        cout << "*                                    *" << endl;
                                        cout << "**************************************\n" << endl;
                                        cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
                                        cin >> menus0;

                                        switch (menus0)
                                        {
                                            case 1:
                                                {
                                                    cout<<"Ingrese Nuevo Carnet "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, carnet);
                                                    actual->setCarnet(carnet);
                                                    break;
                                                }
                                            case 2:
                                                {
                                                    cout<<"Ingrese Nuevo DPI "<<endl;
                                                    cin>>dpi;
                                                    actual->setDpi(dpi);
                                                    break;
                                                }
                                            case 3:
                                                {
                                                    cout<<"Ingrese Nuevo Nombre "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, nombre);
                                                    actual->setNombre(nombre);
                                                    break;
                                                }
                                            case 4:
                                                {
                                                    cout<<"Ingrese Nueva Carrera "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, carrera);
                                                    actual->setCarrera(carrera);
                                                    break;
                                                }
                                            case 5:
                                                {
                                                    cout<<"Ingrese Nueva Contrasena "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, contrasena);
                                                    actual->setContrasena(contrasena);
                                                    break;
                                                }
                                            case 6:
                                                {
                                                    cout<<"Ingrese Nuevos Creditos "<<endl;
                                                    cin>>creditos;
                                                    int cre = std::stoi(creditos);
                                                    actual->setCreditos(cre);
                                                    break;
                                                }
                                            case 7:
                                                {
                                                    cout<<"Ingrese Nueva Edad "<<endl;
                                                    cin.ignore();
                                                    std::getline(cin, edad);
                                                    int ed = std::stoi(edad);
                                                    actual->setEdad(ed);
                                                    break;
                                                }
                                            case 8:
                                                {
                                                    cout<<"Ingrese Nuevo Correo "<<endl;
                                                    cin.ignore();
                                                    cin >> correo;
                                                    actual->setCorreo(correo);
                                                    break;
                                                }

                                        }
                                    } while (menus0 != 9);

                    encontrado = true;
                }

                actual = actual->getSiguiente();
            }while(actual != this->Primero && encontrado != true);

            if(!encontrado){
                cout << "\n Nodo no Encontrado\n\n";
            }

        }else{
            cout << "\n La lista se Encuentra Vacia\n\n";
        }
}


void ListaCircular::eliminar(string dato)
{
    NodoListaDobleCircular *buscar = new NodoListaDobleCircular();
    NodoListaDobleCircular *eliminar = new NodoListaDobleCircular();
    buscar = this->Primero;
    eliminar = NULL;
    bool encontrado = false;
    if (this->Primero != NULL)
    {
        do
        {
            if (buscar->getDpi() == dato)
            {
                cout << "Estudiante " << buscar->getNombre() << " ha sido eliminado\n";
                if (buscar == buscar->getSiguiente())
                {
                    this->Primero = NULL;
                    this->Ultimo = NULL;
                    eliminar = NULL;
                    buscar = NULL;
                    encontrado = true;
                }
                else if (buscar == this->Primero)
                {
                    this->Primero = this->Primero->getSiguiente();
                    this->Primero->setAnterior(this->Ultimo);
                    this->Ultimo->setSiguiente(this->Primero);
                }
                else if (buscar == this->Ultimo)
                {
                    this->Ultimo = this->Ultimo->getAnterior();
                    this->Primero->setAnterior(this->Ultimo);
                    this->Ultimo->setSiguiente(this->Primero);
                }
                else
                {
                    eliminar->setSiguiente(buscar->getSiguiente());
                    buscar->getSiguiente()->setAnterior(eliminar);
                }
                encontrado = true;
            }
            else
            {
                eliminar = buscar;
                buscar = buscar->getSiguiente();
            }

        } while (buscar != this->Primero && encontrado == false);

        if (encontrado == false)
        {
            cout << "No se encontro al estudiante\n"
                 << endl;
        }
        else
        {
            free(eliminar);
        }
    }
    else
    {
        cout << "La lista esta vacia" << endl;
    }
}

bool ListaCircular::buscarCarnet(string carnet)
{
    bool encontrado = false;
    NodoListaDobleCircular *buscar = new NodoListaDobleCircular();
    buscar = this->Primero;
    if (this->Primero != NULL)
    {
        do
        {
            if (buscar->getCarnet() == carnet)
            {
                cout << "Estudiante encontrado\n"
                     << endl;
                encontrado = true;
                return 1;
            }
            buscar = buscar->getSiguiente();
        } while (buscar != this->Primero && encontrado == false);

        if (encontrado == false)
        {
            cout << "No se encontro al estudiante\n"
                 << endl;
            return 0;
        }
    }
    else
    {
        cout << "La lista esta vacia" << endl;
        return 0;
    }
}

