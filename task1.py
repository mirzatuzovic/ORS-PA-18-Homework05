"""
===================   TASK 1   ====================
* Name: Power to the Number
*
* Write a function `numpower()` that will for the
* passed based number `num` and exponent `expo`
* return the value of the number `num` raised to
* the power of `expo`.
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in operators and functions
* for this task.
*
* Use main() function to test your solution.
===================================================
"""

def numpower(x, y):

    exp = x ** y

    return exp

def main():

    x = abs(int(input("Unesi prvi broj: ")))
    y = abs(int(input("Unesi drugi broj: ")))

    print(numpower(x, y))

main()











