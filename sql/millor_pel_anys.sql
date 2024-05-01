SELECT 
    (TRUNCATE(CAST(LEFT(t.release_date, 4) AS UNSIGNED) / 10, 0) * 10) AS Decada,
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
    Decada
ORDER BY 
    Decada ASC;