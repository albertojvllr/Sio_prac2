import functions as f
import matplotlib.pyplot as plt
import numpy as np
def query1(cursor):

    print("Quina proporcio de contingut es troba en mes d'una plataforma de streaming?")

    query1 = f.read_sql_file('sql/prop_pel_plataforma.sql')
    result1 = f.execute_query(cursor, query1)

    # Valores para el gráfico
    values = [result1[0][0]-result1[0][1], result1[0][1]]

    # Etiquetas para el gráfico
    labels = ['Títulos únicos', 'Títulos en otras plataformas']

    # Crea el diagrama de sectores
    plt.pie(values, labels=labels, autopct='%1.1f%%')

    # Añade un título
    plt.title('Proporción de títulos en otras plataformas')

    # Muestra el gráfico
    plt.show()
    
def query2(cursor):

    print("Quina es la distribucio entre s`eries i pel·licules a cada plataforma de streaming?")

    # Ejecuta la consulta y obtén los resultados
    query2 = f.read_sql_file('sql/tys_plataforma.sql')
    result2 = f.execute_query(cursor, query2)

    # Separa los resultados en tres listas: una para los nombres de las plataformas y dos para los valores de las barras
    platform_names = [row[0] for row in result2]
    bar1_values = [row[1] for row in result2]
    bar2_values = [row[2] for row in result2]

    # Crea una lista de números del 1 al número de plataformas para usar como las posiciones en el eje x del gráfico
    x_positions = np.arange(len(platform_names))

    # Define el ancho de las barras
    bar_width = 0.35

    # Crea el gráfico de barras
    plt.bar(x_positions - bar_width/2, bar1_values, bar_width, label='Series')
    plt.bar(x_positions + bar_width/2, bar2_values, bar_width, label='Pelicules')

    # Añade los nombres de las plataformas como etiquetas en el eje x
    plt.xticks(x_positions, platform_names)

    # Añade una leyenda
    plt.legend()

    # Añade un título
    plt.title('Distribució entre series i pel·lícules a cada plataforma de streaming')

    # Muestra el gráfico
    plt.show()
    
def query3(cursor):
    print("Quins son els deu actors que han protagonitzat mes pel·licules?")

    # Ejecuta la consulta y obtén los resultados
    query3 = f.read_sql_file('sql/persones_mes_contingut.sql')
    result3 = f.execute_query(cursor, query3)

    # Separa los nombres de los actores y la cantidad de títulos en dos listas
    actors = [row[0] for row in result3[:10]]
    titles = [row[1] for row in result3[:10]]

    # Crea el gráfico de barras horizontales
    plt.barh(actors, titles, color='orange')

    # Añade un título y etiquetas a los ejes
    plt.title('Els 10 actors que ha protagonitzat més pel·lícules')
    plt.xlabel('Cantidad de títuls')
    plt.ylabel('Noms dels actors')

    # Cambia los incrementos del eje x a 5
    plt.xticks(range(0, max(titles) + 1, 5))

    # Muestra el gráfico
    plt.show()
    
def query4(cursor):
    print("Hi ha alguna zona del mon que hagi produit molt mes contingut que la resta?")
    query4 = f.read_sql_file('sql/pais_mes.sql')
    result4 = f.execute_query(cursor, query4)

    # Separa los nombres de los países, la cantidad de series y la cantidad de películas en tres listas
    countries = [row[0] for row in result4[:10]]
    series = [row[2] for row in result4[:10]]
    movies = [row[3] for row in result4[:10]]

    # Crea una lista de números para el eje x
    x = np.arange(10)

    # Crea las barras para las series y las películas
    plt.bar(x - 0.2, series, 0.4, label='Series')
    plt.bar(x + 0.2, movies, 0.4, label='Películas')

    # Añade un título y etiquetas a los ejes
    plt.title('Cantidad de series y películas por país')
    plt.xlabel('País')
    plt.ylabel('Cantidad')

    # Añade una leyenda
    plt.legend()

    # Cambia las etiquetas del eje x a los nombres de los países
    plt.xticks(x, countries)

    # Muestra el gráfico
    plt.show()

    # Ejecuta la consulta y obtén los resultados
    result4 = f.execute_query(cursor, query4)

    # Separa los nombres de los países y la cantidad total de títulos en dos listas
    countries = [row[0] for row in result4[:10]]
    titles = [row[1] for row in result4[:10]]

    # Crea el diagrama de sectores
    plt.pie(titles, labels=countries, autopct='%1.1f%%')

    # Añade un título
    plt.title('Cantidad de títulos por país')

    # Muestra el gráfico
    plt.show()
    
def query5(cursor):
    print("Quina plataforma de streaming te mes contingut d'accio? I la que menys?")

    query5 = f.read_sql_file('sql/mes_accio.sql')
    result5 = f.execute_query(cursor, query5)

    # Separa los nombres de las plataformas y la cantidad de títulos de acción en dos listas
    platforms = [row[0] for row in result5]
    action_titles = [row[1] for row in result5]

    # Crea el gráfico de barras
    plt.bar(platforms, action_titles, color='green')

    # Añade un título y etiquetas a los ejes
    plt.title('Plataforma de streaming con más títulos de acción')
    plt.xlabel('Plataforma')
    plt.ylabel('Cantidad de títulos')

    # Muestra el gráfico
    plt.show()
    
