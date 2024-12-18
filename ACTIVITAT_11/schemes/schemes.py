#Per dades de partida
def dadaPartida_schema(dada) -> dict:
    return {"dada": dada}

def dadesPartida_schema(dades) -> dict:
    return [dadaPartida_schema(dada) for dada in dades]

#Alfabet
def alfabet_schema(alfabet) -> dict:
    return  {"alfabet": alfabet[0]}

#Per textos de estadistiques
def estadisticaTxt_schema(estadistica) -> dict:
    return {"comencar": estadistica[0],
            "punts" : estadistica[1],
            "total" : estadistica[2],
            "guanyades": estadistica[3],
            "millor": estadistica[4]}

def estadistiquesTxt_schema(estadistiques) -> dict:
    return [estadisticaTxt_schema(estadistica) for estadistica in estadistiques]

#Per dades estadistiques
def estadistica_schema(estadistica) -> dict:
    return {"nom": estadistica[0],
            "punts" : estadistica[1],
            "total" : estadistica[2],
            "guanyades": estadistica[3],
            "dataMillor": estadistica[4],
            "millorPuntuacio": estadistica[5]}

def estadistiques_schema(estadistiques) -> dict:
    return [estadistica_schema(estadistica) for estadistica in estadistiques]


### Activitat 12 ###
def jugador_schema(jugador) -> dict:
    return {
        "id": jugador[0],
        "username": jugador[1],
        "password": jugador[2],
        "partidesJugades": jugador[3],
        "partidesGuanyades": jugador[4],
        "dataMillorPuntuacio": jugador[5],
        "millorPuntuacio": jugador[6]
    }

def jugadors_schema(jugadors) -> dict:
    return [jugador_schema(jugador) for jugador in jugadors]

def partida_schema(partida) -> dict:
    return {
        "id": partida[0],
        "punts": partida[1],
        "estatPartida": partida[2],
        "paraula": partida[3],
        "estatParaula": partida[4],
        "intents": partida[5],
        "jugadorId": partida[6]
    }

def partides_schema(partides) -> dict:
    return [partida_schema(partida) for partida in partides]

def paraula_schema(paraula) -> dict:
    return {
        "paraula": paraula[0],
        "tematica": paraula[1]
    }

def paraules_schema(paraules) -> dict:
    return [paraula_schema(paraula) for paraula in paraules]