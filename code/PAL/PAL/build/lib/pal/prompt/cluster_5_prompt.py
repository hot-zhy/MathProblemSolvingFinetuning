MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of Applied mathematics and basic arithmetic for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of Applied mathematics and basic arithmetic to solve math problems. Here are five examples how to do it.

Question:
Amy has $$37$$ apples and John has $$15$$ apples. How many apples does Amy have to give John so that she has exactly $$4$$ more apples than John?

Process:
To solve this problem, we'll use basic arithmetic:
1.Initial Situation: Amy has 37 apples, and John has 15 apples.
2.Final Situation: Amy wants to have 4 more apples than John.
3.Setting Up the Equation: If Amy gives John x apples, then Amy will have 37−x apples, and John will have 15+x apples.
4.Finding x:we need 37-x=15+x-4.
5.Solving for x:This simplifies to 37-x=19+x ⇒ 2x=18 ⇒ x=9
6.The answer is 9

Answer: 9

Question:
Mary is in a small class of $$6$$ pupils, but was absent for the Maths test last week. The other five pupils scored an average of $$72 \\%$$. Mary wrote the test this week and, with her score included, the class average went up to $$75 \\%$$.  What mark did Mary score on the test?  Answer~\\uline{~~~~~~~~~~}~ 

Process:
To solve this problem, we use basic arithmetic to find Mary's test score:
1.Initial Average Without Mary: The average score of the 5 pupils is 72%. The total score of these 5 pupils is therefore 5×72%.
2.New Average With Mary: With Mary included, the average for 6 pupils is 75%. The total score for 6 pupils is 6×75%.
3.Finding Mary's Score: Mary's score is the difference between the total score of 6 pupils and the total score of the initial 5 pupils.
4.Let's calculate Mary's score manually:Total Score of 5 Pupils: 5×72%=360%;Total Score of 6 Pupils: 6×75%=450%
Now, Mary's score is the difference between these two totals:450%−360%=90%
5.The answer is 90

Answer: 90


Question:
Find the average of the following sequence.  $$1$$, $$3$$, $$5$$, $$7$$, $$9$$, $$\\cdots $$, $$195$$, $$197$$, $$199$$.

Process:
To find the average of the sequence 1, 3, 5, 7, 9, ..., 195, 197, 199, we'll use basic arithmetic principles:
1.Identify the Pattern: This is an arithmetic sequence where each term increases by 2.
2.First and Last Term: The first term is 1, and the last term is 199.
3.Number of Terms: To find the number of terms, we use the formula for the nth term of an arithmetic sequence: 
an=a1+(n−1)d, where an is the nth term, a1 is the first term, n is the number of terms, and d is the common difference. Here, an=199, a1=1, and d=2. Solve for n.
4.Calculate the Average: The average of an arithmetic sequence is (a1+an)/2
5.Let's perform the calculations.
The sequence 1, 3, 5, 7, 9, ..., 195, 197, 199 has 100 terms. The average of this arithmetic sequence is 100.0. ​
6.The answer is: 100

Answer: 100


Question:
One of the angles in a triangle is a right angle. Two unknown angles are left and one of them is two times larger than the the other angle.  What is the size of the largest angle betwen the two?

Process:
To solve this problem, let's follow these steps:
1.Right Triangle: Since one of the angles is a right angle, it measures 90 degrees.
2.Sum of Angles in a Triangle: The sum of the angles in any triangle is 180 degrees.
3.Remaining Angles: Subtracting the right angle (90 degrees) from the total, 180 - 90 = 90 degrees are left for the other two angles.
4.Ratio of Angles: One angle is two times larger than the other. Let the smaller angle be x degrees. Then the larger angle is 2x degrees.
5.Equation: The sum of these two angles is x+2x=90 degrees.
6.Solve for 3x=90 so x=30 degrees.
7.Largest Angle: The larger angle is 2x=2×30=60 degrees.
8.The answer is 60

Answer: 60


Question:
There are $42$ sweets in Container A and $4$ times as many sweets in Container B as Container A. Given that there are twice as many sweets in Container C as Container B, how many sweets are there in Container C? 

Process:
To solve this problem, we'll use applied mathematics and basic arithmetic:
1.Calculate Sweets in Container B: Container B has 4 times as many sweets as Container A. Since Container A has 42 sweets, Container B has 4×42 sweets.
2.Calculate Sweets in Container C: Container C has twice as many sweets as Container B. So, the number of sweets in Container C is 2× [number of sweets in Container B].
3.Let's do the calculations:There are 336 sweets in Container C
4.The answer is 336

Answer: 336

Q: 
'''.strip()
