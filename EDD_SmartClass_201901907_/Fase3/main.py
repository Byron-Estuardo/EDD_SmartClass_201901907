from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet
import hashlib
import base64  # para convertir la imagen y responderla al frontend
import json
from ArbolB import ArbolBPensum
from ListaSimple import ListaSemestre
from Matriz import Matriz
from avl import AVL
from lista_doble import ListaDoble
from lista_doble import ListaDobleMeses
from lista_doble import ListaDobleTareas
from TablaHash import TablaHash
from grafo import Grafos

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

GrafoPensum = Grafos.Grafos()
AVL = AVL.AVL()
CarnetLogueado = 0
TablaApuntes = TablaHash.TablaHash()
ArbolB = ArbolBPensum.arbolB()

def GenerarClave():
    Clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(Clave)
    #print(Clave)

GenerarClave()

def CargarClave():
    return open("clave.key", "rb").read()

Clave = CargarClave()
ferne = Fernet(Clave)
lista1CursosPensum = []
lista2CursosPensum = []
listaconpre = []

#Listas Temporales
listatemp1 = []
listatemp2 = []
listatemp3 = []
listaCodigos = []
SinRepetidos = []

class Objetos:
    def __init__(self, nombre, codigo: int, creditos: int, pre, obligatorio):
        self.nombre = nombre
        self.codigo: int = codigo
        self.creditos: int = creditos
        self.pre = pre
        self.obligatorio = obligatorio

class CursoPensum:
    def __init__(self,nombre, codigo:int, creditos:int, obligatorio) -> None:
        self.nombre = nombre
        self.codigo:int  = codigo
        self.creditos:int = creditos
        self.obligatorio = obligatorio

def GrafoLecturaCursosPensum(ruta):
    with open(ruta, encoding="utf8") as file:
        data = json.load(file)
        for cursos in data['Cursos']:
            codigo = cursos['Codigo']
            nombre = cursos['Nombre']
            creditos = cursos['Creditos']
            preequisitos = cursos['Prerequisitos']
            pres = preequisitos.split(',')
            obligatorio = cursos['Obligatorio']
            ClaseCurso = CursoPensum(str(nombre), int(codigo), int(creditos), str(obligatorio))
            GrafoPensum.insert_node(ClaseCurso)
            lista1CursosPensum.append(ClaseCurso)
            lista2CursosPensum.append(ClaseCurso)
            objeto = Objetos(str(nombre), int(codigo), int(creditos), pres, str(obligatorio))
            listaconpre.append(objeto)

        for i in range(len(lista1CursosPensum)):
            if listaconpre[i].pre[0] != '':
                Curso1 = lista1CursosPensum[i]
                for item in listaconpre[i].pre:
                    for item1 in lista2CursosPensum:
                        if item1.codigo == int(item):
                            print(item)
                            GrafoPensum.link_graph(Curso1, item1)
        GrafoPensum.get_list()

def RevisarQueTodosLosPreEstenEnLaLista(codigo):
    for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == codigo:
            listaCodigos.append(codigo)
            if listaconpre[pos].pre[0] != '':
                for items in listaconpre[pos].pre:
                    codigos = int(items)
                    IngresarEnListas(codigos)

def IngresarEnListas(Codigo):

    for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == Codigo:
            listaCodigos.append(Codigo)
            if listaconpre[pos].pre[0] != '':
                for items in listaconpre[pos].pre:
                    codigos = int(items)
                    RevisarQueTodosLosPreEstenEnLaLista(codigos)

