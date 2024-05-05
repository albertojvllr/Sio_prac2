from prettytable import PrettyTable
def algortime(tipo, genero, duracioMin, duracioMAx, actor, plataforma, valMin, cursor):
    if tipo == "1":
        tipo_contenido = "MOVIE"
    elif tipo == "2":
        tipo_contenido = "SHOW"
    
    AmpliRecomanacio =  True    
    while AmpliRecomanacio:
        NotNul = True
        while NotNul:
            
            cont = 0
            
            sql = f"""
            SELECT t.titol, t.runtime, t.tipus 
            FROM titols t
            """
            # JOINS
            if actor is not None:
                sql += f"""
                JOIN titols_persones tp ON t.Id = tp.id_titol_persona 
                JOIN persones pe ON tp.ID_persona = pe.id 
                """
            
            if plataforma is not None:
                sql += f"""
                JOIN Titols_Plataforma te ON t.ID = te.Id_Titols_plataforma
                JOIN Plataforma p ON te.Id_Plataforma = p.Id
                """
            
            if valMin is not None:
                sql += f"""
                JOIN titols_imdb im ON t.ID = im.Id_Titols
                JOIN imdb i ON im.id_imdb = i.Id   
                """
            # FILTRATGES
            if tipo is not None:
                sql += f"""
                WHERE t.tipus = '{tipo_contenido}'
                """
            else:
                sql += f"""
                WHERE t.tipus IN ("SHOW", "MOVIE")
                """
            
            if actor is not None:
                sql += f"""
                AND pe.nom = '{actor}'
                """
            
            if plataforma is not None:
                sql += f"""
                AND p.Plataforma = '{plataforma}'
                """
            if genero is not None:
                sql += f"""
                AND t.Id IN (
                    SELECT Id_titols 
                    FROM Titols_Genere 
                    WHERE Id_Genere = (
                        SELECT Id 
                        FROM Generes 
                        WHERE Genere = '{genero}'
                    )
                )
                """
            if duracioMin is not None and duracioMAx is not None:
                sql += f"""
                AND t.runtime >= '{duracioMin}' AND t.runtime <= '{duracioMAx}'
                """
            elif duracioMin is not None:
                sql += f"""
                AND t.runtime >= '{duracioMin}' 
                """        
            elif duracioMAx is not None:
                sql += f"""
                AND t.runtime <= '{duracioMAx}' 
                """           
            
            if valMin is not None:
                sql += f"""
                AND i.score >= '{valMin}'
                """
        
            cursor.execute(sql)
            headers = ["Nom", "Duracio", "Tipus"]
            tabla = PrettyTable(headers)

            for row in cursor.fetchall():
                cont+=1
                tabla.add_row(row)
            
            if cont == 0:
                if actor is not None:
                     actor = None
                elif genero is not None:
                    genero = None
                elif duracioMin is not None:
                    duracioMin = None
                elif duracioMAx is not None:
                    duracioMAx = None
                elif plataforma is not None:
                    plataforma = None
                elif valMin is not None:
                    valMin = None
                elif tipo is not None:
                    tipo = None
            else:
                NotNul = False
        
        print(tabla)
                    
        ampliar = input("Prefereixes unes altres recomanacions? Si vols unes altes pulsa INTRO sino escriu NO ")
        if not ampliar:
            AmpliRecomanacio = True
        else:
            AmpliRecomanacio = False
        
        if AmpliRecomanacio:
            if actor is not None:
                actor = None
            elif genero is not None:
                genero = None
            elif duracioMin is not None:
                duracioMin = None
            elif duracioMAx is not None:
                duracioMAx = None
            elif plataforma is not None:
                plataforma = None
            elif valMin is not None:
                valMin = None
            elif tipo is not None:
                tipo = None
