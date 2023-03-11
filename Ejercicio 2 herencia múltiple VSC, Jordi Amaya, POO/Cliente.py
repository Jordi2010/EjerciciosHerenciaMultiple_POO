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

from Peliculas import Peliculas
from Peliculas import categoria1, categoria2, categoria3, pelicula1, pelicula2, pelicula3
class Cliente(Peliculas):
    def __init__(self, categoria,nombrePelicula,nombreCliente):
        super().__init__(categoria,nombrePelicula)
        self.nombreCliente=nombreCliente
    def verPelicula(self):
        if self.categoria==categoria1:
            return "El cliente {} eligió la categoría {} y la pelicula a ver es {}.".format(self.nombreCliente, categoria1.categoria, pelicula1.nombrePelicula)
        elif self.categoria==categoria2:
            return "El cliente {} eligió la categoría {} y la pelicula a ver es {}.".format(self.nombreCliente, categoria2.categoria, pelicula2.nombrePelicula)
        elif self.categoria==categoria3:
            return "El cliente {} eligió la categoría {} y la pelicula a ver es {}.".format(self.nombreCliente, categoria3.categoria, pelicula3.nombrePelicula)
        else:
            return "Error."
eleccion1=Cliente(categoria1,pelicula1, "Jordi")
print(eleccion1.verPelicula())
eleccion1=Cliente(categoria2,pelicula2, "Kevin")
print(eleccion1.verPelicula())
eleccion1=Cliente(categoria3,pelicula3, "Rubén")
print(eleccion1.verPelicula())