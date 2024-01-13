MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of Computational Techniques and Mathematical Formulas for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of Computational Techniques and Mathematical Formulas to solve math problems. Here are five examples how to do it.

Question:
Which is larger $$\\frac{3}{20}$$ or $$0.16$$?  ~\\uline{~~~~~~~~~~}~

Process:
1.Convert to a Common Format: Convert one of the numbers to the same format as the other for direct comparison.
2.Convert Fraction to Decimal: 3/20 can be converted to a decimal by dividing 3 by 20.
3.Compare Decimals: Compare the decimal form of 
3/20 with 0.16
4.3/20=0.15. Comparing 0.15 with 0.16, we see that 
0.16 is larger.
5.The answer is 0.16


Answer: 0.16


Question:
Calculate.　  $${{1}^{2}}+{{3}^{2}}+{{5}^{2}}+\\ldots +{{19}^{2}}$$.

Process:
To calculate the sum $$1^2+3^2+5^2+…+19^2$$, we can use the formula for the sum of the squares of the first n odd numbers. The formula is:$$\\sum_{k=1}^{n} (2k-1)^2 = \\frac{n(4n^2-1)}{3}$$
In this case, we are summing the squares of the first 10 odd numbers (since 19 is the 10th odd number). So, n=10. Applying this formula:$$\\sum_{k=1}^{10} (2k-1)^2 = \\frac{n(4*10^2-1)}{3}$$
Let's calculate this sum.
The sum of the squares of the first 10 odd numbers, 
$$1^2+3^2+5^2+…+19^2$$ is 1330. ​
The answer is 1330

Answer: 1330


Question:
Solve the following equation.  $\\frac{3.5}{3x+2}+\\frac{2}{1.5x+1}=\\frac{4.5}{5-6x}-\\frac{3}{2.5-3x}$

Process:
To solve the equation $\\frac{3.5}{3x+2}+\\frac{2}{1.5x+1}=\\frac{4.5}{5-6x}-\\frac{3}{2.5-3x}$, let's proceed step by step:
1.Simplify the Equation: Convert decimal coefficients to fractions for easier manipulation.
2.Find a Common Denominator: To add or subtract the fractions, we need a common denominator.
3.Combine Terms: Once we have a common denominator, we can combine the terms on each side of the equation.
4.Solve for x: After simplifying the equation, solve for x using algebraic methods.
5.Let's use sympy to solve.
```
from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the equation
equation = Eq((3.5/(3*x + 2)) + (2/(1.5*x + 1)), (4.5/(5 - 6*x)) - (3/(2.5 - 3*x)))

# Solve the equation
solutions = solve(equation, x)
solutions

```
Therefore,the solution to the equation is x=1.
The answer is 1

Answer: 1


Question:
$$17-8\\div (-2)+4\\times (-3) = $$

Process:
To solve the expression 17-8/(-2)+4*(-3). follow the order of operations (PEMDAS/BODMAS):
1.Division and Multiplication(from left to right):
8/(-2)=-4
4*(-3)=-12
2.Addition and Subtraction(from left to right):
17-(-4)+(-12)
3.Calculate:
17+4-12=21-12
4.Final result:
21-12=9
5.The answer is 9

Answer: 9


Question:
Define the operation symbol $$a\\otimes b=\\left( a+b \\right)\\times a$$, find the value of $$(4\\otimes 7)$$

Process:
To solve the problem using the defined operation symbol 
a⊗b=(a+b)×a, let's follow these steps:
1.Understanding: The operation a⊗b involves first adding a and b together, and then multiplying the sum by a.
2.Apply the Operation to 4⊗7:
First, add 4 and 7: 4+7=11.
Then, multiply the sum by 4: 11×4.
3.Calculate the Result:11×4=44
4.The answer is 44

Answer: 44

Q: 
'''.strip()
