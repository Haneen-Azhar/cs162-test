# Indexes and Normalization

### Indexes
Indexes are used to speed up the retrieval of data. By creating an index on commonly queried columns, we improve the performance of our queries, especially as the size of the database grows.

1. **Example (LMS)**: 
   - Adding an index on `StudentID` in the `Submissions` table will speed up queries that look up grades for a particular student.
   - Indexing `CourseID` in the `Enrollments` table will optimize joins when retrieving course enrollments.

2. **Example (Patient Health Records)**:
   - Indexing `PatientID` in the `MedicalRecords` and `Appointments` tables ensures faster lookups of a patient's medical history and appointment schedule.
   - Composite indexes on `DoctorID` and `AppointmentDate` in the `Appointments` table will optimize queries that look for doctors’ appointments in specific date ranges.

### Normalization
Normalization helps to reduce data redundancy and improve the integrity of the database. In both the LMS and Patient Record systems, we apply normalization:

1. **1NF (First Normal Form)**: All tables store atomic data. For example, in the `Patients` table, each patient record stores a single name, address, etc.

2. **2NF (Second Normal Form)**: All non-key attributes are fully dependent on the primary key. For instance, in the `MedicalRecords` table, the `Diagnosis` and `Prescription` depend only on `PatientID`.

3. **3NF (Third Normal Form)**: All attributes are functionally dependent only on the primary key and not on other non-key attributes. For example, the `Assignments` table stores only assignment-specific data, while the `Courses` table stores only course-specific data.

### Performance Considerations
Although normalization reduces redundancy, it can sometimes lead to complex joins, which could affect performance. In read-heavy systems, some denormalization could be considered to reduce the number of joins, but this must be weighed against the potential for data inconsistency.
