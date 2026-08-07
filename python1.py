# Given Input
numbers = [10, 20, 30, 40, 50]

# 1. Access the third element of the list
# (Using index 2 since Python lists are 0-indexed)
third_element = numbers[2]
print(f"Third element: {third_element}")

# 2. List Length: Print the total number of items
list_length = len(numbers)
print(f"Total number of items: {list_length}")

# 3. Check if the list is empty
if not numbers:
    print("The list is empty.")
else:
    print("The list is not empty.")