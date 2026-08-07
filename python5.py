# Given list
numbers = [10, 21, 4, 45, 66, 93, 11]

even = 0
odd = 0

# Check each number
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Display results
print("Even numbers:", even)
print("Odd numbers:", odd)