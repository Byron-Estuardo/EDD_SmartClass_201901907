from analizador.sintactico import parser
import json
from analizador.lexico import todo


def LecturaCursosPensum(ruta):
    with open(ruta) as file:
        data = json.load(file)
        for curso in data['Cursos']:
            print("Codigo: " + curso['Codigo'])
            print("Nombre: " + curso['Nombre'])
            print("Creditos: " + str(curso['Creditos']))
            print("Prerequisitos: " + curso['Prerequisitos'])
            print("Obligatorio: " + str(curso['Obligatorio']))


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


if __name__ == '__main__':
    f = open('Estudiantes.txt', "r", encoding="utf-8")
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
            print("Usuarios")
            print(str(carnet) + " " + dpi + " " + nombre + " " + carrera + " " + correo + " " + contra + " " + str(
                creditos) + " " + str(edad))
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
            for item in FechaSeparada:
                print("SEPARADO FECHA: " + item)
            for item in HoraSeparada:
                print("SEPARADO HORA: " + item)
            print("Tareas")
            print(str(carnet1) + " " + nombre + " " + descrip + " " + materia + " " + fecha + " " + hora + " " + estado)

    # LecturaCursosPensum("D:/Users/bcatu/Escritorio/EDDProyecto/EDD_SmartClass_201901907/EDD_SmartClass_201901907_/Fase2/CursosPensum.json")

    LecturaCursosEstudiante("D:/Users/bcatu/Escritorio/EDDProyecto/EDD_SmartClass_201901907/EDD_SmartClass_201901907_/Fase2/CursosEstudiante.json")

    '''for item in resultado_analisis:
        print(item["type"])
        for at in item["atributos"]:
            print(at)
'''

