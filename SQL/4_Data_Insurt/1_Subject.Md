# Data Insurt

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

## Table Data  [Single Row Insert]

```sql
INSERT INTO subjects (name)
VALUES ('Mathematics');
```

## Table Data  [Multiple Rows Insert]

```sql
INSERT INTO subjects (name)
VALUES 
    ('Physics'),
    ('Chemistry'),
    ('Biology'),
    ('English'),
    ('Bangla');
```

## More Date Insert Examples
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