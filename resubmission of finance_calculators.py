import math

# Print the menu options for the user
print("You will be able to select either of the two calculations described below:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Allow the user to choose which calculation they want to do
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If the user selects 'investment':
if choice == "investment":
    print("You have chosen to calculate the interest on your investment. Please enter the information below:")

    # Ask the user to input principal amount (amount of money they are depositing)
    P = float(input("Please enter the amount of money you would like to deposit: "))

    # Ask the user to input the interest rate (as a percentage)
    r = float(input("Please enter the interest rate percentage. Please enter the VALUE ONLY without the percentage sign: ")) / 100

    # Ask the user to input the number of years they want to invest the money for
    t = float(input("Please enter the number of years you would like to invest your money for: "))

    # Ask the user to input if they want the calculation as simple interest or compound interest
    interest = input("Please state if you would like the interest to be calculated as simple or compound interest. Type 'simple' or 'compound': ").lower()

    # If they select simple interest, calculate and print the result
    if interest == "simple":
        A = P * (1 + r * t)
        print(A)

    # If they select compound interest, calculate and print the result
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print(A)

    # Else, print an error message for invalid input
    else:
        print("You have not entered a valid option. Please state if you would like the interest to be calculated as simple or compound interest. Type 'simple' or 'compound':")

# If the user selects 'bond':
elif choice == "bond":
    print("You have chosen to calculate the amount you will have to pay on a home loan. Please enter the information below:")

    # Ask the user to input the present value of the house
    P = float(input("Please enter the present value of the house: "))

    # Ask the user to input the interest rate
    i = float(input("Please enter the interest rate percentage. Please enter the VALUE ONLY without the percentage sign: ")) / 100 / 12

    # Ask the user to input the number of months over which they want to repay the bond
    n = float(input("Please enter the number of months you plan to take to repay the bond: "))

    # Calculate how much money the user would have to repay each month and print the result
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(repayment)

# Else, print an error message for invalid input
else:
    print("You have not entered a valid option. Please enter either 'investment' or 'bond' from the menu above to proceed.")
