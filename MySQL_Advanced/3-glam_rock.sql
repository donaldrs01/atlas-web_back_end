-- Task 3: Ordering glam rocks bands by lifespan

SELECT
    band_name,
    CASE -- handle case where band still exists (split = NULL)
        WHEN split IS NOT NULL THEN split - formed
        ELSE YEAR(CURDATE()) - formed
    END AS lifespan
FROM
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;