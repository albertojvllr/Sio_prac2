SELECT 
    COUNT(*) AS cantidad_total_titulos,
    SUM(CASE WHEN cnt > 1 THEN 1 ELSE 0 END) AS cantidad_titulos_en_multiples_plataformas,
    SUM(CASE WHEN cnt > 1 THEN 1 ELSE 0 END) / COUNT(*) AS proporcion_titulos_en_multiples_plataformas
FROM (
    SELECT 
        ID_TITOLS_PLATAFORMA,
        COUNT(*) AS cnt
    FROM 
        TITOLS_PLATAFORMA
    GROUP BY 
        ID_TITOLS_PLATAFORMA
) AS subquery;