## JUGADOR ##

def eliminarJugador(connection, idJugador):
    conn = connection
    cursor = conn.cursor()
    try:
        query = f''' DELETE FROM jugador WHERE id = {idJugador} '''
        cursor.execute(query)
        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut eliminar el jugador"

    cursor.close()
    return "Success: Jugador eliminat correctament"

## PARTIDA ##

def eliminarPartida(connection, idPartida):
    conn = connection
    cursor = conn.cursor()
    try:
        query = f''' DELETE FROM partida WHERE id = {idPartida} '''
        cursor.execute(query)
        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut eliminar la partida"

    cursor.close()
    return "Success: Partida eliminada correctament"


## INICI PANTALLA ##

def eliminarIniciPantalla(connection, idioma):
    conn = connection
    cursor = conn.cursor()
    try:
        query = f''' DELETE FROM inici_pantalla WHERE idioma = '{idioma}' '''
        cursor.execute(query)
        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut eliminar el element d'inici"

    cursor.close()
    return "Success: Element d'inici eliminat correctament"


## Paraula ##

def eliminarParaula(connection, paraula):
    conn = connection
    cursor = conn.cursor()
    try:
        query = f''' DELETE FROM paraules_penjat WHERE paraula = '{paraula.paraula}' AND tematica = '{paraula.tematica}' '''
        cursor.execute(query)
        conn.commit()
    except:
        # En cas de haberi cap error fem rollback
        conn.rollback()
        cursor.close()
        return "Error: No s'ha pugut eliminar la paraula"

    cursor.close()
    return "Success: Paraula eliminada correctament"