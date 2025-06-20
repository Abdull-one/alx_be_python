class BankAccount:
    """
    A simple BankAccount class that encapsulates banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The initial account balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")