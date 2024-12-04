def llegirComencarText(connection, idioma):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT text_iniciar from inici_pantalla WHERE idioma = '{idioma}'"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()

    return result


def llegirNombreIntentsPartida(connection, id_jugador):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT intents from partida p JOIN jugador j on (p.jugador_id = j.id) WHERE j.id = {id} AND estat_partida = true"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()

    return result