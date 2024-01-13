MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use continuous calculation or equations or formula application to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use continuous calculation or equations or formula application to solve math problems. Here are five examples how to do it.

Question:I write down a sequence of numbers.  My first number is $160000$ and then I divide by $4$ to get the next number each time. What is the $5^{th}$~number in my sequence?

Process:The given sequence starts with the number 160000. To find the 5th number in the sequence, we need to repeatedly divide the previous number by 4.
Start with the first number: 160000
Divide by 4 to get the second number: 160000 / 4 = 40000
Divide the second number by 4 to get the third number: 40000 / 4 = 10000
Divide the third number by 4 to get the fourth number: 10000 / 4 = 2500
Finally, divide the fourth number by 4 to get the fifth number in the sequence: 2500 / 4 = 625
Therefore, the fifth number in the sequence is 625.

Answer:625

Question:Calculate:  $1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19=$~\\uline{~~~~~~~~~~}~       
    
Process:To calculate the sum of the numbers 1, 3, 5, 7, 9, 11, 13, 15, 17, and 19, you can follow these steps:
Begin by adding the first two numbers together: 1 + 3 = 4.
Add the next number to the sum: 4 + 5 = 9.
Continue this process, adding each subsequent number to the running sum:
9 + 7 = 16
16 + 9 = 25
25 + 11 = 36
36 + 13 = 49
49 + 15 = 64
64 + 17 = 81
81 + 19 = 100
Therefore, the sum of the numbers 1, 3, 5, 7, 9, 11, 13, 15, 17, and 19 is 100.

Answer:100

Question:Write down the next number in this sequence  $1, 2, 3, 5, 8, 13, 21, \\cdots \\cdots $ 

Process:To find the next number in the sequence 1, 2, 3, 5, 8, 13, 21, and so on, we can observe the pattern:
The sequence appears to be following the Fibonacci sequence, where each number is the sum of the two preceding numbers.
Starting with 1 and 2, we can see that 1 + 2 = 3, and 2 + 3 = 5. Continuing this pattern, 3 + 5 = 8, 5 + 8 = 13, and so on.
Therefore, the next number in the sequence would be obtained by adding the two preceding numbers: 13 + 21 = 34.
Hence, the next number in the sequence is 34.

Answer:34

Question:The sum of five consecutive whole numbers is $100$.  What is the smallest of these five numbers? 

Process:Let's denote the smallest number in the sequence as "x."
Since we want to find the sum of five consecutive whole numbers, we can express the sum as:
    x + (x + 1) + (x + 2) + (x + 3) + (x + 4) = 100
Now, we can simplify the equation:
    5x + 10 = 100
Subtracting 10 from both sides:
    5x = 90
Dividing both sides by 5:
    x = 18
Therefore, the smallest number in the sequence is 18.

Answer:18

Question:Work out: $1 + 3 + 5 + \ldots.. + 155 + 157 + 159$. 

Process:To find the sum of the numbers from 1 to 159, including only the odd numbers, we can follow these steps:
Count the number of terms in the sequence: We need to find the count of odd numbers from 1 to 159. Since odd numbers occur at alternate positions, we can divide 159 by 2 and round up to the nearest whole number to find the count:
(159 ÷ 2) = 79.5, rounded up to the nearest whole number, gives us 80.
Therefore, there are 80 terms in the sequence.
Find the average of the first and last terms: The average of the first and last term in an arithmetic sequence gives us the sum of all the terms.
The first term is 1, and the last term is 159.
The average is (1 + 159) ÷ 2 = 80.
Multiply the average by the number of terms: Multiply the average value (80) by the number of terms (80) to find the sum of the sequence:
80 × 80 = 6400.
Therefore, the sum of the numbers from 1 to 159, including only the odd numbers, is 6400.

Answer:6400
Q: 
'''.strip()
