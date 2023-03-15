"""This module implements the Transaction class"""


class Transaction:
    """This class represents a Transaction"""

    def __init__(self, datetime, dollar_amount, name_of_place):
        """
        Initializes transaction
        :param datetime: a datetime
        :param dollar_amount: a float
        :param name_of_place: a string
        """
        self._datetime = datetime
        self._dollar_amount = float(dollar_amount)
        self._name_of_place = name_of_place

    def get_datetime(self):
        """
        :return: datetime as a datetime
        """
        return self._datetime

    def set_datetime(self, datetime):
        """
        Sets datetime
        :param datetime: a datetime
        """
        self._datetime = datetime

    def get_dollar_amount(self):
        """
        :return: dollar amount as a float
        """
        return self._dollar_amount

    def set_dollar_amount(self, dollar_amount):
        """
        Sets dollar amount
        :param dollar_amount: a float
        """
        self._dollar_amount = dollar_amount

    def get_name_of_place(self):
        """
        :return: name of place as a string
        """
        return self._name_of_place

    def set_name_of_place(self, name_of_place):
        """
        Sets name of place
        :param name_of_place: a string
        """
        self._name_of_place = name_of_place

    def __str__(self):
        """
        :return: A user-friendly formatted string that shows transaction details
        """
        return f"Transaction:\n" \
               f"date: {self._datetime.replace(microsecond=0)}\n" \
               f"dollar amount: ${self._dollar_amount:.2f}\n" \
               f"location: {self._name_of_place}"
