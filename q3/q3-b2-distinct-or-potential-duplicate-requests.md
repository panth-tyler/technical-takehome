# Question B.(ii)

Suppose staff want the ability to mark two CDS requests as (1) confidently distinct (i.e., **not** duplicates) or (2) potential duplicates for later discussion.

Describe how you would architect such a system. In your answer, describe alternatives you considered and the tradeoffs of each compared to your preferred design.

We do not expect you to have a perfect or fully fleshed out solution. Feel free to describe or draw out an answer. We just want to see your thought process!

Answer:

I would attempt to keep the schema from becoming overly complicated and use the table structure from Question B (i) answers with some modifications:

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

```sql
CREATE TABLE IF NOT EXISTS
  duplicates (
    duplicate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    is_confirmed_duplicate INTEGER DEFAULT 0,
    is_distinct_request INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
;
```

Adding `is_confirmed_duplicate` and `is_distinct_request` columns would allow the duplicate entities to be marked respectively. Both columns would default to a false (0) value. This would allow queries or views to define a computed _status_ value. A text/varchar `status` column could be used instead of the two new columns but I recommended a state machine style schema with true/false flags and allow the UI to handle the presented state of each duplicate.

This question may also have used an additional foreign key table in-between the duplicates and requests tables if more properties are necessary or if the `is_confirmed_duplicate` and `is_distinct_request` values need to be evaluated per each single response:

```sql
CREATE TABLE IF NOT EXISTS
  duplicates (
    duplicate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
;
```

```sql
CREATE TABLE IF NOT EXISTS
  requests_duplicates (
    request_id INTEGER NOT NULL,
    duplicate_id INTEGER NOT NULL,
    is_confirmed_duplicate INTEGER DEFAULT 0,
    is_distinct_request INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
;
```

This would increase complexity and overall storage per request but would still have high readibility if required.
