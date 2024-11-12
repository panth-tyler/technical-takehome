-- The `requests` table consists of unique request IDs, Senator IDs, titles, and recipients. This table includes only CDS requests.

-- | request_id | senator_id | title                           | recipient                              |
-- | ---------- | ---------- | ------------------------------- | -------------------------------------- |
-- | 43829      | 1          | Improved pavement on Highway 23 | Minnesota Department of Transportation |
-- | 43830      | 2          | Community Center for the Arts   | Community Arts Initiative Inc.         |
-- | 43831      | 3          | Entrepreneurial Fusion Center   | University of Mississippi              |

-- ### Schema: Senators

-- The `senators` table consists of unique IDs, last names, party affiliations, and states.

-- | senator_id | last_name | party      | state |
-- | ---------- | --------- | ---------- | ----- |
-- | 1          | Murray    | Democrat   | WA    |
-- | 2          | Collins   | Republican | ME    |
-- | 3          | Wicker    | Republican | MS    |

-- ### Init Statements
-- I used SQLite for my answers but the project would most likely use PostgreSQL or MS-SQL with slight changes.

CREATE TABLE IF NOT EXISTS
	senators (
		senator_id INTEGER PRIMARY KEY AUTOINCREMENT,

		last_name TEXT NOT NULL,
		party TEXT NOT NULL,
		state TEXT NOT NULL,

		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	)
;
	
CREATE TABLE IF NOT EXISTS
	requests (
		request_id INTEGER PRIMARY KEY AUTOINCREMENT,
		senator_id INTEGER NOT NULL,
		
		title TEXT NOT NULL,
		recipient TEXT NOT NULL,

		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	)
;

INSERT OR REPLACE INTO 
	senators 
		(senator_id, last_name, party, state)
	VALUES 
		(1, 'Murray', 'Democrat', 'WA')
;

INSERT OR REPLACE INTO 
	senators 
		(senator_id, last_name, party, state)
	VALUES
		(2, 'Collins', 'Republican', 'ME')
;

INSERT OR REPLACE INTO 
	senators 
		(senator_id, last_name, party, state)
	VALUES
		(3, 'Wicker', 'Republican', 'MS')
;

INSERT OR REPLACE INTO 
	senators 
		(senator_id, last_name, party, state)
	VALUES
		(4, 'Hyde-Smith', 'Republican', 'MS')
;

INSERT OR REPLACE INTO 
	senators 
		(senator_id, last_name, party, state)
	VALUES
		(5, 'King, Jr', 'Independent', 'ME')
;

INSERT OR REPLACE INTO 
	requests 
		(request_id, senator_id, title, recipient)
	VALUES
		(43829, 1, 'Improved pavement on Highway 23', 'Minnesota Department of Transportation')
;

INSERT OR REPLACE INTO 
	requests 
		(request_id, senator_id, title, recipient)
	VALUES
		(43830, 2, 'Community Center for the Arts', 'Community Arts Initiative Inc.')
;

INSERT OR REPLACE INTO 
	requests 
		(request_id, senator_id, title, recipient)
	VALUES
		(43831, 3, 'Entrepreneurial Fusion Center', 'University of Mississippi')
;

INSERT OR REPLACE INTO 
	requests 
		(request_id, senator_id, title, recipient)
	VALUES
		(43832, 3, 'Structural Improvements', 'The University of Southern Mississippi')
;

INSERT OR REPLACE INTO 
	requests 
		(request_id, senator_id, title, recipient)
	VALUES
		(43833, 5, 'Arts Center for the Community', 'Community Arts Initiative Inc.')
;