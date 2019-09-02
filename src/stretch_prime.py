x = input("Please enter an integer: ")

intX = int(x,0)

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime number"
    
    return "Prime number"

print(checkPrime(intX))