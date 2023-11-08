# Authored by: Arash Tajalli
# Prog_purpose: print receipt for pizzas ordered

import datetime

# eligible for relief? PPTR
# used for personal use? has relief (no license fee) also tax relief == 33% so 0.33
# license fee if used for business

# tax rate $4.20 per $100.00 so 4.20% -> .0420 per year so div tax by 2

###### GLOBAL ####
TAX_RATE = 0.0420
TAX_RE_RATE = 0.33

def main():
    get_user_data()
    calc_data()
    display_tax_bill()
    retry()

def get_user_data():
    global ass_val, el_relief
    ass_val = int(input("\nWhat is the assessed value of the vehicle? $"))
    askAgain = input("\nIs it eligible for tax relief? (i.e. is it used for a business or not?): ")
    if askAgain.upper() == "N" or askAgain == "n":
        el_relief = 0
    elif askAgain.upper() == "Y" or askAgain == "y":
        el_relief = 1
    else:
        print("you'll have to put in a Y or N character please\n")
        get_user_data()

def calc_data():
    global tax_amount, tax_relief, total_due
    tax_relief = 0
    tax_amount = (ass_val * TAX_RATE)/2
    if el_relief == 1:
        tax_relief = tax_amount * TAX_RE_RATE
    total_due = tax_amount - tax_relief

def display_tax_bill():
    moneyformat = '8,.2f'
    pr_pos =  0
    loop_cond = False
    text_display = ["Vehicle Assessed Value","Full Annual Tax Amount", "Relief Amount", "Total Amount Due" ]
    munnie_display = [ass_val, tax_amount, tax_relief, total_due]
    print('-------------------------------------------------------')
    print('**** Charlottesville Personal Property Tax 6 Months ****')
    print('-------------------------------------------------------')
    while loop_cond == False:
        print(text_display[pr_pos])
        print("  " + format(munnie_display[pr_pos],moneyformat) + "\n")
        pr_pos +=1
        if pr_pos == 4:
            loop_cond = True
    print('-----------------------------------------------')
    print(str(datetime.datetime.now()))

def retry():
    askAgain = input("\nDid you need to check any other personal property assessments? ")
    if askAgain.upper() == "N" or askAgain == "n":
        print("\nThanks for checking in!")
        exit()  
    elif askAgain.upper() == "Y" or askAgain == "y":
        main()
    else:
        print("you'll have to put in a Y or N character please\n")
        retry()

main()