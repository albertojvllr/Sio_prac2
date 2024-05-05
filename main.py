import mysql.connector # type: ignore
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import functions as f
import grafics as g
import algoritme as alg



config = {
    'user': "root",
    'password': "",
    'host': "localhost",
    'database': "sio_bd",
}

conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

while(True):
    print("Selecciona una opción:")
    print("1. Gràfics - 2.Algoritme de Recomanació - 3. Sortir")
    input1 = input()
    if input1=="1":
        print("Selecciona un gràfic:")
        print("1. Quina proporcio de contingut es troba en mes d'una plataforma de streaming?")
        print("2. Quina es la distribucio entre s`eries i pel·licules a cada plataforma de streaming?")
        print("3. Quins son els deu actors que han protagonitzat mes pel·licules?")
        print("4. Hi ha alguna zona del mon que hagi produit molt mes contingut que la resta?")
        print("5. Quina plataforma de streaming te mes contingut d'accio? I la que menys?")
        print("6. Hi ha persones que hagin actuat i dirigit una mateixa serie o pel·licula?")
        print("7. Quina es la distribucio de duracio de les series a cada plataforma de streaming? I de les pel·licules?")
        print("8. Quina plataforma de streaming te millor contingut?")
        print("9. Cuáles son los países que más películas y series producen de cada genero?")
        print("10. En quina decada es van fer les millor pel·licules?")
        print("11. Les series i pel·licules mes ben valorades solen ser d'un genere en concret?")
        input2 = input()
        if input2=="1":
            g.query1(cursor)
        if input2=="2":
            g.query2(cursor)
        if input2=="3":
            g.query3(cursor)
        if input2=="4":
            g.query4(cursor)
        if input2=="5":
            g.query5(cursor)
        if input2=="6":
            g.query6(cursor)
        if input2=="7":
            g.query7(cursor)
        if input2=="8":
            g.query8(cursor)
        if input2=="9":
            g.query9(cursor)
        if input2=="10":
            g.query10(cursor)
        if input2=="11":
            g.query11(cursor)
    if input1=="2":
        #Algoritme de recomanació
        print("Fltratge:")
        print("Podeu afegir tots els filtres que vulguessiu, \nen cas de no voler implementar un filtre sol ho teniu que deixar en blanc:")
        tipo = input("1. Películas\n2. Series\n")
        if not tipo:
            tipo = None        
        genero = input("Quins generes voldries veure?")
        if not genero:
            genero = None
        duracionMin = input("Quina es la duracio minima que vols? ")
        if not duracionMin:
           duracionMin = None
        duracionMax = input("Quina es la duracio maxima que vols? ")
        if not duracionMax:
            duracionMax = None        
        actor =  input("Vols que actui algu en concret? ")
        if not actor:
            actor = None
        plataforma =  input("Quina plataforma vols? ")
        if not plataforma:
            plataforma = None
        valMin =  input("Quina valoracio minima vols? ")
        if not valMin:
            valMin = None
        alg.algortime(tipo, genero, duracionMin, duracionMax, actor, plataforma, valMin, cursor)
        break
    if input1=="3":
        break    



