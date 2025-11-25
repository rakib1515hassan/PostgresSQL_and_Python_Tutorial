# Data Insurt into Class Table

## Table Create
#### For MySQL
```sql
CREATE TABLE IF NOT EXISTS classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```
#### For PostgreSQL
```sql
CREATE TABLE IF NOT EXISTS classes (
    class_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```

## Table Data Insert

- [Single Row Insert]
```sql
INSERT INTO classes (name) 
VALUES ('Class vi');
```

- [Multiple Rows Insert]

```sql
INSERT INTO classes (name) 
VALUES
    ('Class vii'),
    ('Class viii'),
    ('Class ix'),
    ('Class x');
    ('Class xi');
    ('Class xii');
```


## Table Data View
- See all data from the classes table:
```sql
SELECT * 
FROM classes;
```

- See specific columns (e.g., name) from the classes table:
```sql
SELECT name 
FROM classes;
```

- See data with a condition (e.g., class_id = 1):
```sql
SELECT * 
FROM classes 
WHERE class_id = 1;
```
