# Question B.(i)

Suppose you are building a system that lets staff track duplicate requests. It provides the following features:

1. Staff can mark CDS requests A and B as duplicates.
2. More than two requests can be duplicates. If A and B are already marked as duplicates, and staff mark C as a duplicate of B, all three requests (A, B, and C) should be considered duplicates.
3. Staff can export all duplicate requests into a CSV or Excel file. The exact format does not matter, but the backend architecture should allow for the efficient retrieval of all duplicate requests. For example, if A, B, and C are considered duplicates, the export should list them as such.

To the best of your ability, describe how you would architect such a system that satisfies the above requirements. In your answer, make sure to respond to these questions:

1. What kind of database would you use to store the data?
2. How might you design the data schema? In particular, how would you efficiently track groups of duplicate requests?
3. For questions 1 and 2, what other options did you consider? What are the tradeoffs between your selected approach and others you might have taken?

We do not expect you to have a perfect or fully fleshed out solution. Feel free to describe or draw out an answer. We just want to see your thought process!

Answer:

Using a relational database, I would define a duplicates table schema:

```sql
CREATE TABLE IF NOT EXISTS
  duplicates (
    duplicate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
;
```

This could escalate in complexity quickly, but if there is a high level of confidence that the current requirements are accurate, I would then add a foreign key to the requests table:

```sql
CREATE TABLE IF NOT EXISTS
  requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    senator_id INTEGER NOT NULL,
    duplicate_id INTEGER,
    
    title TEXT NOT NULL,
    recipient TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
;
```

The complexity would increase if a single Request could be marked as duplicates of other Requests without those other Requests being duplicates of each other. (If A is duplicate of B, and A is duplicate of C, but B and C are not duplicates of each other.) Or if each duplicate needs to track additional properites such as which user reported the duplicate. In this case, a foreign key table could be created and would store the `request_id` and `duplicate_id` keys along with any additional properties.

With the current schema, it would greatly simplify extracting data by the `duplicate_id` for general queries or exporting to CSVs.