def GrafoPreObtener(Codigo):
    GrafoTemporal = Grafos.Grafos()
    listatemp1.clear()
    listatemp2.clear()
    listatemp3.clear()
    listaCodigos.clear()
    SinRepetidos.clear()
    for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == Codigo:
            IngresarEnListas(Codigo)
    for element in listaCodigos:
        if element not in SinRepetidos:
            SinRepetidos.append(element)
    print(SinRepetidos)
    SinRepetidos.sort()
    print(SinRepetidos)
    for CursoCodigo in SinRepetidos:
        for pos in range(len(lista1CursosPensum)):
            if lista1CursosPensum[pos].codigo == CursoCodigo:
                curso = lista1CursosPensum[pos]
                listatemp1.append(curso)
                listatemp2.append(curso)
                listatemp3.append(listaconpre[pos])
                GrafoTemporal.insert_node(curso)
    for i in range(len(listatemp1)):
        if listatemp3[i].pre[0] != '':
            Curso1 = listatemp1[i]
            for item in listatemp3[i].pre:
                for item1 in listatemp2:
                    if item1.codigo == int(item):
                        print(item)
                        GrafoTemporal.link_graph(Curso1, item1)
    GrafoTemporal.get_list()
    GrafoTemporal.GraficarPre()

    ''' 
        for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == Codigo:
            curso = lista1CursosPensum[pos]
            listatemp1.append(curso)
            listatemp2.append(curso)
            listatemp3.append(listaconpre[pos])
            GrafoTemporal.insert_node(curso)
            if listaconpre[pos].pre[0] != '':
                #for posa in range(len(listaconpre)):
                    for items in listaconpre[pos].pre:
                        codigos = int(items)
                        for pos1 in range(len(lista1CursosPensum)):
                            if lista1CursosPensum[pos1].codigo == codigos:
                                Curso1 = lista1CursosPensum[pos1]
                                prueba = listaconpre[pos1]
                                listatemp1.append(Curso1)
                                listatemp2.append(Curso1)
                                listatemp3.append(prueba)
                                GrafoTemporal.insert_node(Curso1)
    for i in range(len(listatemp1)):
        if listatemp3[i].pre[0] != '':
            Curso1 = listatemp1[i]
            for item in listatemp3[i].pre:
                for item1 in listatemp2:
                    if item1.codigo == int(item):
                        print(item)
                        GrafoTemporal.link_graph(Curso1, item1)
    GrafoTemporal.get_list()
    GrafoTemporal.GraficarPre()
        #GrafoTemporal.insert_node(item)
    for i in range(len(lista1CursosPensum)):
        if lista1CursosPensum[i].codigo == Codigo:
            Curso1 = lista1CursosPensum[i]
            if listaconpre[i].pre[0] != '':
                for item in listaconpre[i].pre:
                    for item1 in lista2CursosPensum:
                        if item1.codigo == int(item):
                            print(item)
                            GrafoTemporal.link_graph(Curso1, item1)
    GrafoTemporal.get_list()
    '''

def LecturaApuntes(ruta):
    with open(ruta, encoding="utf8") as file:
        data = json.load(file)
        for Usuarios in data['usuarios']:
            carnet = Usuarios['carnet']
            for apuntes in Usuarios['apuntes']:
                titulo = apuntes['Título']
                body = apuntes['Contenido']
                TablaApuntes.insertar(carnet, titulo, body)

def IngresoAputesManual(titulo, contenido):
    TablaApuntes.insertar(CarnetLogueado, titulo, contenido)

def VerificarCarnetAvl(carnet):
    encontrado = AVL.RevisarExiste(carnet)
    return encontrado

def VerificarQueElCursoExistaEnPensum(Codigo):
    for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == Codigo:
            return True
    return False

def ObtenerDatosCurso(Codigo):
    posicion = 0
    for pos in range(len(lista1CursosPensum)):
        if lista1CursosPensum[pos].codigo == Codigo:
            return posicion
    return -1

