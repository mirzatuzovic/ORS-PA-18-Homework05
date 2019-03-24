"""
===================   TASK 3   ====================
* Name: Convert to Octal
*
* Write a function `dec2oct` that will convert
* positive integer number passed as argument into
* the octal based number. 
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""

def dec2oct(br):

    ostatak = ""
    while br > 0:

        ost = br % 8
        ostatak += str(ost)
        br = br // 8

    return ostatak[-1 :: -1]


def main():

    oct_br = dec2oct(125)
    print("Oktalni broj je: ", oct_br)

main()