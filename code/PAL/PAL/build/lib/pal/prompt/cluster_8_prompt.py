MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use methods of addition, subtraction, multiplication and division to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use methods of addition, subtraction, multiplication and division to solve math problems. Here are five examples how to do it.

Question:$7.55+6.32+6.45-5.32=$

Process:To find the value of the expression 7.55 + 6.32 + 6.45 - 5.32, we perform the addition and subtraction operations between the given numbers. Here's the thinking process:
Begin with the first number, 7.55.
Add the next number, 6.32: 
    7.55 + 6.32 = 13.87.
Add the next number, 6.45: 
    13.87 + 6.45 = 20.32.
Subtract the last number, 5.32: 
    20.32 - 5.32 = 15.
Therefore, the value of the expression 7.55 + 6.32 + 6.45 - 5.32 is 15.

Answer:15

Question:Which number is halfway tetween $$4.6$$ and $$13.8$$?  ~\\uline{~~~~~~~~~~}~

Process:To find the number that is halfway between 4.6 and 13.8, you can calculate the average of these two numbers. Here's the step-by-step process:
Add the two numbers together: 4.6 + 13.8 = 18.4
Divide the sum by 2: 18.4 / 2 = 9.2
Therefore, the number that is halfway between 4.6 and 13.8 is 9.2.

Answer:9.2

Question:$15 \\div 0.05 =$ 

Process:To solve the division problem 15 ÷ 0.05, you can follow these steps:
Rewrite the division problem as a multiplication problem by multiplying the dividend, 15, by the reciprocal of the divisor. The reciprocal of 0.05 is 1/0.05, which is equal to 20.
So, the problem becomes: 15 × 20.
Multiply 15 by 20: 15 × 20 = 300.
Therefore, 15 ÷ 0.05 = 300.

Answer:300

Question:$5 -- 1.02$ 

Process:To subtract 1.02 from 5, follow these steps:
Begin with the rightmost digit (hundredths place) and subtract 2 from 0. Since 0 is smaller than 2, we need to borrow from the next column. And then 0 in the percentile becomes 10, so we substract 2 from 10 to get 8 in the percentile.
Move to the next column (tenths units place) and borrow 1 from the units place. 5 becomes 4, and 0 in the tenths place becomes 10. Then we substract 1 from the tenths place 10 to get 9 in the tenths place for the answer.
Move to the next column (ones place) and subtract 1 from 4, which gives 3.
The final result is 3.98.
Therefore, subtracting 1.02 from 5 equals 3.98.

Answer:3.98

Question:If $5$ mugs cost $£3.50$ and $8$ pens cost $£6.80$ how much change do I get from $£10$ if I buy $7$ mugs and $5$ pens? You MUST show your working. 

Process:Here's how you can calculate the change you would get from £10 when buying 7 mugs and 5 pens:
Calculate the total cost of buying 7 mugs:
The cost of 5 mugs is £3.50.
To find the cost of 1 mug, divide £3.50 by 5: £3.50 ÷ 5 = £0.70.
Multiply the cost of 1 mug (£0.70) by 7: £0.70 × 7 = £4.90.
Therefore, the total cost of buying 7 mugs is £4.90.
Calculate the total cost of buying 5 pens:
The cost of 8 pens is £6.80.
To find the cost of 1 pen, divide £6.80 by 8: £6.80 ÷ 8 = £0.85.
Multiply the cost of 1 pen (£0.85) by 5: £0.85 × 5 = £4.25.
Therefore, the total cost of buying 5 pens is £4.25.
Add the total cost of buying 7 mugs (£4.90) and the total cost of buying 5 pens (£4.25): £4.90 + £4.25 = £9.15.
To calculate the change, subtract the total cost (£9.15) from the amount paid (£10.00):
£10.00 - £9.15 = £0.85.
Therefore, if you buy 7 mugs and 5 pens with £10.00, you would get £0.85 in change.

Answer:0.85
Q: 
'''.strip()
