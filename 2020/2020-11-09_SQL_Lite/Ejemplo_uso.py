import sqlite3

conexion = sqlite3.connect('base_ejemplo.db')

mail = "graciajorge.sist@gmail.com"

cursor = conexion.cursor()

# cursor.execute("""UPDATE Jugadores SET mail='"""+mail+"""', nick='no-reply', clave='ClaveSecreta123' WHERE id_jugador = 2""")
# cursor.execute("""DELETE FROM Jugadores WHERE mail = 'jgracia@mail.com'""")
# cursor.execute("""INSERT INTO Jugadores (nick,mail,clave) VALUES ("amartinez","amartinez@mail.com","Perro123")""")

cursor.execute("""SELECT mail FROM Jugadores WHERE mail='none@mail.com'""")
conexion.commit()

rows = cursor.fetchall()
for row in rows:
    print(row)

conexion.close()
