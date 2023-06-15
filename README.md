## Budget App

The Budget App is a project from the Scientific Programming with Python course on FreeCodeCamp. It is designed to help users manage their budget by providing functionalities for creating, depositing, withdrawing, transferring funds between different categories, generating spend charts, and running unit tests.

### Features

1. **Create Budget Categories:** Users can create different budget categories, such as groceries, entertainment, utilities, etc., to allocate their funds effectively.

2. **Deposit Funds:** Users can deposit funds into their budget categories, specifying the amount and the category.

3. **Withdraw Funds:** Users can withdraw funds from their budget categories, specifying the amount and the category.

4. **Transfer Funds:** Users can transfer funds between different budget categories, ensuring a balanced distribution of their budget.

5. **Check Category Balance:** Users can check the current balance of any budget category to track their expenses and ensure they stay within their allocated limits.

6. **Generate Spend Chart:** Users can generate a spend chart that visually represents the distribution of their expenses across different budget categories.

### Getting Started

To use the Budget App, follow these steps:

1. Clone the repository or download the source code files.

2. Make sure you have Python installed on your machine.

3. Open the terminal or command prompt and navigate to the project directory.

4. Run the `main.py` file using the Python interpreter: `python main.py`.

5. The unit tests for the Budget App will be executed automatically, verifying the correctness of the app's functionality.

6. Follow the on-screen instructions to interact with the Budget App.

7. **Run Unit Tests:** Users can automatically run unit tests for the Budget App by executing the `main.py` file. The tests ensure that the app functions correctly and meets the expected behavior.


### Requirements

The Budget App requires the following dependencies:

- Python 3.x

### Usage Example

```python
# Import the BudgetApp class
import budget
from budget import create_spend_chart

# Create budget categories
Groceries=budget.Category("Groceries")
Entertainment=budget.Category("Entertainment")
Utilities=budget.Category("Utilities")

# Deposit funds into a category
Groceries.deposit(100,"(lots of) banana chips")
Entertainment.deposit(50,"movies and videogames")

# Withdraw funds from a category
Groceries.withdraw( 50)

# Transfer funds between categories
Entertainment.transfer(25,Utilities)

# Check category balance
groceries_balance = Groceries.get_balance()
print(f"Groceries balance: ${groceries_balance}")
print(f"Entertainment balance: ${Entertainment.get_balance()}")
print(f"Utilities balance: ${Utilities.get_balance()}")

# Display all categories and their balances
print(create_spend_chart([Groceries, Entertainment, Utilities]))
```

Special thanks to FreeCodeCamp for providing the Scientific Programming with Python course and inspiring this project.
