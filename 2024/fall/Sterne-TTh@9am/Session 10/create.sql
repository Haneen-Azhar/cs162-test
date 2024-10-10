-- Create a table named 'students'
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
);

-- Insert some sample data into the 'students' table
INSERT INTO students (name, age, grade) VALUES ('Alice', 14, '8th');
INSERT INTO students (name, age, grade) VALUES ('Bob', 15, '9th');
INSERT INTO students (name, age, grade) VALUES ('Charlie', 13, '7th');
