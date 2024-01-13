MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use enumeration method to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use Python to help solve math problems. Here are three examples how to do it.
!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**

Question: A textbook has $$310$$ pages, numbering from $1$ to $310$. What is the sum of all the digits numbering this book?
```
def solution():
    # Single-digit pages
    single_digits = sum(range(1, 10))

    # Double-digit pages
    double_digits_tens = sum(range(1, 10)) * 10  # Tens digit sum
    double_digits_units = sum(range(10)) * 9     # Units digit sum

    # Triple-digit pages
    # Hundreds digit sum
    hundreds_digit = 1*100 + 2*100 + 3*11  
    # Tens and units digit sum (from 00 to 99, three times, plus 00 to 10 once)
    tens_units = (sum(range(10)) * 10 + sum(range(10))) * 3 + sum(range(1, 11))

    # Total sum
    total_sum = single_digits + double_digits_tens + double_digits_units + hundreds_digit + tens_units
    result = total_sum
    return result
```



Question: A textbook has $$510$$ pages and it is numbered from $1$ to $$510$$. The digit $5$ is printed~\\uline{~~~~~~~~~~}~times in numbering this textbook. 
```
def solution():
    # The problem is to find the number of times the digit 5 appears in the page numbers of a textbook numbered from 1 to 510.

    # Count the occurrences of the digit 5 in each place value (units, tens, hundreds)
    total_count = 0

    # Count for units place (e.g., 5, 15, 25, ... 505)
    # There are 51 occurrences in each ten numbers (5, 15, 25, ... 95)
    total_count += (510 // 10)

    # Count for tens place (e.g., 50-59, 150-159, ...)
    # There are 10 occurrences in each hundred numbers (50-59, 150-159, ...)
    total_count += (510 // 100) * 10

    # Check if there are any extra occurrences in the tens place for the last incomplete hundred
    if (510 // 100) != (510 / 100):
        extra_pages = 510 % 100
        if extra_pages >= 50:
            total_count += min(extra_pages - 50 + 1, 10)

    # Count for hundreds place (e.g., 500-510)
    # Since the book has 510 pages, the digit 5 appears in the hundreds place 11 times (500-510)
    if 500 <= 510:
        total_count += 11

    return total_count

```


Question: There are in total $$181$$ digit "$$9$$"s in all of the page numbers of a novel, how many pages are there in the novel? 
```
def solution():
    # The problem is to find the total number of pages in a novel, 
    # given that there are 181 digit "9"s in all of the page numbers.
    # We will count the occurrence of digit "9" in each range of page numbers.

    # Initialize variables to count the total number of pages and the number of 9s encountered
    total_pages = 0
    total_nines = 0

    # Pages with one digit (1-9): Only one 9
    # Pages with two digits (10-99): 9 pages with 9 as the first digit and 10 pages with 9 as the second digit, total 19
    # Pages with three digits (100-999): 100 pages with 9 in the hundreds place, 100 in the tens place, and 100 in the ones place, total 300
    # We continue this pattern until the total number of 9s reaches 181.

    # Count 9s in one-digit pages
    total_nines += 1
    total_pages = 9

    # Count 9s in two-digit pages
    if total_nines + 19 <= 181:
        total_nines += 19
        total_pages = 99
    else:
        remaining_nines = 181 - total_nines
        # Calculate the exact number of pages to reach 181 nines
        total_pages += remaining_nines // 2  # Each two-digit page with a 9 contributes 2 to the count
        return total_pages

    # Count 9s in three-digit pages
    if total_nines + 300 <= 181:
        total_nines += 300
        total_pages = 999
    else:
        remaining_nines = 181 - total_nines
        # Calculate the exact number of pages to reach 181 nines
        total_pages += remaining_nines // 3  # Each three-digit page with a 9 contributes 3 to the count
        return total_pages
	result = total_pages
    return result

```

!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**
'''.strip()
