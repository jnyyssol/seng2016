
#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(0, end):
            print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        
        prime_numbers = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97];

        if (i in prime_numbers):
            str = "%d is a prime" %i
            return str
        else:
            if ((i % 15) == 0):
                return "FizzBuzz"
            elif ((i % 5) == 0):
                return "Buzz"
            elif ((i % 3) == 0):
                return "Fizz"
            else:
                return i
        

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
