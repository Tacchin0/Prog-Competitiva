SELECT city_name, population FROM cities
WHERE population = (SELECT MAX(population) FROM cities
WHERE population <> (SELECT MAX(population) FROM cities))
OR population = (SELECT MIN(population) FROM cities
WHERE population <> (SELECT MIN(population) FROM cities));

/* 

Different Approach 

SELECT city_name, population FROM
    (
    SELECT city_name, population,
    DENSE_RANK() OVER (ORDER BY population DESC) AS highest, 
    DENSE_RANK() OVER (ORDER BY population ASC) AS lowest, 
    FROM cities
    ) temp

WHERE highest = 2 OR lowest = 2;

*/

