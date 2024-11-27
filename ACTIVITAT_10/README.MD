# Activitat 10

## Inserció a la base de dades

Hem de tenir un taula i un fitxer .csv amb les dades:

<img src="readme_img/taula.png"/>

Una vegada llegim el fitxer .csv fem un recorregut del DataFrame 
i per cada fila (paraula, tematica), inserim un registre amb les dades.

<img src="readme_img/dades.png"/>


## Obtenir tematiques

Aprofitarem la conexio que hem fet abans i farme un select DISTINCT 
de les tematiques, amb aixo ja podrem tractar les dades i obtenir 
el JSON amb les tamatiques:

<img src="readme_img/tematiques_swagger.png"/>

## Obtenir una paraula a l'atzar

A continuació volem obtenir una paraula a l'atzar filtrant per tematica asi que
haurem de rebre la tematica per aconseguir tan sols les paraules d'aquesta i
agafar una random, exemples:

- 1
<img src="readme_img/paraula_swagger1.png"/>


- 2
<img src="readme_img/paraula_swagger2.png"/>


- 3
<img src="readme_img/paraula_swagger3.png"/>
