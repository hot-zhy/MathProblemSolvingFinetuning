MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use method of four-rule operation,the principle of place value, logical reasoning to solve math problems.Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''
Question: Tom\\textquotesingle s dad is $$43$$ years old, and his age is $$5$$ less then $$4$$ times the age of Tom. So what is the age of Tom? 

Process:
Let's represent Tom's age with the variable "T".According to the information given, Tom's dad is 43 years old and his age is 5 less than 4 times Tom's age. We can set up an equation to express this relationship:Tom's Dad's age = 4 * Tom's age - 5
Substituting the given values, we have:43 = 4T - 5
To find Tom's age, we can solve this equation:
    4T - 5 = 43
Add 5 to both sides:
    4T = 48
Divide both sides by 4:
    T = 12
Therefore, Tom is 12 years old.
The answer is 12

Answer:12


Question:A younger elephant is $18$ years old this year. The older elephant tells the younger elephant: ``when you grow up to my current age, I will be $62$ years old.'' Find the age of the older elephant this year. 

Process:
Let's denote the current age of the older elephant as "x" years. According to the information given, the younger elephant is currently 18 years old.
The older elephant tells the younger elephant that when the younger elephant grows up to the older elephant's current age, the older elephant will be 62 years old. We can set up the following equation:
    x + 18 = 62
Solving for x, we subtract 18 from both sides of the equation:
    x = 62 - 18
    x = 44
Therefore, the age of the older elephant this year is 44 years.
The answer is 44

Answer:44


Question:Richard is $$12$$ years old.  Adam is twice as old as Richard.  Will is $$\\frac{2}{3}$$ of Adam\\textquotesingle s age.  What is their total age? 

Process:
Let's break down the given information and solve the problem step by step:
    Richard's age: 12 years
    Adam is twice as old as Richard: Adam's age = 2 * Richard's age = 2 * 12 = 24 years
    Will is 2/3 of Adam's age: Will's age = (2/3) * Adam's age = (2/3) * 24 = 16 years
To find their total age, we sum up the ages of Richard, Adam, and Will:
    Total age = Richard's age + Adam's age + Will's age
    Total age = 12 + 24 + 16
    Total age = 52
Therefore, the total age of Richard, Adam, and Will is 52 years.
The answer is 52

Answer:52

Question:A team of $5$~students represent England in a junior international chess competition. One student decides to take their ages and calculate three different averages. The mode age of the team was $7$, the mean age was 9 and the median age was $8$. Given also that the range of their ages is $6$. How old was the second oldest member? 

Process:
Mode age: The mode is the value that appears most frequently in a set of numbers. In this case, the mode age is 7.
Mean age: The mean is calculated by summing all the values in a set and dividing by the number of values. In this case, the mean age is 9.
Median age: The median is the middle value when the set is arranged in ascending or descending order. In this case, the median age is 8.
Range: The range is the difference between the largest and smallest values in a set. In this case, the range is 6.
From the given information, we can determine the following values:
    Mode age: 7
    Mean age: 9
    Median age: 8
    Range: 6
To find the ages of the team members, we can start by arranging them in ascending order. Since the median age is 8, we know that at least two team members have ages below 8,and the mode age is 7,so at least two team members have an age of 7,that is the youngest two member’s age is 7.
Let's assume the age of the second oldest member is x.
The ages of the team members can be arranged as follows:
    7,7, 8, x, ?
The range of the ages is 6, so the difference between the largest and smallest ages is 6. Since the smallest age is 7, the largest age is 7 + 6 = 13.
The team members' ages are now:
    7,7, 8, x, 13
The mean age is 9, which is calculated by summing all the ages and dividing by 5 (the number of team members):
	(7+7 + 8 + x + 13) / 5 = 9
Simplifying the equation, we get:
	(35+ x) / 5 = 9
Multiplying both sides of the equation by 5, we have:
	35 + x = 45
Subtracting 28 from both sides, we find:
	x = 10
Therefore, the age of the second oldest member is 10.
The answer is 10

Answer:10


Question:On Brian\\textquotesingle s $14$th birthday, Brian\\textquotesingle s father was $41$. Brian noticed that his age was the reverse of his father\\textquotesingle s age. How old will Brian be the next time his age is the reverse of his father\\textquotesingle s age? 

Process:
We know that Brian's father was 41 on Brian's 14th birthday.let's assume Brian's age is x years , so, when Brian is x years old, his father would be (41 + x-14) years old.
Based on the problem statement, we can write the equation:
    x = reverse of (41 + x-14)
Let's reverse (41 + x-14):
    Reverse of (41 + x-14) = reverse of (x+27)
Now, we have the equation:
    x = reverse of (x+27)
To find the value of x, we can try different values and check if the reverse of (x+27) matches x.
Let's start with x = 15:
    reverse of (27+15) = 42
Here, the reverse of (x+27) is not equal to x.
    Let's try x = 16:
    reverse of (16+27) = 43
Here, the reverse of (x+27) is not equal to x as well.
Continuing the process, we can try different values for x until we find a solution where the reverse of (x+27) is equal to x.
After trying different values, we find that when x = 25:
    reverse of (25+27) = 52
Here, the reverse of (x+27) exactly matches x.
Therefore, when Brian is 25 years old, his age will be the reverse of his father's age again.
The answer is 25

Answer:25


Q: 
'''.strip()
