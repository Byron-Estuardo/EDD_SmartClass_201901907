import json

from flask import Flask
from flask_restful import reqparse, Resource, Api, request

from ArbolB import AB
from ListaSimple import ListaSemestre
from Matriz import Matriz
from analizador.sintactico import parser
from avl import AVL
from lista_doble import ListaDoble
from lista_doble import ListaDobleMeses
from lista_doble import ListaDobleTareas

app = Flask(__name__)
api = Api(app)

AVL = AVL.AVL()
ArbolB = AB.arbolB()

def VerificarCarnetAvl(carnet):
    encontrado = AVL.RevisarExiste(carnet)
    return encontrado

def LecturaCursosPensum(ruta):
    with open(ruta) as file:
        data = json.load(file)
        for curso in data['Cursos']:
            cursos = curso['Codigo']
            nombre = curso['Nombre']
            creditos = curso['Creditos']
            pre = curso['Prerequisitos']
            obligatorio = curso['Obligatorio']
            ArbolB.insertarDatos(cursos, nombre, creditos, pre, obligatorio)

def LecturaCursosEstudiante(ruta):
    with open(ruta) as file:
        data = json.load(file)
        print(data)
        for curso in data['Estudiantes']:
            print("Carnet: " + curso['Carnet'])
            print(curso["AÃ±os"])
            for años in curso['AÃ±os']:
                print("Año: " + años['AÃ±o'])
                for semestes in años['Semestres']:
                    print("Creditos: " + str(semestes['Semestre']))
                    for Cursos in semestes['Cursos']:
                        print("Codigo: " + Cursos['Codigo'])
                        print("Nombre: " + Cursos['Nombre'])
                        print("Creditos: " + str(Cursos['Creditos']))
                        print("Prerequisitos: " + Cursos['Prerequisitos'])
                        print("Obligatorio: " + str(Cursos['Obligatorio']))

def ConvertirMesATexto(mes):
    if mes == "01":
        convertido = "Enero"
        return convertido
    elif mes == "02":
        convertido = "Febrero"
        return convertido
    elif mes == "03":
        convertido = "Marzo"
        return convertido
    elif mes == "04":
        convertido = "Abril"
        return convertido
    elif mes == "05":
        convertido = "Mayo"
        return convertido
    elif mes == "06":
        convertido = "Junio"
        return convertido
    elif mes == "07":
        convertido = "Julio"
        return convertido
    elif mes == "08" :
        convertido = "Agosto"
        return convertido
    elif mes == "09":
        convertido = "Septiembre"
        return convertido
    elif mes == "10":
        convertido = "Octubre"
        return convertido
    elif mes == "11":
        convertido = "Noviembre"
        return convertido
    elif mes == "12":
        convertido = "Diciembre"
        return convertido
    else:
        convertido = "ERROR"
        return convertido

def ConvertirTextoAMes(mes):
    if mes == "Enero":
        convertido = "01"
        return convertido
    elif mes == "Febrero":
        convertido = "02"
        return convertido
    elif mes == "Marzo":
        convertido = "03"
        return convertido
    elif mes == "Abril":
        convertido = "04"
        return convertido
    elif mes == "Mayo":
        convertido = "05"
        return convertido
    elif mes == "Junio":
        convertido = "06"
        return convertido
    elif mes == "Julio":
        convertido = "07"
        return convertido
    elif mes == "Agosto":
        convertido = "08"
        return convertido
    elif mes == "Septiembre":
        convertido = "09"
        return convertido
    elif mes == "Octubre":
        convertido = "10"
        return convertido
    elif mes == "Noviembre":
        convertido = "11"
        return convertido
    elif mes == "Diciembre":
        convertido = "12"
        return convertido
    else:
        convertido = "ERROR"
        return convertido

