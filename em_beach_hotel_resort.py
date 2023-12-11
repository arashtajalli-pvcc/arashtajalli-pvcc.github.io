# Emerald_Beach_Hotel_&_Resort
# Your-Name: Arash Tajalli
# Prog purpose: Create a calculation on hotel guest costs based on room type, 
# number of nights, and sales/occupancy tax rates from a CSV file and 
# output the results to a web page sales report 

import datetime

# HTML output addition
outfile = "emerald-web-page.html"

# Variables
cust =[]
cust_fin = []
room_tuple = ("SR","DR","SU")
room_prices = (195,250,350)
#"Sales_tax", "Occupancy_tax"
tax_int = (0.065,0.1125)

def main():
    read_in_em_csv()
    # display_cust_list()
    calc_list()
    open_out_file()
    create_output_html()

def read_in_em_csv():
    global cust
    cust_data = open("emerald.csv", "r")
    cust_in = cust_data.readlines() #read the entire file inco cust_in
    cust_data.close()

    #split the data into fields
    for i in cust_in: #separate the data by commas and add to the list
        cust.append(i.split(","))


def display_cust_list():
    line = "---------------------------------"

    print(line)
    print("**** CUSTOMER SALES REPORT *******")
    for i in range(len(cust)):
        for p in range(len(cust[i])):
            print("\t")
            print(str(cust[i][p]))
        print(line)

def calc_list():
    global grandtotal
    grandtotal =0

    for i in range(len(cust)):
        room_type = str(cust[i][2])
        num_nights = int(cust[i][3])
        if room_type ==room_tuple[0]:
            subtotal = room_prices[0] * num_nights
        elif room_type ==room_tuple[1]:
            subtotal = room_prices[1]*num_nights
        else:
            subtotal = room_prices[2]*num_nights

        salestax  = subtotal * tax_int[0]
        occupancy = subtotal * tax_int[1]
        total     = subtotal + salestax + occupancy
             
        grandtotal += total

        cust[i].append(subtotal)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #33ADAD; background-image: url(wp_em_beach.jpg); color: #000000;">\n' )

def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    endtd = '</td><td>'

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    f.write('\n<table border="3"   style ="background-color: #34cb75;  font-family: Georgia; margin: auto;">\n')
    f.write('<tr><td colspan = 7>\n')
    f.write('<h2>Emerald Beach Hotel and Resort</h2></td></tr>')
    f.write('<tr><td colspan = 7>\n')
    f.write('Sales Report Date/Time:' +today +'</td>')
    
    f.write(tr + 'Last' + td + "First" + td + "Num Nights" +td + "Subtotal" + td + "Sales Tax" + td+ "Occ. Tax" +td +"Total" + endtr)
    for i in range(len(cust)):
        f.write(tr + cust[i][0] + td + cust[i][1] + td + cust[i][3] +td + "$" + format(cust[i][4],currency) + td + "$" + format((cust[i][4]*tax_int[0]),currency) + td + "$" + format((cust[i][4]*tax_int[1]),currency) +td + "$" + format(cust[i][4]+((cust[i][4]*tax_int[0])+(cust[i][4]*tax_int[1])),currency) + endtr)
    f.write("<tr><td colspan = 3>\n" "GRAND TOTAL:" + "</td><td colspan =4>\n" + "$" + format(grandtotal,currency) + endtd)
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')


main()

