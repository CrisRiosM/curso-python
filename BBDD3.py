
import sqlite3
miConexion=sqlite3.connect("Gestion de productos Sierra Maestra")
miCursor=miConexion.cursor()


# miCursor.execute('''
	
# 	CREATE TABLE PRODUCTOS_SIERRA (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#     NOMBRE_ARTICULO VARCHAR(50),
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))
# ''')

# productos=[
    
#     ("MEZCLUM 400g", 17000, "HIDROPONICO"),
#     ("MEZCLUM 200g", 9000, "HIDROPONICO"),
#     ("HIERBA BUENA 500g", 9000, "TIERRA"),
#     ("HIERBA BUENA 250g", 9000, "TIERRA"),

# ]



# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",productos)
# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR12', 'OREGANO 500', 9000 , 'TIERRA' )")

#CRUD

#Consulta de alguna seccion: read

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='HIDROPONICO'")
# productos=miCursor.fetchall()
# print(productos)

#Actualizar: update
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=17500 WHERE NOMBRE_ARTICULO='MEZCLUM 400g'" )




miConexion.commit()
miConexion.close()