def AgregarCursosEstudiantesManual(Codigo, year, semestre):
    nodo = AVL.find(CarnetLogueado)
    # Buscar el carnet en el AVL
    veriAños = nodo.años.BuscarExiste(int(year))
    if veriAños == False:
        NuevoMeses = ListaDobleMeses.ListaDobleMeses()
        NuevoSemestres = ListaSemestre.ListaSemestre()
        # Si no existe el año se crea uno
        nodo.años.Insertar(int(year), NuevoSemestres, NuevoMeses)
    # Obtenemos el nodo del año
    nodo1 = nodo.años.BuscarNodo(int(year))
    veriSemestres = nodo1.semestre.BuscarExiste(int(semestre))
    if veriSemestres == False:
        arbolbtemp = ArbolBPensum.arbolB()
        nodo1.semestre.Insertar(int(semestre), arbolbtemp)
    nodo2 = nodo1.semestre.BuscarNodo(int(semestre))
    variable = VerificarQueElCursoExistaEnPensum(Codigo)
    if variable == True:
        posicionBusqueda = ObtenerDatosCurso(Codigo)
        if posicionBusqueda != -1:
            Codigos = lista1CursosPensum[posicionBusqueda].codigo
            name = lista1CursosPensum[posicionBusqueda].nombre
            creditoss = lista1CursosPensum[posicionBusqueda].creditos
            obligatorio = lista1CursosPensum[posicionBusqueda].obligatorio
            nodo2.curso.insertarDatos(Codigos, name, creditoss, "", obligatorio)
    else:
        print("El Curso no se encuentra en el pensum Actual")

def LecturaCursosEstudiante(ruta):
    with open(ruta) as file:
        data = json.load(file)
        print(data)
        for curso in data['Estudiantes']:
            print("Carnet: " + curso['Carnet'])
            carnet = curso['Carnet']
            NuevoMeses = ListaDobleMeses.ListaDobleMeses()
            NuevoSemestres = ListaSemestre.ListaSemestre()
            veri = VerificarCarnetAvl(carnet)
            # Verificar que el carnet Exista
            if veri == True:
                # print("Carnet Encontrado")
                nodo = AVL.find(carnet)
                # Buscar el carnet en el AVL
                for años in curso['AÃ±os']:
                    years = años['AÃ±o']
                    veriAños = nodo.años.BuscarExiste(years)
                    if veriAños == False:
                        # Si no existe el año se crea uno
                        nodo.años.Insertar(years, NuevoSemestres, NuevoMeses)
                    # Obtenemos el nodo del año
                    nodo1 = nodo.años.BuscarNodo(years)
                    for semestes in años['Semestres']:
                        veriSemestres = nodo1.semestre.BuscarExiste(años['Semestres'])
                        if veriSemestres == False:
                            arbolbtemp = ArbolBPensum.arbolB()
                            nodo1.semestre.Insertar(años['Semestres'], arbolbtemp)
                        nodo2 = nodo1.semestre.BuscarNodo(años['Semestres'])
                        for Cursos in semestes['Cursos']:
                            print("Codigo: " + Cursos['Codigo'])
                            Codigo = Cursos['Codigo']
                            variable = VerificarQueElCursoExistaEnPensum(Codigo)
                            if variable == True:
                                nodo2.curso.insertarDatos(int(Cursos['Codigo']), Cursos['Nombre'], Cursos['Creditos'], Cursos['Prerequisitos'], Cursos['Obligatorio'])
                            else:
                                print("El Curso no se encuentra en el pensum Actual")

