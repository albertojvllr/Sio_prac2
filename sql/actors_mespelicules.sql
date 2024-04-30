SELECT
    pe.NOM AS actor,
    COUNT(tp.ID_TITOL_PERSONA) AS cantidad_peliculas_protagonizadas
FROM
    PERSONES pe
    JOIN TITOLS_PERSONES tp ON pe.ID = tp.ID_PERSONA
    JOIN TITOLS t ON tp.ID_TITOL_PERSONA = t.ID
WHERE
    t.TIPUS = 'MOVIE'
GROUP BY
    pe.NOM
ORDER BY
    cantidad_peliculas_protagonizadas DESC
LIMIT
    10;