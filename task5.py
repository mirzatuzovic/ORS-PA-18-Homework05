"""
===================   TASK 5   ====================
* Name: Average Value
*
* Write a function `averageval` that will take a
* integer list as an argument and return the 
* average value of the list elements.  
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""

def averageval(lista):

    zbir = 0

    for i in lista:

        zbir = zbir + i
    prosjek = zbir / len(lista)

    return prosjek

def main():

    prosjecna_vrijednost = averageval([4,6,8,10,12,14,16,18])
    print(prosjecna_vrijednost)

main()
