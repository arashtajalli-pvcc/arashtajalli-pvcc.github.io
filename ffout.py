# Your-name: Arash-Tajalli
# Prog Purpose

import datetime

########### LISTS of data ##########3
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

######## NEW LISTS for calculated amounts ########

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
net_pay = []
ret_pay = []

total_gross = 0
total_net = 0

############ TUPLES of constants ##########
#         C    S    J    M
# indexes 0    1    2    3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#          fed   state   ss   med   ret
# indexes   0      1     3     4     5
DED_RATE = (.12, .03, .062, .0145, .04)


######## define program functions ##########
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
    #calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

    #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soc = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]

    #STUDENTS: calculate other deductions and NET PAY here:

        net = pay - fed - state -soc - med- ret
    #add to totals
        total_gross += pay
        total_net += net

    #append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
    #STUDENTS: append other deductions and net pay here:
        soc_sec.append(soc)
        medicare.append(med)
        ret_pay.append(ret)
        net_pay.append(net)

def display_results():
    currency = '8,.2f'
    line = '---------------------------------------------'
    tab = "\t"

    print(line)
    print('**************FRESH FOODS MARKET*************')
    print('-------------- WEEKLY PAYROLL REPORT --------')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "  Emp Name" + tab + "  Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab +" Medicare" + tab + "Net"
    print(titles1 + titles2)

#STUDENTS: Create the missing code to print out employee data, one line at a time
    for i in range(num_emps):
        data1 = emp[i] + "   " + job[i] + format(gross_pay[i], currency) + "      " +format(fed_tax[i],currency) + "      " + format(state_tax[i],currency) + "      " + format(soc_sec[i],currency) + format(medicare[i],currency) + "      " +format(net_pay[i],currency)
        print(data1)
    print(line)
    print("(***************** TOTAL GROSS: $" +format (total_gross, '10,.2f'))
    print("(***************** TOTAL NET  : $" +format (total_net, '10,.2f'))
    print(line)

def create_output_file():
    currency = '8,.2f'
    line = '\n----------------------------------------------'
    tab = "\t"

    ################# output file ###################
    out_file = "payroll.txt"
    f = open(out_file, "a")  
    f.write(line)
    f.write('\n********* FRESH FOODS MARKET ************')
    f.write('\n********* WEEKLY PAYROLL REPORT ************')
    f.write('\n'+tab + str(datetime.datetime.now()))
    f.write(line)
    titles1 = "\nEmp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" +tab +"Medicare" +tab + "Net"
    f.write(titles1 + titles2)

#STUDENTS: Create the missing code to f.write out employee data, one line at a time
    for i in range(num_emps):
        data1 = "\n" + emp[i] + " " + job[i] + format(gross_pay[i], currency)
        f.write(data1)
    f.write(line)
    f.write("\n********************* TOTAL GROSS: $" + format(total_gross, currency))
    f.write("\n********************* TOTAL NET: $" + format(total_net, currency))
    f.write(line)
    f.close()
    print("Open " +out_file + " to view your report.")

############# call on main program to execute ##########
main()