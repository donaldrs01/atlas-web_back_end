-- Task 2: Orders data by nb_fans (non-unique fans)

SELECT -- select origin column and add up total fans
    origin,
    SUM(fans) AS nb_fans
FROM 
    bands
GROUP BY -- group by origin column
    origin 
ORDER BY 
    nb_fans DESC;