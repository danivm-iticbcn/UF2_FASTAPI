## JUGADOR ##

def insertarJugador(connection, jugador):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f'''INSERT INTO jugador VALUES ({jugador.id}, '{jugador.username}', '{jugador.password}', 
                    {jugador.partidesJugades}, {jugador.partidesGuanyades}, '{jugador.dataMillorPuntuacio}', 
                    {jugador.millorPuntuacio}) '''

        cursor.execute(query)

        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut insertar l'usuari"

    cursor.close()

    return "Success: Usuari insertat correctament"


## PARTIDA ##

def insertarPartida(connection, partida):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f'''INSERT INTO partida VALUES ({partida.id}, {partida.punts}, '{partida.estatPartida}', 
                    '{partida.paraula}', '{partida.estatParaula}', {partida.intents}, 
                    {partida.jugadorId}) '''

        cursor.execute(query)

        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut insertat la partida"

    cursor.close()

    return "Success: Partida insertada correctament"

## INICI PANTALLA ##

def insertarIniciPantalla(connection, iniciPartida):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f'''INSERT INTO inici_pantalla VALUES ('{iniciPartida.idioma}', '{iniciPartida.lletres}', '{iniciPartida.textIniciar}', 
                    '{iniciPartida.textPunts}', '{iniciPartida.textTotal}', '{iniciPartida.textGuanyades}', 
                    '{iniciPartida.textMillorPuntuacio}') '''

        cursor.execute(query)

        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut insertar el element d'inici"

    cursor.close()

    return "Success: Element d'inici insertat correctament"

## PARAULA ##

def insertarParaula(connection, paraula):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f'''INSERT INTO paraules_penjat VALUES ('{paraula.paraula}', '{paraula.tematica}') '''

        cursor.execute(query)

        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut insertar la paraula"

    cursor.close()

    return "Success: Paraula d'inici insertat correctament"