SELECT 
    p.Plataforma,
    AVG(i.Score) AS ValoracionPromedio
FROM 
    Plataforma p
LEFT JOIN 
    Titols_Plataforma tp ON p.Id = tp.Id_plataforma
LEFT JOIN 
    Titols t ON tp.Id_Titols_plataforma = t.ID
LEFT JOIN 
    titols_imdb it ON t.ID = it.Id_Titols
LEFT JOIN 
    IMDB i ON it.ID_IMDB = i.ID
WHERE 
    t.Tipus IN ('SHOW', 'MOVIE')
GROUP BY 
    p.Plataforma
ORDER BY 
    ValoracionPromedio DESC;