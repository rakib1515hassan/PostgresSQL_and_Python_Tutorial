# Table Create

## Syntax: SQL Syntax for Creating a Table

```base 
CREATE TABLE [IF NOT EXISTS] table_name (
    column1 datatype [constraints],
    column2 datatype [constraints],
    column3 datatype [constraints],
    ...
    [table_constraints]
);
```


## Subjects table
```bash
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

## Classes table

```bash
CREATE TABLE IF NOT EXISTS classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```

## Students table

```bash
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    gender ENUM('male', 'female', 'others')
);

```

## StudentDetails table (One-to-One with students)

```bash
CREATE TABLE IF NOT EXISTS student_details (
    student_details_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL UNIQUE,
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    profile_pic VARCHAR(255), -- Stores image path or URL
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

## Teachers table

```bash
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    gender ENUM('male', 'female', 'others'),
    joining_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Batches table

```bash
CREATE TABLE IF NOT EXISTS batches (
    batch_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    class_id INT NOT NULL,
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

## Batch Enrollments table

```bash
CREATE TABLE IF NOT EXISTS batch_enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    batch_id INT NOT NULL,
    student_id INT NOT NULL,
    roll_number INT NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (batch_id, student_id),
    UNIQUE KEY (batch_id, roll_number)
);
```

## Batch Teachers (Many-to-Many: batch - subject - teacher)

```bash
CREATE TABLE IF NOT EXISTS batch_teachers (
    batch_id INT NOT NULL,
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,
    PRIMARY KEY (batch_id, teacher_id, subject_id),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

## Exams table

```bash
CREATE TABLE IF NOT EXISTS exams (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    batch_id INT NOT NULL,
    exam_name VARCHAR(100) NOT NULL,
    exam_date DATE NOT NULL,
    total_marks DECIMAL(5,2) NOT NULL,
    passing_marks DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

## Exam Subjects table

```bash
CREATE TABLE IF NOT EXISTS exam_subjects (
    exam_subject_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_id INT NOT NULL,
    subject_id INT NOT NULL,
    max_marks DECIMAL(5,2) NOT NULL,
    exam_date DATE NOT NULL,
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (exam_id, subject_id)
);
```

## Exam Results table

```bash
CREATE TABLE IF NOT EXISTS exam_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_subject_id INT NOT NULL,
    student_id INT NOT NULL,
    marks_obtained DECIMAL(5,2) NOT NULL,
    grade VARCHAR(2),
    remarks VARCHAR(200),
    FOREIGN KEY (exam_subject_id) REFERENCES exam_subjects(exam_subject_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (exam_subject_id, student_id)
);
```

## Batch Subjects (Subjects taught in each batch)

```bash
CREATE TABLE IF NOT EXISTS batch_subjects (
    batch_id INT NOT NULL,
    subject_id INT NOT NULL,
    PRIMARY KEY (batch_id, subject_id),
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```


## 🔸 ON DELETE / ON UPDATE Actions

| Option          | Description |
|-----------------|-------------|
| **CASCADE**     | Parent row delete/update হলে child row গুলোকেও delete/update করে দেয়। |
| **SET NULL**    | Parent row delete/update হলে child table-এর foreign key field-টি `NULL` করে দেয়। |
| **SET DEFAULT** | Parent row delete/update হলে child table-এর foreign key field-টি default value-তে সেট করে। (Not supported in all DBMS) |
| **RESTRICT**    | যদি child table-এ related row থাকে, তাহলে parent row delete/update করা যাবে না। (এইটা default behavior অনেক সময়) |
| **NO ACTION**   | `RESTRICT` এর মতোই কাজ করে, তবে এটি defer করা যায় (বেশিরভাগ DBMS-এ `RESTRICT` আর `NO ACTION` একি রকম কাজ করে)। |


Example: 

```bash
-- SET NULL example
FOREIGN KEY (student_id) REFERENCES students(student_id)
    ON DELETE SET NULL

-- SET DEFAULT example (only works if default is defined and supported)
FOREIGN KEY (student_id) REFERENCES students(student_id)
    ON DELETE SET DEFAULT

-- RESTRICT example
FOREIGN KEY (student_id) REFERENCES students(student_id)
    ON DELETE RESTRICT

```