# Hangman game

## How to play the game?

One player thinks of a word or phrase and the other tries to guess what it is one letter at a time.
The first player draws a number of dashes equivalent to the number of letters in the word. If the guessing player suggests a letter that occurs in the word, the other player fills in the blanks with that letter in the right places. If the word does not contain the suggested letter, the other player draws one element of a hangman’s gallows. As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word. The number of incorrect guesses before the game ends is up to the players, but completing a character in a noose provides a minimum of ten wrong answers until the game ends.

## Objective

Guess the word/phrase before your man gets hung!

## Signature
```python
def hangman(clue_word):
    pass
```

## Test examples
```python
python3 hangman.py Inception
Welcome to Hangman! Let's play!
_ _ _ _ _ _ _ _ _

Guess a letter: n

_ n _ _ _ _ _ _ n

Guess a letter: o

_ n _ _ _ _ _ o n

Guess a letter: p

_ n _ _ p _ _ o n

Guess a letter: k

Incorrect!

Guess a letter:

...
Guess a letter:

I n c e p t i o n

Congratulations!

```

If the player cannot guess the word in ten tries, the game ends and the user should receive this final message!

```
You lost!
 _________
|    |    |
|  \ O /  |
|    |    |
|    |    |
|   / \   |
```

## Matrix Bombing

You are given a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

* All of the **3 to 8 neighbours** (depending on where you hit!) of the target are reduced by the value of the target.
* Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10  10  10
10   9  10
10  10  10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary, where keys are the matrix positions, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

## Signature:
```python
def matrix_bombing_plan(m):
    pass
```

## Test Example:
```python
>>> matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```

We can see that if we drop the bomb at `(1, 1)` or `(2, 1)`, we will do the most damage!


# Money Tracker

In a file called `money_tracker.py` implement a program that tracks user incomes and expenses.
We are going to use the TDD approach to create our small application. Write your tests in `test_money_tracker.py`.

Your application must have the following functionalities:
- Show all user data(incomes and expenses).
- Show user data for specific date.
- Lists all expense categories.
- Lists all income categories.
- The user can add new income or expense for specific date and category.
- The user must be able to create new categories.

In the `money_tracker.py` module you must have these methods:

```python
def list_user_data(all_user_data):
    pass


def show_user_incomes(all_user_data):
    pass


def show_user_savings(all_user_data):
    pass


def show_user_deposits(all_user_data):
    pass


def show_user_expenses(all_user_data):
    pass


def list_user_expenses_ordered_by_categories(all_user_data):
    pass


def show_user_data_per_date(date, all_user_data):
    pass


def list_income_categories(all_user_data):
    pass


def list_expense_categories(all_user_data):
    pass


def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass
```

The user data is going to be saved in a file called `money_tracker.txt`. In order to have a working program, you should parse the information saved in the file. The `modey_tracker.txt` has a specific format:
```txt
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
```

The following test example is based on the data in the `money_tracker.txt`
## Examples:
```python
Hello, Peter!
Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 4
New income amount:
>>> 10
New income type:
>>> Deposit
New income date:
23-03-2019


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
10, Deposit, New income


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
```


** To be able to test your methods, you have to pass parameters that are not going to change with time.

## Example
```python
>>> all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
>>> show_user_incomes(all_user_data)
[(10, 'Deposit'), (50, 'Savings'), (700, 'Salary')]
```

For the `all_user_data` parameter use the `dict` data structure.

** Do not forget to catch the exceptions:**
- when a user passes an invalid option(number out of the range (1, 6))
- when the file with the user data does not exist
- when a user tries to add an income/expense with a negative amount of money. For this example, you have to create your custom exception.


## Test Examples:
```python
>>> list_user_expenses_ordered_by_categories({'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
[(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'), (12, 'Eating Out'), (15, 'Food'), (41.79, 'Food'), (7, 'House'), (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')]
>>> show_user_data_per_date('23-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
[(50, 'Savings', 'New Income'), (15, 'Food', 'New Expense'), (200, 'Deposit', 'New Income'), (5, 'Sports', 'New Expense'), (10, 'Deposit', 'New income')]  
>>> list_income_categories({'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
['Deposit', 'Salary', 'Savings']   
>>> add_income('Salary', 600, '25-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
>>> add_expense('Health', 2.5, '25-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})

```
