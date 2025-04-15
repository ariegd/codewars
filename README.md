# codewars
Ejercitando en el lenguaje Python

## [Functional SQL](https://www.codewars.com/kata/545434090294935e7d0010ab/train/python)

# Filter groups with having():
```
def odd(group):
    return group[0] == "odd"

# SELECT * FROM numbers GROUP BY parity HAVING odd(number) = true <- I know, this is not a valid SQL statement, but you can understand what I am doing
query().select().from_(numbers).group_by(parity).having(odd).execute()
# [["odd", [1, 3, 5, 7, 9]]]
```

In this Kata we are going to mimic the SQL syntax.

To do this, you must implement the query() function. This function returns an object with the following methods:
```
def select ...
def from_ ...
def where ...
def order_by ...
def group_by ...
def having ...
def execute ...
The methods are chainable and the query is executed by calling the execute method.
```
⚠️ Note: The order of appearance of a clause in a query doesn't matter. However, when it comes time for you to run the query, you MUST execute the clauses in this logical order: from first, then where, then groupBy, then having, then select and finally orderBy.

Multilevel grouping:
```
def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while number % divisor != 0:
        divisor += 1

    return divisor == number

def prime(number):
    return "prime" if is_prime(number) else "divisible"
    
# SELECT * FROM numbers GROUP BY parity, is_prime
query().select().from_(numbers).group_by(parity, prime).execute()
# [["odd", [["divisible", [1, 9]], ["prime", [3, 5, 7]]]], ["even", [["prime", [2]], ["divisible", [4, 6, 8]]]]]
```

