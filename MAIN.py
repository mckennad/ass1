import database, sys


d = {} 

run = True;
while run:
#while program is set to run



    try:
        infile = open("DatabaseEx.txt","r")
    except IOError as err:
        errno, strerror = err.args
        print("I/O error({0}): {1}".format(errno, strerror))
        sys.exit()
        #detects open error and outputs error code and message
    except FileNotFoundError as err:
        errno, strerror = err.args
        print("FileNotFoundError error({0}): {1}".format(errno, strerror))
        sys.exit()
        #detects open error and outputs error code and message
    except NameError as err:
        errno, strerror = err.args
        print("NameError error({0}): {1}".format(errno, strerror))
        sys.exit()
        #detects open error and outputs error code and message

    
    
    for rec in infile:
        ID,rest = rec.split(":",1)
        d[ID] = rest
    infile.close()
    #moved this code inside while loop as 'd' needs to update every time user returns here

    choiceNeeded = True
    while choiceNeeded:
        try:
            choice = int(database.mainOptions())
        except ValueError:
            print("\nThat is not an option, please try again.")
            #catches whether input is a numeral
        else:
            choiceNeeded = False


    if int(choice) == 1:
        database.addNewEmployee(d)
    elif int(choice) == 2:
        database.searchForEmployee(d)
    elif int(choice) == 3:
        database.removeEmployee(d)
    elif int(choice) == 4:
        database.displayDatabase()
    elif int(choice) == 5:
        sys.exit()
        #ends program (QUIT)
    else:
        print("That is not an option, Please try again.")
        #if input is not a match, error occurs.  Unfortunately, this will lead to both notifications to appear when input is not a numeral, could set up while loop omn if checks and have it change boolean value depending on int check, but bah
