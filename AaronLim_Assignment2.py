#Done by: Aaron Lim
#Mod: CSIT110
#student ID(UOW): 5985171
#Date: 15/10/2018

import csv

def menu():
    #variable to exit the loop
    #true to continue the loop (when user keyed in any integer)
    #false to exit the loop (when user keyed in 0)
    ok = True
    while(ok == True):    
        print("===============================================")
        print("1: Display modules average scores")
        print("2: Display modules top scorer")
        print("0: Exit")
        choice = int(input("Enter choice: "))
        if (choice == 1 or choice == 2 or choice == 0):
            ok = False
        else:
            print("===============================================")
            print("Invalid choice, please enter again")   
    #returning the int
    return choice

def display_modules_average_scores():
    filePath = "data.csv"
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        #variables
        CSIT110 = 0
        CSIT121 = 0
        CSIT135 = 0
        CSIT142 = 0
        count = 0
        mod1 = 'CSIT110'
        mod2 = 'CSIT121'
        mod3 = 'CSIT135'
        mod4 = 'CSIT142'
        #sum the modules
        for row in reader:
            CSIT110 += int(row[mod1])
            CSIT121 += int(row[mod2])
            CSIT135 += int(row[mod3])
            CSIT142 += int(row[mod4])
            count += 1
        #division the modules and round to 2 decimal place
        CSIT110 = round((CSIT110 / count),2)
        CSIT121 = round((CSIT121 / count),2)
        CSIT135 = round((CSIT135 / count),2)
        CSIT142 = round((CSIT142 / count),2)
        #printing it out
        print("===============================================")
        print("Display Modules Average Scores")
        print("===============================================")
        print("{0:^8}|{1:^9}|{2:^9}|{3:^9}".format(mod1,mod2,mod3,mod4))
        print("{0:^8}|{1:^9}|{2:^9}|{3:^9}".format(CSIT110,CSIT121,CSIT135,CSIT142))        

def display_modules_top_scorer():
    #variables
    mod1 = 'CSIT110'
    mod2 = 'CSIT121'
    mod3 = 'CSIT135'
    mod4 = 'CSIT142' 
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0     
    fName = 'first_name'
    lName = 'last_name'
    filePath = "data.csv"
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)    
        #getting the maximum value
        for row in reader:
            if(max1 < int(row[mod1])):
                max1 = int(row[mod1])
            if(max2 < int(row[mod2])):
                max2 = int(row[mod2])
            if(max3 < int(row[mod3])):
                max3 = int(row[mod3])
            if(max4 < int(row[mod4])):
                max4 = int(row[mod4])
        #printing out 1st line
        print('===============================================')
        print('Display modules top scorer')
        print('===============================================')
        print('{0:<8}|{1:^12}|{2:^10}'.format('module', 'First Name', 'Last Name'))
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)  
        #getting max value for module 1 and printing it out
        for row in reader:
            if(max1 == int(row[mod1])):
                print('{0:<8}|{1:>11} | {2:<9}'.format(mod1, row[fName], row[lName])) 
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)  
        #getting max value for module 2 and printing it out
        for row in reader:    
            if(max2 == int(row[mod2])):
                print('{0:<8}|{1:>11} | {2:<9}'.format(mod2, row[fName], row[lName]))  
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)  
        #getting max value for module 3 and printing it out
        for row in reader:    
            if(max3 == int(row[mod3])):
                print('{0:<8}|{1:>11} | {2:<9}'.format(mod3, row[fName], row[lName]))  
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)  
        #getting max value for module 4 and printing it out
        for row in reader:        
            if(max4 == int(row[mod4])):
                print('{0:<8}|{1:>11} | {2:<9}'.format(mod4, row['first_name'], row['last_name']))  

def main():
    #boolean, to exit the loop user key in 0, to continue key in any integer
    ok = True
    while(ok == True):
        choice = menu()
        if(choice == 1):
            display_modules_average_scores()
        elif(choice == 2):
            display_modules_top_scorer()
        elif(choice == 0):
            ok = False
    print("===============================================")
    print("Thank you for using Students' Result System")
    print("===============================================")
    
#main function
main()