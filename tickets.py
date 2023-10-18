# Name: Arash-Tajalli
# Prog Purpose: This program finds the costt of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%
#   Price for a drink: $4.99
#   Price for a bag of Popcorn: $8.99

import datetime

######### define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99
PR_POPCORN = 8.99
PR_DRINK = 4.99

# define global variables
num_tickets = 0
tick_sales = 0
num_popcorn = 0
num_drink = 0
drink_sales = 0
ticket_cost = 0
subtotal = 0
sales_tax  = 0
total = 0

######### define program functions ##########
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()
        retry()
        

def retry():
    askAgain = input("\nWould you like to order again (Y or N)?: ")
    if askAgain.upper() == "N" or askAgain == "n":
        print("Thank you for your order. Enjoy your movie! ")
        exit()
    elif askAgain.upper() == "Y" or askAgain == "y":
        main()
    else:
        print("you'll have to put in a Y or N character please\n")
        retry()

def get_user_data():
    global num_tickets, num_popcorn, num_drink
    num_tickets = int(input("Number of movie tickets: "))
    num_popcorn = int(input("How many bags of popcorn would you like?: "))
    num_drink = int(input("How many drinks would you like?: "))

def perform_calculations():
    global subtotal, sales_tax, total, ticket_cost, num_popcorn, tick_sales, num_drink, drink_sales
    tick_sales = num_tickets*PR_TICKET
    drink_sales = num_drink*PR_DRINK
    subtotal = (num_tickets * PR_TICKET)+(num_popcorn * PR_POPCORN)+(num_drink*PR_DRINK)
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyformat = '12,.2f'
    print('---------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('---------------------------------')
    print('Tickets  $   '+ str(num_tickets) + format(num_tickets*PR_TICKET, moneyformat))
    print('Popcorn $    '+ str(num_popcorn) + format(num_popcorn*PR_POPCORN,moneyformat))
    print('Drinks $     '+ str(num_drink) + format(drink_sales, moneyformat))
    print('Subtotal $     '+ format(subtotal, moneyformat))
    print('Sales Tax  $   ' + format(sales_tax, moneyformat))
    print('Total    $     ' + format(total, moneyformat))
    print('---------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ###############
main()