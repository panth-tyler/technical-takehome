# Question 3: Matchmaking

## Background

Every year, the Senate Appropriations Committee solicits funding requests from Senators for specific projects, accounts, or legislative language. This process contributes to the annual appropriations bill, such as the [FY24 bill](https://www.congress.gov/bill/118th-congress/house-bill/2882) passed in March 2024. Member offices sometimes submit duplicate requests, particularly for Congressionally Directed Spending (CDS). CDS requests are requests for specific projects (e.g., to repair a bridge in Seattle, WA). More information on funded CDS requests for FY24 can be found [here](https://www.appropriations.senate.gov/fy-2024-congressionally-directed-spending).

## Part A: SQL

Suppose the CDS request data is stored in a SQL database with two tables: `requests` and `senators`. Below is a sample of the data in both tables.

### Schema: (CDS) Requests

The `requests` table consists of unique request IDs, Senator IDs, titles, and recipients. This table includes only CDS requests.

| request_id | senator_id | title                           | recipient                              |
| ---------- | ---------- | ------------------------------- | -------------------------------------- |
| 43829      | 1          | Improved pavement on Highway 23 | Minnesota Department of Transportation |
| 43830      | 2          | Community Center for the Arts   | Community Arts Initiative Inc.         |
| 43831      | 3          | Entrepreneurial Fusion Center   | University of Mississippi              |

### Schema: Senators

The `senators` table consists of unique IDs, last names, party affiliations, and states.

| senator_id | last_name | party      | state |
| ---------- | --------- | ---------- | ----- |
| 1          | Murray    | Democrat   | WA    |
| 2          | Collins   | Republican | ME    |
| 3          | Wicker    | Republican | MS    |

### Question A.(i)

Write a SQL query (in your SQL dialect of choice) that lists the `request_id`s for requests made by Democrat Senators.

### Question A.(ii)

Each state is represented by two Senators, but not all Senators make CDS requests. Write a SQL query that lists all states where only one of the two Senators made a request.

## Part B: Architecture Design˜

### Question B.(i)

Suppose you are building a system that lets staff track duplicate requests. It provides the following features:

1. Staff can mark CDS requests A and B as duplicates.
2. More than two requests can be duplicates. If A and B are already marked as duplicates, and staff mark C as a duplicate of B, all three requests (A, B, and C) should be considered duplicates.
3. Staff can export all duplicate requests into a CSV or Excel file. The exact format does not matter, but the backend architecture should allow for the efficient retrieval of all duplicate requests. For example, if A, B, and C are considered duplicates, the export should list them as such.

To the best of your ability, describe how you would architect such a system that satisfies the above requirements. In your answer, make sure to respond to these questions:

1. What kind of database would you use to store the data?
2. How might you design the data schema? In particular, how would you efficiently track groups of duplicate requests?
3. For questions 1 and 2, what other options did you consider? What are the tradeoffs between your selected approach and others you might have taken?

We do not expect you to have a perfect or fully fleshed out solution. Feel free to describe or draw out an answer. We just want to see your thought process!

### Question B.(ii)

Suppose staff want the ability to mark two CDS requests as (1) confidently distinct (i.e., **not** duplicates) or (2) potential duplicates for later discussion.

Describe how you would architect such a system. In your answer, describe alternatives you considered and the tradeoffs of each compared to your preferred design.

We do not expect you to have a perfect or fully fleshed out solution. Feel free to describe or draw out an answer. We just want to see your thought process!


> Answers are provided in SQL and Markdown files.