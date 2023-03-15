-- Task 8
SELECT 
    id, name
FROM
    cities
WHERE
    state_id in (SELECT id from states WHERE name like 'California')
ORDER BY id ASC
;