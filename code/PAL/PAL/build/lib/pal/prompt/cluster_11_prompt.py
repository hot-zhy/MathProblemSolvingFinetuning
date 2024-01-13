MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use equations and logical reasoning to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use equations and calculations to solve math problems. Here are eight examples how to do it. 

Question: Elias had $$5$$ times as many stickers as Aileen. After Elias gave away $$88$$ stickers and Aileen lost $$8$$ stickers, they had the same number of stickers left. How many stickers did each of them have in the end?

Process:
Let's assume Aileen initially had x stickers. Since Elias had 5 times as many stickers as Aileen, Elias initially had 5x stickers.
After Elias gave away 88 stickers, he was left with 5x - 88 stickers.
After Aileen lost 8 stickers, she was left with x - 8 stickers.
According to the problem, both Elias and Aileen had the same number of stickers after these changes. So we can set up an equation:
5x - 88 = x - 8
Now we can solve this equation to find the value of x, which represents the initial number of stickers Aileen had.
Subtracting x from both sides:
5x - x - 88 = -8
Simplifying:
4x - 88 = -8
Adding 88 to both sides:
4x = 80
Dividing by 4:
x = 20
So Aileen initially had 20 stickers.
To find the number of stickers Elias had initially, we can substitute x into the expression 5x.
Elias initially had 5 * 20 = 100 stickers.
After Elias gave away 88 stickers, he was left with 100 - 88 = 12 stickers.
After Aileen lost 8 stickers, she was left with 20 - 8 = 12 stickers.
Therefore, both Elias and Aileen had 12 stickers in the end.
The answer is: 5.

Answer: 12.


Question: At a bus stop, men and women were waiting for their buses. When the first bus arrived, $$36$$ women boarded it and left. The number of women at the bus stop became $$\\frac{3}{5}$$ of the number of men. Then, the second bus arrived and $$48$$ men boarded it. There is now an equal number of men and women still waiting at the bus stop. How many people in total were there at the bus stop at first?

Process:
Let's assume the number of men at the bus stop initially is M, and the number of women initially is W.
After the first bus arrived, 36 women boarded it and left. Therefore, the number of women left at the bus stop became W - 36.
According to the given information, the number of women left became 3/5 of the number of men, which can be expressed as:
W - 36 = (3/5)M
After the second bus arrived, 48 men boarded it. This means the number of men left is M - 48.
We are also told that there is an equal number of men and women still waiting at the bus stop. Therefore:
W - 36 = M - 48
Now we have a system of two equations that we can solve to find the values of M and W, which represent the initial number of men and women, respectively.
Let's solve the system of equations:
Equation 1: W - 36 = (3/5)M
Equation 2: W - 36 = M - 48
To solve the system of equations, we can use elimination by substitution.
First we simplify the equation 2 and use an expression with M to represent W.
Adding 36 to both sides of Equation 2:
W = M - 12
Then, let's substitute this expression into equation 1.
Equation 1: M - 12 - 36 = (3/5)M
Simplifying:
M - 48 = (3/5)M
By subtracting (3/5)M from both sides of Equation 1, we get:
(2/5)M - 48 = 0
Adding 48 to both sides of Equation 1:
(2/5)M = 48
Dividing both sides by (2/5):
M = 120
Now we get the value of M, we can solve the value of W easily.
We have solved that W = M - 12, we replace M in equation with 120.
W = 120 - 12
Simplifying:
W = 108
We have assumed that M and N represent the initial number of men and women, respectively.
So the number of men at the bus stop initially is 120, and the number of women initially is 108.
People in total at the bus stop at first is the sum of the number of men and the number of women.
So the answer of it is that 108 + 120 = 228
The answer is: 228.

Answer: 228.


Question: The ratio of Don\textquotesingle s stickers to Ben\textquotesingle s stickers was $2 : 3$. After Don\textquotesingle s bought another $10$ stickers and Ben lost $5$ stickers, the ratio became $6 : 7$. Find the number of stickers Don had at first. 

Process: 
Let's assume that Don initially had 2x stickers and Ben initially had 3x stickers.
After Don bought another 10 stickers, he would have a total of 2x+10 stickers.
After Ben lost 5 stickers, he would have a total of 3x−5 stickers.
According to the problem, the new ratio of Don's stickers to Ben's stickers is 6:7. 
This can be written as $$\\frac{2x+10}{3x-5}$$ = $$\\frac{6}{7}$$.
To solve this equation, we can cross-multiply:
7(2x+10)=6(3x−5)
Using the law of multiplication allocation:
14x+70=18x−30
Simplifying:
4x=100
Dividing by 4:
x=25
Therefore, Don initially had 2x=2*25=50 stickers.
The answer is: 50.

Answer: 50.


Question:There are $206$ bones in the human body. The bones in the hands account for $\\dfrac{27}{103}$~of the total. If the finger bones account for $\\dfrac{14}{27}$~of the total hand bones, how many finger bones are there in the human body? 

Process:
We know that there are 206 bones in the human body.
The bones in the hands account for 27/103 of the total. So, we can calculate the number of bones in the hands by using the following equation: 
    (27/103) * 206 = 54 bones in the hands.
Now we need to find out how many finger bones there are in the hand bones. They account for 14/27 of the total hand bones. So, we can calculate the number of finger bones with the following equation: 
    (14/27) * 54 = 28 finger bones.
Therefore, there are 28 finger bones in the human body.
The answer is: 28.

Answer:28


