-- Task 9
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = cities.state_id
ORDER BY cities.id ASC
;