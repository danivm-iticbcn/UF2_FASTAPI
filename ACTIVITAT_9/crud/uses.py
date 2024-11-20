def read_users(connection):
    conn = connection
    connCursor = conn.cursor()

    connCursor.execute("SELECT * FROM users")
    result = connCursor.fetchall()
    connCursor.close()
    return result