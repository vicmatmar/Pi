import profile

# My first prime number checker attemp.
# I'm sure there are faster ways... (see https://stackoverflow.com/questions/15285534/isprime-function-for-python-language)
# I'm not checking for numbers such as 2 or less
def IsPrimeNumber(number):
    # Check division remainders (mod) starting from 2 up to the number-1
    for x in range (2, (int)(number/2)):
        mod = number % x;
        if mod == 0:
            return False;
    # If we made it this far it means we have a prime.  Yeah!!!
    return True;

def IsPrimeNumberRangeChecker(start, end):
    for numberToCheck in range(start,end):
        if IsPrimeNumber(numberToCheck):
            print(numberToCheck)
        numberToCheck += 1;

# Can use this to check results: https://primes.utm.edu/curios/includes/primetest.php
# Or this: http://www.math.com/students/calculators/source/prime-number.htm
def main():


    profile.run(
        'IsPrimeNumberRangeChecker(3, 10000000)'
    )

    

if __name__== "__main__":
  main()
