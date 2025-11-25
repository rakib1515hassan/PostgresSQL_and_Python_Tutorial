# SQL Query to Create a School Database

## Syntax :

```bash
CREATE DATABASE data_base_name;
```

## 1. To create a database named school_db in SQL, you would use the following query:

```bash
CREATE DATABASE school_db;
```


### 2. With character set specification (if needed):

```bash
CREATE DATABASE school_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```


### 3. With existence check (to avoid errors if database already exists):

```bash
CREATE DATABASE IF NOT EXISTS school_db;
```

### 4. Create Data base with check exists or not
```bash
CREATE DATABASE IF NOT EXISTS school_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

