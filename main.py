# DSC510
# Week 5
# Programming Assignment - 5.1
# Author: Joseph Madden
# Date: 09/27/2022
# The purpose of this program is to perform different math operating using loops and functions.

base_cost = 0.87
# declare and initialize a variable for calculated_cost to remove the undefined error
calculated_cost = 0
print("Welcome to my Basic Calculator - the fiber optic cable installation company")
name = input("What is your name: \n")
print('')
print('Hi', name, 'I am happy to help you!')
#function to calculate addition, subtraction, multiplication and division
def perform_calculation('num'):
try:
    value1 = float(input('Please enter first number:\n'))
    value2 = float(input('Please enter second number:\n'))
    if 'num' == 1:
        calc = value1 + value2
        print("Addition of given numbers", value1, "&", value2, "is :", calculated_cost)
    elif 'num' == 2:
        calc = value1 - value2
        print("Subtraction of given numbers", value1, "&", value2, "is :", calculated_cost)
    elif 'num' == 3:
        calc = value1 * value2
        print("multiplication of given numbers", value1,  "&", value2, "is :", calculated_cost)
    elif 'num' == 4:
        if value2 != 0:
            calc = round(value1 / value2, 2)
            print("Division of given numbers", value1, "&", value2, "is :", calculated_cost)
        else:
            print('Please provide second non-zero number')
except Exception as ex:
    print('Error occurred: ', ex)

    #function to calculate average of given numbers
    def calculate_average():
        try:
            max_value = int(input('How many numbers you wish to enter\n'))
            count = 0
            total = 0
            if max_value > 0:
                for value in range(max_value):
                    print('Please enter number', value + 1, ":")
                    number = float(input())
                    count = count + 1
                    total = total + number
                    print('Average of given numbers is: ', round(total / count, 2))
                else:
                    print('Please enter valid non-zero number')
        except 'exception' as 'ex':
            print('Error occurred: ', ex)

#main section of program where user input asked for math operations

    user_input = 'Yes'
    try:
        while user_input = input("Would like to perorm math operations? enter Yes or No\n")
        if user_input.lower() == 'Yes':
            user_choice = int(input(
                'Please enter the appropriate number 1:Addition, 2:Subtraction, 3:Multiplication, 4:Division, 5:Average\n'))
            if user_choice in [1, 2, 3, 4]:
               perform_calculation('choice')
            elif user_choice == 5:
                calculate_average()
            else:
                print('Please enter valid number from given options')
            'else_keyword'
            print('Thank you!')
    except Exception as ex:
        print('Error occurred: ', ex)

