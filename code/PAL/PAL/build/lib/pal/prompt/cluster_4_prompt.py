MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use Number Theory Principles and Methods for reasoning. Please think step by step. And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of Number Theory Principles and Methods to solve math problems. Here are five examples how to do it.

Question: 
If $$p$$ and $$p+107$$ are both prime numbers, find the value of $$p$$

Process:
To solve the problem "If p and p+107 are both prime numbers, find the value of p", we can use several Number Theory Principles and Methods. Here's a step-by-step reasoning:
1.Understanding Prime Numbers: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Since p and p+107 are both prime, they cannot be divisible by any other number than 1 and themselves.
2.Considering Even and Odd Properties: Except for 2, all prime numbers are odd. If p is an odd number, then p+107 (being the sum of two odd numbers) will also be even, which cannot be a prime number unless p+107 is 2 (which is not possible here since 107 is greater than 2). Therefore, p must be 2, the only even prime number.
3.Substituting and Verifying: If p=2, then p+107=109. We need to check whether both 2 and 109 are prime numbers.
4.Verification: 2 is a prime number (as it is only divisible by 1 and itself). 109 is a prime number (it has no divisors other than 1 and itself).
So, the only value of p that satisfies the condition that both p and p+107 are prime numbers is p=2.
The answer is: 2.

Answer: 2


Question:
$$50$$ students stand in a line facing the teacher, and report the number from left to right one by one: $$1$$, $$2$$, $$3$$, .. etc. After reporting, the teacher asks students who reported multiples of $$4$$ turn backwards. Then let the students whose reported number is a multiple of $$6$$ turn backwards.  How many students are still facing teachers? 

Process:
To solve the problem where 50 students stand in a line and turn backwards based on certain conditions, we'll use principles of Number Theory. Let's break it down step by step:
1.Identifying Multiples of 4: Students reporting multiples of 4 (4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48) will first turn backwards. There are 
⌊50/4⌋=12 such students.
2.Identifying Multiples of 6: Next, students reporting multiples of 6 (6, 12, 18, 24, 30, 36, 42, 48) will turn backwards. There are ⌊50/6⌋=8 such students. However, some of these students might have already turned backwards because their numbers are also multiples of 4.
3.Considering Overlaps (Multiples of 12): Since 12 is the least common multiple of 4 and 6, any student who reports a multiple of 12 would have already turned backwards in the first step. These students are (12, 24, 36, 48). There are ⌊50/12⌋=4 such students.
4.Total Students Turned Backwards:
-Initially, 12 students (multiples of 4) turn. -Additional 8 students (multiples of 6) turn, but this count includes those who already turned. 
-Subtract 4 students (multiples of 12) who were counted twice. 
-Total = 12 (multiples of 4) + 8 (multiples of 6) - 4 (counted twice) = 16 students.
5.Students Still Facing the Teacher:
-Total students = 50
-Students turned = 16
-Students still facing the teacher = 50 - 16 = 34
6.The answer is 34.

Answer:34


Question:
At the school scavenger hunt, class $A$, $B$, $C$ each has $8$, $12$, $20$ students who want to participate. The participating students will need to split into groups of the same size. They can\\textquotesingle t group up with students from other classes. How many students will each group have? 

Process:
To solve the problem of splitting students from classes A, B, and C into groups of the same size without mixing classes, we need to use the concept of Greatest Common Divisor (GCD) in Number Theory. Let's approach it step by step:
1.Understanding the Problem: Class A has 8 students, class B has 12 students, and class C has 20 students. We need to find the largest group size such that students in each class can be divided into groups of this size without leaving anyone out.
2.Finding the GCD: The group size must be a divisor common to 8, 12, and 20. The GCD of these numbers will give us the largest possible group size.
3.Calculating GCD for 8 and 12:
-The divisors of 8 are 1, 2, 4, 8.
-The divisors of 12 are 1, 2, 3, 4, 6, 12.
-The common divisors are 1, 2, 4, and the greatest among them is 4.
4.Calculating GCD for 4 and 20 (since 4 is the GCD of 8 and 12):
-The divisors of 4 are 1, 2, 4.
-The divisors of 20 are 1, 2, 4, 5, 10, 20.
-The common divisors are 1, 2, 4, and the greatest among them is 4.
5.Conclusion: The greatest common divisor of 8, 12, and 20 is 4. This means the largest possible group size that can be formed in each class without mixing students and without leaving anyone out is 4.
6.The answer is 4.

Answer:4


Question:
A certain positive integer has exactly eight factors. Two of these factors are $$15$$ and $$21$$. What is the sum of all eight factors?

Process:
To solve this problem,let's follow these steps:
1.Identify the Number: The number must be a multiple of both 15 (3 × 5) and 21 (3 × 7). Its least common multiple (LCM) is 3 × 5 × 7 = 105.
2.Check the Number of Factors: Since the number must have exactly eight factors, we need to check if 105 has eight factors.
3.List All Factors of 105: The factors of 105 are 1, 3, 5, 7, 15, 21, 35, and 105.
4.Sum the Factors: The sum is 1 + 3 + 5 + 7 + 15 + 21 + 35 + 105. Let's calculate this sum.
5.The sum of all eight factors of the number 105, which includes 15 and 21 as factors, is 192.
6.The answer is 192.

Answer:192


Question:
Think Academy has $32$ pencils and $40$ pens to give students as gifts. Each student should receive the same amount of pencils and pens, leaving no spare pens or pencils left. How many students at most will be able to receive the gift?

Process:
To solve this problem, we will use the Greatest Common Divisor (GCD) principle from Number Theory:
1.Identify the Problem: We have 32 pencils and 40 pens to distribute evenly among students, with no leftovers.
2.Calculate the GCD: The GCD of 32 and 40 will tell us the maximum number of students that can receive the gifts without any leftovers.
3.Find the Maximum Number of Students: The GCD of 32 and 40 is the maximum number of students who can receive the gifts.
4.Let's calculate the GCD of 32 and 40 to find the solution.The greatest common divisor (GCD) of 32 and 40 is 8. Therefore, the maximum number of students who can receive the gifts without any spare pens or pencils left is 8.
5.The answer is 8.

Answer:8
Q: 
'''.strip()
