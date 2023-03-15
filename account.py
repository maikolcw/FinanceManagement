"""This module implements the Account class"""


class Account:
    """This class represents all account activities"""

    def __init__(self, user, bank, budget_finance_dictionary):
        """
        Initializes Account object. The budget finance dictionary is a dictionary with
        budget finance objects. These budget finance objects can be accessed with a budget category
        key.
        :param user: user object
        :param bank: bank object
        :param budget_finance_dictionary: dictionary of budget finance objects
        """
        self._user = user
        self._bank = bank
        self._budget_finance_dictionary = budget_finance_dictionary

    def get_user_name(self):
        """
        Gets account username
        :return: string
        """
        return self._user.get_name()

    def get_user_type(self):
        """
        Gets account user type
        :return: string
        """
        return self._user.get_usertype()

    def get_budget_allocated(self, budget_category):
        """
        Gets account budget allocated for a certain budget category
        :param budget_category: string
        :return: float
        """
        return self._budget_finance_dictionary[budget_category].get_budget_total_amount_allocated()

    def get_budget_left(self, budget_category):
        """
        Gets account budget left for a certain budget category
        :param budget_category: string
        :return: float
        """
        return self._budget_finance_dictionary[budget_category].get_budget_amount_left()

    def get_budget_spent(self, budget_category):
        """
        Get account budget spent for a certain budget category
        :param budget_category: string
        :return: float
        """
        return self._budget_finance_dictionary[budget_category].get_budget_amount_spent()

    def get_notification_dictionary(self, budget_category):
        """
        Get budget notification dictionary for a certain budget category
        :param budget_category: string
        :return: dictionary
        """
        return self._budget_finance_dictionary[budget_category].get_notification_dictionary()

    def is_transaction_feasible(self, transaction_amount):
        """Returns false if amount will cause bank balance to go below 0"""
        return not self._bank.get_bank_balance() - float(transaction_amount) < 0

    def is_account_locked(self, budget_category):
        """
        Checks if the account is locked for "The Rebel" users and if budget category is
        locked for other users
        :param budget_category: str
        :return: boolean
        """
        if self.get_user_type() == "The Angel":
            return False
        elif self.get_user_type() == "The Troublemaker":
            return self.get_budget_finance_status(budget_category)
        else:
            if self.is_two_budget_locked():
                return self.is_two_budget_locked()
            else:
                return self.get_budget_finance_status(budget_category)

    def withdraw_from_bank(self, amount):
        """
        Withdraws x amount due to a transaction
        :param amount: float
        """
        self._bank.subtract_from_balance(float(amount))

    def add_a_transactions(self, budget_category, transaction):
        """
        Add a transaction to the transaction list for a certain budget category
        :param budget_category:
        :param transaction:
        """
        self._budget_finance_dictionary[budget_category].add_to_transactions(transaction)

    def update_budget(self, budget_category, transaction_amount):
        """
        Update account budget's amount left and spent for a certain budget category
        :param budget_category: string
        :param transaction_amount: float
        """
        self._budget_finance_dictionary[budget_category].update_budget(transaction_amount)

    def print_transactions(self, budget_category):
        """
        Prints a record of saved transactions
        """
        for transaction in self._budget_finance_dictionary[budget_category].get_transaction_list():
            print(transaction)

    def get_budget_finance_status(self, budget_category):
        """
        Retrieves lock status of budget finance object
        :param budget_category: str
        :return: boolean
        """
        return self._budget_finance_dictionary[budget_category].get_budget_status()

    def set_budget_finance_status(self, budget_category, status):
        """
        Sets lock status of budget finance object
        :param budget_category: str
        :param status: boolean
        """
        return self._budget_finance_dictionary[budget_category].set_budget_status(status)

    def get_bank(self):
        """
        Gets bank object
        :return: bank object
        """
        return self._bank

    def is_two_budget_locked(self):
        """
        Check if account has two budget category locked, specifically for "The Rebel" users
        :return: boolean
        """
        games_lock = self.get_budget_finance_status("Games and Entertainment")
        clothes_lock = self.get_budget_finance_status("Clothing and Accessories")
        food_lock = self.get_budget_finance_status("Eating Out")
        misc_lock = self.get_budget_finance_status("Miscellaneous")
        count = 0
        lock_list = [games_lock, clothes_lock, food_lock, misc_lock]
        for lock in lock_list:
            if lock:
                count += 1
        if count > 1:
            return True
        else:
            return False

    def __str__(self):
        """
        :return: A user-friendly formatted string that shows account details
        """
        return f"User: {self._user}\n" \
               f"{self._bank}\n" \
               f"{self._budget_finance_dictionary['Games and Entertainment']}\n" \
               f"{self._budget_finance_dictionary['Clothing and Accessories']}\n" \
               f"{self._budget_finance_dictionary['Eating Out']}\n" \
               f"{self._budget_finance_dictionary['Miscellaneous']}"
