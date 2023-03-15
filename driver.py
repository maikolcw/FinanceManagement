# Name: Maikol Chow Wang

from account import Account
from bank import Bank
from budget import Budget
from budget_finance import BudgetFinance
from fam import FAM
from user import User


def load_test_account():
    # Existing account username is : "UserOne"
    user_one = User("UserOne", 27, "The Angel")
    notification_dictionary = {"Near": 0, "PassPercent": 0, "Exceed": 0}

    # set up budget for each category at 1000 dollar amount
    budget_entertainment = Budget("Games and Entertainment", False, 0, 1000, 1000, notification_dictionary)
    budget_clothing = Budget("Clothing and Accessories", False, 0, 1000, 1000, notification_dictionary)
    budget_eating = Budget("Eating Out", False, 0, 1000, 1000, notification_dictionary)
    budget_misc = Budget("Miscellaneous", False, 0, 1000, 1000, notification_dictionary)
    transaction_list_entertainment = []
    transaction_list_clothing = []
    transaction_list_eating = []
    transaction_list_misc = []

    # set up one bank object at 10000 dollar amount
    bank_one = Bank("test bank", 1234, 10000)

    # budget finance objects
    budget_finance_entertainment = BudgetFinance(budget_entertainment, transaction_list_entertainment)
    budget_finance_clothing = BudgetFinance(budget_clothing, transaction_list_clothing)
    budget_finance_eating = BudgetFinance(budget_eating, transaction_list_eating)
    budget_finance_misc = BudgetFinance(budget_misc, transaction_list_misc)

    # set up budget finance dictionary
    budget_finances_dictionary = {"Games and Entertainment": budget_finance_entertainment,
                                  "Clothing and Accessories": budget_finance_clothing,
                                  "Eating Out": budget_finance_eating,
                                  "Miscellaneous": budget_finance_misc
                                  }

    test_user_account = Account(user_one, bank_one, budget_finances_dictionary)
    return test_user_account


def main():
    test_account = load_test_account()
    account_list = [test_account]
    fam = FAM(account_list)
    fam.fam_main_menu()


if __name__ == '__main__':
    main()
