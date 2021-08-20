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

void ListaCircular::modificar(string dato)
{

    bool encontrado = false;
    NodoListaDobleCircular *buscar = new NodoListaDobleCircular();
    buscar = this->Primero;
    string carne_bueno;
    string dpi_bueno;
    string correo_bueno;
    string respuesta;

    if (this->Primero != NULL)
    {
        do
        {
            if (buscar->getDpi() == dato)
            {
                cout << "Estudiante encontrado\n"
                     << endl;
                cout << "Escriba el nuevo carne:\n";
                cin >> carne_bueno;

                cout << "Escriba el nuevo dpi:\n";
                cin >> dpi_bueno;

                if (carne_bueno.size() != 9)
                {
                    cout << "Los digitos del carne deben ser 9\n";
                    cout << "desea intentar otra vez (Y/N)\n";
                    cin >> respuesta;
                    if (respuesta == "Y" || respuesta == "y")
                    {
                    }
                    else if (respuesta == "N" || respuesta == "n")
                    {
                        encontrado = true;
                    }
                    else
                    {
                        encontrado = true;
                    }
                }
                else if (dpi_bueno.size() != 13)
                {
                    cout << "Los digitos del dpi deben ser 13\n";
                    cout << "desea intentar otra vez (Y/N)\n";
                    cin >> respuesta;
                    if (respuesta == "Y" || respuesta == "y")
                    {
                    }
                    else if (respuesta == "N" || respuesta == "n")
                    {
                        encontrado = true;
                    }
                    else
                    {
                        encontrado = true;
                    }
                }
                else
                {
                	string NOM, CARR, CORR, CONT,CRE, EDAD;
					int CRE1, EDAD1;
                    buscar->setCarnet(carne_bueno);
                    buscar->setDpi(dpi_bueno);
                    cout << "Escriba el nuevo nombre:\n";
                    cin>>  NOM;
                    cout << "Escriba la nueva carrera:\n";
                    cin>>  CARR;
                    cout << "Escriba el nuevo correo:\n";
                    cin >>  CORR;
                    cout << "Escriba el nuevo password:\n";
                    cin >>  CONT;
                    cout << "Escriba los nuevos creditos:\n";
                    cin >>  CRE;
                    cout << "Escriba la nueva edad:\n";
                    cin >>  EDAD;
                    stringstream ers3;
					ers3 << CRE;
					ers3 >> CRE1;
					stringstream s3;
					s3 << EDAD;
					s3 >> EDAD1;
					buscar->setNombre(NOM);
					buscar->setCarrera(CARR);
					buscar->setCorreo(CORR);
					buscar->setCreditos(CRE1);
					buscar->setEdad(EDAD1);
                    encontrado = true;
                }
            }
            buscar = buscar->getSiguiente();
        } while (buscar != this->Primero && encontrado == false);

        if (encontrado == false)
        {
            cout << "No se encontro al estudiante\n"
                 << endl;
        }
    }
    else
    {
        cout << "La lista esta vacia" << endl;
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

