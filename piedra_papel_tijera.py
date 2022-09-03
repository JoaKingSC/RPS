import random
from traceback import print_tb

def eleccion(numero):
    elegido = str()
    if numero == 1:
        elegido = "Piedra"
    elif numero == 2:
        elegido = "Papel"
    elif numero == 3:
        elegido = "Tijera"

    return elegido


def impr_eleccion():
    print("Usuario ha elegido: " + usuario)
    print("PC ha elegido: " + pc)

seguir_jugando = 1;
while seguir_jugando == 1:
    print("Elige: 1.Piedra 2.Papel 3.Tijera")
    usuario = int(input())

    while usuario > 3 or usuario < 1:
        usuario = int(input("Debe ser un numero entre 1 y 3: "))

    pc = random.randint(1, 3)

    usuario = eleccion(usuario)
    pc = eleccion(pc)

    print()

    if usuario == pc:
        print("Empate")
        impr_eleccion()
    elif (usuario == "Piedra" and pc == "Tijera") or (usuario == "Papel" and pc == "Piedra") or (usuario == "Tijera" and pc == "Papel"):
        print("Has Ganado!")
        impr_eleccion()
    else:
        print("Has Perdido :(")
        impr_eleccion()

    print()
    print("Seguir Jugando: 1")
    print("Dejar de Jugar: Cualquier numero")
    seguir_jugando = int(input())
    print()