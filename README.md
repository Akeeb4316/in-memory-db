# In-Memory Database with Transactions

## Description
This project implements an in-memory key-value database with transaction support. The database provides basic operations such as `begin_transaction`, `put`, `get`, `commit`, and `rollback`. Transactions ensure changes are isolated and reversible until committed, making this a simple implementation of transactional behavior.

---

## How to Run the Code

### **Prerequisites**
1. Install **Python 3.6 or higher** on your system.
   - Download from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Clone this repository to your local system:
   ```bash
   git clone https://github.com/Akeeb4316/in-memory-db
   cd in-memory-db

## Suggestions for Improvement
To make this assignment an “official” part of the course, clearer instructions should be provided to specify edge cases, such as what happens when rollback() or commit() is called without an active transaction. Additional methods like delete(key) could be introduced to make the implementation more robust and aligned with real-world use cases. Incorporating a unit testing framework (e.g., pytest) with predefined test cases would simplify grading and ensure consistency in evaluations. Providing starter code for the database structure would help students focus on the logic rather than the setup. Lastly, adding performance requirements or scalability considerations (e.g., large numbers of keys) could elevate the difficulty for advanced learners.
