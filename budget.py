"""This module implements the Budget class"""


class Budget:
    """This class represents a Budget for transactions"""

    def __init__(self, budget_category, status, amount_spent, amount_left, total_amount_allocated,
                 notification_dictionary):
        """
        Initializes the budget object
        :param budget_category: a string
        :param status: a boolean
        :param amount_spent: a float
        :param amount_left: a float
        :param total_amount_allocated: a float
        :param notification_dictionary: dictionary
        """
        self._budget_category = budget_category
        self._status = status
        self._amount_spent = amount_spent
        self._amount_left = amount_left
        self._total_amount_allocated = total_amount_allocated
        self._notification_dictionary = notification_dictionary

    def get_budget_category(self):
        """
        :return: category as a string
        """
        return self._budget_category

    def set_budget_category(self, budget_category):
        """
        Sets budget category
        :param budget_category: a string
        """
        self._budget_category = budget_category

    def get_status(self):
        """
        :return: status as a boolean
        """
        return self._status

    def set_status(self, status):
        """
        Sets status
        :param status: a boolean
        """
        self._status = status

    def get_amount_spent(self):
        """
        :return: amount spent as a float
        """
        return self._amount_spent

    def set_amount_spent(self, amount_spent):
        """
        Sets amount spent
        :param amount_spent: a float
        """
        self._amount_spent = amount_spent

    def get_amount_left(self):
        """
        :return: amount left as a float
        """
        return self._amount_left

    def set_amount_left(self, amount_left):
        """
        Sets amount left
        :param amount_left: a float
        """
        self._amount_left = amount_left

    def get_total_amount_allocated(self):
        """
        :return: total amount allocated as a float
        """
        return self._total_amount_allocated

    def set_total_amount_allocated(self, total_amount_allocated):
        """
        Sets total amount allocated
        :param total_amount_allocated: a float
        """
        self._total_amount_allocated = total_amount_allocated

    def get_notification_dictionary(self):
        """
        Gets notification dictionary to check budget warning
        :return: dictionary
        """
        return self._notification_dictionary

    def update_budget(self, transaction_amount):
        """
        Updates budget amount spent and left from transaction amount
        :param transaction_amount: float
        """
        self._amount_spent += transaction_amount
        self._amount_left -= transaction_amount

    def __str__(self):
        """
        :return: A user friendly formatted string that shows budget details
        """
        return f"Budget category: {self._budget_category}\n" \
               f"Status: {self._status}\n" \
               f"Amount spent: ${self._amount_spent:.2f}\n" \
               f"Amount left: ${self._amount_left:.2f}\n" \
               f"Total amount allocated: {self._total_amount_allocated:.2f}\n"
