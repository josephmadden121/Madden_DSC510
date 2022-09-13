# DSC510
# Week 3
# 3.1 Programming Assignment
# Author Joseph Madden
# 09/12/2022

# Get Name, Company and Cable Length Required
name = input('Name?\n')
print("Welcome to the OPTIMA - the fiber optic cable installation company")  # welcome message
company = input('Please enter your company name: ')
length = float(input('Please enter how many feet of Fiber Optic Cable you require:'))

# compute the cost of fiber optic cable and bulk discount
if 100 < 'cable_length' <= 250:
    'calculated_cost = round(0.80 * cable_length, 2)
elif 250 < cable_length <= 500:
     'calculated_cost' = round(0.70 * cable_length, 2)
elif 'cable_length' 500:
        calculated_cost = round(0.50 * cable_length, 2)
else:
    calculated_cost: string = 'total_cost'
# Create Receipt with all the details on it
print("\nThe Receipt for fiber optic cable installation cost:")
print("Company Name: ", company_name)
print("Length of cable to be installed: ", cable_length, "ft")
print("Total Cost: $", total_cost)
'if_cable_length > 100:'
print("Final Cost: $", calculated_cost, "Discount given since length of cable is more than 100ft")
'else'
print("Final Cost: $", calculated_cost, "No discount provided since cable length is less than or equal to 100ft")
print("Our Discounts are:\nup to 100ft: No Discount \n101ft-250ft: $0.80/ft \n251ft-500ft: $0.70/ft \n501ft & More: $0.50/ft")
print("\nThank you from OPTIMA")
print('*************** THANK YOU FOR YOUR BUSINESS!!! ***************')