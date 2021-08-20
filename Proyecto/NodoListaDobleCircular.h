#ifndef NODOLISTADOBLECIRCULAR_H
#define NODOLISTADOBLECIRCULAR_H
#include <iostream>
#include <string>

using namespace std;

class NodoListaDobleCircular
{
	private:
		string carnet;
		string dpi;
		string nombre;
		string carrera;
		string contra;
		int creditos;
		int edad;
		string correo;
		NodoListaDobleCircular *siguiente;
		NodoListaDobleCircular *anterior;
		friend class ListaCircular;
	public:
		NodoListaDobleCircular();
		NodoListaDobleCircular(string carnet_, string dpi_, string nombre_, string carrera_, string contra_, int creditos_, int edad_, string correo_);
		NodoListaDobleCircular(string carnet_, string dpi_, string nombre_, string carrera_, string contra_, int creditos_, int edad_, string correo_, NodoListaDobleCircular *siguiente_, NodoListaDobleCircular *anterior_);
		
		string getCarnet();
		string getDpi();
		string getNombre();
		string getCarrera();
		string getContra();
		int getCreditos();
		int getEdad();
		string getCorreo();
		NodoListaDobleCircular *getSiguiente();
		NodoListaDobleCircular *getAnterior();
		
		void setCarnet(string carnet_);
		void setDpi(string dpi_);
		void setNombre(string nombre_);
		void setContrasena(string contra_);
		void setCreditos(int creditos_);
		void setEdad(int edad_);
		void setCorreo(string correo_);
		void setCarrera(string carrera_);
		void setSiguiente(NodoListaDobleCircular *siguiente_);
		void setAnterior(NodoListaDobleCircular *anterior_);
};

#endif
