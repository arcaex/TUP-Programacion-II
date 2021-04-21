import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

cursor.execute("""SELECT Paises.continente,Ciudades.nombre FROM Paises,Ciudades WHERE Paises.id_pais=Ciudades.id_pais AND Paises.id_pais=8""")

conexion.commit()

rowsCursor = cursor.fetchall()

for fila in rowsCursor:
    print(fila)

conexion.close()