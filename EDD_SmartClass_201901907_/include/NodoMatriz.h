#ifndef NODOMATRIZ_H
#define NODOMATRIZ_H
#include <iostream>
#include<string>

using namespace std;

class NodoMatriz
{
    public:
        NodoMatriz();
        NodoMatriz(string id_,string mes_,string dia_,string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_);
        string getId();
        string getMes();
        string getDia();
        string getHora();
        string getCarnet();
        string getNombre();
        string getDescripcion();
        string getMateria();
        string getFecha();
        string getEstado();
        void setId(string id_);
        void setMes(string mes_);
        void setDia(string dia_);
        void setHora(string hora_);
        void setCarnet(string carnet_);
        void setNombre(string nombre_);
        void setDescripcion(string descripcion_);
        void setMateria(string materia_);
        void setFecha(string fecha_);
        void setEstado(string estado_);

    private:
        string id;
        string mes;
        string hora;
        string dia;
        string carnet;
        string nombre;
        string descripcion;
        string materia;
        string fecha;
        string estado;
};

#endif // NODOMATRIZ_H
