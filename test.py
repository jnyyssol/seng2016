import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()


        self.failIf(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)


    def test_fizz(self):
        app = FizzBuzz()

        self.failIf(app.calc(3) != "Fizz")
        self.failIf(app.calc(6) != "Fizz")
        self.failIf(app.calc(9) != "Fizz")

    def test_buzz(self):
        app = FizzBuzz()

        self.failIf(app.calc(5) != "Buzz")
        self.failIf(app.calc(10) != "Buzz")
        self.failIf(app.calc(20) != "Buzz")


    def test_fizzbuzz(self):
        app = FizzBuzz()
			
        self.failIf(app.calc(15) != "FizzBuzz")
        self.failIf(app.calc(30) != "FizzBuzz")
        self.failIf(app.calc(45) != "FizzBuzz")
		
    def test_number(self):
        app = FizzBuzz()
		
        self.failIf(app.calc(2) != 2)
        self.failIf(app.calc(4) != 4)
        self.failIf(app.calc(8) != 8)
		
		
def main():
    unittest.main()

if __name__ == "__main__":
    main()
