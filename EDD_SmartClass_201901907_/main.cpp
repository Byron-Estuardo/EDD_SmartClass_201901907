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
int contador = 0;
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
    getline(archivo, linea);
    while (getline(archivo, linea))
    {

        stringstream stream(linea);
        string carnet, dpi, nombre, carrera, password, creditos, edad, correo;
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

void Linealizacion(){
    //alv la verdad es que no se que pdo, con parentesis no jala, pero sin parentesis si, que pdo PosLinealizado1= (hora+9)*(dia+30*mes)
    //alguien que me explique que pasa con esto alv
    int dia, hora, mes, PosLinealizado, PosLinealizado1;
    for(int x=0; x<5; x++){
        for (int y=0; y<30; y++){
            for (int z=0; z<9; z++){
                if(Matriz[x][y][z]!=NULL){
                    mes=x;
                    dia=y;
                    hora=z;
                    PosLinealizado= hora+9*(dia+30*mes);
                    string indexID = std::to_string(PosLinealizado);
                    Linealizado->insertar(indexID, Matriz[x][y][z]->getMes(), Matriz[x][y][z]->getDia(), Matriz[x][y][z]->getHora(), Matriz[x][y][z]->getCarnet(), Matriz[x][y][z]->getNombre(), Matriz[x][y][z]->getDescripcion(), Matriz[x][y][z]->getMateria(), Matriz[x][y][z]->getFecha(), Matriz[x][y][z]->getEstado());
                }else{
                    mes=x;
                    dia=y;
                    hora=z;
                    PosLinealizado=hora+9*(dia+30*mes);
                    string indexID = std::to_string(PosLinealizado);
                    Linealizado->insertar(indexID, "", "", "", "", "", "", "", "", "");
                }
            }
        }
    }
}

void PrintMatriz(){
    for(int x=0; x<5; x++){
        for (int y=0; y<30; y++){
            for (int z=0; z<9; z++){
                if(Matriz[x][y][z]!=NULL){
                    cout<<"-------------------------------------\n"<<endl;
                    cout<<"Tarea No. "<<Matriz[x][y][z]->getId()<<endl;
                    cout<<Matriz[x][y][z]->getId()<<endl;
                    cout<<Matriz[x][y][z]->getMes()<<endl;
                    cout<<Matriz[x][y][z]->getDia()<<endl;
                    cout<<Matriz[x][y][z]->getHora()<<endl;
                    cout<<Matriz[x][y][z]->getCarnet()<<endl;
                    cout<<Matriz[x][y][z]->getNombre()<<endl;
                    cout<<Matriz[x][y][z]->getDescripcion()<<endl;
                    cout<<Matriz[x][y][z]->getMateria()<<endl;
                    cout<<Matriz[x][y][z]->getFecha()<<endl;
                    cout<<Matriz[x][y][z]->getEstado()<<endl;
                    cout<<"-------------------------------------\n"<<endl;
                }
            }
        }
    }
}

int ConversionHoras(string hora){
    switch(stoi(hora)){
        case 8:
            return 0;
        break;
        case 9:
            return 1;
        break;
        case 10:
            return 2;
        break;
        case 11:
            return 3;
        break;
        case 12:
            return 4;
        break;
        case 13:
            return 5;
        break;
        case 14:
            return 6;
        break;
        case 15:
            return 7;
        break;
        case 16:
            return 8;
        break;
        default:
            return -1;

    }
}

int ConversionMes(string mes){
    switch(stoi(mes)){
        case 7:
            return 0;
        break;
        case 8:
            return 1;
        break;
        case 9:
            return 2;
        break;
        case 10:
            return 3;
        break;
        case 11:
            return 4;
        break;
        default:
            return -1;

    }
}

void InicializarMatriz(){
    for(int x=0; x<5; x++){
        for (int y=0; y<30; y++){
            for (int z=0; z<9; z++){
                Matriz[x][y][z]=NULL;
            }
        }
    }
}

void carga_tareas(string ruta){
    InicializarMatriz();
    ifstream archivo(ruta);
    string linea;
    char delimitador = ',';
    getline(archivo, linea);
    while (getline(archivo, linea))
    {
        stringstream stream(linea);
        string id,mes,dia,hora,carnet,nombre,descripcion, materia, fecha,estado;

        getline(stream,mes,delimitador);
        getline(stream,dia,delimitador);
        getline(stream,hora,delimitador);
        getline(stream,carnet,delimitador);
        getline(stream,nombre,delimitador);
        getline(stream,descripcion,delimitador);
        getline(stream,materia,delimitador);
        getline(stream,fecha,delimitador);
        getline(stream,estado,delimitador);
        if(Matriz[ConversionMes(mes)][(stoi(dia)-1)][ConversionHoras(hora)] == NULL){
            id = to_string(contador);
            Matriz[ConversionMes(mes)][(stoi(dia)-1)][ConversionHoras(hora)]= new NodoMatriz(id,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,estado);
            contador++;
        }else{
            cout<<"Ya Existe una tarea en esa Posicion"<<endl;
        }

    }

    archivo.close();
    Linealizacion();
    //PrintMatriz();
    //Linealizado->PrintList();
}

void AgregarTareas()
{
    int buscar, opcion;
    bool answer;
    string mes, dia, hora, carnet, nombre, descripcion, materia,fecha, estado;
    do
    {

        cout << "************ Menu de tareas **********" << endl;
        cout << "*                                    *" << endl;
        cout << "*          1. Ingresar               *" << endl;
        cout << "*          2. Modificar              *" << endl;
        cout << "*          3. Eliminar               *" << endl;
        cout << "*          4. Linealizar             *" << endl;
        cout << "*          5. Salir                  *" << endl;
        cout << "*                                    *" << endl;
        cout << "**************************************" << endl;
        cout << "Ingrese una opcion: ";
        cin >> opcion;
        switch (opcion)
        {
        case 1:
            {
                cout << "Ingrese el mes\n";
                cin >> mes;
                cout << "Ingrese el dia\n";
                cin >> dia;
                cout << "Ingrese la hora\n";
                cin >> hora;
                cout << "Ingrese el carne\n";
                cin >> carnet;
                cout << "Ingrese el nombre\n";
                cin >> nombre;
                cout << "Ingrese la descripcion\n";
                cin >> descripcion;
                cout << "Ingrese la materia\n";
                cin >> materia;
                cout << "Ingrese la fecha\n";
                cin >> fecha;
                cout << "Ingrese el estado\n";
                cin >> estado;
                int mes1, dia1, hora1;
                mes1 = atoi(mes.c_str());
                dia1 = atoi(dia.c_str());
                hora1 = atoi(hora.c_str());
                if (mes1 < 11 && mes1 > 6)
                {
                }
                else
                {
                    cout << "Error: Fecha invalida \n";
                    cout << "Error: revisar cola de errores\n";
                    Cola.Encolar("Tarea carne:" + carnet, "Mes invalido");
                }
                if (dia1 < 31 && dia1 > 0)
                {
                }
                else
                {
                    cout << "Error: Fecha invalida \n";
                    cout << "Error: revisar cola de errores\n";
                    Cola.Encolar("Tarea carne:" + carnet, "Dia invalido");
                }
                if (hora1 < 17 && hora1 > 7)
                {
                }
                else
                {
                    cout << "Error: Fecha invalida \n";
                    cout << "Error: revisar cola de errores\n";
                    Cola.Encolar("Tarea carne:" + carnet, "Hora invalida");
                }
                if(Matriz[ConversionMes(mes)][(stoi(dia)-1)][ConversionHoras(hora)] == NULL){
                    string id = to_string(contador);
                    Matriz[ConversionMes(mes)][(stoi(dia)-1)][ConversionHoras(hora)]= new NodoMatriz(id,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,estado);
                    contador++;
                }else{
                    cout<<"Ya Existe una tarea en esa Posicion"<<endl;
                }

                break;
            }
        case 2:
           {
                cout << "Ingrese el id de la tarea";
                cin >> buscar;
                int PosLinealizado;
                string verifi = std::to_string(buscar);
                for(int x=0; x<5; x++){
                    for (int y=0; y<30; y++){
                        for (int z=0; z<9; z++){
                            if(Matriz[x][y][z]->getId() == verifi){
                                int mes=x;
                                int dia=y;
                                int hora=z;
                                PosLinealizado= hora+9*(dia+30*mes);
                                string envio = std::to_string(PosLinealizado);
                                Linealizado->Modificar(envio);
                            }
                            else{
                                cout<< "Tarea no existente" <<endl;
                            }
                        }
                    }
                }
                break;
           }
        case 3:
            {

                cout << "Ingrese el id de la tarea";
                cin >> buscar;
                int PosLinealizado;
                string verifi = std::to_string(buscar);
                for(int x=0; x<5; x++){
                    for (int y=0; y<30; y++){
                        for (int z=0; z<9; z++){
                            if(Matriz[x][y][z]->getId() == verifi){
                                int mes=x;
                                int dia=y;
                                int hora=z;
                                PosLinealizado= hora+9*(dia+30*mes);
                                string envio = std::to_string(PosLinealizado);
                                Linealizado->Eliminar(envio);
                                Matriz[x][y][z]->setCarnet("");
                                Matriz[x][y][z]->setDescripcion("");
                                Matriz[x][y][z]->setDia("");
                                Matriz[x][y][z]->setEstado("");
                                Matriz[x][y][z]->setFecha("");
                                Matriz[x][y][z]->setHora("");
                                Matriz[x][y][z]->setMateria("");
                                Matriz[x][y][z]->setMes("");
                                Matriz[x][y][z]->setNombre("");

                            }
                            else{
                                cout<< "Tarea no existente" <<endl;
                            }
                        }
                    }
                }
                break;
            }

        case 4:
            {
                Linealizacion();
            }
        default:
            break;
        }

    } while (opcion != 4);
}

void AgregarUsuarios()
{
    int opcion;
    do
    {
        string buscar, carnet, nom, carr, mail, contra, dpi;
        bool answer;
        int carne_bueno;
        int dpi_bueno;
        int cre, age;

        cout << "\n\n******** Menu de usuarios ********" << endl;
        cout << "*                                    *" << endl;
        cout << "*          1. Ingresar               *" << endl;
        cout << "*          2. Modificar              *" << endl;
        cout << "*          3. Eliminar               *" << endl;
        cout << "*          4. Regresar               *" << endl;
        cout << "*                                    *" << endl;
        cout << "**************************************\n" << endl;
        cout << "Ingrese una opcion: ";
        cin >> opcion;
        switch (opcion)
        {
        case 1:
            cout << "Ingrese el carnet del estudiante\n";
            cin >> carnet;
            cout << "Ingrese el dpi del estudiante\n";
            cin >> dpi;
            cout << "Ingrese el nombre del estudiante\n";
            cin >> nom;
            cout << "Ingrese la carrera del estudiante\n";
            cin >> carr;
            cout << "Ingrese el correo del estudiante\n";
            cin >> mail;
            cout << "Ingrese la password del estudiante\n";
            cin >> contra;
            cout << "Ingrese los creditos del estudiante\n";
            cin >> cre;
            cout << "Ingrese la edad del estudiante\n";
            cin >> age;
            answer = revisarCorreo(mail, "Estudiante", dpi);
            carne_bueno = carnet.size();
            dpi_bueno = dpi.size();
            if (carne_bueno != 9 && dpi_bueno != 13 && answer == 0)
            {
                cout << "Error: El carnet, dpi y correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet, correo y dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (carne_bueno != 9 && dpi_bueno != 13)
            {
                cout << "Error: El carnet y dpi del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet y dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (dpi_bueno != 13 && answer == 0)
            {
                cout << "Error: El dpi y correo del estudiante: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El dpi y correo del estudiante: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (carne_bueno != 9 && answer == 0)
            {
                cout << "Error: El carnet y correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet y correo del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (carne_bueno != 9)
            {
                cout << "Error: El carnet del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El carnet del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (dpi_bueno != 13)
            {
                cout << "Error: El dpi del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El dpi del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else if (answer == 0)
            {
                cout << "Error: El correo del estudiante con dpi: " + dpi + " no es valido" << endl;
                cout << "Error: revisar cola de errores" << endl;
                Cola.Encolar("Estudiante", "El correo del estudiante con dpi: " + dpi + " no es valido");
                ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }
            else
            {
                cout << "Estudiante" + nom + "\n";
                cout << "carne valido\n";
                cout << "dpi valido\n";
               ListaUsuarios->insertar(carnet, dpi, nom, carr, contra, cre, age, mail);
            }

            break;
        case 2:

            cout << "Ingrese el DPI del estudiante a modificar\n";
            cin >> buscar;
            ListaUsuarios->modificar(buscar);

            break;
        case 3:
            cout << "Ingrese el DPI del estudiante a eliminar\n";
            cin >> buscar;
            ListaUsuarios->eliminar(buscar);
            break;
        default:
            cout << "Caracter invalido" << endl;
            break;
        }
    } while (opcion != 4);
}

void GenerarReportes()
{
    int opcion;
    do
    {
        cout << "************* Menu de reportes *************" << endl;
        cout << "*                                          *" << endl;
        cout << "* 1. Lista de estudiantes                  *" << endl;
        cout << "* 2. Lista de tareas linealizada           *" << endl;
        cout << "* 3. Busqueda en estructura linealizada    *" << endl;
        cout << "* 4. Busqueda de posicion linealizada      *" << endl;
        cout << "* 5. Cola de errores                       *" << endl;
        cout << "* 6. Codigo generado de salida (No Sirve)  *" << endl;
        cout << "* 7. Salir                                 *" << endl;
        cout << "*                                          *" << endl;
        cout << "********************************************" << endl;
        cout << "Escriba el numero de la opcion que desee: ";
        cin >> opcion;
        switch (opcion)
        {
        case 1:
            cout << "Graficando......" << endl;
            ListaUsuarios->grafico();
            cout << "Grafico Generado Con Exito" << endl;
            break;
        case 2:
            cout << "Graficando......" << endl;
            Linealizado->Grafico();
            cout << "Grafico Generado Con Exito" << endl;
            break;
        case 3:
            {
                int PosLinealizado;
                string dia1, mes1, hora1;
                int dia, mes, hora;
                cout << "ingrese el mes"<< endl;
                cin >> mes1;
                cout << "ingrese el dia"<< endl;
                cin >> dia1;
                cout << "ingrese la hora"<< endl;
                cin >> hora1;
                mes = ConversionMes(mes1);
                hora = ConversionHoras(hora1);
                dia = stoi(dia1);
                PosLinealizado= hora+9*(dia+30*mes);
                string indexID = std::to_string(PosLinealizado);
                Linealizado->buscarPos(indexID);
            }
            break;
        case 4:
            {
                int PosLinealizado;
                string dia1, mes1, hora1;
                int dia, mes, hora;
                cout << "ingrese el mes"<< endl;
                cin >> mes1;
                cout << "ingrese el dia"<< endl;
                cin >> dia1;
                cout << "ingrese la hora"<< endl;
                cin >> hora1;
                mes = ConversionMes(mes1);
                hora = ConversionHoras(hora1);
                dia = stoi(dia1);
                PosLinealizado= hora+9*(dia+30*mes);
                string indexID = std::to_string(PosLinealizado);
                Linealizado->buscar2(indexID);
            }
            break;
        case 5:
            cout << "Graficando......" << endl;
            Cola.grafico();
            cout << "Grafico Generado Con Exito" << endl;
            break;
        case 6:
            cout<<"Esto no sirve"<<endl;
            break;
        default:
            break;
        }
    } while (opcion != 7);
}

void CargasManuales(){
    bool repetir = true;
    int menu0;
    do
    {
        cout << "******* Menu Ingreso Manual **********" << endl;
        cout << "*                                    *" << endl;
        cout << "*          1. Usuarios               *" << endl;
        cout << "*          2. Tareas                 *" << endl;
        cout << "*          4. Salir                  *" << endl;
        cout << "*                                    *" << endl;
        cout << "**************************************\n" << endl;
        cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
        cin >> menu0;

        switch (menu0)
        {
        case 1:
                AgregarUsuarios();
            break;

        case 2:
                AgregarTareas();
            break;
        case 3:
            break;

        }
    } while (repetir);
}

int main() {

	int valor = 0;

    do
	{
        int menu0,menu2,menu3,menu4, menu1;
        cout << "************ Menu Principal **********" << endl;
        cout << "*                                    *" << endl;
        cout << "*          1. Carga de usuarios      *" << endl;
        cout << "*          2. Carga de tareas        *" << endl;
        cout << "*          3. Ingreso manual         *" << endl;
        cout << "*          4. Reportes               *" << endl;
        cout << "*          5. Salir                  *" << endl;
        cout << "*                                    *" << endl;
        cout << "**************************************\n" << endl;
		cout << "Bienvenido al Menu Principal!"<< endl;
        cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
        cin >> menu0;
        valor = menu0;
        switch(menu0)
        {
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
                string ruta;
                cout<< "Ingrese la Ruta del archivo:"<<endl;
                cin >> ruta;
                carga_tareas(ruta);
                cout<< "Tareas Creadas..."<<endl;
                cout<< "Linealizando...."<<endl;
                cout<< "Linealizacion Completa!"<<endl;
                //PrintMatriz();
                break;
            }
        case 3:
            {
                cout << "******* Menu Ingreso Manual **********" << endl;
                cout << "*                                    *" << endl;
                cout << "*          1. Usuarios               *" << endl;
                cout << "*          2. Tareas                 *" << endl;
                cout << "*          4. Salir                  *" << endl;
                cout << "*                                    *" << endl;
                cout << "**************************************" << endl;
                cout << "Por favor ingrese el numero de opci\xA2n"<< endl;
                cin >> menu0;

                switch (menu0)
                {
                case 1:
                        AgregarUsuarios();
                    break;

                case 2:
                        AgregarTareas();
                    break;
                case 3:
                    break;
                }
            }
        case 4:
            {
                GenerarReportes();
            }
        case 5:
            {
                break;
            }
        }
    }while(valor != 5);
    return 0;
}