def LecturaCursosEstudiantesJson(ruta):
    with open(ruta, encoding="utf8") as file:
        data = json.load(file)
        for estudiantes in data['Estudiantes']:
            carnet = estudiantes['Carnet']
            veri = VerificarCarnetAvl(carnet)
            if veri == True:
                nodo = AVL.find(carnet)
                for years in estudiantes['Años']:
                    año = years['Año']
                    veriAños = nodo.años.BuscarExiste(año)
                    if veriAños == False:
                        NuevoMeses = ListaDobleMeses.ListaDobleMeses()
                        NuevoSemestres = ListaSemestre.ListaSemestre()
                        nodo.años.Insertar(año, NuevoSemestres, NuevoMeses)
                    nodo1 = nodo.años.BuscarNodo(año)
                    for semester in years['Semestres']:
                        semestre = semester['Semestre']
                        veriSemestres = nodo1.semestre.BuscarExiste(semestre)
                        if veriSemestres == False:
                            arbolbtemp = ArbolBPensum.arbolB()
                            nodo1.semestre.Insertar(semestre, arbolbtemp)
                        nodo2 = nodo1.semestre.BuscarNodo(semestre)
                        for Cursos in semester['Cursos']:
                            Codigo = Cursos['Codigo']
                            variable = VerificarQueElCursoExistaEnPensum(Codigo)
                            if variable == True:
                                nodo2.curso.insertarDatos(int(Cursos['Codigo']), Cursos['Nombre'], Cursos['Creditos'],
                                                          Cursos['Prerequisitos'], Cursos['Obligatorio'])
                            else:
                                print("El Curso no se encuentra en el pensum Actual")

def GraficoCursosEstudiante(year, semestre):
    nodo = AVL.find(CarnetLogueado)
    # Buscar el carnet en el AVL
    veriAños = nodo.años.BuscarExiste(int(year))
    if veriAños == True:
        nodo1 = nodo.años.BuscarNodo(int(year))
        veriSemestres = nodo1.semestre.BuscarExiste(int(semestre))
        if veriSemestres == True:
            nodo2 = nodo1.semestre.BuscarNodo(int(semestre))
            nodo2.curso.graficar()

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
    elif mes == "08":
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

def LecturaArchivoEstudiantesJSON(ruta):
    with open(ruta) as file:
        data = json.load(file)
        for estudiante in data['estudiantes']:
            carnet = int(estudiante['carnet'])
            dpi1 = str(estudiante['DPI'])
            nombre1 = str(estudiante['nombre'])
            carrera1 = str(estudiante['carrera'])
            correo1 = str(estudiante['correo'])
            contra1 = str(estudiante['password'])
            creditos = ""
            edad1 = str(estudiante['edad'])
            conversion = str(carnet)
            prueba = conversion.encode()
            carnet2 = ferne.encrypt(prueba)
            prueba1 = dpi1.encode()
            dpi = ferne.encrypt(prueba1)
            prueba2 = nombre1.encode()
            nombre = ferne.encrypt(prueba2)
            prueba3 = contra1.encode('utf-8')
            encriptado1 = hashlib.sha256(prueba3).hexdigest()
            encriptado12 = encriptado1.encode()
            contra = ferne.encrypt(encriptado12)
            prueba4 = edad1.encode()
            edad = ferne.encrypt(prueba4)
            prueba52 = carrera1.encode()
            carrera = ferne.encrypt(prueba52)
            prueba5 = correo1.encode()
            correo = ferne.encrypt(prueba5)
            veri = VerificarCarnetAvl(carnet)
            #print(carnet2)
            if veri == False:
                NuevoAños = ListaDoble.ListaDoble()
                AVL.insertar(carnet, carnet2, dpi, nombre, carrera, correo, contra, creditos, edad, NuevoAños)
            else:
                print("Carnet Repetido")

