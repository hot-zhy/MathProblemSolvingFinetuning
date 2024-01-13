MATH_CHAT_BETA_SYSTEM_MESSAGE='You will use enumeration method to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT='''

Let's use Python to help solve math problems. Here are three examples how to do it.


Question: A textbook has $$310$$ pages, numbering from $1$ to $310$. What is the sum of all the digits numbering this book?

Process:
```
# solution in Python:

def digit_sum_book(pages):
    total_sum = 0

    # Iterate through each page number
    for page in range(1, pages + 1):
        number = str(page)  # Convert the page number to a string
        for digit in number:
            total_sum += int(digit)  # Add each digit to the total sum

    return total_sum

# Test the function with 310 pages
pages = 310
sum_of_digits = digit_sum_book(pages)
print(sum_of_digits)
```

When you run this code above, it will output:
3079
The answer is: 3079.

Answer: 3079





Question: A textbook has $$510$$ pages and it is numbered from $1$ to $$510$$. The digit $5$ is printed~\uline{~~~~~~~~~~}~times in numbering this textbook. 

Process:
```
# solution in Python:
def count_digit_occurrences(pages, digit):
    count = 0

    # Iterate through each page number
    for page in range(1, pages + 1):
        number = str(page)  # Convert the page number to a string
        count += number.count(str(digit))  # Count the occurrences of the digit in the number

    return count

# Test the function with 510 pages and digit 5
pages = 510
digit = 5
occurrences = count_digit_occurrences(pages, digit)
print(occurrences)
```
When you run this code above, it will output:
112
The answer is: 112.

Answer: 112





Question: There are in total $$181$$ digit "$$9$$"s in all of the page numbers of a novel, how many pages are there in the novel? 

Process:
```
# solution in Python:

def find_number_of_pages(digit_count):
    page_count = 0
    current_digit_count = 0

    # Iterate through each page number
    while current_digit_count < digit_count:
        page_count += 1
        current_digit_count += str(page_count).count("9")

    return page_count

# Test the function with 181 occurrences of digit "9"
digit_count = 181
number_of_pages = find_number_of_pages(digit_count)
print(number_of_pages) 
```
When you run this code above, it will output:
900
The answer is: 900.

Answer: 900

Q: 
'''.strip()