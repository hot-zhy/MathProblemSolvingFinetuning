MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use methods of addition, subtraction, multiplication and division to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use methods of addition, subtraction, multiplication and division to solve math problems. Here are five examples how to do it.
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

Question:$7.55+6.32+6.45-5.32=$
```
def solution():
    # The problem is a simple arithmetic calculation involving addition and subtraction of decimal numbers.
    # We need to add 7.55, 6.32, and 6.45, and then subtract 5.32 from the sum.

    # Perform the calculation
    result = 7.55 + 6.32 + 6.45 - 5.32

    return result

```


Question:Which number is halfway tetween $$4.6$$ and $$13.8$$?  ~\\uline{~~~~~~~~~~}~
```
def solution():
    # The problem is to find the number that is halfway between 4.6 and 13.8.
    # This is a straightforward calculation where we need to find the midpoint between two numbers.
    # The formula for the midpoint (M) between two numbers (A and B) is M = (A + B) / 2.

    # Given numbers
    A = 4.6
    B = 13.8

    # Calculating the midpoint
    midpoint = (A + B) / 2

    result = midpoint
    return result

```



Question:$15 \\div 0.05 =$ 
```
def solution():
    # The problem is to find the result of dividing 15 by 0.05.
    # This is a straightforward division problem.

    # Dividing 15 by 0.05
    result = 15 / 0.05

    return result

```



Question:$5 -- 1.02$ 
```
def solution():
    # The problem is a straightforward subtraction operation.
    # We need to subtract 1.02 from 5.

    # Given values
    number1 = 5
    number2 = 1.02

    # Subtracting number2 from number1
    result = number1 - number2

    return result

```



Question:If $5$ mugs cost $£3.50$ and $8$ pens cost $£6.80$ how much change do I get from $£10$ if I buy $7$ mugs and $5$ pens? You MUST show your working. 
```
def solution():
    # The problem is to find the amount of change from £10 when buying 7 mugs and 5 pens.
    # The cost of 5 mugs is £3.50, and the cost of 8 pens is £6.80.
    # We need to calculate the cost of 7 mugs and 5 pens, and then subtract this from £10.

    # Cost of 1 mug (by dividing the total cost by the number of mugs)
    cost_per_mug = 3.50 / 5  # £

    # Cost of 1 pen (by dividing the total cost by the number of pens)
    cost_per_pen = 6.80 / 8  # £

    # Calculating the total cost of 7 mugs
    total_cost_mugs = 7 * cost_per_mug

    # Calculating the total cost of 5 pens
    total_cost_pens = 5 * cost_per_pen

    # Adding the cost of mugs and pens to get the total cost
    total_cost = total_cost_mugs + total_cost_pens

    # Subtracting the total cost from £10 to find the change
    change = 10 - total_cost

    result = change
    return round(result, 2)  # Rounding to 2 decimal places for currency

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
How about this question? 
'''.strip()