def LecturaArchivoFaseAnt(ruta):
    f = open(ruta, "r", encoding="utf-8")
    mensaje = f.read()
    f.close()
    from analizador.sintactico import parser
    resultado_analisis = parser.parse(mensaje)
    separadorFecha = "/"
    separadorHora = ":"

    for item in resultado_analisis:
        if item["type"] == "user":
            atributos = item["atributos"]
            carnet = int(atributos[0]["Carnet"].replace("\"", ""))
            dpi1 = str(atributos[1]["DPI"].replace("\"", ""))
            nombre1 = str(atributos[2]["Nombre"].replace("\"", ""))
            carrera1 = str(atributos[3]["Carrera"].replace("\"", ""))
            correo1 = str(atributos[4]["Correo"].replace("\"", ""))
            contra1 = str(atributos[5]["Password"].replace("\"", ""))
            creditos = str(atributos[6]["Creditos"])
            edad1 = str(atributos[7]["Edad"])
            conversion = str(carnet)
            prueba = conversion.encode()
            carnet2 = ferne.encrypt(prueba)
            prueba1 = dpi1.encode()
            dpi = ferne.encrypt(prueba1)
            prueba2 = nombre1.encode()
            nombre = ferne.encrypt(prueba2)
            prueba3 = contra1.encode('utf-8')
            encriptado1 = hashlib.sha256(prueba3).hexdigest()
            encriptado12 = encriptado1.encode()
            contra = ferne.encrypt(encriptado12)
            prueba4 = edad1.encode()
            edad = ferne.encrypt(prueba4)
            prueba52 = carrera1.encode()
            carrera = ferne.encrypt(prueba52)
            prueba5 = correo1.encode()
            correo = ferne.encrypt(prueba5)
            veri = VerificarCarnetAvl(carnet)
            if veri == False:
                NuevoAños = ListaDoble.ListaDoble()
                AVL.insertar(carnet, carnet2, dpi, nombre, carrera, correo, contra, creditos, edad, NuevoAños)
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

def RegistrarAvl(var1, var2, var3, var4, var5, var6, var7):
    carnet = int(var1)
    dpi1 = str(var2)
    nombre1 = str(var3)
    carrera = str(var4)
    correo1 = str(var5)
    contra1 = str(var6)
    creditos = ""
    edad1 = str(var7)
    conversion = str(carnet)
    prueba = conversion.encode()
    carnet2 = ferne.encrypt(prueba)
    prueba1 = dpi1.encode()
    dpi = ferne.encrypt(prueba1)
    prueba2 = nombre1.encode()
    nombre = ferne.encrypt(prueba2)
    prueba3 = contra1.encode('utf-8')
    encriptado1 = hashlib.sha256(prueba3).hexdigest()
    encriptado12 = encriptado1.encode()
    contra = ferne.encrypt(encriptado12)
    prueba4 = edad1.encode()
    edad = ferne.encrypt(prueba4)
    prueba5 = correo1.encode()
    correo = ferne.encrypt(prueba5)
    veri = VerificarCarnetAvl(carnet)

    if veri == False:
        NuevoAños = ListaDoble.ListaDoble()
        AVL.insertar(carnet, carnet2, dpi, nombre, carrera, correo, contra, creditos, edad, NuevoAños)
    else:
        print("Carnet Repetido")

@app.route('/', methods=['POST'])
def login():
    if request.method == 'POST':
        varError = ""
        usuario = int(request.json['Usuario'])
        contra = str(request.json['Contra'])
        contra1 = contra.encode()
        CodificadoContra = hashlib.sha256(contra1).hexdigest()
        verifiAVL = VerificarCarnetAvl(usuario)
        if verifiAVL == True:
            nodo = AVL.find(usuario)
            contrase = nodo.password
            primerdesifrado = ferne.decrypt(contrase)
            decode = primerdesifrado.decode()
            if decode == CodificadoContra:
                ingresi = True
                CarnetLogueado = int(usuario)
            else:
                varError = "La contraseña es incorrecta"
                ingresi= False
        else:
            varError = "Usuario con el carnet " + '"' + str(usuario) + '" No se encuentra Registrado'
            ingresi = False

        # grafo1.insertar(valor)
        response = jsonify({'Error': varError, 'Ingreso': ingresi})
        #print('Valores regresados ' + str(usuario) + ' ' + str(contra) + ' ' + str(ingresi))
        print("metodo post")
        return response

@app.route('/Administrador/CargarPensum', methods=['POST'])
def CargaPensumJson():
    if request.method == 'POST':
        ruta = request.json['Ruta']
        GrafoLecturaCursosPensum(str(ruta))
        response = jsonify({'response': 'Valores regresados ', 'Ingreso': ruta, 'Respuesta': 'Datos Ingresados'})
        print('Valores regresados ' + ruta)
        print("metodo post")
        return response

