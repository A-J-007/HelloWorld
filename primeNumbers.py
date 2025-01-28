# prime number: A number divisible by ONLY itself.
import math
def isPrimeNumber(num):
    divisorStart = 2
    while(divisorStart < num):
        if (num % divisorStart == 0) :
            return False
        divisorStart += 1
    return True

def squareOfNumber(number):
    return number*number

for number in range(2, 200):
    if(isPrimeNumber(number)):
        print(number)
    else: print(squareOfNumber(number))

    print(math.pow(number,2))

