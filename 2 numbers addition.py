# Function to calculate the sum of two numbers
def calculate_sum(num1, num2):
    return num1 + num2

# Input: Get two numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the sum
sum_result = calculate_sum(number1, number2)

# Output: Display the result
print(f"The sum of {number1} and {number2} is {sum_result}.")
