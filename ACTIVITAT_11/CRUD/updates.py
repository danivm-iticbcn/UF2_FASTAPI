from dns.e164 import query


def incrementarIntents(connection, id_jugador):
    conn = connection
    cursor = conn.cursor()

    try:
        #Obtenim id de partida per saber quina hem de incrementar
        queryObtenirIdPartida = f"SELECT p.id from partida p join jugador j on (p.jugador_id = j.id) WHERE j.id = {id_jugador} AND estat_partida = true"
        cursor.execute(queryObtenirIdPartida)
        idPartida = cursor.fetchone()

        #Incrementem
        queryIncrementar = f"UPDATE partida SET intents = intents + 1 WHERE id = {idPartida[0]}"
        cursor.execute(queryIncrementar)

        conn.commit()
    except:
        #En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "No s'ha pugut incrementar el numero d'intents"

    cursor.close()

    return "Intents incrementat correctament"