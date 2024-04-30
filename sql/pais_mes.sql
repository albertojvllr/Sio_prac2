SELECT 
    c.COUNTRY,
    COUNT(ct.ID_TITOLS_COUNTRY) AS cantidad_titulos,
    SUM(CASE WHEN t.TIPUS = 'SHOW' THEN 1 ELSE 0 END) AS cantidad_series,
    SUM(CASE WHEN t.TIPUS = 'MOVIE' THEN 1 ELSE 0 END) AS cantidad_peliculas

FROM 
    COUNTRIES c
JOIN 
    COUNTRIES_TITOLS ct ON c.ID = ct.ID_COUNTRY
JOIN 
    TITOLS t ON ct.ID_TITOLS_COUNTRY = t.ID
GROUP BY 
    c.COUNTRY
ORDER BY 
    cantidad_titulos DESC;