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

def pasos_para_jugar ():
    lista_opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]
    mano_jugador = (input("Elige una de las opciones a continuación: Piedra, Papel, Tijeras, Lagartija o Spock: ")).lower()
    mano_npc = lista_opciones[r.randint(0,4)]