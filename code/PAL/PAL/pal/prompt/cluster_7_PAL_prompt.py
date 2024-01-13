MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of basic arithmetic operations with whole numbers for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of basic arithmetic operations with whole numbers to solve math problems. 
Here are some examples how to do it.
!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**

Question:
Multiply $$345$$ by $$67$$.
```
def solution():
    # The problem is to multiply two numbers: 345 and 67.
    # This is a straightforward multiplication calculation.

    # Multiplying 345 by 67
    result = 345 * 67

    return result

```


Question:
Work out $628 \\times ~5$
```
def solution():
    # The problem is to multiply two numbers: 628 and 5
    # This is a straightforward multiplication calculation.

    # Multiplying 628 by 5
    result = 628 * 5

    return result
```

Question:
Calculate:  $$599999+59999+5999+599+59+5=$$~\\uline{~~~~~~~~~~}~
```
def solution():
    # This problem is a simple addition of numbers.
    # We need to add 599999, 59999, 5999, 599, 59, and 5 together.
    # This can be done directly.

    # Adding the numbers
    total = 599999 + 59999 + 5999 + 599 + 59 + 5
    result = total
    return result
```


Question:
A number $M$ when divided by $$2$$, $$3$$, $$4$$, $$5$$, $$6$$, $$7$$, $$8$$, $$9$$ and $$10$$ gives non-zero remainders. If these remainders are all different, what is the smallest possible $M$?
```
def solution():
    from math import gcd

    # Function to find LCM of two numbers
    def lcm(x, y):
        return x * y // gcd(x, y)

    # Finding LCM of 2, 3, 4, 5, 6, 7, 8, 9, and 10
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    lcm_result = 1
    for number in numbers:
        lcm_result = lcm(lcm_result, number)

    # Adjust for non-zero remainders
    M = lcm_result - 1
    result =  M
    return result

```


Question:
$816\\div17$
```
def solution():
    # The problem is a simple division: 816 divided by 17.
    # This is a straightforward calculation without the need for complex steps or methods.
    # We just need to divide 816 by 17.

    result = 816 / 17
    return result
```

Here are some examples how to do it.
!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**
How about this question? 
'''.strip()
