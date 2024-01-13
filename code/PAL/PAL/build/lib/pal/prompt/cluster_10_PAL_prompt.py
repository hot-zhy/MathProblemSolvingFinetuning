MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use Chinese Remainder Theorem or enumeration methods to solve math problems. Please think step by step.And response briefly..'
MATH_CHAT_BETA_PROMPT = '''

Let's use Chinese Remainder Theorem or enumeration methods help solve math problems. 
Here are some examples how to do it.
!!important
**
you must use python and response in the following structure
Please structure your code response in the same format as the following examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

Q:A three-digit integer has remainder $1$ when it is divided by $7$ and remainder $5$ when divided by $9$. What is the smallest possible value of the number?
```
def solution():
    # The problem is to find the smallest three-digit integer that has a remainder of 1 when divided by 7,
    # and a remainder of 5 when divided by 9. 
    # This can be solved using the Chinese Remainder Theorem or by checking numbers sequentially.

    # Start checking from the smallest three-digit number, 100
    for number in range(100, 1000):
        # Check if the number satisfies both conditions
        if number % 7 == 1 and number % 9 == 5:
            result = number
            break

    return result

```

Q:What is the remainder when $${{2}^{10}}$$ is divided by $$3$$? 
```
def solution():
    # The problem is to find the remainder when 2^10 is divided by 3.
    # This is a simple calculation of the power of a number and then finding the remainder.

    # Calculate 2^10
    power_result = 2**10

    # Find the remainder when power_result is divided by 3
    remainder = power_result % 3

    return remainder

```

Q:There is such a positive integer: if it is divided by $$5$$, the remainder is $$3$$; if it is divided by $$6$$, the remainder is $$4$$; if it is divided by $$7$$, the remainder is $$1$$. Find the least possible value of such a number. 
```
def solution():
    # The problem is to find the least positive integer that, when divided by 5, gives a remainder of 3;
    # when divided by 6, gives a remainder of 4; and when divided by 7, gives a remainder of 1.
    # This is a problem of solving simultaneous congruences, which can be approached using the Chinese Remainder Theorem.

    # The conditions can be written as:
    # x ≡ 3 (mod 5)
    # x ≡ 4 (mod 6)
    # x ≡ 1 (mod 7)

    # We can find such a number by checking each number starting from the largest remainder's related number
    # which is 7 in this case, until we find a number that satisfies all three conditions.

    num = 7
    while True:
        if num % 5 == 3 and num % 6 == 4 and num % 7 == 1:
            return num
        num += 1
    return num
```

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

How about this Question?

'''.strip()
