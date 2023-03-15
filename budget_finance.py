class BudgetFinance:
    """This class represents the interactions between a budget and its transactions"""

    def __init__(self, budget, transaction_list):
        """
        Initializes the budget finance object
        :param budget: a budget object
        :param transaction_list: list of transactions
        """
        self._budget = budget
        self._transaction_list = transaction_list

    def get_budget_category(self):
        """
        Get budget category
        :return: string
        """
        return self._budget.get_budget_category()

    def set_budget_category(self, budget_category):
        """
        Set budget category
        :param budget_category: string
        """
        self._budget.set_budget_category(budget_category)

    def get_budget_status(self):
        """
        Get budget status
        :return: string
        """
        return self._budget.get_status()

    def set_budget_status(self, status):
        """
        Set budget status
        """
        self._budget.set_status(status)

    def get_budget_amount_spent(self):
        """
        Get budget amount spent
        :return: float
        """
        return self._budget.get_amount_spent()

    def set_budget_amount_spent(self, amount_spent):
        """
        Set budget amount spent
        :param amount_spent: float
        """
        self._budget.set_amount_spent(amount_spent)

    def get_budget_amount_left(self):
        """
        Get budget amount left
        :return: float
        """
        return self._budget.get_amount_left()

    def set_budget_amount_left(self, amount_left):
        """
        Set budget amount left
        :param amount_left: float
        """
        self._budget.set_amount_left(amount_left)

    def get_budget_total_amount_allocated(self):
        """
        Get budget total amount allocated
        :return: float
        """
        return self._budget.get_total_amount_allocated()

    def set_budget_total_amount_allocated(self, total_amount_allocated):
        """
        Set budget total amount allocated
        :param total_amount_allocated: float
        """
        self._budget.set_total_amount_allocated(total_amount_allocated)

    def get_notification_dictionary(self):
        """
        Get notification dictionary
        :return: notification dictionary
        """
        return self._budget.get_notification_dictionary()

    def get_transaction_list(self):
        """
        Get transaction list
        :return: list of Transaction objects
        """
        return self._transaction_list

    def set_transaction_list(self, transaction_list):
        """
        Sets the transaction ist
        :param transaction_list: list of Transaction objects
        """
        self._transaction_list = transaction_list

    def add_to_transactions(self, transaction):
        """
        Add a transaction to the transaction list
        :param transaction: transaction object
        """
        self._transaction_list.append(transaction)

    def update_budget(self, transaction_amount):
        """
        Updates a budget's amount left and spent
        :param transaction_amount: transaction amount
        """
        self._budget.update_budget(transaction_amount)

    def __str__(self):
        """
        :return: A user friendly formatted string that shows budget finance details
        """
        return f"Budget Category: {self._budget.get_budget_category()}\n" \
               f"Budget Allocated: {self._budget.get_total_amount_allocated()}\n"