def query6(cursor):
    print("Hi ha persones que hagin actuat i dirigit una mateixa serie o pel·licula?")

    query6 = f.read_sql_file('sql/actuat_i_dirigit_mes_pel.sql')
    result6 = f.execute_query(cursor, query6)

    # Separa los nombres y el número de títulos en dos listas
    nombres = [row[0] for row in result6[:30]]
    num_titols = [row[1] for row in result6[:30]]

    # Crea el gráfico de barras verticales
    plt.bar(nombres, num_titols)

    # Añade un título y etiquetas a los ejes
    plt.title('Número de títulos por actor/director')
    plt.xlabel('Actor/Director')
    plt.ylabel('Número de títulos')

    # Rota las etiquetas del eje x para que se vean mejor
    plt.xticks(rotation=90)

    # Muestra el gráfico
    plt.show()

def query7(cursor):
    print("Quina es la distribucio de duracio de les series a cada plataforma de streaming? I de les pel·licules?")
    query7 = f.read_sql_file('sql/distr_duracio.sql')
    result7 = f.execute_query(cursor, query7)
    
    # Separa los nombres de las plataformas, las duraciones de las series y las duraciones de las películas en tres listas
    platforms = [row[0] for row in result7]
    series_durations = [row[1] for row in result7]
    movie_durations = [row[2] for row in result7]

    # Crea una matriz de índices para las barras
    indices = np.arange(len(platforms))

    # Crea las barras para las series
    plt.bar(indices - 0.2, series_durations, 0.4, label='Series')

    # Crea las barras para las películas
    plt.bar(indices + 0.2, movie_durations, 0.4, label='Películas')

    # Añade un título y etiquetas a los ejes
    plt.title('Duración media por plataforma')
    plt.xlabel('Plataforma')
    plt.ylabel('Duración media')

    # Añade las etiquetas de las plataformas en el eje x
    plt.xticks(indices, platforms)

    plt.yticks(np.arange(0, round(max(max(series_durations), max(movie_durations)))+1, 5))

    # Añade una leyenda
    plt.legend()

    # Muestra el gráfico
    plt.show()

def query8(cursor):
    print("Quina plataforma de streaming te millor contingut?")
    query8 = f.read_sql_file('sql/millor_contingut.sql')
    result8 = f.execute_query(cursor, query8)

    # Separa los nombres de las plataformas y la valoración media en dos listas
    platforms = [row[0] for row in result8]
    ratings = [row[1] for row in result8]

    # Crea el gráfico de barras
    plt.bar(platforms, ratings, color='purple')

    # Añade un título y etiquetas a los ejes
    plt.title('Valoración media por plataforma')
    plt.xlabel('Plataforma')
    plt.ylabel('Valoración media')

    plt.yticks(np.arange(0, 10.5, 0.5))
    
    # Muestra el gráfico
    plt.show()
    
def query9(cursor):
    print("Cuáles son los países que más películas y series producen de cada genero?")
    query9 = f.read_sql_file('sql/pais_genero.sql')
    result9 = f.execute_query(cursor, query9)


    genres = [row[0] for row in result9]
    countries = [row[1] for row in result9]
    series = [row[2] for row in result9]
    movies = [row[3] for row in result9]

    # Crea un array con las posiciones de las barras en el eje X
    bar_positions = np.arange(len(genres))

    # Crea el gráfico de barras para las series
    plt.bar(bar_positions, series, color='b')

    # Crea el gráfico de barras para las películas, apiladas encima de las series
    plt.bar(bar_positions, movies, bottom=series, color='r')

    # Añade un título y etiquetas a los ejes
    plt.title('Cantidad de títulos por género y país')
    plt.xlabel('Género y país')
    plt.ylabel('Cantidad de títulos')

    # Añade las etiquetas de los géneros y países en el eje X
    plt.xticks(bar_positions, [f'{g}, {c}' for g, c in zip(genres, countries)], rotation=90)

    # Ajusta los límites del eje x
    plt.xlim(min(bar_positions) - 1, max(bar_positions) + 1)

    # Añade una leyenda
    plt.legend(['Series', 'Películas'])

    # Muestra el gráfico
    plt.show()
    
def query10(cursor):
    print("En quina decada es van fer les millor pel·licules?")
    query10 = f.read_sql_file('sql/millor_pel_anys.sql')
    result10 = f.execute_query(cursor, query10)

    # Separa los años y la valoración media en dos listas
    years = [str(row[0]) for row in result10]
    ratings = [row[1] for row in result10]

    # Ajusta el tamaño de la figura
    plt.figure(figsize=(10, 5))

    # Crea el gráfico de barras
    plt.bar(years, ratings, color='r')

    # Añade un título y etiquetas a los ejes
    plt.title('Valoración media por año')
    plt.xlabel('Año')
    plt.ylabel('Valoración media')

    # Ajusta los límites del eje y
    plt.ylim(5.5, 7)

    # Rota las etiquetas del eje x y ajusta su tamaño
    plt.xticks(rotation=45, fontsize=8)

    # Muestra el gráfico
    plt.show()
    
def query11(cursor):
    print("Les series i pel·licules mes ben valorades solen ser d'un genere en concret?")
    query11 = f.read_sql_file('sql/gen_val.sql')
    result11 = f.execute_query(cursor, query11)

    # Separa los géneros y las valoraciones en dos listas
    genres = [row[0] for row in result11]
    ratings = [row[1] for row in result11]

    # Crea el diagrama de barras horizontales
    plt.barh(genres, ratings, color='b')

    # Añade un título y etiquetas a los ejes
    plt.title('Valoración media por género')
    plt.xlabel('Valoración media')
    plt.ylabel('Género')

    # Ajusta los límites del eje x
    plt.xlim(5, 7.5)

    # Muestra el diagrama
    plt.show()