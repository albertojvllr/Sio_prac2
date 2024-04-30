SELECT 
    g.Genere,
    AVG(i.Score) AS Promedio_Score
FROM 
    Titols t
JOIN 
    titols_imdb it ON t.ID = it.Id_Titols
JOIN 
    IMDB i ON it.ID_IMDB = i.ID
JOIN 
    Titols_Genere tg ON t.ID = tg.Id_titols
JOIN 
    Generes g ON tg.Id_Genere = g.ID
WHERE 
    t.Tipus IN ('SHOW', 'MOVIE')
GROUP BY 
    g.Genere
ORDER BY 
    Promedio_Score DESC;