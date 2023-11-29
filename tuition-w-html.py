# Name: Arash Tajalli
# Prog Purpose: This program computes PVCC college tuition & fees 
# based on number of credits and outputs it into an html file
# PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# Define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Define global variables 
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

# html output addition
outfile = 'tuition-webpage.html'

######## define program functions ########
def main():
    open_outfile()
    more = True

    while more:
        get_user_data()
        perform_calculations()
        # display_results()
        display_results2()
        
        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            more = False
            f.write('</body></html>')    
            f.close()    

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE: enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Enter scholarship amount: "))

def perform_calculations():
    global total, balance, ituition, otuition, instition_fee, activity_fee, capital_fee
    ituition = RATE_TUITION_IN * numcredits
    otuition = RATE_TUITION_OUT * numcredits
    instition_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    capital_fee = RATE_CAPITAL_FEE * numcredits
    if inout == 1:
        total = ituition + instition_fee + activity_fee
        balance = scholarshipamt-(ituition + instition_fee + activity_fee)
    elif inout == 2:
        total = otuition + instition_fee + activity_fee + capital_fee
        balance = scholarshipamt-(otuition + instition_fee + activity_fee + capital_fee)


def open_outfile():
    global f
    f = open(outfile, 'a')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #33ADAD; background-image: url(wp-tuition.jpeg); color: #000000;">\n')
    

def display_results2():
    global f
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #FFADAD;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>PVCC TUITION</h2></td></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('*** PUBLIC INSTITUTION OF HIGHER EDUCATION ***\n')
    
    if inout == 2:
        f.write(tr + 'Out-of-State Tuition' + endtd + str(numcredits) + endtd + format(otuition,currency) + endtr)
    else:
        f.write(tr + 'In-State Tuition' + endtd + str(numcredits) + endtd + format(ituition,currency) + endtr)
    f.write(tr + 'Institution Fee ' + endtd + " " + endtd + format(instition_fee,currency) + endtr)
    f.write(tr + 'Activity Fee ' + endtd + " " + endtd + format(activity_fee,currency) + endtr)
    f.write(tr + 'Total Cost ' + endtd + " " + endtd +  format(total,currency)  + endtr)
    f.write(tr + 'Scholarship amount ' + endtd + " " + endtd +  format(scholarshipamt*-1,currency)  + endtr)
    f.write(tr + 'Balance ' + endtd + " " + endtd +  format((total - scholarshipamt),currency)  + endtr)
    f.write('<tr><td colspan= "3">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')


def display_results():
    line ='---------------------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** PIEDMONT VIRGINIA COMMUNITY COLLEGE ****')
    print(line)
    if inout == 1:
        print('Tuition Amount                   $ ' + format(ituition,moneyf))
    elif inout == 2:
        print('Tuition Amount                   $ ' + format(otuition,moneyf))
    print('Institution Fee                  $ ' + format(instition_fee,moneyf))
    print('Activity Fee                     $ ' + format(activity_fee,moneyf))
    if inout == 2:
        print('Capital Fee                      $ ' + format(capital_fee,moneyf))
    print('Total Cost                       $ ' + format(total,moneyf))
    print('Scholarship Amount               $ ' + format(scholarshipamt,moneyf))
    print('Balance                          $ ' + format(balance,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

main()