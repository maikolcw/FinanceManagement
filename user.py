"""This module implements a User class"""


class User:
    """
    Represents a user in FAM program which is identified by their name,
    age, user type.
    """

    def __init__(self, name, age, user_type):
        """
        Initializes user
        :param name: a string
        :param age: an int
        :param user_type: a string
        """
        self._name = name
        self._age = age
        self._userType = user_type

    def get_name(self):
        """
        :return: name as a string
        """
        return self._name

    def set_name(self, name):
        """
        Sets user's name
        :param name: a string
        """
        self._name = name

    def get_age(self):
        """
        :return: age as an int
        """
        return self._age

    def set_age(self, age):
        """
        Sets user's age
        :param age: an int
        """
        self._age = age

    def get_usertype(self):
        """
        :return: user type as a string
        """
        return self._userType

    def set_usertype(self, user_type):
        """
        Sets user type
        :param user_type: a string
        """
        self._userType = user_type

    def __str__(self):
        """
        :return: A user friendly formatted string that shows user details
        """
        return f"name: {self._name}\n" \
               f"age: {self._age}\n" \
               f"user type: {self._userType}\n" \
