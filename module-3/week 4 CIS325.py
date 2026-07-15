class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner                 # public attribute
        self.__balance = starting_balance  # private attribute
        self.__transactions = []           # private attribute

    def deposit(self, amount):             # public method
        if self.__is_valid_amount(amount):
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            print(f"Deposit successful: ${amount:.2f}")
        else:
            print("Deposit failed: amount must be greater than zero.")

    def withdraw(self, amount):            # public method
        if not self.__is_valid_amount(amount):
            print("Withdrawal failed: amount must be greater than zero.")
        elif amount > self.__balance:
            print("Withdrawal failed: insufficient funds.")
        else:
            self.__balance -= amount
            self.__record_transaction("Withdrawal", amount)
            print(f"Withdrawal successful: ${amount:.2f}")

    def show_balance(self):                # public method
        print(f"Current balance for {self.owner}: ${self.__balance:.2f}")

    def show_transactions(self):           # public method
        print("Transaction History:")
        for transaction in self.__transactions:
            print(transaction)

    def __is_valid_amount(self, amount):   # private method
        return amount > 0

    def __record_transaction(self, transaction_type, amount):  # private method
        self.__transactions.append(f"{transaction_type}: ${amount:.2f}")


# Class instance
my_account = BankAccount("Jared", 100.00)

my_account.show_balance()
my_account.deposit(50.00)
my_account.withdraw(25.00)
my_account.withdraw(200.00)
my_account.deposit(-10.00)
my_account.show_balance()
my_account.show_transactions()
