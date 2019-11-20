x = input("Please enter an integer: ")

intX = int(x)

def checkPrime(num):
    if num <= 1: 
        return "Not a prime number"
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime number" 
    return "Prime number"

print(checkPrime(intX))
