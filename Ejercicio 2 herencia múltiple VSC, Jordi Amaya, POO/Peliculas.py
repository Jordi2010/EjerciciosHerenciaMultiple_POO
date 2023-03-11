# Ejercicios de herencia múltiple.
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

# Ejercicio 2. Cree el siguiente ejercicio utilizando POO. Una plataforma de streaming publica contenido
# como series, películas y documentales según sea la clasificación de su categoría. Podemos tomar 3
# categorías (Acción, Comedia y Terror) tomando en cuenta que esta seria la primera clase, debemos de
# heredar a una clase películas la categoría a la que pueda estar ligada la película mostrando un mensaje
# de referencia a su criterio.
# La última clase ara referencia a las dos clases anteriores ya que esta será la Cliente donde por una
# estructura de condición mostrará la película a ver. Ejemplo: si el usuario escoge Acción imprimir las
# películas de acción a las que se hagan referencia. Puede trabajar solo con 1 película para cada categoría.

from Categorias import Categorias
from Categorias import categoria1, categoria2, categoria3

class Peliculas(Categorias):
    def __init__(self, categoria, nombrePelicula):
        super().__init__(categoria)
        self.nombrePelicula=nombrePelicula
    def categorizarPelicula(self):
        return "La pelicula {} es de la categoría {}.".format(self.nombrePelicula, self.categoria)
pelicula1=Peliculas(categoria1.categoria, "John Wick 4")
print(pelicula1.categorizarPelicula())
pelicula2=Peliculas(categoria2.categoria, "Ace Ventura")
print(pelicula2.categorizarPelicula())
pelicula3=Peliculas(categoria3.categoria, "Viernes 13")
print(pelicula3.categorizarPelicula())