# Ejercicios de herencia múltiple.
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

# Ejercicio 1. Cree el siguiente ejercicio utilizando POO. En este ejercicio debe de simular el registro de
# notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para iniciar el
# ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
# El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un estudiante de una
# materia en específico. El mensaje para mostrar queda a su discreción.

class Materias():
    def __init__(self, materia, seccion):
        self.materia=materia
        self.seccion=seccion
materia1=Materias("Lógica Computacional", "B")
materia2=Materias("Programación Estructurada", "A")
materia3=Materias("Programación Orientada a Objetos", "A")