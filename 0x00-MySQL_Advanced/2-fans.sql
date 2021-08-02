-- SQL SCRIPT THAT RANKS COUNTRY
-- ORDER BY UNIQUE FANS
SELECT origin AS origin, SUM(fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
