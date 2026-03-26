def instrucciones ():
    mensaje = """
    Bienvenido a Piedra, Papel, Tijera, Lagartija, Spock

    Reglas del juego:
    - Piedra aplasta Tijera y Lagartija
    - Papel cubre Piedra y refuta a Spock
    - Tijera corta Papel y decapita Lagartija
    - Lagartija come Papel y envenena a Spock
    - Spock vaporiza Piedra y rompe Tijera

    Cada opción gana contra 2 y pierde contra 2.

    Elige una opción:
    1. Piedra
    2. Papel
    3. Tijera
    4. Lagartija
    5. Spock
    """

    print(mensaje)

import random as r

def pasos_para_jugar ():
    lista_opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]
    mano_jugador = (input("Elige una de las opciones a continuación: Piedra, Papel, Tijeras, Lagartija o Spock: ")).lower()
    mano_npc = lista_opciones[r.randint(0,4)]
    if mano_jugador == mano_npc:
        print("Empatamos nub.")
    elif (mano_jugador == "piedra" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "pape" and (mano_npc == "piedra" or mano_npc == "spock")) or (mano_jugador == "tijeras" and (mano_npc == "pape" or mano_npc == "lagartija")) or (mano_jugador == "lagartija" and (mano_npc == "pape" or mano_npc == "spock")) or (mano_jugador == "spock" and (mano_npc == "piedra" or mano_npc == "tijeras")):
        print("Me ganaste crack.")
    elif (mano_jugador == "piedra" and (mano_npc == "pape" or mano_npc == "spock")) or (mano_jugador == "pape" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "tijeras" and (mano_npc == "piedra" or mano_npc == "spock")) or (mano_jugador == "lagartija" and (mano_npc == "piedra" or mano_npc == "tijeras")) or (mano_jugador == "spock" and (mano_npc == "pape" or mano_npc == "lagartija")):
        print("Perdiste nub.")