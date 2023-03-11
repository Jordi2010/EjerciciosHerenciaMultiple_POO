# Ejercicios de herencia múltiple.
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

# Ejercicio 3. Desarrolla en POO el siguiente ejercicio. Para comenzar necesitamos 3 clases Juego,
# jugador 1 y jugador 2. Donde el jugador 1 debe de tener un luchador puede ser cualquiera y un poder de
# 100%. El jugador 2 debe de tener un luchador, puede ser cualquiera un poder 100%.
# Cuando herede los jugadores 1 y 2 al juego debe de realizar la siguiente lógica. Si el jugador 1 lanza un
# golpe al jugador 2 restarle 30% de vida y mostrar el total de vida del jugador afectado y hacer lo mismo
# con el otro jugador. Quien golpea primero queda a criterio suyo.

from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador2 import luchador2

class Juego(Jugador1, Jugador2):
    def luchar():
        vida=(luchador2.poder2-30)
        return "{} (jugador {}) acaba de lanzar un golpe de 30% a {} (jugador {}), ahora el nivel de vida de {} (jugador {}) es: {}%.".format(Jugador1.nombre1, Jugador1.njugador1, Jugador2.nombre2, Jugador2.njugador2,Jugador2.nombre2, Jugador2.njugador2,vida)
pelea=Juego
print(pelea.luchar())