Question: 65\%~ ~65\% of the animals in a farm were cows and the rest were goats. When 240 more cows and goats were added to the farm, the percentage of cows increased by 20\% and the number of goats doubled. How many goats were there in the farm at first? 

Process:
Let's assume the total number of animals on the farm initially is x.
According to the problem, 65% of the animals were cows, so the number of cows initially is 0.65x. The remaining animals, which are goats, account for 100% - 65% = 35% of the total.
Therefore, the number of goats initially is 0.35x.
After 240 more cows and goats were added to the farm, the new total number of animals becomes x + 240.
The percentage of cows increases by 20%, so the new percentage of cows becomes 65% + 20% = 85%.
The number of cows after the addition is 85% of the new total, which is 0.85(x + 240).
The number of goats after the addition is twice the initial number of goats, so it becomes 2 * 0.35x = 0.7x.
According to the problem, the sum of the number of cows and goats after the addition is equal to the new total number of animals on the farm:
0.85(x + 240) + 0.7x = x + 240
Simplifying the equation:
0.85x + 204 + 0.7x = x + 240
Combining like terms:
1.55x + 204 = x + 240
Subtracting x from both sides:
0.55x + 204 = 240
Subtracting 204 from both sides:
0.55x = 36
Dividing both sides by 0.55:
x = 36 / 0.55
Solving for x:
x ≈ 65.45
The problem want to solve the number of goats in the farm at first.
The number of goats initially is 0.35x, so the number of goats is 0.35 * 65.45 = 22.9075
Since the number of goats in the farm at first is a whole number, the closest whole number to 22.9075 is 23.
Therefore, there were 23 goats in the farm initially.
The answer is: 23.

Answer: 23.


Question: Daniel spent three weeks preparing and writing a presentation on whales.  He began work on the project on the $$15$$\textsuperscript{th} May. What date did he finish the project? 

Process:
To determine the date when Daniel finished the project, we need to add three weeks to the starting date of May 15th.
Each week consists of seven days. Therefore, three weeks would be 3 * 7 = 21 days.
Starting from May 15th, if we add 21 days, we will get the date when Daniel finished the project.
May has 31 days, so let's calculate:
May 15 + 21 = May 36.
However, May only has 31 days, so we need to adjust the date.
We subtract 31 from 36, which gives us 5.
The next month of May is June.
Therefore, Daniel finished the project on June 5th.
The answer is: June 5th.

Answer: June 5th


Question: Student $$A$$ and Student $$B$$ both had a mathematics test. Student $$B$$ told student $$A$$ "I scored $$50$$ points less than you in the mathematics test." Student A told student B "if you gave me $$25$$ points, then my score would be $$5$$ times that of yours." What is the score Student $$A$$ got on the mathematics test? 

Process:
Let's assume that Student A's score is represented by x and Student B's score is represented by y.
According to the information given, Student B scored 50 points less than Student A, so we can write the equation:
y=x−50
Student A then says that if Student B gave him 25 points, his score would be 5 times that of Student B's.
From this information, we can know that if A's points add by 25 and B's points reduce by 25, A's score would be 5 times that of Student B's.
So we can write the equation:
x+25=5(y-25)
Now we have a system of two equations that we can solve to find the value of x, which represents Student A's score.
Substituting the value of y from the first equation into the second equation, we have:
x+25=5((x−50)-25)
Simplifying this equation:
x+25=5(x−75)
x+25=5x−375
4x=400
x=100
Therefore, Student A's score on the mathematics test is 100.
So, the score that Student A got on the mathematics test is 100.
The answer is: 100.

Answer: 100


Question: Melvin, Nelson and Oliver were playing cards.  At first Melvin started with $$40$$ cards and then he gained $$\frac{5}{8}$$ more than his original number of cards from Nelson.  In the next round, Melvin and Nelson each lost $$\frac{1}{4}$$ of Melvin\textquotesingle s original number of cards to Oliver.  In the final round, Melvin gained $$\frac{1}{8}$$ of his original number of cards from Nelson. After the final round, Melvin, Nelson and Oliver all have the same number of cards. What was the total number of cards Melvin, Nelson and Oliver had at first? 

Process:
Since we have known the original number of cards of Melvin, which is 40, and the original numbers of cards of Nelson and Oliver are unkonwn,
let's assume that the original number of cards of Nelson is N, and the original number of cards of Oliver is O.
At first turn, Melvin gained 5/8 more than his original number of cards from Nelson.
So the number of cards of Melvin becomes 40 + (5/8)*40 = 65. 
The number of cards of Nelson becomes N - (5/8)*40 =  N - 25.
In the next round, Melvin and Nelson each lost (1/4) of Melvin's original number of cards to Oliver.
So the number of cards of Melvin becomes 65 - (1/4)*40 = 55. 
The number of cards of Nelson becomes N - 25 - (1/4)*40 = N - 35. 
The number of cards of Oliver becomes O + (1/4)*40*2 = O + 20
In the final round, Melvin gained $$\frac{1}{8}$$ of his original number of cards from Nelson.
So the number of cards of Melvin becomes 55 + (1/8)*40 = 60. 
The number of cards from Nelson becomes N - 35 - (1/8)*40 = N - 40.
After the final round, Melvin, Nelson and Oliver all have the same number of cards.
Now Melvin has 60 cards. Nelson has N - 40 cards. And Oliver has O + 20 cards.
So we can get two equations:
N - 40 = 60
O + 20 = 60
Solving these two equations:
N = 100
O = 40
So the total number of cards Melvin, Nelson and Oliver had at first is 100 + 40 + 40 = 180.
The answer is: 180.

Answer: 180

Q: 
'''.strip()
