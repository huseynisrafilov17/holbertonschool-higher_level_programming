-- Dunno.
SELECT score, COUNT(id) AS `number` FROM second_table
GROUP BY score
ORDER BY `number` DESC;
