# Name: Arash-Tajalli, Danilo-Meraz
# Prog Purpose: Branch Barbeque Buffet Transactions
# Price for adults: $19.95
# Price for children: $11.95
# Service fee rate: 10% == int(0.10)
# Sales tax rate: 6.2% == int(0.062)
import datetime

######### define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = 0.062
SERVICE_FEE_RATE = 0.10
PR_ADULT = 19.95
PR_CHILD = 11.95

# define global variables
num_adult_bbq = 0
ad_sale = 0
num_child_bbq = 0
ch_sale = 0
subtotal = 0
service_fee = 0
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
        print("Thank you for your order. Enjoy your food! ")
        exit()
    elif askAgain.upper() == "Y" or askAgain == "y":
        main()
    else:
        print("you'll have to put in a Y or N character please\n")
        retry()

def get_user_data():
    global num_adult_bbq, num_child_bbq
    print("Welcome to the Branch Barbeque Cafe™! Please let me know how many bodies are entering the establishment today! ")
    num_adult_bbq = int(input("Number of Adults?: "))
    print("Any children as well?: ")
    num_child_bbq = int(input("Number of Childeren?: "))

def perform_calculations():
    global subtotal, total, sales_tax, SALES_TAX_RATE, num_adult_bbq, num_child_bbq, ad_sale, ch_sale, service_fee
    ad_sale= num_adult_bbq*PR_ADULT
    ch_sale= num_child_bbq*PR_CHILD
    subtotal = (ad_sale)+(ch_sale)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE_RATE
    total = subtotal + sales_tax + service_fee

def display_results():
    moneyformat = '12,.2f'
    print('---------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('---------------------------------')
    print("ITEM         Number      $$")
    print('Adults       '+ str(num_adult_bbq) + format(ad_sale, moneyformat))
    print('Children     '+ str(num_child_bbq) + format(ch_sale, moneyformat))
    print('Subtotal       '+ format(+subtotal, moneyformat))
    print('Service fee    '+ format(service_fee, moneyformat))
    print('Sales Tax      ' + format(sales_tax, moneyformat))
    print('Total          ' + format(total, moneyformat))
    print('---------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ###############
main()