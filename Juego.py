def instrucciones():
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

def pasos_para_jugar():
    lista_opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]
    mano_jugador = (input()).lower()
    mano_npc = lista_opciones[r.randint(0,4)]
    jugada = 0
    if mano_jugador == mano_npc:
        print(f"Empatamos nub... Ambos elegimos {mano_jugador}.")
        jugada = 1
    elif (mano_jugador == "piedra" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "papel" and (mano_npc == "piedra" or mano_npc == "spock")) or (mano_jugador == "tijeras" and (mano_npc == "papel" or mano_npc == "lagartija")) or (mano_jugador == "lagartija" and (mano_npc == "papel" or mano_npc == "spock")) or (mano_jugador == "spock" and (mano_npc == "piedra" or mano_npc == "tijeras")):
        print(f"Me ganaste crack. Mi {mano_npc} perdió contra tu {mano_jugador}.")
        jugada = 2
    elif (mano_jugador == "piedra" and (mano_npc == "papel" or mano_npc == "spock")) or (mano_jugador == "papel" and (mano_npc == "tijeras" or mano_npc == "lagartija")) or (mano_jugador == "tijeras" and (mano_npc == "piedral" or mano_npc == "spock")) or (mano_jugador == "lagartija" and (mano_npc == "piedra" or mano_npc == "tijeras")) or (mano_jugador == "spock" and (mano_npc == "papel" or mano_npc == "lagartija")):
        print(f"Perdiste nub. Mi {mano_npc} le ganó a tu {mano_jugador}.")
        jugada = 3
    return jugada

instrucciones()
contador = 0
for i in range(999):
    jugada2 = pasos_para_jugar()
    if jugada2 == 2:
        contador += 1
    print(f"Juegos ganados: {contador}")
    revisar = (input("Quieres seguir jugando?: ")).lower()
    if revisar == "no":
        break