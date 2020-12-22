# creacion de campos clave: Un campo clave es un dato que define de manera única 
#cada registro de una tabla. Un campo clave no puede tener valores nulos y siempre 
#debe tener un índice único. Los campos clave son columnas de información que se 
#encuentran integrados en una tabla que nos identifican de 
#forma única cada registro de la misma.


import sqlite3
miConexion=sqlite3.connect("Gestion de productos Sierra Maestra")
miCursor=miConexion.cursor()


# miCursor.execute('''
	
# 	CREATE TABLE PRODUCTOS (
#     CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY, 
#     NOMBRE_ARTICULO VARCHAR(50),
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))
# ''')

productos=[
    
    ("AR01","MEZCLUM 400g", 17000, "HIDROPONICO"),
    ("AR02","MEZCLUM 200g", 9000, "HIDROPONICO"),
    ("AR03","HIERBA BUENA 500g", 9000, "TIERRA"),
    ("AR04","HIERBA BUENA 250g", 9000, "TIERRA"),

]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",productos)
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR12', 'OREGANO 500', 9000 , 'TIERRA' )")

miConexion.commit()
miConexion.close()