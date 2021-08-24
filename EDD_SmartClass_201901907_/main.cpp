#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iomanip>
#include "Colaa.h"
#include "ListaCircular.h"
#include "NodoMatriz.h"
#include "ListaDobleEnlazada.h"

using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int Tamano = 0;


Colaa Cola;
ListaCircular *ListaUsuarios = new ListaCircular();
NodoMatriz *Matriz[5][30][9];
ListaDobleEnlazada *Linealizado = new ListaDobleEnlazada();

string TamanoArchivo(string ruta)
{
	fstream archivo;
	archivo.open(ruta.c_str(), ios::in);
	string texto, linea;
	if(archivo.is_open()){
		getline(archivo, linea);
		char delimitador = ',';
		while(getline(archivo, linea)){
			Tamano++;
		}
		archivo.close();
	}
	else {
		cout << "No se pudo abrir el archivo" <<endl;
	}
}

string LecturaArchivo(string ruta)
{
	fstream archivo;
	int contador=0;
	archivo.open(ruta.c_str(), ios::in);
	string texto, linea;
	if(archivo.is_open()){
		getline(archivo, linea);
		char delimitador = ',';
		string Nombre, Carrera, Contrasena, Carnet, DPI, Creditos, Edad, Correo;
		/*
		while(getline(archivo, linea)){
			cout << "Linea" << endl;
			cout << linea << endl;
			texto = texto + linea + "\n";
			stringstream stream(linea);
			int  Carnet1, DPI1, Creditos1, Edad1;

			getline(stream, Carnet, delimitador);
			getline(stream, DPI, delimitador);
			getline(stream, Nombre, delimitador);
			getline(stream, Carrera, delimitador);
			getline(stream, Contrasena, delimitador);
			getline(stream, Creditos, delimitador);
			getline(stream, Edad, delimitador);
			getline(stream, Correo, delimitador);
			cout<< contador<<endl;
			contador++;
			stringstream ss;
			ss << Carnet;
			ss >> Carnet1;
		//	Lis_Nombre[contador] = (Carnet1);
			for (stream)
		}
		for(int i=0; i<=Tamano; i++){
			getline(archivo, linea);
			cout << "Linea" << endl;
			cout << linea << endl;
			texto = texto + linea + "\n";
			string arr("@");
			string com(".com");
			string org(".org");
			string es(".es");
			stringstream stream(linea);
			int  Carnet1, DPI1, Creditos1, Edad1;

			getline(stream, Carnet, delimitador);
			getline(stream, DPI, delimitador);
			getline(stream, Nombre, delimitador);
			getline(stream, Carrera, delimitador);
			getline(stream, Contrasena, delimitador);
			getline(stream, Creditos, delimitador);
			getline(stream, Edad, delimitador);
			getline(stream, Correo, delimitador);
			stringstream ss;
			ss << Carnet;
			ss >> Carnet1;
			stringstream ss1;
			ss1 << DPI;
			ss1 >> DPI1;
			stringstream ss2;
			ss2 << Creditos;
			ss2 >> Creditos1;
			stringstream ss3;
			ss3 << Edad;
			ss3 >> Edad1;
			cout<<Carnet.length()<<endl;
			cout<<DPI.length()<<endl;
			//cout<<Carnet.length()<<endl;
			if(Carnet.length() == 9){
				if(DPI.length() == 13){
					if(strstr(Correo.c_str(),arr.c_str())){
						if(strstr(Correo.c_str(),com.c_str()) || strstr(Correo.c_str(),org.c_str()) || strstr(Correo.c_str(),es.c_str())){
							List_Carnet[i] = Carnet1;
							Lis_DPI[i] = DPI1;
							Lis_Nombre[i] = Nombre;
							Lis_Carrera[i] = Carrera;
							Lis_Contrasena[i] = Contrasena;
							Lis_Creditos[i] = Creditos1;
							Lis_Edad[i] = Edad1;
							Lis_Correo[i] = Correo;
						}
						else{
							cout<<"Correo incorrecto"<<endl;
						}
					}
					else{
						cout<<"Correo incorrecto"<<endl;
					}

				}
				else{
					cout<<"DPI incorrecto"<<endl;
				}
			}
			else{
				cout<<"Carnet incorrecto"<<endl;
			}
			cout<< i <<endl;
		}
		*/
		archivo.close();
	}
	else {
		cout << "No se pudo abrir el archivo" <<endl;
	}
	return texto;
}

