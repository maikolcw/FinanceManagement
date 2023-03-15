This program (Financial AllinOne Management) helps users in finance management, by simulating account balances, balance tracking, and balance restrictions. The system will register a user, keep track of all the spending/transactions on their bank account, and lock the account if certain conditions are met.

A UML diagram will help identify all the classes, attributes, and behaviors the program will need.


Registering A User

On startup, the user (usually a parent) must register their child's financial details. This includes (but is not necessarily limited to):

●	The users name

●	Age

●	User Type 

●	Bank Account number

●	Bank Name

●	Bank Balance

●	Their budgets 



Budget Categories

Each child that is being monitored is assigned the following budget categories. The exact value of each budget is assigned when registering the child as a user.

●	Games and Entertainment

●	Clothing and Accessories

●	Eating Out

●	Miscellaneous




A User Menu

Once the user account is set up and the budgets have been created, the system prompts the user with the following menu options. 

1.	View Budgets
Selecting this option shows the user the current status of their budgets (locked or not) in addition to the amount spent, amount left, and the total amount allocated to the budget.

2. Record a Transaction
This takes the user to a sub-menu where they are prompted to enter the transaction details (refer to the "Record Transactions" heading below).

3. View Transactions by Budget
This takes the user to a sub-menu where they select their budget category and view all the transactions to date in that category.

4. View Bank Account Details
The application prints out the bank account details of the user and all transactions conducted to date alongside the closing balance.



Record Transactions

The application maintains a collection of transactions which represent money going out of the users bank account. Provides the user an option to enter transaction details.

Each transaction contains the following information:

●	The timestamp the transaction was recorded (a nicely formatted datetime value).

●	The dollar amount (positive, non-zero number).

●	The budget category that this transaction belongs to.

    ●	Provides users with a list of categories and prompts users to select one.

●	The name of the shop/website where the purchase took place.

The user is not allowed to record a transaction if the transaction would cause their bank balance to go below zero. Additionally, the system subtracts the required amount from the users bank balance once a transaction has been recorded.

Depending on the type of user (more on this in the User Types section below), after a transaction has been recorded system will perform checks to see if a warning or notification should be issued. A list of transactions that have taken place in a budget category will be printed out to the console if:

●	The user receives a warning that they are getting close to exceeding their assigned budget for the category in question

●	The user receives a notification that they have exceeded their assigned budget for the category in question.

The transactions printed will be the transactions pertaining to the budget category in question. That is, if the user gets a warning that they are about to exceed their budget for "Games and Entertainment", then any transactions belonging to this category will be printed for review.



Lock Out

The app has the ability to lock a user out of recording transactions (and effectively spending any money) based on certain conditions as specified by their User Type (more on this in the User Types section below).

If a user has been locked from a budget category:

●	They will be notified of this via a console message.

●	Any attempt at recording transactions in the affected budget category will be denied.



User Types

Every family and every child is unique. The F.A.M. recognizes this and supports different types of users. The app provides different moderation levels for each user type.


The Angel

The Angel represents a user whose parents are not worried at all. This child has never broken a single rule. 

This user type:

●	Never gets locked out of a budget category. They can continue spending money even if they exceed the budget in question.

●	Gets politely notified if they exceed a budget category.

●	Gets a warning if they exceed more than 90% of a budget.


The Troublemaker

The Troublemaker represents a user who often finds themselves in trouble. These are usually minor incidents and their parents are concerned but not worried. Parents usually set up a FAM account to monitor their expenses and impose light restrictions.

This user type:

●	Gets a warning if they exceed more than 75% of a budget category.

●	Gets politely notified iIf they exceed a budget category.

●	Gets locked out of conducting transactions in a budget category if they exceed it by 120% of the amount assigned to the budget in question.

 
The Rebel

The Rebel represents a user who refuses to follow any rules. Parents of these children are quite worried and turn to F.A.M. when they are out of options. 

This user type is strictly monitored: 

●	They get a warning for every transaction after exceeding 50% of a budget. 

●	Gets ruthlessly notified if they exceed a budget category. 

●	Gets locked out of conducting transactions in a budget category if they exceed it by 100% of the amount assigned to the budget in question.

●	If they exceed their budget in 2 or more categories then they get locked out of their account completely



