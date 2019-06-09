# Reverse Polish Notation

Reverse polish notation, or RPN, is one of the three commonly used calculation notations. The other two are polish notation and infix notation.

The latter, infix notation, is the one most commonly used across the world and is probably the form of notation that is most familiar to readers. Infix notation is the standard taught in schools, with the operator placed "in" the formula. For example, to show the calculation 6 plus 3, infix notation is written as 6 + 3.

In contrast, the polish and reverse polish notations place the operator on either side of the numbers. Polish notation would note the above calculation as + 10 5. Reverse polish notation is simply the opposite of that, with the operator appearing after the numbers. The infix notation formula of 6 + 3 is noted as 6 3 + in RPN.

Our task today is to calculate an RPN expression and use the TDD approach to do it.

An RPN expression is one of the following:
* a number `x`, in which case the value of the expression is that of `x`
* a sequence of form `e1 e2 op`, where `e1` and `e2` are RPN expressions and `op`

## Signature
```python
def rpn_calc(expression):
    pass
```

## Test Examples
## Test examples
```python
>>> rpn_calc('20 4 /')
5
>>> rpn_calc('4 2 + 3 -')
3
>>> rpn_calc('3 5 8 * 7 + *')
141
>>> rpn_calc('9 SQRT')
3
```

Testing
========================

Let's rewrite tasks - https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists.
The condition is to using TDD (Test Driven Development) flow.

After that, let's start with coding new problems and tests. You should think how the user can break your code. So you have to add validations. :)

## Simplify fractions

Implement a function, called ```simplify_fraction(fraction)``` that takes a tuple of the form ```(nominator, denominator)``` and simplifies the fraction.

The function should return the fraction in it's irreducible form.

For example, a fraction ```3/9``` can be reduced by dividing both the nominator and the denominator by 3. We end up with ```1/3``` which is irreducible.

### Signature

```python
def simplify_fraction(fraction):
    # Implementation
```

### Test examples

```
>>> simplify_fraction((3,9))
(1,3)
>>> simplify_fraction((1,7))
(1,7)
>>> simplify_fraction((4,10))
(2,5)
>>> simplify_fraction((63,462))
(3,22)
```

## Collect fractions

Implement a function, called ```collect_fractions(fractions)``` where ```fractions``` is a list of tuples of the form ```(nominator, denominator)```.

Both the nominator and the denominator are integers.
The function should return the sum of the fractions.

### Signature

```python
def collect_fractions(fractions):
    # Implementation
```

### Test examples

```
>>> collect_fractions([(1, 4), (1, 2)])
(3, 4)
>>> collect_fractions([(1, 7), (2, 6)])
(10,21)
```


## Sort array of fractions

Implement a function, called ```sort_fractions(fractions)``` where ```fractions``` is a list of tuples of the form ```(nominator, denominator)```.

Both the nominator and the denominator are integers.

The function should return the list, sorted in increasing order.

### Signature

```python
def sort_fractions(fractions):
    # Implementation
```

### Test examples

```
>>> sort_fractions([(2, 3), (1, 2)])
[(1, 2), (2, 3)]
>>> sort_fractions([(2, 3), (1, 2), (1, 3)])
[(1, 3), (1, 2), (2, 3)]
>>> sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
```


Queries
=========

Implement and *test* the following python functions:

## Filter
Write a function that takes one positional argument that is the name of a file. Use can use this example data set.
Implement your function in such a way that it accepts as many keyword arguments as the user wants. Every keyword argument must be a valid name of a column in the CSV file:
```
   full_name, favourite_color, company_name, email, phone_number, salary
```
Your function should filter the data set and return an array of arrays for every raw that matches the query.

Support the following behavior:

### Filter by one argument

```
    filter('example_data.csv', full_name="Diana Harris")
```
That should return all of the records named "Diana Harris"

### Filter by more then one arguments
```
    filter('example_data.csv', full_name="Diana Harris", favourite_color="lime")
```
That should filter using **AND** statement. This is going to return all of the records named "Diana Harris" that have lime as a favorite color.

### __startswith
```
    filter('example_data.csv', full_name__starswith="Diana")
```
That should filter all records have name starting with "Diana"

### __contains
```
    filter('example_data.csv', email__contains="@gmail")
```
That should return all records that are using gmail.

### __gt and __lt
```
    filter('example_data.csv', salary__gt=1000, salary__lt=3000)
```
This is short for 'grater than' and 'less than'. This query should return all of the records that are heaving more salary in the interval (1000, 3000).

### order_by
```
    filter('example_data.csv', salary__gt=1000, salary__lt=3000, order_by='salary')
```
If you have the ``order_by`` argument that means that you have to order your results by this field starting withe lowest value.

## count
Write another function that behaves the exact same way as filter but it returns only the count of the results.

## first
Write another function that behaves the exact same way as filter but it returns only the first result.

## last
Write another function that behaves the exact same way as filter but it returns only the last result.


CodingSkills
========

The problem where you analyze the given json with data and returns some results.

You have a data.json file in this repo. It is full with people objects. Every person have ``skills`` array with languages objects in it. Every skill has name and level.

Write a program that does two things:
- Read data.json file as an argument in the console.
- Prints all languages and the best person in every language.

```
$ python3 coding_skill.py data.json
```

```
C++ - Cherna Ninja
PHP - Rado Rado
Python - Ivo Ivo
C# - Pavli Pavli
Haskell - Rado Rado
Java - Rado Rado
JavaScript - Rosi Rosi
Ruby - Rosi Rosi
CSS - Pavli Pavli
C - Cherna Ninja
```


