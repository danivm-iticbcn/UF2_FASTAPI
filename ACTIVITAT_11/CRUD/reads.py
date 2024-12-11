def llegirNombreIntentsPartida(connection, id_jugador):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT intents from partida p JOIN jugador j on (p.jugador_id = j.id) WHERE j.id = {id_jugador} AND estat_partida = true"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()

    return result


def llegirAlfabet(connection, idioma):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT lletres FROM inici_pantalla WHERE idioma = '{idioma}'"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()

    return result


def llegirTextEstadistiques(connection, idioma):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT text_iniciar, text_punts, text_total, text_guanyades, text_millor_puntuacio FROM inici_pantalla WHERE idioma = '{idioma}'"
    cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()

    return result

def llegirEstadistiquesJugador(connection, id_jugador):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT j.username, p.punts, j.partides_jugades, j.partides_guanyades, j.data_millor_puntuacio, j.millor_puntuacio FROM jugador j JOIN partida p ON (j.id = p.jugador_id) WHERE j.id = {id_jugador} AND p.estat_partida = true"
    cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()

    return result