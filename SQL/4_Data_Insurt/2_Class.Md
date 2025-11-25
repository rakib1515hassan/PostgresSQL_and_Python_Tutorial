# Data Insurt into Class Table

## Table Create
#### For MySQL
```sql
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```
#### For PostgreSQL
```sql
CREATE TABLE IF NOT EXISTS subjects (
    subject_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

## Table Data Insert

- [Single Row Insert]
```sql
INSERT INTO subjects (name)
VALUES ('Mathematics');
```

- [Multiple Rows Insert]

```sql
INSERT INTO subjects (name)
VALUES 
    ('Physics'),
    ('Chemistry'),
    ('Biology'),
    ('English'),
    ('Bangla');
```

- More Date Insert Examples
```sql
INSERT INTO subjects (name) VALUES
('Mathematics'),
('Physics'),
('Chemistry'),
('Biology'),
('English'),
('Bangla'),
('Computer Science'),
('History'),
('Geography'),
('Economics');
```


## Table Data View
- See all data from the subjects table:
```sql
SELECT * 
FROM subjects;
```

- See specific columns (e.g., name) from the subjects table:
```sql
SELECT name 
FROM subjects;
```

- See data with a condition (e.g., subject_id = 1):
```sql
SELECT * 
FROM subjects 
WHERE subject_id = 1;
```

- See data with a condition (e.g., name = 'Physics'):
```sql
SELECT * 
FROM subjects 
WHERE name = 'Physics';
```

- See data with sorting (e.g., order by name ascending):
```sql
SELECT * 
FROM subjects 
ORDER BY name ASC;
```
- See data with sorting (e.g., order by name descending):
```sql
SELECT * 
FROM subjects
ORDER BY name DESC;
```

- See data with limit (e.g., limit to 5 rows):
```sql
SELECT * 
FROM subjects 
LIMIT 5;
```

- See data with offset (e.g., skip first 2 rows):
```sql
SELECT * 
FROM subjects 
OFFSET 2;
```

- See data with limit and offset (e.g., limit to 5 rows, skip first 2 rows):
```sql
SELECT * 
FROM subjects 
LIMIT 5 OFFSET 2;
```

- Search data with pattern matching (e.g., names starting with 'C'):
```sql
SELECT * 
FROM subjects
WHERE name LIKE '%bio%';
```
- Search data with case insensitive pattern matching (e.g., names containing 'bio'):
```sql
SELECT * 
FROM subjects
WHERE UPPER(name) LIKE UPPER('%bio%');
```
- Search data with case insensitive pattern matching (e.g., names containing 'bio'):
```sql
SELECT * 
FROM subjects
WHERE LOWER(name) LIKE LOWER('%bio%');
```