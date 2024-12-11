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