def instrucciones ():
    pass

def pasos_para_jugar ():
    lista_opciones = ["piedra", "papel", "tijeras", "lagartija", "spock"]
    mano_jugador = (input("Elige una de las opciones a continuación: Piedra, Papel, Tijeras, Lagartija o Spock: ")).lower()
    mano_npc = lista_opciones[r.randint(0,4)]