bool revisarCorreo(string palabra, string tipo, string id)
{
    bool well = false;
    bool well1 = false;
    bool well2 = false;

    string word = "";
    for (auto x : palabra)
    {
        if (x == '@')
        {
            well = true;
            word = "";
        }
        else if (x == '.')
        {
            well1 = true;
            word = "";
        }
        else
        {
            word = word + x;
        }
        if (word == "es" || word == "com" || word == "org")
        {
            well2 = true;
        }
        else
        {
            well2 = false;
        }
    }
    if (well == false || well1 == false || well2 == false)
    {
        cout << "Error: El correo no es valido \n";
        cout << "Error: revisar cola de errores\n";
        //q.enqueue(tipo, "El correo del estudiante con dpi: " + id + " no es valido");
        cout << "El correo del estudiante con dpi: " + id + " no es valido\n";
        return 0;
    }
    else
    {
        cout << "Correo valido \n";
        return 1;
    }
}

void carga_estudiantes(string documento)
{
    Cola.Inicializar();
    bool answer="";
    ifstream archivo(documento);
    string linea;
    char delimitador = ',';
    // Leemos la primer línea para descartarla
    getline(archivo, linea);
    // While para leer todas las líneas
    while (getline(archivo, linea))
    {

        stringstream stream(linea); // Convertir la cadena a un stream
        string carnet, dpi, nombre, carrera, password, creditos, edad, correo;
        // Extraer todos los valores de esa fila
        getline(stream, carnet, delimitador);
        getline(stream, dpi, delimitador);
        getline(stream, nombre, delimitador);
        getline(stream, carrera, delimitador);
        getline(stream, password, delimitador);
        getline(stream, creditos, delimitador);
        getline(stream, edad, delimitador);
        getline(stream, correo, delimitador);
        int credit, age;
        credit = atoi(creditos.c_str());
        age = atoi(edad.c_str());
        answer = revisarCorreo(correo, "Estudiante", dpi);
        if (carnet.size() != 9 && dpi.size() != 13 && answer == 0)
            {
                cout << "Error: El carnet, dpi y correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet, correo y dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else if (carnet.size() != 9 && dpi.size() != 13)
            {
                cout << "Error: El carnet y dpi del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet y dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else if (dpi.size() != 13 && answer == 0)
            {
                cout << "Error: El dpi y correo del estudiante: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El dpi y correo del estudiante: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else if (carnet.size() != 9 && answer == 0)
            {
                cout << "Error: El carnet y correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet y correo del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else if (carnet.size() != 9)
            {
                cout << "Error: El carnet del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else if (dpi.size() != 13)
            {
                cout << "Error: El dpi del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }else if(answer == 0)
            {
                cout << "Error: El correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El correo del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
            else
            {
                cout<<"Estudiante:      "+nombre+"\n";
                cout<<"carne valido:    "+carnet+"\n";
                cout<<"dpi valido:      "+dpi+"\n";
                cout<<"correo valido:      "+correo+"\n";
                cout<<"\n";
                ListaUsuarios->insertar(carnet, dpi, nombre, carrera, password, credit, age, correo);
            }
    }
    cout<< Cola.Tamano() <<endl;
    archivo.close();
}

int main() {

	int valor = 0;

    do
	{
        int menu0,menu2,menu3,menu4, menu1;
        cout << "************ Men\xA3 Principal **********" << endl;
        cout << "*                                    *" << endl;
        cout << "*          1. Carga de usuarios      *" << endl;
        cout << "*          2. Carga de tareas        *" << endl;
        cout << "*          3. Ingreso manual         *" << endl;
        cout << "*          4. Reportes               *" << endl;
        cout << "*          5. Salir                  *" << endl;
        cout << "*                                    *" << endl;
        cout << "**************************************\n" << endl;
		cout << "Bienvenido al Men\xA3 Principal!"<< endl;
        cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
        cin >> menu0;
        valor = menu0;
        switch(menu0)
        {
        case 1:
            {
                cout << "\n********* Menu de Usuarios **********" << endl;
                cout << "*                                    *" << endl;
                cout << "*          1. Ingresar               *" << endl;
                cout << "*          2. Modificar              *" << endl;
                cout << "*          3. Eliminar               *" << endl;
                cout << "*          4. Salir                  *" << endl;
                cout << "*                                    *" << endl;
                cout << "**************************************\n" << endl;
                cout<< "Ingrese el numero de opci\xA2n:  \n";
                cin >> menu1;
                switch(menu1){
        		case 1:
        		    {
                        string ruta;
                        cout<< "Ingrese la Ruta del archivo:"<<endl;
                        cin >> ruta;
                        carga_estudiantes(ruta);
                        break;
        		    }
                case 2:
                    {
                        ListaUsuarios->grafico();
                        ListaUsuarios->mostrar();
                        break;
                    }
                case 3:
                    {
                        cout<< "Hola"<<endl;
                        Cola.grafico();
                        break;
                    }
                case 4:
                    {
                        cout<< "Ingrese la Ruta del archivo: \n"<<endl;
                    }
                }
            }
        }
    }while(valor != 5);
    return 0;
}




