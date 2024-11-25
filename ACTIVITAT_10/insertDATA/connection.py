import psycopg2 as pg

def createConection():
    conn = pg.connect(
        database="postgres",
        user="dani",
        password="system",
        host="localhost",
        port="5432"
    )

    print("Connexió establerta correctament")
    return conn