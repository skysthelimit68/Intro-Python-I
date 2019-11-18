# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even(input_num):
    return input_num % 2 == 0 

print("Even!" if is_even(num) else "Odd!")

