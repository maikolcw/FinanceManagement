"""This module houses the Bank class"""


class Bank:
    """
    Represents a Bank account for a User identified by its account number.
    """

    def __init__(self, bank_name, account_number, bank_balance):
        """
        Initializes Bank details
        :param bank_name: a string
        :param account_number: an int
        :param bank_balance: a float
        """
        self._bank_name = bank_name
        self._account_number = account_number
        self._bank_balance = bank_balance

    def get_name(self):
        """
        :return: bank name as a string
        """
        return self._bank_name

    def get_account_number(self):
        """
        :return: account number as an int
        """
        return self._account_number

    def get_bank_balance(self):
        """
        :return: bank balance as a float
        """
        return self._bank_balance

    def set_bank_name(self, bank_name):
        """
        Sets bank name
        :param bank_name: a string
        """
        self._bank_name = bank_name

    def set_account_number(self, account_number):
        """
        Sets account number
        :param account_number: an int
        """
        self._account_number = account_number

    def set_bank_balance(self, bank_balance):
        """
        Sets bank balance
        :param bank_balance: a float
        """
        self._bank_balance = bank_balance

    def add_to_balance(self, amount):
        """
        Add x amount to bank balance
        :param amount: a float
        """
        self._bank_balance += amount

    def subtract_from_balance(self, amount):
        """
        Remove x amount from bank balance
        :param amount: a float
        """
        self._bank_balance -= amount

    def __str__(self):
        """
        :return: A user friendly formatted string that shows Bank details
        """
        return f"Bank name: {self._bank_name}\n" \
               f"Account number: {self._account_number}\n" \
               f"Balance: ${self._bank_balance:.2f}\n"
