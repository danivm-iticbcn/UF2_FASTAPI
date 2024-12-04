from dns.e164 import query


def incrementarIntents(connection, id_jugador):
    conn = connection
    cursor = conn.cursor()

    #Obtenim id de partida per saber quina hem de incrementar
    queryObtenirIdPartida = f"SELECT id from partida p join jugador j on (p.jugador_id = j.id) WHERE j.id = {id} AND estat_partida = true"
    cursor.execute(queryObtenirIdPartida)

    #Incrementem
    idPartida = cursor.fetchone()
    queryIncrementar = f"UPDATE partida SET intents = intents + 1 WHERE id = {idPartida}"
    cursor.execute(queryIncrementar)

    cursor.commit()
    cursor.close()

    return "Intents incrementat correctament"