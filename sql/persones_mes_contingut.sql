SELECT 
    p.NOM AS persona,
    COUNT(DISTINCT CASE WHEN tp.ROL = 'ACTOR' THEN t.ID END) AS cantidad_titulos_como_actor,
    COUNT(DISTINCT CASE WHEN tp.ROL = 'DIRECTOR' THEN t.ID END) AS cantidad_titulos_como_director
FROM 
    PERSONES p
JOIN 
    TITOLS_PERSONES tp ON p.ID = tp.ID_PERSONA
JOIN 
    TITOLS t ON tp.ID_TITOL_PERSONA = t.ID
GROUP BY 
    p.NOM
HAVING 
    COUNT(DISTINCT CASE WHEN tp.ROL = 'ACTOR' THEN t.ID END) > 0
    AND COUNT(DISTINCT CASE WHEN tp.ROL = 'DIRECTOR' THEN t.ID END) > 0
ORDER BY 
    cantidad_titulos_como_actor DESC;