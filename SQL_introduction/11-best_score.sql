-- bbest score
SELECT
	score, name
FROM
	second_table
	where score >= 10
	order by score desc
