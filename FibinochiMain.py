#This prints off a intro to the program, and prompts the user for an input.
print("     This program will take an input number and output all of the fibonacci numbers in the series untill it gets \n"
      "to number. For example if you input 5 it will print (1, 1, 2, 3, 5).\n"
      "Be careful entering large numbers. This program runs in O(2^n)")
print "\n"
try:
    do_math_until_this = int(input("Input a number: "))
except ValueError:
    print("This is not an integer. Please enter an integer.")
print "\n"


#fib_math does the hardwork here of figuring out what the next digit will be.
def fib_math(input_number):

    if(input_number == 0):
        return 1
    elif(input_number == 1):
        return 1
    else:
        return (fib_math(input_number - 2) +fib_math(input_number - 1))


def fib_sequence(input_number):
    x = fib_math(input_number-1)
    if((input_number-1)>0):
        fib_sequence(input_number-1)#This is where the recursion happens.
    print x

#This is where our program actually executes.
fib_sequence(do_math_until_this)