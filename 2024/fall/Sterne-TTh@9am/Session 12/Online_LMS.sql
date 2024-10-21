-- Online Learning Management System Schema

-- Courses Table
CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT NOT NULL,
    Instructor TEXT NOT NULL
);

-- Students Table
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL,
    Email TEXT UNIQUE
);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INTEGER PRIMARY KEY,
    CourseID INTEGER,
    StudentID INTEGER,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Assignments Table
CREATE TABLE Assignments (
    AssignmentID INTEGER PRIMARY KEY,
    CourseID INTEGER,
    Description TEXT,
    DueDate DATE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Submissions Table
CREATE TABLE Submissions (
    SubmissionID INTEGER PRIMARY KEY,
    AssignmentID INTEGER,
    StudentID INTEGER,
    SubmissionDate DATE,
    Grade INTEGER,
    FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Grades Table (newly added for storing total grades)
CREATE TABLE Grades (
    GradeID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    TotalGrade INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Mock Data
INSERT INTO Courses (CourseName, Instructor) VALUES ('Math 101', 'Dr. Smith');
INSERT INTO Students (StudentName, Email) VALUES ('Alice', 'alice@email.com');
INSERT INTO Enrollments (CourseID, StudentID) VALUES (1, 1);
INSERT INTO Assignments (CourseID, Description, DueDate) VALUES (1, 'Chapter 1 Problems', '2023-10-20');
INSERT INTO Submissions (AssignmentID, StudentID, SubmissionDate, Grade) VALUES (1, 1, '2023-10-19', 90);
INSERT INTO Grades (StudentID, TotalGrade) VALUES (1, 90);

-- Queries

-- 1. List all courses Alice is enrolled in
SELECT CourseName
FROM Courses
JOIN Enrollments ON Courses.CourseID = Enrollments.CourseID
JOIN Students ON Enrollments.StudentID = Students.StudentID
WHERE Students.StudentName = 'Alice';

-- 2. List all students in Math 101
SELECT StudentName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Courses ON Enrollments.CourseID = Courses.CourseID
WHERE Courses.CourseName = 'Math 101';

-- 3. Find Alice's grade for Chapter 1 Problems
SELECT Grade
FROM Submissions
JOIN Assignments ON Submissions.AssignmentID = Assignments.AssignmentID
JOIN Students ON Submissions.StudentID = Students.StudentID
WHERE Assignments.Description = 'Chapter 1 Problems' AND Students.StudentName = 'Alice';

-- Advanced Queries

-- 4. Calculate the average grade for Alice across all courses
SELECT AVG(Grade) AS AverageGrade
FROM Submissions
WHERE StudentID = 1;

-- 5. List the top 3 students with the highest grades for a particular assignment
SELECT Students.StudentName, Submissions.Grade
FROM Submissions
JOIN Students ON Submissions.StudentID = Students.StudentID
WHERE AssignmentID = 1
ORDER BY Submissions.Grade DESC
LIMIT 3;

-- 6. Calculate the total grade for each student in Math 101
SELECT Students.StudentName, SUM(Submissions.Grade) AS TotalGrade
FROM Submissions
JOIN Enrollments ON Submissions.StudentID = Enrollments.StudentID
JOIN Courses ON Enrollments.CourseID = Courses.CourseID
JOIN Students ON Students.StudentID = Enrollments.StudentID
WHERE Courses.CourseName = 'Math 101'
GROUP BY Students.StudentName;

-- Transaction Example (Updated)

BEGIN TRANSACTION;

-- Insert the assignment submission into Submissions
INSERT INTO Submissions (AssignmentID, StudentID, SubmissionDate, Grade) 
VALUES (1, 1, '2023-10-20', 85);

-- Update the student’s total grade in the Grades table
UPDATE Grades SET TotalGrade = TotalGrade + 85 WHERE StudentID = 1;

-- If both operations succeed, commit the transaction
COMMIT;

-- If anything fails, rollback the transaction
ROLLBACK;
