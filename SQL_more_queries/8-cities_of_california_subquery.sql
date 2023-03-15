-- Task 8
SELECT 
    id, name
FROM
    cities
WHERE
    state_id IN (SELECT id FROM states WHERE name LIKE 'California')
ORDER BY id ASC
;