
from datetime import datetime
from getpass import getpass
import os


date = str(datetime.date(datetime.now()))
time = str(datetime.time(datetime.now()))


while True:
#while statement
    print("###############\n Main Menu - Life Logs and stuff\n###############")
    print("\nAre you a new user, returning, or want to exit? \n1) New \n2) Returning \n0) Exit\n")
    person = input()

    if person == "1": #Create New User
        name = input("Enter your First and Last name: ")
        create = input("Please create a username: ")
        path = "/home/covid2020/Desktop/Users/" + create + ".txt"
        #looks for user name.txt, if one matches, will return with "user already exists." otherwise, file will be created, see below
        while os.path.exists(path):
            create = input("Username already exists.\nPlease enter new Username: ")
            path = "/home/covid2020/Desktop/Users/" + create + ".txt"
        
        
        while True:
            passs = getpass(prompt = "Create a password: ") #asks to create password, getpass makes invisible text, checks for matching password to confirm
            password = getpass(prompt = "Retype password: ")
            if password == passs:
                
                break
            elif password != passs:
                print("Passwords dont match. Please try again \n")
            
        while True:    #asking for more personal info, must be character specific
            print ("Enter your birth month and day: ")
            mon = input("Month , use 3 lttrs (MMM): ")
            day = input("Day (DD): ")
            MMDD = len(mon + day)
            if MMDD > 5:
                print("Too many characters \n")
            elif MMDD == 5:
                break    
            
        MMDD = mon + "" + day
            
        security = input("\nFor security, enter a 4 digit pin: ") #more security, I want to use this for password security
        
        print("\n#################################\nCongrats. You've created a user account")
        print("Please check for correct information\n#################################")
        print("\nName: " + name + "\nUsername: " + create + "\nPassword: " + password +
            "\nBirthday: " + MMDD + "\nUser Pin: " + security)

        
        input("\nInformation saved. To log in as returning user click enter.")
        with open(path, "w") as file:
                file.write(create + " = Username"+ "\nPassword: " + password + 
                        "\nBirthday: " + mon + " " + day +
                        "\nUser Pin =  " + "P" + security +
                        "\nUser ~" + name + "~ created account on " + date) #the P is added to the user pin, for "extra" security, still working on the details


    if person == "2": #returning user
        user = input("\nEnter your Username(case sensitive): ")
        path = "/home/covid2020/Desktop/Users/" + user + ".txt" 
        if os.path.exists(path): #checks for if user.txt exists
 
            t = 0
            while t < 3: #if wrong password, will ask 3 times until fail
                pw = getpass(prompt = "Enter your password: ")
                temp = "Password: " + pw
                with open(path) as search: #searches user file for their created password
                    if temp in search.read():
                        welcum = open(path, "r")
                        
                        print("\nWelcome back " + welcum.read(7) + "\n") #reads the first line of the txt file, which contains the username
                        break
                    if temp not in search.read(): 
                        t += 1
                        print("Try Again!")
                        
                    if t == 3:
                        
                        print("\n############## \nToo Man Tries Dumb Dumb :P\n##############")
                        break
            #####
            while True: #Main screen asking user what they want to log
                blog = input("\nWhat would you like to log today?\n 1) Workouts \n 2)Money Manage \n 3)Regular Blog \n 0) Go Back/Log Out \n\n")
                
                
                
                if blog == "1": #WorkoutLog
                    print("***********Work Out Log*********")  
                    log = open(path, 'a')
                    t = 0
                    while t < 3:  
                        log = open(path, 'a')                       
                        work = input("\nType/Explain Your workout. Enter details. Example: 'I did X amount of push ups and ran X miles'\nDO NOT CLICK ENTER UNTIL YOU ARE FINISHED TYPING \n\n: ")
                        input("Click enter to log info")
                            
                        log.write("\n\n" + "***********Work Out Log*********\n" + time + "\nWorkout logged on " + date + "\n" + work) #writing info to file
                        log.close() #close to save info

                        more = input("Would you like to log more(Y/N)\n: ")
                        M = more.upper()
                        if M == "Y":
                                ...
                                    
                        if M == "N":
                                break
                                
                if blog == "2": #Money Manage
                    while True:
                        log = open(path, 'a')
                        print("***********Money Management Log*********")
                        pick = input("Do you want to enter your \n1)Paycheck Information \n2)Spending Information \n3)Go Back\n")
                        if pick == "1":
                            check1 = input("\nEnter date of last paycheck: ")
                            check2 = input("Enter the amount of the paycheck: ")
                            check3 = input("If you added savings, enter your savings: ")
                            check4 = input("If you want to add extra information, add here: ")
                            log.write("\n\n" + "***********Money Management Log - Payceck Info*********\n" + time + "\nPaycheck logged on " + date + "\nDate Paid: " + check1 +"\nPaycheck Amount: " + check2 +"\nSavings: " + check3 +"\nNotes: " + check4 ) #writing info to file
                            
                            log.close() #once file is closed, info is saved
                            input("\nPayceck information logged success! \nClick enter to coninue")     
                        
                        if pick == "2":
                            while True:
                                log = open(path, 'a')
                                amount = []
                                it = []
                                entry = int(input("\nHow many entries are you adding \nExample, if are adding your groceries, and you bought 200 items,\nyour entries will equal 200:::\n>>>> "))
                               except ValueError:
                                    if entry == '':
                                        leave = input("So I take it you don't want to be here? (y/n))
                                        if leave == y or leave == Y:
                                            break
                                        if leave == n or leave == N:
                                            Apologies = input("Really? Must have typed enter by accident. \nGuess you're gonna have to start over from the beginning.")
                                            break
                                        else:
                                            input('We only take numbers.')
                                for e in range(entry):
                                    item = input("Enter Item: ")
                                    amt = float(input("Enter Price(with decimals,no dollar sign needed): "))
                                        #amt2 = int(amt)
                                        #price = float(amt)
                                    it.append(item) #adds item to list for logging later
                                    amount.append(amt) #adds prices to list for later log/sum, see below
                                overall = sum(amount)
                                print("\nAmount spent is: $" + str(overall))
                                correct = input("Does information look correct? (Y/N): ")
                                c = correct.upper()
                                
                                if c == "Y":
                                    log = open(path, 'a')
                                    log.write("\n\n" + "***********Money Management Log - Spending*********\n" + time + "\nSpending logged on " + date)
                                    log.close() #loggs information
                                    
                                    log = open(path, 'a')
                                    log.write("\nItems Bought:") #logs the items with prices
                                    
                                    with log as new:
                                        for (x ,y) in zip(it, amount): #displays the item next to the price with zip from two lists
                                            new.write("\n{} {}\n".format(x,y))
                                    log = open(path, "a")
                                    log.write("Total: " + str(overall)) #adds total amount spent to the file
                                    log.close       
                                    input("Items Logged. Click enter to continue.")
                                    break
                                if c == "N":
                                        ... 
    
                        if pick == "3":
                            break                 
                    
                    
                    
                    
                if blog == "3": #Regula Blog
                    rblog = input("\nThis is a space to just write about anything you want. Have fun with it.\n Do not hit enter until you are finished typing.\n>>>>>")
                    rblog2 = input("\nYou have hit enter, if you want to exit, hit enter again.\nIf you want to type more, DO IT! (then hit enter): ")
                    input("\nClick enter to log info") 
                    log = open(path, 'a')
                    log.write("\n*******Daily Blog********\n" + rblog + "\n" + rblog2)  
                    log.close()                  
                    
                if blog == "0":
                    break
            
            
            
            
        else:
            input("Username does not exist. Click enter to continue")
            
    if person == "0":
        print("Wow... ok. Bye Then")
        break
