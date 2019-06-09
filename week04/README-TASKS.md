# The Cash Desk Problem

We are going to train our OOP skill by implementing a few classes, which will represent a cash desk.

The cash desk will do the following things:

* Take money as single bills
* Take money as batches (пачки!)
* Keep a total count
* Tell us some information about the bills it has

## The Bill class

Create a class, called `Bill` which takes one parameter to its constructor - the `amount` of the bill - an integer.

This class will only have **dunders** so you wont be afraid of them anymore!

The class should implement:

* `__str__` and `__repr__`
* `__int__`
* `__eq__` and `__hash__`
* If amount is negative number, raise an `ValueError` error.
* If type of amount isn't `int`, raise an `TypeError` error.

Here is an example usage:

```python
from cashdesk import Bill

a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a) # 10
str(a) # "A 10$ bill"
print(a) # A 10$ bill

a == b # False
a == c # True

money_holder = {}

money_holder[a] = 1 # We have one 10% bill

if c in money_holder:
    money_holder[c] += 1

print(money_holder) # { "A 10$ bill": 2 }
```


## The BatchBill class

We are going to implement a class, which represents more than one bill. A `BatchBill`!

The class takes a list of `Bills` as the single constructor argument.

The class should have the following methods:

* `__len__(self)` - returns the number of `Bills` in the batch
* `total(self)` - returns the total amount of all `Bills` in the batch

We should be able to iterate the `BatchBill` class with a for-loop.

Here is an example:

```python
from cashdesk import Bill, BillBatch

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill
```

In order to do that, you need to implement the following method:

```python
def __getitem__(self, index):
    pass
```

## The CashDesk classs

Finally, implement a `CashDesk` class, which has the following methods:

* `take_money(money)`, where `money` can be either `Bill` or `BatchBill` class
* `total()` - returns the total amount of money currenly in the desk
* `inspect()` - prints a table representation of the money - for each bill, how many copies of it we have.

For example:

```python
from cashdesk import Bill, BillBatch, CashDesk

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()

# We have a total of 390$ in the desk
# We have the following count of bills, sorted in ascending order:
# 10$ bills - 2
# 20$ bills - 1
# 50$ bills - 1
# 100$ bills - 3

```



# Car Racing

You are a big car racing fan!

You want to implement a Python program, that is going to simulate a car race. It feels good to add all your friends and their cars and watch them go round and round. And, of course, some times - even crash.

Your championship is going to consist of several races.

The contestants are located in an extral `cars.json` file that you have to load. There is a sample [`cars.json`](cars.json) file in this repository.

Your final idea is to implement a program that:

- Loads `cars.json` file
- Runs the races
- After every race - store the result in  `result.json` - you should keep the points of every contestant for the given race. 

Here is a complete breakdown of the classes that you want to have:

## Car

`Car` class will have the following methods:

- `__init__`, which takes `car`, `model` and `max_speed`
- All dunders you need - for example, `__str__` would be nice

## Driver

`Driver` class will have the following methods:

- `__init__` takes `name`, `car` (which is an object from `Car` class) 
- All dunders you need - for example, `__str__` would be nice

## Race

`Race` class will have:
- `__init__` takes `drivers`(list of `Driver`-s) and `crash_chance` (chance for crash for every race - number between 0 and 1)
- `result()` - returns the standings after the race + the crashed drivers.

Every driver takes a points for his place in a ranking list:

* For first place - 8
* Second place - 6
* Third place - 4.
* All other places are scored with 0.

**If someone crashes, he takes no points for the given race.**

You must save the result for the given race in `result.json`.

## Championship

`Championship` class will have:

- `__init__` takes `name` and `races_count` - how many races we need to make for the given championship. 
- `top3()` - returns the best 3 drivers after final race

Use the name of the championship as a unique key for it. This will help you store the data.

## Bundling everything together

In order to make the race happen, we need to glue everything together.

Here is an example usage:

```
$ python3 race.py
Hello PyRacer!
Please, call command with the proper argument:
 $ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json
 $ python3 race.py standings -> This will print the standings for each championship that has ever taken place.
```

If we want to start:

```
$ python3 race.py start pandarace 3
Starting a new championship called pandarace with 3 races.
Running 3 races ...

Race #1
###### START ######
Ivo - 8
Pavlin - 6
Slavqna - 4

Race #2
###### START ######
Ivo - 8
Slavqna - 6
Rado - 4

Unfortunately, Pavlin has crashed.

Race #3
###### START ######
Rado - 8

Unfortunately, Ivo has crashed.
Unfortunately, Slavqna has crashed.
Unfortunately, Pavlin has crashed.

Total championship standings:

Ivo - 16
Rado - 12
Slavqna - 10
Pavlin - 6
```

Figure out how to store everyting in the `result.json` file!


# Money Tracker

Remember the Money Tracker application that you created two weeks ago?
Now it is time to use your OO knowledge and implement it again.

You have to create the following structure:

* in `category.py` you have to implement three classes.
  - parent class Category
  - two child classes - Income and Expense

* in `parse_money_tracker_data.py` you have to parse the data coming from `money_tracker.txt` and return list of the rows
* in `aggregated_money_tracker.py` you need to process the list of rows and create an aggregated object
* `money_tracker_menu.py` is responsible to call the MoneyTracker methods based on the option provided from the user
* the `money_tracker.py` module should process the user data, This class takes just one attribute - AggregatedMoneyTracker object.
* and the `main.py` is the starting point of the application.

**Do not forget to implement**
- at least these dunders `__str__`, `__repr__`, `__eq__`
- tests for your implementation
