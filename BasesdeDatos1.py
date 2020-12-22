#creacion de bases de datos BBDD
#CONECION CON BBDD Y INSERCION DE REGISTROS EN BBDD

#Sistemas gestores de bases de datos y python (SQL Structure Query Language)
#SQL lenguaje estructurado de cunsulta. Otros son Mysql y SQlite

# Pasos a seguir
#1 Abrir - Crear conexion
#2 crear Cursor
#3 ejecutar query (consulta) SQL
#4 Manejar los resultados de la query (CRUD: Create, Read, Update, Delete)
#5 cerrar puntero
#6 cerrar conexion

import sqlite3

#1 Abrir - Crear conexion 

miConexion=sqlite3.connect("PrimeraBase")

#2 crear puntero o cursor
miCursor=miConexion.cursor()

#3 ejecutar query (consulta) SQL
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") 
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# variosProductos=[

# ("Camiseta",10, "DEPORTES"),
# ("Jarron",90, "CERAMICA"),
# ("Xbox",1000, "JUEGO")
# ]

# #para insertar muchos datos, tienes que usar tantos ???(interrogantes) como columnas en tu BD
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

# miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
print(variosProductos)

for producto in variosProductos:
    print("Nombre del articulo: ", producto[0], "seccion: ", producto[2])


miConexion.commit()


#6 cerrar conexion
miConexion.close()