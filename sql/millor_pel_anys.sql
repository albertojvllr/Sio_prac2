SELECT 
    SUBSTRING(t.release_date, 1, 3) AS Decada,
    AVG(i.Score) AS PuntuacionPromedio
FROM 
    Titols t
LEFT JOIN 
    titols_imdb it ON t.ID = it.Id_Titols
LEFT JOIN 
    IMDB i ON it.ID_IMDB = i.ID
WHERE 
    t.Tipus = 'MOVIE'
GROUP BY 
    SUBSTRING(t.release_date, 1, 3)
ORDER BY 
    PuntuacionPromedio DESC;