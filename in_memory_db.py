class InMemoryDB:
    def __init__(self):
        self.main_state = {}  # Main database state
        self.transaction_state = None  # Holds transaction changes
        self.transaction_active = False

    def get(self, key):
        if self.transaction_active and key in self.transaction_state:
            return self.transaction_state[key]
        return self.main_state.get(key, None)

    def put(self, key, value):
        if not self.transaction_active:
            raise Exception("No active transaction. Use begin_transaction() first.")
        self.transaction_state[key] = value

    def begin_transaction(self):
        if self.transaction_active:
            raise Exception("A transaction is already active.")
        self.transaction_active = True
        self.transaction_state = {}

    def commit(self):
        if not self.transaction_active:
            raise Exception("No active transaction to commit.")
        for key, value in self.transaction_state.items():
            self.main_state[key] = value
        self.transaction_active = False
        self.transaction_state = None

    def rollback(self):
        if not self.transaction_active:
            raise Exception("No active transaction to rollback.")
        self.transaction_active = False
        self.transaction_state = None
