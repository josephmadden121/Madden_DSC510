# DSC510
# Week 4
# Programming Assignment - 4.1
# Author: Joseph Madden
# Date: 09/20/2022
# The purpose of this program is to create function to calculate the cable installation cost.

# declare the variable for base cost
base_cost = 0.87
print("Welcome to the OPTIMA - the fiber optic cable installation company")  # welcome message
company_name = input("Please tell us your company name: \n")  # save the company name given by user
try:
    cable_length = float(input("Now tell us length of cable to be installed in feet: \n"))  # save the cable length
    total_cost = round(base_cost * cable_length, 2)  # round the total cost to 2 digits

    # function to calculate the cost of cable based on cable length and discounted cost.
    def cost_calculator(cable_len, 'cst'):
        final_cost = round(cost*cable_len, 2)
        return final_cost

    if 100 < cable_length <= 250:
        cost = 0.80
        calculated_cost = cost_calculator(cable_length, 'cst')
    elif 250 < cable_length <= 500:
        cost = 0.70
        calculated_cost = cost_calculator(cable_length, 'cst')
    elif cable_length > 500:
        cost = 0.50
        calculated_cost = cost_calculator(cable_length, 'cst')
    elif 0 < cable_length <= 100:
        cost = base_cost
        calculated_cost = cost_calculator(cable_length, 'cst')
    else:
        print("\nPlease provide non-zero cable length to calculate the cost")
    # Create Receipt with all the details on it
    print("\nThe Receipt for fiber optic cable installation cost:")
    print("Company Name: ", company_name)
    print("Length of cable to be installed: ", cable_length, "ft")
    if cable_length > 100:
        print("Total Cost: $", total_cost)
        print("Final Cost: $",calculated_cost, "Discount given since length of cable is more than 100ft")
    elif 0 < cable_length <= 100:
        print("Total Cost: $", total_cost)
        print("Final Cost: $",calculated_cost, "No discount provided since cable length is less than or equal to 100ft")
    print("Our Discounts are based on length of cable:\nup to 100ft: No Discount \n101ft-250ft: $0.80/ft \n251ft-500ft: $0.70/ft \n501ft & More: $0.50/ft")
    print("\nThank you from OPTIMA")
except ValueError as error:
    print("Please provide valid cable length in feet")
    print("Error Received: ", error)
except Exception as e:
    print("Error Received: ", e)