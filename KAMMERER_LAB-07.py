#!/usr/bin/env python
# coding: utf-8

# In[6]:


# ONE
#
#
# Create a program that allows the user to input two digits. 
# So the only valid number are those from 10 to 99.
#    1. Uses a while loop to create a process that will be repeated over and over until 
#       the user input a valid number.
#    2. If the user inputs a valid number, the program will generate a message that says, 
#       ‘The number [display the number] is valid.’ Be sure that the program will stop after this by 
#       using a break statement.
#    3. If the number is invalid, the program will generate a message that says, ‘The number [display 
#       the number] is valid. Please follow the instructions and write a two-digits number.’ Also, the 
#       program will allow inputting a new number and will repeat the process.
#    4. The program only will stop if a valid number is entered.


def number_validator():
    user_number= None
    while (user_number not in range(10, 99)):
        user_number = int(input("\nPlease enter a two digit number (10-99): "))
        if user_number in range(10, 99):
            print(F"\tThe number {user_number} is valid.")
            break
        else:
            print(F"\n\tThe number {user_number} is invalid.")


number_validator()


# In[29]:


# TWO
#
#
# Write a program that calculates the years a person would have to
#     wait to make their initial investment of $10,000 to duplicate 
#     just by receiving the interest of the investing account. We 
#     know the interest is 7% annually, but we will calculate the 
#     interest rate at 5% to discount taxes.
#
# The interest gained during the year will be added to the initial
#     investment. You need to calculate the interest every year with
#     the updated investment.
#
#     1. Create 5 variables, rate, initial_balance, balance, 
#        target, and year.
#     2. Use a while loop to repeat the process of calculating the
#        new balance.
#     3. Use the variable year as a counter to keep track of the
#        number of years that passes every time the while loop
#        goes over the sequence.
#     4. Print a message that uses the variable year to inform how
#        many years should pass to duplicate the initial among at 
#        the given interest rate.


def yearly_interest():    
    
    interest_rate = 0.05
    principal = 10000
    balance = principal
    year = 1
    n = 1
    target = int(input("Input a valid target: "))

    # main loop
    while (int(target) >= balance):
        # compound interest formula
        balance = principal*((1+(interest_rate/n))**(n*year))
        year = year + 1
    
    print(F"\nIt will take {year} years for an interest rate of \
{'{:.2%}'.format(interest_rate)} to turn {'${:,.2f}'.format(principal)}\
 into {'${:,.2f}'.format(target)}.")
    
    
yearly_interest()
    


# In[51]:


# THREE
#
#
# Write a program that calculates the months a person would have 
#     to wait to save $60,000.
#
# Their initial savings of $10,000, but the person will save 
#     $2,000 every month to meet the goal.
#
# The money is in an investing account with an annual rate of 7%.
#     We will calculate the interest rate at 5% to discount taxes.
#
# The interest gained during the month will be added to the 
#     initial investment. You need to calculate the interest every
#     year with the updated investment.
#
# It is a similar problem to exercise TWO, but now you are 
#     handling months, and the balance will be increased with 
#     the monthly savings.
#
# Print a message that uses the variable month to inform how many
#     months should pass to achieve the savings goal.

def monthly_interest():
    monthly_savings = 2000
    interest_rate = 0.05
    principal = 10000
    balance = principal
    year = 1
    n = 1
    target = 60000

    # main loop
    while (int(target) >= balance):
        # compound interest formula
        balance = monthly_savings+principal*((1+(interest_rate/n))**(n*year))
        year = year + 1
    
    month = year*12
    print(F"\nIt will take {round(month)} months ({year} years) for an interest\
 rate of {'{:.0%}'.format(interest_rate)} to turn {'${:,.2f}'.format(principal)}\
 into {'${:,.2f}'.format(target)}, with a monthly savings of {'${:,.2f}'.format(monthly_savings)}.")
    
monthly_interest()

