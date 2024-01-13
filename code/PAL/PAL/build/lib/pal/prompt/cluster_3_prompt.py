MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use method of four-rule operation, algebraic expressions to solve math problems.Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''
Question:Solve the equation below.$$2x+3x+2=30+6x-8x$$

Process:
To solve the given equation, let's simplify the expression on both sides and combine like terms:
    2x + 3x + 2 = 30 + 6x - 8x
Combining like terms on the left side:
    5x + 2 = 30 + 6x - 8x
On the right side, we can simplify 6x - 8x as -2x: 
    5x + 2 = 30 - 2x
To isolate the x terms on one side, let's add 2x to both sides:
    5x + 2 + 2x = 30 - 2x + 2x
Simplifying both sides:
    7x + 2 = 30
Next, subtract 2 from both sides to isolate the x term:
    7x + 2 - 2 = 30 - 2
Simplifying both sides:
    7x = 28
Finally, to find the value of x, divide both sides by 7:
    7x/7 = 28/7
Simplifying:
    x = 4
Therefore, the solution to the equation is x = 4.
The answer is 4

Answer:4

Question:$$10-3\\left( x-2 \\right)=4x-5\\left( 4-x \\right)$$, $x=$~\\uline{~~~~~~~~~~}~

Process:
To solve the equation, let's simplify the expression on both sides and then solve for the variable x.
Starting with the given equation:
    10−3(x−2)=4x−5(4−x)
Firstly, distribute the multiplication:
    10−3x+6=4x−20+5x
Combine like terms:
    16−3x=9x−20
Next, let's isolate the variable terms on one side and the constants on the other side. To do this, we can add 3x to both sides and add 20 to both sides:
    16−20=9x+3x
    −4=12x
Now we can solve for x by dividing both sides by 12:
    −4/12=x
    −1/3=x
Therefore, the solution to the equation is:
    x=−1/3
The answer is −1/3

Answer: −1/3


Question:Each letter represents a distinct number. Calculate the value of $$B$$.  $$C+B=18$$  $$B=A+A+A$$  $$C+A=10$$ 

Process:
To find the value of B, we can use the given information and solve for B step by step.
From the equation C + B = 18, we know that B must be a positive integer less than 18 since C and B are distinct numbers.
From the equation B = A + A + A, we can deduce that B must be a multiple of 3 since it is the sum of three As.
From the equation C + A = 10, we can deduce that A must be a positive integer less than 10 since C and A are distinct numbers.
Hence,We have the following equations:
    C + B = 18
    B = A + A + A
    C + A = 10
Let's use the third equation to solve for C in terms of A:
    C = 10 - A
Substituting this value of C in the first equation:
    10 - A + B = 18
Now, let's substitute the value of B from the second equation:
    10 - A + A + A = 18
Simplifying:
    10 + 2A = 18
Subtracting 10 from both sides:
    2A = 8
Dividing both sides by 2:
    A = 4
Now that we have the value of A, we can substitute it back into the third equation to solve for C:
    C + 4 = 10
Subtracting 4 from both sides:
    C = 6
Finally, we can substitute the values of A and C into the second equation to find B:
    B = 4 + 4 + 4
    B = 12
Therefore, the correct value for B is 12.
The answer is 12

Answer:12


Qusetion:If $$a=1$$, $$b=2$$, and $$c=3$$, then $$\\overline{abc}=123$$. Find the value of $$m$$ according to this rule.  $$\\overline{14m}=8\\times \\overline{1m}-3$$.

Process:
To find the value of m using the given equation, let's break down the equation step by step.
Given:14m=8×1m−3
We can substitute the given values for a, b, and c:
14m=8×12−3
We know that12=1×10+2=12, so we can simplify the equation further:
1×100+4×10+m=8×(1×10+m)-3
100+40+m = 8×(10+m)-3
140+m = 80+8m-3
63=7m
m=9
Therefore, The only digit that satisfies the equation is m = 9.
The answer is 9

Answer:9


Process:$$2$$ similar wallets and $$3$$ similar watches cost ＄$$433$$. $$5$$ similar wallets and $$4$$ similar watches cost ＄$$701$$. How much does a wallet cost? 

Question:
To find the cost of a wallet, we can set up a system of equations based on the given information.
Let's assume the cost of one wallet is 'w' and the cost of one watch is 'x'.
From the first statement, "2 similar wallets and 3 similar watches cost $433", we can write the equation:
2w + 3x = 433 ...(Equation 1)
From the second statement, "5 similar wallets and 4 similar watches cost $701", we can write the equation:
5w + 4x = 701 ...(Equation 2)
Now, we can solve this system of equations to find the values of 'w' and 'x'.
Multiplying Equation 1 by 4 and Equation 2 by 3 to eliminate 'x':
8w + 12x = 1732
15w + 12x = 2103
Subtracting these two equations, we get:
7w = 371
Dividing both sides by 7:
w = 371/7
Therefore, the cost of one wallet is 371/7.
The answer is 371/7

Answer:371/7


Q: 
'''.strip()
