# Arguments
# write a function print_three_numbers that prints all numbers in the order they are given

def print_three_numbers(num1, num2, num3):
    print(f"number 1 is : {num1}")
    print(f"number 2 is : {num2}")
    print(f"number 3 is : {num3}")


## call it with positional arguments
print_three_numbers(5, 2, 3)

# call it with named argments
print_three_numbers(num1 = 5, num2 = 2, num3 = 3)

# call it with positional and named arguments, ONLY CAN write positional arguments before named arguments
print_three_numbers(5, num3 = 3, num2 = 2)

## write a function called print_all_numbers that will print any amount of numbers
# if we add a start to the argument, we unpack the argument

def print_all_numbers(*argv):
    print(argv)   # turns all argv into a tuple
    for arg in argv:
        print(arg)

print_all_numbers(1, 2, 3)
print_all_numbers(1)
print_all_numbers(1, 2, 3, 4, 5)

num_tuple = (1, 2, 3, 4, 5)
print(num_tuple)   # prints out (1, 2, 3, 4, 5)
print(*num_tuple)  # prints out 1 2 3 4 5



## write a function that will print all numbers, in reverse order if we specify a reverse variable

def print_all_numbers_maybe_reverse(*args, reverse = False) :
    if reverse == True:
        for i in range(len(args)-1, -1, -1):
            print(f"Number at {i} is {args[i]}")
    else:
        for i in range(len(args)):
            print(f"Number at {i} is {args[i]}")


print_all_numbers_maybe_reverse(1, 2, 3, reverse = True)
print_all_numbers_maybe_reverse(1, 2, 3)


#return the "centered" average of an array of ints, except ignoring largest and smallest values

# one pass solution 
def centered_average(nums):
    if len(nums) < 3: return None
    lg = sm = total = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > lg : lg = nums[i]
        elif nums[i] < sm : sm = nums[i]
        total += nums[i]
    return (total - lg - sm) // (len(nums) - 2)

# short and pretty but multiple passes
def centered_average_2(nums):
    if len(nums) < 3 : return None
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0])) 
print(centered_average([1, 2]))

print(centered_average_2([1, 2, 3, 4, 100]))
print(centered_average_2([1, 1, 5, 5, 10, 8, 7]))
print(centered_average_2([-10, -4, -2, -4, -2, 0])) 
print(centered_average_2([1, 2]))

