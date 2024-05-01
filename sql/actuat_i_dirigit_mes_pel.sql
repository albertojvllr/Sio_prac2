SELECT 
    p.nom,
    COUNT(*) as num_titols
FROM 
    (SELECT id_persona, id_titol_persona FROM titols_persones WHERE rol = 'actor') actor
JOIN 
    (SELECT id_persona, id_titol_persona FROM titols_persones WHERE rol = 'director') director 
ON 
    actor.id_persona = director.id_persona AND actor.id_titol_persona = director.id_titol_persona
JOIN
    persones p ON actor.id_persona = p.id
GROUP BY
    p.nom
ORDER BY
    num_titols DESC;