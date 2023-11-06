# Authored by: Arash Tajalli && Lewis Fassero
# Prog_purpose: print receipt for pizzas ordered

import datetime

###GLOBAL
SALES_TAX = .055
PR_PIZZA_XL = 21.99
PR_PIZZA_L = 17.99
PR_PIZZA_M = 12.99
PR_PIZZA_SM = 9.99

PR_DRINKS = 3.99

PR_BR_STICKS = 6.99

def main():
    get_user_data()
    order_calcs()
    display_results()

def get_user_data():
    global pizza_size, num_pizza, num_drinks, num_br_sticks
    print("\t\n1.Small \t\n2.Medium \t\n3.Large \t\n4.X-Large")
    pizza_size = int(input("What size pizza would you like? "))
    num_pizza = int(input("How many of those pizzas would you like? "))
    num_drinks = int(input("How many drinks would you like? "))
    num_br_sticks = int(input("How many orders of breadsticks would you like? "))
    

def order_calcs():
    global pizza_total, subtotal, drinks_total, br_sticks_total
    if pizza_size == 1:
        pizza_total = num_pizza * PR_PIZZA_SM
    elif pizza_size == 2:
        pizza_total = num_pizza * PR_PIZZA_M
    elif pizza_size == 3:
        pizza_total = num_pizza * PR_PIZZA_L
    else :
        pizza_total = num_pizza * PR_PIZZA_XL
    drinks_total = PR_DRINKS * num_drinks
    br_sticks_total = PR_BR_STICKS * num_br_sticks
    subtotal = br_sticks_total + drinks_total + pizza_total


def display_results():
    moneyformat = '8,.2f'
    print('---------------------------------')
    print('**** Palermo Pizza ****')
    print('---------------------------------')
    print("ITEM         Number    $$")
    print('Pizza           '+ str(num_pizza) + str('$  ')+format(pizza_total, moneyformat))
    print('breadsticks     '+ str(num_br_sticks) + str('$  ')+format(br_sticks_total, moneyformat))
    print('Drinks          '+ str(num_drinks) + str('$  ')+format(drinks_total, moneyformat))
    print('Subtotal         $  '+ format(subtotal, moneyformat))
    print('Sales Tax        $  ' + format(SALES_TAX*subtotal, moneyformat))
    print('Total            $  ' + format(subtotal*(1+SALES_TAX), moneyformat))
    print('---------------------------------')
    print(str(datetime.datetime.now()))


#### execution ####
main()