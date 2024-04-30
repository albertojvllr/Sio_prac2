SELECT 
    t.titol AS ID_Contenido,
    i.Score AS Valoracion_IMDB,
    i.tmdb_score AS Valoracion_TMDBscore
FROM 
    Titols t
JOIN 
    titols_imdb it ON t.ID = it.Id_Titols
JOIN 
    IMDB i ON it.ID_IMDB = i.ID
WHERE 
    t.Tipus IN ('SHOW', 'MOVIE')
GROUP BY 
    t.ID;