import connection
import pandas as pd

paraules = pd.read_csv('paraules_temàtica_penjat.csv')

#Establim connexio am la db
conn = connection.createConection()
cursorConn = conn.cursor()

#Introduim les paraules
for x in range(len(paraules)):
    paraula = paraules['WORD'][x]
    tematica = paraules['THEME'][x]

    query = f"INSERT INTO paraules_penjat(paraula, tematica) values('{paraula}', '{tematica}')"
    cursorConn.execute(query)

#Desem i tanquem connexio
conn.commit()
conn.close()



