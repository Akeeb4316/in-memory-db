from in_memory_db import InMemoryDB

if __name__ == "__main__":
    db = InMemoryDB()

    # Test case: Get a value before putting it
    print(db.get("A"))  # Output: None

    # Test case: Put a value without a transaction
    try:
        db.put("A", 5)
    except Exception as e:
        print(e)  # Output: No active transaction

    # Test case: Begin a transaction and put a value
    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Output: None (not visible until commit)

    # Test case: Commit the transaction
    db.commit()
    print(db.get("A"))  # Output: 5

    # Test case: Begin another transaction and rollback
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))  # Output: None

from in_memory_db import InMemoryDB

if __name__ == "__main__":
    db = InMemoryDB()

    # Test case 1: Get a value before putting it
    print(db.get("A"))  # Output: None

    # Test case 2: Put a value without a transaction
    try:
        db.put("A", 5)
    except Exception as e:
        print(e)  # Output: No active transaction

    # Test case 3: Begin a transaction and put a value
    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Output: None (not visible until commit)

    # Test case 4: Commit the transaction
    db.commit()
    print(db.get("A"))  # Output: 5

    # Test case 5: Begin another transaction, update value, and rollback
    db.begin_transaction()
    db.put("A", 10)
    db.rollback()
    print(db.get("A"))  # Output: 5

    # Test case 6: Add multiple keys and commit
    db.begin_transaction()
    db.put("B", 20)
    db.put("C", 30)
    db.commit()
    print(db.get("B"))  # Output: 20
    print(db.get("C"))  # Output: 30
