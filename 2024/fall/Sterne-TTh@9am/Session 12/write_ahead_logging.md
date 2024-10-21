# Write-Ahead Logging (WAL) and ACID Guarantees

Write-Ahead Logging (WAL) ensures data consistency by logging changes before making actual updates to the database. This guarantees the **Durability** of the ACID properties, as even if a failure occurs, the log will allow the database to restore its previous consistent state.

### ACID Properties

1. **Atomicity**: Ensures that all parts of a transaction are completed successfully, or none at all. For example, in an LMS, when registering a student for a course and recording their assignment submission, if any part of this operation fails, the entire transaction rolls back, ensuring there’s no incomplete or inconsistent data.

2. **Consistency**: Ensures that only valid data according to all defined rules (e.g., foreign key constraints, column types) is written into the database. For example, in the Patient Health Record system, if a doctor's specialty doesn't match the diagnosis, the transaction will fail, ensuring only valid data is written.

3. **Isolation**: Guarantees that concurrent transactions do not affect each other. For example, two students submitting assignments simultaneously should not affect each other’s records. Each transaction should be executed in isolation.

4. **Durability**: Ensures that once a transaction is committed, it will persist even in the case of a system crash. This is achieved through WAL, which logs the changes before writing them to the database.

### Write-Ahead Logging Example

Imagine a book exchange database where two people exchange books. Each exchange involves:
1. Decreasing Alice’s balance by 30.
2. Increasing Bob’s balance by 30.

If a failure occurs after decreasing Alice’s balance but before updating Bob’s balance, the WAL will revert Alice’s balance, preventing inconsistencies. 

Here’s how it works step-by-step:

1. **Begin Transaction**: We start a new transaction that will include both the deduction from Alice and the addition to Bob.
2. **Log Operations**: 
   - Deduct 30 from Alice.
   - Add 30 to Bob.
3. **Apply to Database**: We then update the database with Alice’s new balance.
4. **If Failure Occurs**: If a failure occurs before Bob’s balance is updated, the WAL log will revert Alice’s balance to its previous state (before the transaction started).
5. **Commit**: If the entire transaction succeeds, we commit it, making it permanent.

By writing to the log before applying changes, WAL ensures that if a failure occurs, the system can recover to a consistent state.
