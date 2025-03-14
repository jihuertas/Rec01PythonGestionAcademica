import json
from datetime import datetime

class Asignatura:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        # Verificar que el alumno no esté ya inscrito y agregarlo (1 punto)

    
    def eliminar_alumno(self, alumno):
        # Verificar que el alumno esté inscrito y eliminarlo (1 punto)
        
    
    def mostrar_info(self):
        print(f"Asignatura: {self.nombre} ({self.codigo}) - Profesor: {self.profesor}")
        print("Alumnos inscritos:")
        for alumno in self.alumnos:
            print(f"- {alumno.nombre} ({alumno.matricula})")

class Alumno:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.asignaturas = []
        self.calificaciones = {}
    
    def inscribirse(self, asignatura):
        # Agregar la asignatura a la lista de asignaturas del alumno (1 punto)
    
    def retirarse(self, asignatura):
        # Verificar que el alumno esté inscrito y eliminar la asignatura de la lista (1 punto)
    
    def ver_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for examen, calificacion in self.calificaciones.items():
            print(f"{examen}: {calificacion}")

class Examen:
    def __init__(self, nombre, fecha, asignatura):
        self.nombre = nombre
        self.fecha = fecha
        self.asignatura = asignatura
        self.calificaciones = {}
    
    def asignar_calificacion(self, alumno, calificacion):
        # Verificar que el alumno esté inscrito en la asignatura y asignar la calificación (1 punto)
    
    def mostrar_calificaciones(self):
        print(f"Calificaciones del examen {self.nombre} ({self.fecha}):")
        for matricula, calificacion in self.calificaciones.items():
            print(f"Matricula {matricula}: {calificacion}")

class GestorAcademico:
    def __init__(self):
        self.asignaturas = {}
        self.alumnos = {}
        self.examenes = {}
    
    def agregar_asignatura(self, nombre, codigo, profesor):
        # Agregar la asignatura al diccionario de asignaturas, usando el código como clave (1 punto)
    
    def agregar_alumno(self, nombre, matricula):
        # Agregar el alumno al diccionario de alumnos, usando la matrícula como clave (1 punto)
    
    def agregar_alumno_a_asignatura(self, matricula, codigo_asignatura):
        # Verificar que el alumno y la asignatura existan y agregar al alumno a la asignatura (1,5 puntos)

    
    def registrar_examen(self, nombre, fecha, codigo_asignatura):
        # Verificar que la asignatura exista y registrar el examen (1,5 puntos)

    
    def listar_datos(self):
        print("\nAsignaturas:")
        for asignatura in self.asignaturas.values():
            asignatura.mostrar_info()
        print("\nAlumnos:")
        for alumno in self.alumnos.values():
            print(f"{alumno.nombre} ({alumno.matricula})")
        print("\nExámenes:")
        for examen in self.examenes.values():
            print(f"{examen.nombre} - {examen.fecha} ({examen.asignatura.nombre})")
    
    def guardar_datos(self, archivo):
        datos = {
            "asignaturas": {k: v.__dict__ for k, v in self.asignaturas.items()},
            "alumnos": {k: v.__dict__ for k, v in self.alumnos.items()},
            "examenes": {k: v.__dict__ for k, v in self.examenes.items()}
        }
        with open(archivo, "w") as f:
            json.dump(datos, f)
    
    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

### **Interfaz de Usuario Simple (Consola):**
if __name__ == "__main__":
    gestor = GestorAcademico()
    while True:
        print("\nSistema de Gestión Académica")
        print("1. Agregar asignatura")
        print("2. Agregar alumno")
        print("3. Registrar examen")
        print("4. Agregar alumno a asignatura")
        print("5. Listar datos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la asignatura: ")
            codigo = input("Código de la asignatura: ")
            profesor = input("Nombre del profesor: ")
            gestor.agregar_asignatura(nombre, codigo, profesor)
        elif opcion == "2":
            nombre = input("Nombre del alumno: ")
            matricula = input("Número de matrícula: ")
            gestor.agregar_alumno(nombre, matricula)
        elif opcion == "3":
            nombre = input("Nombre del examen: ")
            fecha = input("Fecha del examen (YYYY-MM-DD): ")
            codigo = input("Código de la asignatura: ")
            gestor.registrar_examen(nombre, fecha, codigo)
        elif opcion == "4":
            matricula = input("Número de matrícula del alumno: ")
            codigo = input("Código de la asignatura: ")
            gestor.agregar_alumno_a_asignatura(matricula, codigo)
        elif opcion == "5":
            gestor.listar_datos()
        elif opcion == "6":
            gestor.guardar_datos("datos.json")
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")