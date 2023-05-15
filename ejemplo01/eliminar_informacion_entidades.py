"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad
nombre = "LDU"
pais = "Ecuador"
ciudad = "Quito"
titulos = 10
cadena_sql = """INSERT INTO Equipo (nombre, pais, ciudad, titulos) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, pais, ciudad, titulos)

# ejecutar el SQL
cursor.execute(cadena_sql)

# nuevo registo
nombre = "BARCELONA"
pais = "Ecuador"
ciudad = "Guayaquil"
titulos = 15
cadena_sql = """INSERT INTO Equipo (nombre, pais, ciudad, titulos) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, pais, ciudad, titulos)
cursor.execute(cadena_sql)

# nuevo registo
nombre = "EMELEC"
pais = "Ecuador"
ciudad = "Guayaquil"
titulos = 12
cadena_sql = """INSERT INTO Equipo (nombre, pais, ciudad, titulos) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, pais, ciudad, titulos)
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

print("-------------------------------------------------")
# inicio proceso de elminación
cadena = """DELETE from Equipo WHERE nombre='%s'""" % ("BARCELONA")
cursor.execute(cadena)
conn.commit()


# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))


# cerrar el enlace a la base de datos (recomendado)
cursor.close()
