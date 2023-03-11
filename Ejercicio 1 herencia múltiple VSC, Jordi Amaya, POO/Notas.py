# Ejercicios de herencia múltiple.
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

# Ejercicio 1. Cree el siguiente ejercicio utilizando POO. En este ejercicio debe de simular el registro de
# notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para iniciar el
# ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
# El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un estudiante de una
# materia en específico. El mensaje para mostrar queda a su discreción.

from Estudiantes import Estudiantes
from Materias import Materias
from Materias import materia1, materia2, materia3

class Notas(Estudiantes, Materias):
    pass
    def verNotas1():
        notaLab=9
        notaPar=8
        return "Las notas del estudiante {} en la materia {} sección {} fueron: LABORATORIO {} y PARCIAL {}".format(Estudiantes.estudiante1, materia1.materia, materia1.seccion, notaLab, notaPar)
    def verNotas2():
        notaLab=10
        notaPar=9
        return "Las notas del estudiante {} en la materia {} sección {} fueron: LABORATORIO {} y PARCIAL {}".format(Estudiantes.estudiante2, materia2.materia, materia2.seccion, notaLab, notaPar)
    def verNotas3():
        notaLab=8
        notaPar=8
        return "Las notas del estudiante {} en la materia {} sección {} fueron: LABORATORIO {} y PARCIAL {}".format(Estudiantes.estudiante3, materia3.materia, materia3.seccion, notaLab, notaPar)
estudianteNotas=Notas
print(estudianteNotas.verNotas1())
print(estudianteNotas.verNotas2())
print(estudianteNotas.verNotas3())