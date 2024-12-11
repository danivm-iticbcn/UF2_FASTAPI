

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

### Activitat 12 ###

def modificarJugador(connection, jugador):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f'''UPDATE jugador SET username = '{jugador.username}', password = '{jugador.password}', 
                    partides_jugades = {jugador.partidesJugades}, partides_guanyades = {jugador.partidesGuanyades},
                    data_millor_puntuacio = '{jugador.dataMillorPuntuacio}', millor_puntuacio = {jugador.millorPuntuacio}
                    WHERE id = {jugador.id}'''

        cursor.execute(query)

        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "No s'ha pugut modificar l'usuari"

    cursor.close()

    return "Usuari modificat correctament"