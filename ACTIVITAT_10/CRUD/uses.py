def read_themes(connection):
    conn = connection
    cursor = conn.cursor()

    query = "SELECT DISTINCT tematica from paraules_penjat"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result



def read_word(connection, theme):
    conn = connection
    cursor = conn.cursor()

    query = f"SELECT paraula from paraules_penjat where tematica = '{theme}'"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result