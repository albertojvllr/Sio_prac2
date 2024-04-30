SELECT 
    p.Plataforma,
    AVG(CASE WHEN t.Tipus = 'SHOW' THEN t.Runtime END) AS DuracionPromedioSeries,
    AVG(CASE WHEN t.Tipus = 'MOVIE' THEN t.Runtime END) AS DuracionPromedioPeliculas
FROM 
    Titols t
JOIN 
    Titols_Plataforma tp ON t.ID = tp.Id_Titols_plataforma
JOIN 
    Plataforma p ON tp.Id_plataforma = p.Id
WHERE 
    t.Tipus IN ('SHOW', 'MOVIE')
GROUP BY 
    p.Plataforma;