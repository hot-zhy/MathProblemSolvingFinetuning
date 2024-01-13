MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of permutation and combination problems for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of permutation and combination problems to solve math problems. Here are five examples how to do it.


Question: There are $$5$$ girls and $$7$$ boys in a class. How many ways are there to form a group of $$4$$ if there must be at least $$1$$ boy in the group?

Process:
To determine the number of ways to form the group of 4 with at least 1 boy, we can use its inverse proposition to solve this problem.
    Since the inverse proposition of at least one item is that there are no items, 
    we can know that the inverse proposition of the problem is that: the number of ways a group of 4 students if there must be no boy in the group.
    To solve this problem, we can do as follows:
        First, we solve the the inverse proposition of the problem.
            Select 4 girls from the 5 available girls: C(5, 4) = 5 ways.
        Then, we calculate all possible scenarios.
            Select 4 students from all the available students.
            The number of all students is 5 + 7 = 12.
            So there is C(12, 4) = 495 ways.
        Finally, we remove the ways of inverse proposition from all ways.
            495 - 5 = 490
        So 490 is the number of ways to form the group of 4 with at least 1 boy.    
The answer is: 490.

Answer: 490




Question: There are $6$ people sitting around an eight-seater circular table. How many different orders are there for them to sit? (If we can get the same order after rotating the table, then we regard the two orders as the same one.) 

Process:
To find the number of different orders for the 6 people to sit around the circular table, we can use the concept of permutations.
We have 6 people and 8 seats on the circular table. 
The first person can choose any of the 8 seats. 
Once the first person is seated, the second person can choose any of the remaining 7 seats. 
Similarly, the third person can choose any of the remaining 6 seats, and so on.
Therefore, the total number of different orders for the people to sit is given by the product of the number of choices for each person:
8 choices for the first person × 7 choices for the second person × 6 choices for the third person × 5 choices for the fourth person × 4 choices for the fifth person × 3 choices for the sixth person.
This can be written as:
8 × 7 × 6 × 5 × 4 × 3 = 20,160.
So, there are 20,160 different orders for the 6 people to sit around the circular table, considering that the same order after rotating the table is regarded as the same one.
The answer is: 20160.

Answer: 20160




Question: How many different ways are there to divide $30$ books to $5$ kids, to make sure each of them gets at least two books?

Process:
To divide 30 books among 5 kids, ensuring that each child receives at least two books, we can use a combinatorial approach.
First, we distribute 2 books to each child, which leaves us with 20 books to distribute freely among the 5 kids.
We can represent this problem using stars and bars. Let's denote the number of additional books received by each child as x1, x2, x3, x4, and x5, respectively.
We need to find the number of solutions to the equation x1 + x2 + x3 + x4 + x5 = 20, where xi represents the number of additional books received by the i-th child.
Using the stars and bars formula, the number of solutions to this equation is given by C(20 + 5 - 1, 5 - 1) or C(24, 4).
Using the binomial coefficient formula, C(n, k) = n! / (k! * (n - k)!), we can calculate C(24, 4) as:
C(24, 4) = 24! / (4! * (24 - 4)!) = (24 * 23 * 22 * 21) / (4 * 3 * 2 * 1) = 10,626.
Therefore, there are 10,626 different ways to divide 30 books among 5 kids, ensuring that each child receives at least two books.
The answer is: 10626.

Answer: 10626





Question: Use all the digits $$9$$, $$0$$, $$2$$ and $$3$$ to form a number that is closest to $$2978$$.

Process:
To form a number using the digits 9, 0, 2, and 3 that is closest to 2978, we can analyze the digits and find the closest number to 2978.
Let's analyze the digits:
For the thousands digit, we found that the digit 2 is the closest number to the thousands digit of 2978, which is also 2.
So the thousands digit of new number can be set to 2.
The remaining digits are 9, 0, 3.
For the hundreds digit, we found that the digit 9 is the closest number to the thousands digit of 2978, which is also 9.
So the hundreds digit of new number can be set to 9.
The remaining digits are 0, 3.
For the tens digit, we found that the digit 3 is the closest number to the thousands digit of 2978, which is also 7.
The remaining digits are 0.
Since we have only one remaining digit, so the units digit is 0.
After the analysis, we can get the number 2930, which is the closest number to 2978.
The answer is 2930.

Answer: 2930





Question: Ali, Bala, Charles, Dan and Ella are standing side by side in a line to take a photo. If Ali and Bala must stand together and Dan must stand at the furthest left, how many different arrangements are there?

Process:
To determine the number of different arrangements of Ali, Bala, Charles, Dan, and Ella that satisfy the given conditions, we can treat Ali and Bala as a single entity (AB). 
This reduces the problem to arranging four objects: AB, Charles, Dan, and Ella.
Since Dan must stand at the furthest left, which means he has been arranged, we don't need to take him into account.
So we only need to arrange three objects: AB, Charles, and Ella.
Let's consider the different cases:
Case 1: Ali and Bala are arranged as AB.
In this case, we have AB, Charles, and Ella. We can arrange these three entities in 3! = 6 ways.
Case 2: Ali and Bala are arranged as BA.
In this case, we have BA, Charles, and Ella. We can arrange these three entities in 3! = 6 ways.
To obtain the total number of arrangements, we sum up the arrangements from both cases:
Total arrangements = Case 1 + Case 2 = 6 + 6 = 12
Therefore, there are 12 different arrangements of Ali, Bala, Charles, Dan, and Ella that satisfy the given conditions.
The answer is 12.

Answer: 12

Q: 
'''.strip()
