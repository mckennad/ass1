print("Employee FMS \n \n Select one of the following \n \n    1) Add a new employee \n    2) Search for an employee \n    3) Remove an employee from FMS \n    4) Display entire employee FMS \n    5) Quit \n")
#Opening option list (option 5 was forgotten on assignment sheet) 


line = input()

if line == '1':
#if input is 1, proceed to AddEmployee procedures
    
    while AddEmployee:
        print("Please enter ID number")
        a = input()
        print("Please enter first name")
        b = input()
        print("Please enter last name")
        c = input()
        print("Please enter dept")
        d = input()
        #grab 4 variables so they can be compared/used later
        

        while EmployeeCanBeAdded:
            d={}
            infile = open("/home/francoc/Documents/DMck/CS3130/Ass1/P2","r")
            #reads document

            for rec in infile:
                ID,rest = rec.split(":",1)
                    if a == ID:
                        EmployeeCanBeAdded == false
                        #if ID already exists fall out of Adding block
                    d[ID] = rest
                infile.close()

            


            for key in d:
                print(key, d[key].split(":"))




#REDOING, makes more sense to have multiple files


#database.py			MAIN.py
#				import database
#def fred():			database.fred()
