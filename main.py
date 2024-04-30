import mysql.connector # type: ignore

def execute_query(cursor, query):
    try:
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

config = {
    'user': "root",
    'password': "776472",
    'host': "localhost",
    'database': "sio_bd",
}

conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

#Primeres preguntes

query1 = read_sql_file('sql/prop_pel_plataforma.sql')
query2 = read_sql_file('sql/tys_plataforma.sql')
query3 = read_sql_file('sql/persones_mes_contingut.sql')
query4 = read_sql_file('sql/pais_mes.sql')
query5 = read_sql_file('sql/mes_accio.sql')
query6 = read_sql_file('sql/actors_mespelicules.sql')

#Segones preguntes

query7 = read_sql_file('sql/distr_duracio.sql')
query8 = read_sql_file('sql/millor_contingut.sql')
query9 = read_sql_file('sql/pais_genero.sql')
query10 = read_sql_file('sql/millor_pel_anys.sql')
query11 = read_sql_file('sql/corr_imdb_tmdb.sql')
query12 = read_sql_file('sql/gen_val.sql')

#Primeres query

print("Quina proporcio de contingut es troba en mes d'una plataforma de streaming?")
execute_query(cursor, query1)
print("Quina es la distribucio entre s`eries i pel·licules a cada plataforma de streaming?")
execute_query(cursor, query2)
print("Quins son els deu actors que han protagonitzat mes pel·licules?")
execute_query(cursor, query3)
print("Hi ha alguna zona del mon que hagi produit molt mes contingut que la resta?")
execute_query(cursor, query4)
print("Quina plataforma de streaming te mes contingut d'accio? I la que menys?")
execute_query(cursor, query5)
print("Hi ha persones que hagin actuat i dirigit una mateixa s`erie o pel·licula?")
execute_query(cursor, query6)

#Segones query

print("Quina es la distribucio de duracio de les series a cada plataforma de streaming? I de les pel·licules?")
execute_query(cursor, query7)
print("Quina plataforma de streaming te millor contingut?")
execute_query(cursor, query8)
print("Cuáles son los países que más películas y series producen de cada genero?")
execute_query(cursor, query9)
print("En quina decada es van fer les millor pel·licules?")
execute_query(cursor, query10)
print("Es correlaciona la valoracio del contingut a IMDB i a TMDB?")
execute_query(cursor, query11)
print("Les series i pel·licules mes ben valorades solen ser d'un genere en concret?")
execute_query(cursor, query12)


cursor.close()
conexion.close() 