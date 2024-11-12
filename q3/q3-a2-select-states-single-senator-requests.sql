-- Question A.(ii)
-- Each state is represented by two Senators, but not all Senators make CDS requests. Write a SQL query that lists all states where only one of the two Senators made a request.

WITH senator_state_requests AS (
    SELECT 
        s.senator_id,
        s.state
    FROM 
        senators s
	WHERE 
		EXISTS (
			SELECT 1 FROM requests WHERE senator_id = s.senator_id
		)
	GROUP BY
		s.senator_id,
        s.state
)
SELECT
	ssr.state
FROM
	senator_state_requests ssr
GROUP BY
	ssr.state
HAVING
	COUNT(ssr.state) = 1
;