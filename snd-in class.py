def g(arg):
    return arg


def p(arg):
    return True


def f(args):
    result = []

    for arg in args:
        if p(arg):
            result.append(g(arg))

    return result

def ff(args):
    return [g(arg) for arg in args]
    # List comprehension



def sum_of_digits(n):
    return sum(to_digits(n))


def to_digits(n):
    n = abs(n)

    return [int(ch) for ch in str(n)]


def join(items, delimiter):
    result = ''
    n = len(items)

    for index in range(n):
        item = items[index]

        result = result + item

        if index != n - 1:
            result += delimiter

    return result


def to_number(digits):
    chars = [str(digit) for digit in digits]

    return int(join(chars, ''))

def fact(n):
    if n in [0, 1]:
        return 1

    result = 1

    for x in range(n):
        result *= x + 1

    return result


def fact_digits(n):
    return sum([fact(digit) for digit in to_digits(n)])

print(fact_digits(145))



def reverse_string(string):
    result = ''
    n = len(string)

    for i in range(n):
        result += string[n - i - 1]

    return result

def palindrome(obj):
    string_repr_of_obj = str(obj)
    return string_repr_of_obj == reverse_str(string_repr_of_obj)

def char_histogram(string):
    out = {}
    for c in string:
        out[c] = out.get(c, 0) + 1
    return out
