import sys

#Solving some basic math problems in python

def main():
    #Check if the correct number of arguments were provided
    if len(sys.argv) !=3:
        print("Usage: python math-problems.py <integer1> <integer2>")
        sys.exit(1) #Exit the program indicating an error

    try:
        #Convert command line arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("You should provide two integers")
        sys.exit(1) #Exit the program indicating an error

    #Addition
    addition_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {addition_result}")

    #Multiplication
    multiplication_result = num1 * num2
    print(f"The product of {num1} and {num2} is {multiplication_result}")

    #Division
    if num2 !=0:
        division_result = num1 / num2
        print(f"The division of {num1} and {num2} is {division_result}")
    else:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    main()