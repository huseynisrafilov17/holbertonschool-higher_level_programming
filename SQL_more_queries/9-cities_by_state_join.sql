-- Join Task.
SELECT cities.id, cities.name, states.name FROM cities, states
INNER JOIN cities ON cities.state_id = states.id
ORDER BY cities.id;
