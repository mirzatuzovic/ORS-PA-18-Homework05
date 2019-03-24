"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

broj=int(input("Unesite broj: "))
broj=abs(broj)

pr=1

while broj>0:
    pr*=broj%10
    broj=broj//10

def main():

    proizvod = pr
    print("Proizvod cifara je: ", proizvod)

main()