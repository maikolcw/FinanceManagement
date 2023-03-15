import datetime

from account import Account
from bank import Bank
from budget import Budget
from budget_finance import BudgetFinance
from transaction import Transaction
from user import User

"""This module implements the FAM class"""


class FAM:
    """
    This class represents a UI the user will interact with for the FAM program.
    """

    def __init__(self, account_list):
        """
        Initializes the FAM object
        :param account_list: list of account objects
        """
        self._account_list = account_list

    def fam_main_menu(self):
        """
        This method houses the new user and existing user menu
        """
        user_input = None
        print("\nWelcome to the FAM")
        print("---------------")
        while user_input != 3:
            print("1. New User")
            print("2. Existing User")
            print("3. Quit")
            string_input = input("Please select an option (1-3)")

            if string_input == "":
                continue

            user_input = int(string_input)

            if user_input == 1:
                current_account_selected = FAM.fam_new_user_menu()
                self._account_list.append(current_account_selected)
            if user_input == 2:
                current_account_selected = self.fam_find_existing_account()
                FAM.fam_existing_user_menu(current_account_selected)

    @staticmethod
    def fam_existing_user_menu(account):
        """
        The existing user menu lets users record a transaction, view budgets, view transactions by budget,
        and view bank account details.
        :param account: account object
        """
        try:
            user_input = None
            print("\nExisting User Menu")
            print("---------------")
            while user_input != 5:
                print("1. Record a transaction")
                print("2. View budgets")
                print("3. View transactions by budget")
                print("4. View bank account details")
                print("5. Quit")
                string_input = input("Please select an option (1-5)")

                if string_input == "":
                    continue

                user_input = int(string_input)
                if user_input == 1:
                    budget_category_input = FAM.pick_budget_category()
                    if account.is_account_locked(budget_category_input):
                        if account.is_two_budget_locked() and account.get_user_type() == "The Rebel":
                            print("Sorry you have exceeded two budget categories and your account is locked!")
                        else:
                            print(f"Cannot make transaction, {budget_category_input} budget is locked!")
                    else:
                        place_info = input("Enter the place you went to: ")
                        amount_info = float(input("Enter the amount spent: (a number)"))
                        if account.is_transaction_feasible(amount_info):
                            new_transaction = Transaction(datetime.datetime.now(), amount_info, place_info)
                            account.withdraw_from_bank(amount_info)
                            account.add_a_transactions(budget_category_input, new_transaction)
                            account.update_budget(budget_category_input, amount_info)
                            print(f"\nYou added the transaction of ${amount_info:.2f} at {place_info}\n")
                            FAM.perform_check(account, budget_category_input)
                        else:
                            print("Sorry that transaction will put your bank balance below 0.")
                if user_input == 2:
                    games_budget = account.get_budget_allocated("Games and Entertainment")
                    clothes_budget = account.get_budget_allocated("Clothing and Accessories")
                    eating_budget = account.get_budget_allocated("Eating Out")
                    misc_budget = account.get_budget_allocated("Miscellaneous")
                    print(f"\nAllocated Budgets\n"
                          f"------------------------\n"
                          f"Games and Entertainment: ${games_budget}\n"
                          f"Lock status: {account.get_budget_finance_status('Games and Entertainment')}\n"
                          f"Amount spent: ${account.get_budget_spent('Games and Entertainment')}\n"
                          f"Amount left: ${account.get_budget_left('Games and Entertainment')}\n"

                          f"Clothing and Accessories: ${clothes_budget}\n"
                          f"Lock status: {account.get_budget_finance_status('Clothing and Accessories')}\n"
                          f"Amount spent: ${account.get_budget_spent('Clothing and Accessories')}\n"
                          f"Amount left: ${account.get_budget_left('Clothing and Accessories')}\n"

                          f"Eating Out: ${eating_budget}\n"
                          f"Lock status: {account.get_budget_finance_status('Eating Out')}\n"
                          f"Amount spent: ${account.get_budget_spent('Eating Out')}\n"
                          f"Amount left: ${account.get_budget_left('Eating Out')}\n"

                          f"Miscellaneous: ${misc_budget}\n"
                          f"Lock status:{account.get_budget_finance_status('Miscellaneous')}\n"
                          f"Amount spent: ${account.get_budget_spent('Miscellaneous')}\n"
                          f"Amount left: ${account.get_budget_left('Miscellaneous')}\n")

                if user_input == 3:
                    budget_category_input = FAM.pick_budget_category()
                    account.print_transactions(budget_category_input)

                if user_input == 4:
                    user_bank = account.get_bank()
                    print(f"Bank Info:\n"
                          f"-------------------------\n")
                    print(f"Bank name: {user_bank.get_name()}")
                    print(f"Account number: {user_bank.get_account_number()}")
                    print(f"Bank balance: {user_bank.get_bank_balance()}")
                    print(f"Total transactions: \n")

                    print(f"Games and Entertainment\n"
                          f"--------------------------\n")
                    account.print_transactions("Games and Entertainment")
                    print(f"Clothing and Accessories\n"
                          f"--------------------------\n")
                    account.print_transactions("Clothing and Accessories")
                    print(f"Eating Out\n"
                          f"--------------------------\n")
                    account.print_transactions("Eating Out")
                    print(f"Miscellaneous\n"
                          f"--------------------------\n")
                    account.print_transactions("Miscellaneous")
        except ValueError:
            print(f"Error: Please input proper values.")
            FAM.fam_existing_user_menu(account)

    @staticmethod
    def perform_check(account, budget_category):
        """
        Helper method that perform checks if user is near or passed a budget limit
        :param account: account object
        :param budget_category: string
        """
        if account.get_user_type() == "The Angel":
            FAM.perform_angel_check(account, budget_category)
        if account.get_user_type() == "The Troublemaker":
            FAM.perform_trouble_maker_check(account, budget_category)
        if account.get_user_type() == "The Rebel":
            FAM.perform_rebel_check(account, budget_category)

    @staticmethod
    def perform_angel_check(account, budget_category):
        """
        Helper method for perform check that specifically checks for Angel users
        :param account: account object
        :param budget_category: string
        """
        print_counter = 0
        if account.get_budget_left(budget_category) > 0:
            if account.get_budget_left(budget_category) / account.get_budget_allocated(budget_category) <= 0.1:
                if account.get_notification_dictionary(budget_category)["Near"] != 1:
                    print("Warning: Getting close to exceeding assigned budget")
                    print_counter = 1
        if account.get_budget_spent(budget_category) > account.get_budget_allocated(budget_category):
            if account.get_notification_dictionary(budget_category)["Exceed"] != 1:
                print("Notification: You have exceeded the budget")
                account.get_notification_dictionary(budget_category)["Exceed"] = 1
                print_counter = 1
        if account.get_budget_spent(budget_category) / account.get_budget_allocated(budget_category) > 0.9:
            if account.get_notification_dictionary(budget_category)["PassPercent"] != 1:
                print("Warning: You have exceeded more than 90% of a budget")
                account.get_notification_dictionary(budget_category)["PassPercent"] = 1
                print_counter = 1
        if print_counter == 1:
            print(account.print_transactions(budget_category))

    @staticmethod
    def perform_trouble_maker_check(account, budget_category):
        """
        Helper method for perform check that specifically checks for Troublemaker users
        :param account: account object
        :param budget_category: string
        """
        print_counter = 0
        if account.get_budget_left(budget_category) > 0:
            if account.get_budget_left(budget_category) / account.get_budget_allocated(budget_category) <= 0.1:
                if account.get_notification_dictionary(budget_category)["Near"] != 1:
                    print("Warning: Getting close to exceeding assigned budget")
                    print_counter = 1
        if account.get_budget_spent(budget_category) > account.get_budget_allocated(budget_category):
            if account.get_notification_dictionary(budget_category)["Exceed"] != 1:
                print("Notification: You have exceeded the budget")
                account.get_notification_dictionary(budget_category)["Exceed"] = 1
                print_counter = 1
        if account.get_budget_spent(budget_category) / account.get_budget_allocated(budget_category) > 0.75:
            if account.get_notification_dictionary(budget_category)["PassPercent"] != 1:
                print("Warning: You have exceeded more than 75% of a budget")
                account.get_notification_dictionary(budget_category)["PassPercent"] = 1
                print_counter = 1
        if account.get_budget_spent(budget_category) / account.get_budget_allocated(budget_category) > 2.2:
            print(f"Warning: You have exceeded more than 120% of the budget, {budget_category} has been locked!")
            account.set_budget_finance_status(budget_category, True)
        if print_counter == 1:
            print(account.print_transactions(budget_category))

    @staticmethod
    def perform_rebel_check(account, budget_category):
        """
        Helper method for perform check that specifically checks for Rebel users
        :param account: account object
        :param budget_category: string
        """
        print_counter = 0
        if account.get_budget_left(budget_category) > 0:
            if account.get_budget_left(budget_category) / account.get_budget_allocated(budget_category) <= 0.1:
                if account.get_notification_dictionary(budget_category)["Near"] != 1:
                    print("Warning: Getting close to exceeding assigned budget")
                    print_counter = 1
        if account.get_budget_spent(budget_category) / account.get_budget_allocated(budget_category) > 2:
            if account.get_notification_dictionary(budget_category)["Exceed"] != 1:
                print("Notification: Hey, you have exceeded 100% of the budget!!!")
                print(f"Your {budget_category} budget is locked!")
                account.set_budget_finance_status(budget_category, True)
                if account.is_two_budget_locked():
                    print("You are locked out for the entire account.")
                print_counter = 1
        if account.get_budget_spent(budget_category) / account.get_budget_allocated(budget_category) > 0.5:
            if account.get_notification_dictionary(budget_category)["PassPercent"] != 1:
                print("Warning: You have exceeded more than 50% of a budget")
                print_counter = 1
        if print_counter == 1:
            print(account.print_transactions(budget_category))

    def fam_find_existing_account(self):
        """
        Find account menu that checks if an account exists
        :return: account object
        """
        searched_user_account = None
        while searched_user_account is None:
            user_account_input = input("Please enter account user name:")
            searched_user_account = self.find_account(user_account_input)
        return searched_user_account

    def find_account(self, user_name):
        """
        Helper function for fam_find_existing_account()
        :param user_name: string
        :return: account object
        """
        if self.does_account_exist(user_name):
            for account in self._account_list:
                if account.get_user_name() == user_name:
                    return account
        else:
            print("Sorry that account does not exist")
            return None

    def does_account_exist(self, user_name):
        """
        Helper function for find_account() to check if account exists
        :param user_name: string
        :return: boolean
        """
        a_boolean = False
        for account in self._account_list:
            if account.get_user_name() == user_name:
                a_boolean = True
        return a_boolean

    @staticmethod
    def fam_new_user_menu():
        """
        Menu for new user registration that guide user to make user, bank, and budget finance
        objects for an account object
        """
        user = FAM.fam_make_user_menu()
        bank = FAM.fam_make_bank_menu()
        budget_games_entertainment = FAM.fam_make_budget_menu("Games and Entertainment")
        budget_clothing_accessories = FAM.fam_make_budget_menu("Clothing and Accessories")
        budget_eating_out = FAM.fam_make_budget_menu("Eating Out")
        budget_miscellaneous = FAM.fam_make_budget_menu("Miscellaneous")
        transaction = []
        budget_finance_games_entertainment = BudgetFinance(budget_games_entertainment, transaction)
        budget_finance_clothing_accessories = BudgetFinance(budget_clothing_accessories, transaction)
        budget_finance_eating_out = BudgetFinance(budget_eating_out, transaction)
        budget_finance_miscellaneous = BudgetFinance(budget_miscellaneous, transaction)
        budget_finance_dictionary = \
            {budget_finance_games_entertainment.get_budget_category(): budget_finance_games_entertainment,
             budget_finance_clothing_accessories.get_budget_category(): budget_finance_clothing_accessories,
             budget_finance_eating_out.get_budget_category(): budget_finance_eating_out,
             budget_finance_miscellaneous.get_budget_category(): budget_finance_miscellaneous}
        temp_account = Account(user, bank, budget_finance_dictionary)
        print(f"The following account has been made: ")
        print(temp_account)
        return temp_account

    @staticmethod
    def fam_make_user_menu():
        """
        Menu for making a new user object
        """
        try:
            user_input = None
            print("\nPlease fill in the following account information:")
            print("-----User Info------")
            name_input = input("What is the user name? ")
            age_input = int(input("What is the user age? "))
            user_temp = 0
            while user_input != 0:
                print("1. The Angel")
                print("2. The Troublemaker")
                print("3. The Rebel")
                user_type_input = input("Please select an user type: ")
                if user_type_input == "":
                    continue
                user_input = int(user_type_input)
                if user_input == 1:
                    user_temp = User(str(name_input), str(age_input), "The Angel")
                    user_input = 0
                if user_input == 2:
                    user_temp = User(str(name_input), str(age_input), "The Troublemaker")
                    user_input = 0
                if user_input == 3:
                    user_temp = User(str(name_input), str(age_input), "The Rebel")
                    user_input = 0
            print("The follower user info has been created: ")
            print(user_temp)
            return user_temp
        except ValueError:
            print(f"Error: Please input proper values.")
            FAM.fam_make_user_menu()

    @staticmethod
    def fam_make_bank_menu():
        """
        Menu for making a new bank object
        """
        try:
            print("-----Bank Info------")
            bank_name_input = input("What is the bank name? ")
            user_input = input("What is the account number? (must be any int) ")
            account_number_input = int(user_input)
            user_input = input("What is the bank balance? (must be a number)")
            bank_balance_input = float(user_input)
            if bank_balance_input < 1:
                raise ValueError
            temp_bank = Bank(bank_name_input, account_number_input, bank_balance_input)
            print("The following bank info has been created: ")
            print(temp_bank)
            return temp_bank
        except ValueError:
            print(f"Error: Please input proper values.")
            FAM.fam_make_bank_menu()

    @staticmethod
    def fam_make_budget_menu(budget_category):
        """
        Menu for making a new budget object
        """
        try:
            print(f"-----{budget_category}------")
            budget_category_input = budget_category
            total_amount_allocated_input = float(input("Please enter the total amount allocated: (a number)"))
            if total_amount_allocated_input < 1:
                raise ValueError
            notification_dictionary = {"Near": 0, "PassPercent": 0, "Exceed": 0}
            temp_budget = Budget(budget_category_input, False, 0,
                                 total_amount_allocated_input, total_amount_allocated_input,
                                 notification_dictionary)
            print("The following budget info has been created: ")
            print(temp_budget)
            return temp_budget
        except ValueError:
            print(f"Error: Please input proper values.")
            FAM.fam_make_budget_menu(budget_category)

    @staticmethod
    def pick_budget_category():
        """
        Menu for picking a budget category
        """
        user_input = None
        budget_category_input = 0
        while user_input != 0:
            print("1. Games and Entertainment")
            print("2. Clothing and Accessories")
            print("3. Eating Out")
            print("4. Miscellaneous")
            user_type_input = input("Please select category type: ")
            if user_type_input == "":
                continue
            user_input = int(user_type_input)
            if user_input == 1:
                budget_category_input = "Games and Entertainment"
                user_input = 0
            if user_input == 2:
                budget_category_input = "Clothing and Accessories"
                user_input = 0
            if user_input == 3:
                budget_category_input = "Eating Out"
                user_input = 0
            if user_input == 4:
                budget_category_input = "Miscellaneous"
                user_input = 0
        return budget_category_input
