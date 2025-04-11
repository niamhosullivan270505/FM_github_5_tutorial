# This script defines a function to check if a number is positive.
def is_positive(number):  # Added missing colon
    if number > 0:
        return True
    else:
        return False  # Fixed indentation

# Testing
test_number = -5
output = is_positive(test_number)
print("Is the number positive?", output)