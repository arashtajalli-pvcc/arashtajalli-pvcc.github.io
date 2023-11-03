# NAME: Arash-Tajalli
# PROG Purpose: This program finds the cost of pet vaccinse & memdications for dogs and cats
# 
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
# 
# PET CARE MEDS PRICING
# ----------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAP  $35.00
#   3. Influenza $48.00
#   4. Leptospirosis    $21.00
#   5. Lyme Disease $41.00
#   6. Rabies   $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, Up to 25 ibs: $9.99
#   Medium-sized dogs, 26 to 50 ibs: $11.99
#   Large dogs, 51 to 100 ibs: $13.99

import datetime

############ define Global Variables #################
#define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define global variables

############### define program functions ##############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "0":
            get_dog_data()
            perform_dog_calculations
            display_dog_results
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y/N)? ")
        if askAgain.upper() == "N":
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet Name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? ")
    pet_weight = input("Weight of your pet (in pounds): ")

######### DOG FUNCTIONS ##############

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog_Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Influenza \n\t6.Lyme Disease \n\t7.Rabies \n\t8.Full Vaccine Package \n\t9.NONE"
    dogmenu = dog1 + dog2
    pet_vax = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention is recommended for all dogs.")
    heart_yesno = input("would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global vax_cost, chews_cost, total
    #### vaccines

    if pet_vax_type == 1:
        vax_cost = PR_BORD

    elif pet_vax_type == 2:
        vax_cost = PR_DAPP
    
    elif pet_vax_type == 3:
        vax_cost = PR_FLU

    else:
        PR_ALL = PR_BORD +PR_DAPP + PR_FLU
        vax_cost = 0.85 * PR_ALL

    ###### Heart worm chews
    if num_chews != 0:
        if pet_weight <25:
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 & pet_weight <50:
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE
    ###### find total
    total = vax_cost + chews_cost
    print("DOG CALCS")

def display_dog_results():
    print("DISPLAY DOGS")

############# CAT functions ############
def get_cat_data():
    print("CAT DATA")

def perform_cat_calculations():
    print("CAT CALCS")

def display_cat_results():
    print("DISPLAY CATS")