import psycopg2 as pg

def createConection():
    conn = pg.connect(
        database="postgres",
        password="system",
        host="localhost",
        user="dani",
        port="5432"
    )

    print("Connexió establerta correctament")
    return conn