@app.route('/Administrador/MasivaEstudiantesJson', methods=['POST'])
def RegistrarMasivoJson():
    print("Entro??")
    if request.method == 'POST':
        print('Carga Masiva json')
        ruta = request.json['Ruta']
        LecturaArchivoEstudiantesJSON(str(ruta))

        response = jsonify({'response': 'Valores regresados ', 'Ingreso': ruta, 'Respuesta': 'Datos Ingresados'})
        print('Valores regresados ' + ruta)
        print("metodo post")
        return response

@app.route('/Administrador/MasivaEstudiantesTxt', methods=['POST'])
def CargaMasivaEstudiantes():
    if request.method == 'POST':
        print('Carga Masiva txt')
        ruta = request.json['Ruta']
        LecturaArchivoFaseAnt(str(ruta))
        AVL.pre_orden()
        response = jsonify({'response': 'Valores regresados ', 'Ingreso': ruta, 'Respuesta': 'Datos Ingresados'})
        print('Valores regresados ' + ruta)
        print("metodo post")
        return response

@app.route('/Administrador/MasivoApuntes', methods=['POST'])
def RegistrarMasivoJsonApuntes():
    if request.method == 'POST':
        ruta = request.json['Ruta']
        print(ruta)
        LecturaApuntes(str(ruta))
        #AVL.graficar()
        response = jsonify({'response': 'Valores regresados ', 'Ingreso': ruta, 'Respuesta': 'Datos Ingresados'})
        print('Valores regresados ' + ruta)
        print("metodo post")
        return response

@app.route('/Registro', methods=['POST'])
def Registrar():
    print("Entro??")
    if request.method == 'POST':
        print('Carga Masiva json')
        carnet = int(request.json['Carnet'])
        Dpi = request.json['DPI']
        name = request.json['Nombre']
        carr = request.json['Carrera']
        cor = request.json['Correo']
        pas = request.json['Contra']
        edad = request.json['Edad']
        veri = VerificarCarnetAvl(carnet)
        RegistrarAvl(carnet, Dpi, name, carr, cor, pas, edad)
        AVL.pre_orden()
        response = jsonify({'Existe': veri, 'Respuesta': 'Datos Ingresados'})
        print('Valores regresados ' + str(veri))
        print("metodo post")
        return response

@app.route('/Administrador/GraficoAvlEncriptado', methods=['GET'])
def GraficoAvlEncriptado():
    AVL.graficar()
    b64_string = ""
    with open("AVL.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    #print(str(b64_string.decode('utf-8')))
    response = jsonify({'response': 'se grafico', 'Imagen': str(b64_string.decode('utf-8'))})

    return response

@app.route('/Administrador/GraficoGrafoPensum', methods=['GET'])
def GraficoGrafos():
    GrafoPensum.GraficarPensum()
    b64_string = ""
    with open("GrafoPensum.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    #print(str(b64_string.decode('utf-8')))
    response = jsonify({'response': 'se grafico', 'Imagen': str(b64_string.decode('utf-8'))})

    return response

@app.route('/Administrador/GraficoAvl', methods=['GET'])
def GraficoAvl():
    AVL.graficarDes()
    b64_string = ""
    with open("AVLDes.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    #print(str(b64_string.decode('utf-8')))
    response = jsonify({'response': 'se grafico', 'Imagen': str(b64_string.decode('utf-8'))})

    return response

@app.route('/Administrador/GraficoApuntes', methods=['GET'])
def GraficoApuntes():
    TablaApuntes.reporteTable()
    b64_string = ""
    with open("TablaApuntes.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    #print(str(b64_string.decode('utf-8')))
    response = jsonify({'response': 'se grafico', 'Imagen': str(b64_string.decode('utf-8'))})

    return response

if __name__ == '__main__':
    app.run(port=3000, debug=True)
