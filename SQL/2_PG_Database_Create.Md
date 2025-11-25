# SQL Query to Create a School Database

## Syntax :

```sql
CREATE DATABASE data_base_name;
```

## 1. To create a database named school_db in SQL, you would use the following query:

```sql
CREATE DATABASE school_db;
```


### 2. With character set specification (if needed):

```sql
CREATE DATABASE school_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```


### 3. With existence check (to avoid errors if database already exists):

```sql
CREATE DATABASE IF NOT EXISTS school_db;
```

### 4. Create Data base with check exists or not
```sql
CREATE DATABASE IF NOT EXISTS school_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

