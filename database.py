






def mainOptions():
    print("\nEmployee FMS \n \n Select one of the following \n \n    1) Add a new employee \n    2) Search for an employee \n    3) Remove an employee from FMS \n    4) Display entire employee FMS \n    5) Quit \n")
#Opening option list (option 5 was forgotten on assignment sheet)

    line = input()

    return line




def checkForEmployee(dic,empID):
#checks to see if employeeID already exists and returns a boolean value

    for ID in dic:
        if ID == empID:
            return True
            #returns true if empID already exists

    return False
    #returns false value if empID not found in database




def addNewEmployee(dic):
#Gathers info, calls searchForEmployee, if EmpID doesn't exist, adds new employee and asks to do it again

    print("\nPlease enter ID number")
    a = input()



    if (len(a) != 4):
    #checks to see if ID is proper length
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        addResponse = input()
        if addResponse == 'y':
            addNewEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return

    try:
        a = int(a)
        #checks to see if input is made of numerals
    except ValueError:
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        addResponse = input()
        if addResponse == 'y':
            addNewEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return


    if checkForEmployee(dic,a) == True:
    #checks to see if ID already exists
        print("Employee ID already exists \n Enter 'y' to try again")
        #if ID already exists, asks user if they want to try again
        addResponse = input()
        if addResponse == 'y':
            addNewEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return

    fNameNeeded = True
    while fNameNeeded:
        print("Please enter first name")
        b = input()
        if b.isalpha():
            fNameNeed = False
            
            
    lNameNeeded = True
    while lNameNeeded:    
        print("Please enter last name")
        c = input()
        if c.isalpha():
            lNameNeed = False


    deptNeeded = True
    while deptNeeded:
        print("Please enter dept")
        d = input()
        if d.isalpha():
            deptNeeded = False


    newLine = [a,":",b,":",c,":",d]

    infile = open("DatabaseEx.txt","a")
    infile.writelines(newLine)
    infile.write("\n")
    infile.close()
    #appends newLine to textfile


    dic = {}
    infile = open("DatabaseEx.txt","r")
    for rec in infile:
        ID,rest = rec.split(":",1)
        dic[ID] = rest
    infile.close()
    #updates dic in the case that user wants to add another employee


    print("\nEmployee has been added \n Enter 'y' to add another")
        #Confirms addition and if user wants to add another
    addResponse = input()
    if addResponse == 'y':
        addNewEmployee(dic)
        #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
        return
        #ends adding once done
    else:
        return



def searchForEmployee(dic):
#checks for employee and if found, display details

    print("\nPlease enter ID number")
    a = input()




    if (len(a) != 4):
    #checks to see if ID is proper length
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        searchForResponse = input()
        if searchForResponse == 'y':
            searchForEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return

    try:
        a = int(a)
        #checks to see if input is made of numerals
    except ValueError:
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        searchForResponse = input()
        if searchForResponse == 'y':
            searchForEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return




    if checkForEmployee(dic,a) == False:
    #checks to see if ID already exists
        print("Employee ID does not exist \n Enter 'y' to try again")
        #if ID doesn't exist, asks user if they want to try again
        searchForResponse = input()
        if searchForResponse == 'y':
            searchForEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends
        else:
            return



    for ID in dic:
        if ID == a:
            #print(dic[ID].split(":"))      prints in different format
            for key in dic[ID].split(":"):
                print(key)
                #displays tuples by line (doesn't reprint 'a' or EmployeeID).  Instructions do not mention formatting rules




    print("\nEnter 'y' to display another employee")        
    searchForResponse = input()
    if searchForResponse == 'y':
        searchForEmployee(dic)
        #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
        return
        #ends
    else:
        return


def removeEmployee(dic):
#checks for employee and if found removes it from text file
    
    print("\nPlease enter ID number")
    a = input()




    if (len(a) != 4):
    #checks to see if ID is proper length
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        removeResponse = input()
        if removeResponse == 'y':
            removeEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return


    try:
        a = int(a)
        #checks to see if input is made of numerals
    except ValueError:
        print("ID number must be 4 numbers long.  Enter 'y' to try again?")
        removeResponse = input()
        if removeResponse == 'y':
            removeEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends adding once done
        else:
            return




    if checkForEmployee(dic,a) == False:
    #checks to see if ID already exists
        print("Employee ID does not exist \n Enter 'y' to try again")
        #if ID doesn't exist, asks user if they want to try again
        removeResponse = input()
        if removeResponse == 'y':
            removeEmployee(dic)
            #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
            return
            #ends
        else:
            return




    infile = open("DatabaseEx.txt","w")

    for ID in dic:
        if ID != a:
            newLine = [ID,":",dic[ID]]
            infile.writelines(newLine)

    infile.close()
    #opens up text file, and writes over it (except the line with the matching empID)
    

    dic = {}
    infile = open("DatabaseEx.txt","r")
    for rec in infile:
        ID,rest = rec.split(":",1)
        dic[ID] = rest
    infile.close()
    #updates dic in the case that user wants to remove another employee


    print("\nEmployee has been removed \n Enter 'y' to try again")
    removeResponse = input()
    if removeResponse == 'y':
        removeEmployee(dic)
        #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
        return
        #ends
    else:
        return



def displayDatabase():

    print("\n")
    #just for spacing

    infile = open("DatabaseEx.txt","r")
    
    for line in infile:
        print (line, end="")
        #prints text file line by line

    print("\nEnter 'y' to display again")
    displayResponse = input()
    if displayResponse == 'y':
        displayDatabase()
        #calls method again if they want to try again (Recursive and can lead to issues, but not caring for such a small program)
        #ends
    else:
        return
        
