def instrucciones ():
    pass

import random as r

def pasos_para_jugar ():
    lista_opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]
    mano_jugador = (input("Elige una de las opciones a continuación: Piedra, Papel, Tijeras, Lagartija o Spock: ")).lower()
    mano_npc = lista_opciones[r.randint(0,4)]
    if mano_jugador == mano_npc:
        print("Empatamos nub.")
    elif (mano_jugador == "piedra" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "paper" and (mano_npc == "piedra" or mano_npc == "spock")) or (mano_jugador == "tijeras" and (mano_npc == "paper" or mano_npc == "lagartija")) or (mano_jugador == "lagartija" and (mano_npc == "paper" or mano_npc == "spock")) or (mano_jugador == "spock" and (mano_npc == "piedra" or mano_npc == "tijeras")):
        print("Me ganaste crack.")
    elif (mano_jugador == "piedra" and (mano_npc == "paper" or mano_npc == "spock")) or (mano_jugador == "paper" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "tijeras" and (mano_npc == "piedra" or mano_npc == "spock")) or (mano_jugador == "lagartija" and (mano_npc == "piedra" or mano_npc == "tijeras")) or (mano_jugador == "spock" and (mano_npc == "paper" or mano_npc == "lagartija")):
        print("Perdiste nub.")