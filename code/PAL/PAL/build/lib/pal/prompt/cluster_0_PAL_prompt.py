MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use method of combination,calculation of number and place values,ratio calculation and logical reasoning to solve math problems.Please think step by step. And response briefly'
MATH_CHAT_BETA_PROMPT = '''
Let's use the relevant knowledge of combination,calculation of number and place values,ratio calculation and logical reasoning to solve math problems. Here are three examples how to do it.
!!important
**
you must use python and response in the following structure
Please structure your code response in the same format as the following examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**
Question: $$36$$ is a square number because it can be written $$6\\times6$$.  Similarly, $$64=8\\times8$$ is a square number.  $$1000$$ is a cube number because it can be written $$10\\times10\\times10$$  Similarly, $$343=7\\times7\\times7$$ is a cube number.  The French mathematician Pierre de Fermat claimed correctly that there is only one square number that is $$2$$ less than a cube number.  It is less than $$50$$.  What is it?  ANSWER~\\uline{~~~~~~~~~~}~，
```
def solution():
    # Fermat's claim is about finding a square number that is 2 less than a cube number, and it is less than 50.
    # This means we need to find a number 'n' such that n^3 - 2 is a square number, and n^3 < 50.

    # We will iterate over possible cube numbers less than 50 and check if n^3 - 2 is a square number.
    for n in range(1, int(50 ** (1/3)) + 1):  # Cube root of 50 is approximately 3.684, so we check up to 4
        cube = n ** 3
        if cube < 50:
            square_candidate = cube - 2
            # Check if square_candidate is a perfect square
            if int(square_candidate ** 0.5) ** 2 == square_candidate:
                result = square_candidate
                break

    return result

```

Question:$$\\overline{ABCD}$$ represents a $$4$$-digit number, and $$\\overline{EFG}$$~ represents a $$3$$-digit number. $$A-G$$ each represents a different number from $$1$$ to $$9$$. Given that the sum of these two numbers is $$1993$$, find the difference between the largest possible product and the least possible product of these two numbers. 
```
```

Question:I am a number with $$3$$ decimal places.  The digit $$9$$ is in the thousandths place.  The digit $$7$$ is in the hundredths place.  The digit $$6$$ is in the tenths place.  The ones place has a value of $$4$$.  Round off this number to one decimal place.  What number am I?~\\uline{~~~~~~~~~~}~     Tongtong says, \\"I think the answer to the above is $$9764.0$$.\\"  Is she correct? If not, state the correct answer. 
```
```

Question:On a ferry, the total number of cars, bikes and lorries is an even number and is less than $$100$$. The number of cars is four-thirds of the number of bikes. The number of bikes is one quarter more than the number of lorries. How many cars, bikes and lorries are there on the ferry?
```
```

Question:（AMC 2020 Question \\#26）  Janine thinks of three numbers.  Between them, they use the digits 1, 3, 5, 6, 7, 8 and 9, with each digit being used exactly once.  The second number is 2 times the first number.  The third number is 4 times the first number.  What is the third number? 
```
```

!!important
**
you must use python and response in the following structure
Please structure your code response in the same format as the following examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**
How about this question? 

'''.strip()
