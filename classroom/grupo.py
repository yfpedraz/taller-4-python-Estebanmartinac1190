

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    def listadoAsignaturas(self, **kwargs):
        if (self._asignaturas is None):
            self._asignaturas = []
        
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))
                
            
    def agregarAlumno(self, alumno, lista=None):
        if(lista is not None):
            lista.append(alumno)
            if (self.listadoAlumnos is not None):
                self.listadoAlumnos = list(set(self.listadoAlumnos.extend(lista)))
            else:
                self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
