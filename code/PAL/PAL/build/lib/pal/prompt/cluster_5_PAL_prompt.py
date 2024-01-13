MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of Applied mathematics and basic arithmetic for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of Applied mathematics and basic arithmetic to solve math problems. Here are five examples how to do it.
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

Question:
Amy has $$37$$ apples and John has $$15$$ apples. How many apples does Amy have to give John so that she has exactly $$4$$ more apples than John?
```
def solution():
    # Amy has 37 apples, John has 15 apples.
    # Let x be the number of apples Amy gives to John.
    # After giving x apples, Amy will have (37 - x) apples, and John will have (15 + x) apples.
    # Amy needs to have 4 more apples than John, so (37 - x) = (15 + x) + 4.

    # Simplify and solve the equation
    x = (37 - 15 - 4) // 2  # Simplified from 37 - x = 19 + x
    result = x
    return result

```

Question:
Mary is in a small class of $$6$$ pupils, but was absent for the Maths test last week. The other five pupils scored an average of $$72 \\%$$. Mary wrote the test this week and, with her score included, the class average went up to $$75 \\%$$.  What mark did Mary score on the test?  Answer~\\uline{~~~~~~~~~~}~ 
```
def solution():
    # The problem is to find Mary's test score given the change in class average after including her score.
    # Initially, 5 pupils scored an average of 72%. After Mary's test, the average of 6 pupils became 75%.

    # Total score of 5 pupils before Mary's test = 5 * 72
    total_score_before = 5 * 72

    # Total score of 6 pupils after Mary's test = 6 * 75
    total_score_after = 6 * 75

    # Mary's score is the difference between the total score after and before her test.
    marys_score = total_score_after - total_score_before
    result = marys_score
    return result

```


Question:
Find the average of the following sequence.  $$1$$, $$3$$, $$5$$, $$7$$, $$9$$, $$\\cdots $$, $$195$$, $$197$$, $$199$$.
```
def solution():
    # The sequence 1, 3, 5, 7, 9, ..., 195, 197, 199 is an arithmetic sequence with a common difference of 2.
    # The average of an arithmetic sequence is given by (First Term + Last Term) / 2.

    first_term = 1  # First term of the sequence
    last_term = 199  # Last term of the sequence

    # Calculate the average
    average = (first_term + last_term) / 2
    result = average
    return result
```


Question:
One of the angles in a triangle is a right angle. Two unknown angles are left and one of them is two times larger than the the other angle.  What is the size of the largest angle betwen the two?
```
def solution():
    # The sum of angles in a triangle is 180 degrees.
    # Given one angle is 90 degrees (right angle), and one angle is twice the other.
    # Let the smaller angle be x, then the larger angle is 2x.
    # The sum of angles is x + 2x + 90 = 180.

    # Solving for x
    x = (180 - 90) / 3  # Simplified from x + 2x + 90 = 180

    # The largest angle between the two unknown angles is 2x
    largest_angle = 2 * x
    result=largest_angle
    return result

```


Question:
There are $42$ sweets in Container A and $4$ times as many sweets in Container B as Container A. Given that there are twice as many sweets in Container C as Container B, how many sweets are there in Container C? 
```
def solution():
    # The problem involves finding the number of sweets in Container C.
    # We are given the number of sweets in Container A and the ratios of sweets in Containers B and C to Container A.

    # Number of sweets in Container A
    sweets_A = 42

    # Container B has 4 times as many sweets as Container A
    sweets_B = 4 * sweets_A

    # Container C has twice as many sweets as Container B
    sweets_C = 2 * sweets_B
    result = sweets_C
    return result

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
