# Activitat 11

## Esquema de la base de dades:
<img src="readme_img/esquema_db.jpg"/>

Queries:

A la taula de jugador he afegit el camp de data per la millor puntuacio per tenir millor estructura de dades.

- Jugador:
<img src="readme_img/jugador.png"/>


- Partida
<img src="readme_img/partida.png"/>


- Inici pantalla:
<img src="readme_img/inici_pantalla.png"/>

## END POINTS

### Get Informació inicial de la pantalla

Per temes d'optimitzacio de codi he obviat el end point on tan sols recuperem el text de començar partida i he ficat un on rescatem totes les dades inicials que es demanen.

<img src="readme_img/info_inicial.png"/>


### Get intents de partida

En aquest pas tan sols rebrem el numero de intents actuals de la partida:

<img src="readme_img/n_intents.png"/>

### Post augmentar intents

A continuació augmentarem el numero de intents de la partida, a més retornara el nº de intents.

<img src="readme_img/augmentar_intents.png"/>

### Get alfabet

Aqui rebrem un string amb tots els caracters disponibles:

<img src="readme_img/alfabet.png"/>

### Get puntuació del jugador

Per finalitzar agafarem les dades dels punts del jugador:

<img src="readme_img/puntuacio_jugador.png"/>