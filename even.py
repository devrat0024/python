# Initialize the sum to 0
even_sum = 0
# Iterate through numbers from 1 to 101 (inclusive) with a step of 1
for num in range(1, 101):
    # Check if the number is even
    if num % 2 == 0:
        # If the number is even, add it to the sum
        even_sum += num

# Print the sum of even numbers
print("Sum of even numbers from 1 to 101:", even_sum)
