# Are two words anagrams?
Create a function, that reads two words from the standard input and output and returns if the two of them are anagrams.
For anagrams, check here - https://en.wikipedia.org/wiki/Anagram

For example, `listen` and `silent` are anagrams.
**Consider lowering the case of the two words since the case does not matter. `SILENT` and `listen` are also anagrams.**

## Signature:
```python
def anagrams():
    pass
```


## Expected output
* `ANAGRAMS` if the words are anagrams of each other
* `NOT ANAGRAMS` if the two words are not anagrams of each other


## Test Examples

Input:

```
TOP_CODER COTO_PRODE
```

Output:

```
NOT ANAGRAMS
```

---

Input:

```
boro kilata
```

Output:

```
NOT ANAGRAMS
```

Also, should not make songs together.

---

Input:

```
BRADE BEARD
```

Output:

```
ANAGRAMS
```



# Credit card validation

Implement a function, called `is_credit_card_valid(number)`, which returns True/False based on the following algorithm:

* Each credit card number must contain odd count of digits.
* We transform the number with the following steps (based on the fact that we start from index 0)
  - All digits, read from right to left, at even positions (index), **remain the same.**
  - Every digit, read from right to left, at odd position is replaced by the result, that is obtained from doubling the given digit.
* After the transformation, we find the sum of all digits in the transformed number.
* The number is valid, if the sum is divisible by 10.

For example: `79927398713` is valid, because:

* When we double and replace all digits at odd position we get: `7 (18 = 2 * 9) 9 (4 = 2 * 2) 7 (6 = 2 * 3) 9 (16 = 2 * 8) 7 (2 = 2 * 1) 3`
* The sum of all digits of the new number is 70, which is divisible by 10 => the card number is valid.


## Signature:
```python
def is_credit_card_valid(number):
    pass
```

## Test Examples:
```python
>>> is_credit_card_valid(79927398713)
True
>>> is_credit_card_valid(79927398715)
False
```

# Goldbach Conjecture

Implement a function, called `goldbach(n)` which returns a list of tuples, that is the goldbach conjecture for the given number `n`.

The Goldbach Conjecture states:

> Every even integer greater than 2 can be expressed as the sum of two primes.

Keep in mind that there can be more than one combination of two primes, that sums up to the given number!

__The result should be sorted by the first item in the tuple.__

For example:

* `4 = 2 + 2`
* `6 = 3 + 3`
* `8 = 3 + 5`
* `10 = 3 + 7 = 5 + 5`
* `100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53`

## Signature

```python
def goldbach(n):
    pass
```

## Test examples

```python
>>> goldbach(4)
[(2,2)]
>>> goldbach(6)
[(3,3)]
>>> goldbach(8)
[(3,5)]
>>> goldbach(10)
[(3,7), (5,5)]
>>> goldbach(100)
[(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
