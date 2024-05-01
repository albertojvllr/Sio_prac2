import mysql.connector # type: ignore
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import functions as f
import grafics as g

config = {
    'user': "root",
    'password': "776472",
    'host': "localhost",
    'database': "sio_bd",
}

conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

g.query1(cursor)
g.query2(cursor)
g.query3(cursor)
g.query4(cursor)
g.query5(cursor)
g.query6(cursor)
g.query7(cursor)
g.query8(cursor)
g.query9(cursor)
g.query10(cursor)
g.query11(cursor)


