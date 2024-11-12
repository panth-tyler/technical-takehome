-- Question A.(i)
-- Write a SQL query (in your SQL dialect of choice) that lists the `request_id`s for requests made by Democrat Senators.

SELECT
	r.request_id
FROM
	requests r
	INNER JOIN
		senators s
	ON
		s.senator_id = r.senator_id
		AND s.party = 'Democrat'
;