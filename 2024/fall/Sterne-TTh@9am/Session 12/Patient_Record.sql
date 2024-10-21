-- Patient Health Record and Medical History Tracker Schema

-- Patients Table
CREATE TABLE Patients (
    PatientID INTEGER PRIMARY KEY,
    PatientName TEXT NOT NULL,
    DateOfBirth DATE,
    Address TEXT
);

-- Doctors Table
CREATE TABLE Doctors (
    DoctorID INTEGER PRIMARY KEY,
    DoctorName TEXT NOT NULL,
    Specialty TEXT
);

-- Appointments Table
CREATE TABLE Appointments (
    AppointmentID INTEGER PRIMARY KEY,
    PatientID INTEGER,
    DoctorID INTEGER,
    AppointmentDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- MedicalRecords Table
CREATE TABLE MedicalRecords (
    RecordID INTEGER PRIMARY KEY,
    PatientID INTEGER,
    Diagnosis TEXT,
    Prescription TEXT,
    DateOfVisit DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- Mock Data
INSERT INTO Patients (PatientName, DateOfBirth, Address) VALUES ('John Doe', '1985-01-15', '123 Elm St');
INSERT INTO Doctors (DoctorName, Specialty) VALUES ('Dr. Adams', 'Cardiology');
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate) VALUES (1, 1, '2023-10-25');
INSERT INTO MedicalRecords (PatientID, Diagnosis, Prescription, DateOfVisit) VALUES (1, 'High Blood Pressure', 'Medication A', '2023-10-10');

-- Queries

-- 1. List all doctors John Doe has appointments with
SELECT DoctorName
FROM Doctors
JOIN Appointments ON Doctors.DoctorID = Appointments.DoctorID
JOIN Patients ON Appointments.PatientID = Patients.PatientID
WHERE Patients.PatientName = 'John Doe';

-- 2. Find the medical history of John Doe
SELECT Diagnosis, Prescription, DateOfVisit
FROM MedicalRecords
JOIN Patients ON MedicalRecords.PatientID = Patients.PatientID
WHERE Patients.PatientName = 'John Doe';

-- 3. List all patients Dr. Adams has appointments with
SELECT PatientName
FROM Patients
JOIN Appointments ON Patients.PatientID = Appointments.PatientID
JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
WHERE Doctors.DoctorName = 'Dr. Adams';

-- Advanced Queries

-- 4. List the number of appointments each doctor has in a given month
SELECT Doctors.DoctorName, COUNT(Appointments.AppointmentID) AS AppointmentCount
FROM Doctors
JOIN Appointments ON Doctors.DoctorID = Appointments.DoctorID
WHERE AppointmentDate BETWEEN '2023-11-01' AND '2023-11-30'
GROUP BY Doctors.DoctorName;

-- 5. List the patients who have visited more than one doctor
SELECT Patients.PatientName, COUNT(DISTINCT Doctors.DoctorID) AS DoctorCount
FROM Patients
JOIN Appointments ON Patients.PatientID = Appointments.PatientID
JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
GROUP BY Patients.PatientName
HAVING DoctorCount > 1;

-- 6. Find all doctors who have treated a patient for multiple diagnoses
SELECT Doctors.DoctorName, COUNT(DISTINCT MedicalRecords.Diagnosis) AS DiagnosisCount
FROM Doctors
JOIN Appointments ON Doctors.DoctorID = Appointments.DoctorID
JOIN MedicalRecords ON Appointments.PatientID = MedicalRecords.PatientID
WHERE Appointments.PatientID = 1
GROUP BY Doctors.DoctorName
HAVING DiagnosisCount > 1;

-- Transaction Example (Updated)

BEGIN TRANSACTION;

-- Insert the new appointment
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate) 
VALUES (1, 1, '2023-11-25');

-- Insert the new medical record
INSERT INTO MedicalRecords (PatientID, Diagnosis, Prescription, DateOfVisit) 
VALUES (1, 'Asthma', 'Inhaler', '2023-11-20');

-- If both operations succeed, commit the transaction
COMMIT;

-- If any operation fails, rollback the transaction
ROLLBACK;
