WITH total_titles AS (
    SELECT 
        g.GENERE,
        c.COUNTRY,
        COUNT(DISTINCT CASE WHEN t.TIPUS = 'SHOW' THEN tg.ID_TITOLS END) AS cantidad_series,
        COUNT(DISTINCT CASE WHEN t.TIPUS = 'MOVIE' THEN tg.ID_TITOLS END) AS cantidad_peliculas
    FROM 
        GENERES g
    JOIN 
        TITOLS_GENERE tg ON g.ID = tg.ID_GENERE
    JOIN 
        TITOLS t ON tg.ID_TITOLS = t.ID
    JOIN 
        COUNTRIES_TITOLS ct ON t.ID = ct.ID_TITOLS_COUNTRY
    JOIN 
        COUNTRIES c ON ct.ID_COUNTRY = c.ID
    GROUP BY 
        g.GENERE, c.COUNTRY
),
ranked_countries AS (
    SELECT 
        GENERE,
        COUNTRY,
        cantidad_series,
        cantidad_peliculas,
        ROW_NUMBER() OVER(PARTITION BY GENERE ORDER BY (cantidad_series + cantidad_peliculas) DESC) as rn
    FROM 
        total_titles
)
SELECT 
    GENERE,
    COUNTRY,
    cantidad_series,
    cantidad_peliculas
FROM 
    ranked_countries
WHERE 
    rn <= 5
ORDER BY 
    GENERE, rn;