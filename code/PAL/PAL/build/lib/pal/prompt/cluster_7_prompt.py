MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of basic arithmetic operations with whole numbers for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of basic arithmetic operations with whole numbers to solve math problems. Here are five examples how to do it.

Question:
Multiply $$345$$ by $$67$$.

Process:
we multiply 345 by 67 then get 23115.
The answer is 23115.

Answer: 23115


Question:
Work out $628 \\times ~5$

Process:
we multiply 628 by 5 then get 3140.
The answer is 3140.

Answer: 3140


Question:
Calculate:  $$599999+59999+5999+599+59+5=$$~\\uline{~~~~~~~~~~}~

Process:
1.Start by adding the last two numbers:
59+5=64
2.Next, add 599:
64+599=663
3.Then add 5999:
663+5999=6662
4.Now, add 59999:
6662+59999=66661
5.Finally, add 599999:
66661+599999=666660
6.The answer is 666660.

Answer: 666660


Question:
A number $M$ when divided by $$2$$, $$3$$, $$4$$, $$5$$, $$6$$, $$7$$, $$8$$, $$9$$ and $$10$$ gives non-zero remainders. If these remainders are all different, what is the smallest possible $M$?

Process:
To solve this problem, let's consider the nature of the remainders when a number M is divided by 2,3,4,5,6,7,8,9, and 10. We're looking for the smallest number M that, when divided by each of these, gives different non-zero remainders.

The key insight is that if M gives different non-zero remainders when divided by each of these numbers, then M+1 must be divisible by all of these numbers (since the remainders effectively "fill up" the gaps to the next multiple). The smallest number divisible by all these numbers is their least common multiple (LCM).

The numbers 2,3,4,5,6,7,8,9, and 10 include several multiples of each other:
4 is a multiple of 2.
6 is a multiple of 2 and 3.
8 is a multiple of 2 and 4.
9 is a multiple of 3.
10 is a multiple of 2 and 5.
Therefore, we only need the LCM of 2,3,5,7, and 8, as these are the unique bases.

Let's calculate the LCM of these numbers and then subtract 1 to find M.

The smallest possible number M that gives different non-zero remainders when divided by 2,3,4,5,6,7,8,9,and 10 is 839.
The answer is 839.

Answer: 839


Question:
$816\\div17$

Process:
Let's divide 816 by 17 then we get 48.
The answer is 48.

Answer: 48

Q: 
'''.strip()
