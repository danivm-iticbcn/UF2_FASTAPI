#Per textos inicials
def txt_schema(text) -> dict:
    return {"text": text}

def txts_schema(texts) -> dict:
    return [txt_schema(text) for text in texts]

#Per dades de partida
def dadaPartida_schema(dada) -> dict:
    return {"dada": dada}

def dadesPartida_schema(dades) -> dict:
    return [dadaPartida_schema(dada) for dada in dades]