def LecturaArchivoFaseAnt(ruta):
    f = open(ruta, "r", encoding="utf-8")
    mensaje = f.read()
    f.close()

    resultado_analisis = parser.parse(mensaje)
    separadorFecha = "/"
    separadorHora = ":"

    for item in resultado_analisis:
        if item["type"] == "user":
            atributos = item["atributos"]
            carnet = int(atributos[0]["Carnet"].replace("\"", ""))
            dpi = str(atributos[1]["DPI"].replace("\"", ""))
            nombre = str(atributos[2]["Nombre"].replace("\"", ""))
            carrera = str(atributos[3]["Carrera"].replace("\"", ""))
            correo = str(atributos[4]["Correo"].replace("\"", ""))
            contra = str(atributos[5]["Password"].replace("\"", ""))
            creditos = int(atributos[6]["Creditos"])
            edad = int(atributos[7]["Edad"])
            veri = VerificarCarnetAvl(carnet)
            if veri == False:
                NuevoAños = ListaDoble.ListaDoble()
                AVL.insertar(carnet, dpi, nombre, carrera, correo, contra, creditos, edad, NuevoAños)
            else:
                print("Carnet Repetido")
        else:
            atributos = item["atributos"]
            carnet1 = int(atributos[0]["Carnet"].replace("\"", ""))
            nombre = str(atributos[1]["Nombre"].replace("\"", ""))
            descrip = str(atributos[2]["Descripcion"].replace("\"", ""))
            materia = str(atributos[3]["Materia"].replace("\"", ""))
            fecha = str(atributos[4]["Fecha"].replace("\"", ""))
            hora = str(atributos[5]["Hora"].replace("\"", ""))
            estado = str(atributos[6]["Estado"].replace("\"", ""))
            FechaSeparada = fecha.split(separadorFecha)
            HoraSeparada = hora.split(separadorHora)
            dia = FechaSeparada[0]
            mes = str(FechaSeparada[1])
            año = str(FechaSeparada[2])
            horaSep = HoraSeparada[0]
            MinSep = HoraSeparada[1]
            NuevoMeses = ListaDobleMeses.ListaDobleMeses()
            NuevoSemestres = ListaSemestre.ListaSemestre()
            veri = VerificarCarnetAvl(carnet1)
            # Verificar que el carnet Exista
            if veri == True:
                # print("Carnet Encontrado")
                nodo = AVL.find(carnet1)
                # Buscar el carnet en el AVL
                veriAños = nodo.años.BuscarExiste(año)
                if veriAños == False:
                    # Si no existe el año se crea uno
                    nodo.años.Insertar(año, NuevoSemestres, NuevoMeses)
                # Obtenemos el nodo del año
                nodo1 = nodo.años.BuscarNodo(año)
                ConvertidoMes = ConvertirMesATexto(mes)
                veriMeses = nodo1.meses.BuscarExiste(ConvertidoMes)
                if veriMeses == False:
                    # Si no existe el mes se crea uno nuevo
                    NuevaMatriz = Matriz.Matriz_Dispersa()
                    nodo1.meses.Insertar(ConvertidoMes, NuevaMatriz)
                # obtenemos el nodo de meses
                nodo2 = nodo1.meses.BuscarNodo(ConvertidoMes)
                # Verificamos que exista el nodo en la matriz
                veriMatriz = nodo2.tareas.buscar(int(horaSep), int(dia))
                if veriMatriz == False:
                    NuevaListaTareas = ListaDobleTareas.ListaDobleTareas()
                    nodo2.tareas.insertar(int(horaSep), int(dia), NuevaListaTareas)
                nodo3 = nodo2.tareas.buscarNodo(int(horaSep), int(dia))
                nodo4 = nodo3.derecha
                nodo5 = nodo4.recordatorio
                nodo5.Insertar(carnet1, nombre, descrip, materia, fecha, hora, estado)
            else:
                print("El Carnet no Existe")

parser = reqparse.RequestParser()
parser.add_argument('task')


class CargaMasiva(Resource):
    def post(self):

        inputJson = request.get_json(force=True)

        peticion = inputJson['tipo']

        path = inputJson['path']

        print(path)

        print(peticion)
        if peticion == "estudiante":
            LecturaArchivoFaseAnt(str(path))
        return "Archivo Cargado"

api.add_resource(CargaMasiva, '/CargaMasiva')

if __name__ == '__main__':
    app.run(host='localhost',port=3000, debug=True)
    #LecturaArchivoFaseAnt("D:/Users/bcatu/Escritorio/EDDProyecto/EDD_SmartClass_201901907/EDD_SmartClass_201901907_/Fase2/Estudiantes.txt")
    #LecturaCursosPensum("D:/Users/bcatu/Escritorio/EDDProyecto/EDD_SmartClass_201901907/EDD_SmartClass_201901907_/Fase2/CursosPensum.json")
    # LecturaCursosEstudiante("D:/Users/bcatu/Escritorio/EDDProyecto/EDD_SmartClass_201901907/EDD_SmartClass_201901907_/Fase2/CursosEstudiante.json")
    # AVL.pre_orden()

