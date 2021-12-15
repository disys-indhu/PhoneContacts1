class phone_Contacts:

    def __init__(self,Firstname,Lastname,Phone_number,Groups):
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.groups=Groups
        a["firstname"] = self.firstname
        a["lastname"] = self.lastname
        a["phno"] = self.phonenumber
        a["Group"] = self.groups
        database.append(a)

    def open_phcontacts(self):
        print("Phone Contacts")


    def firstname_verification(self):
        name = str(input("Enter firstname:"))
        con.append(name)
        if not name.isalpha():
            raise TypeError("Firstname contain only letters")


    def lastname_verification(self):
        name = str(input("Enter Lastnamename:"))
        con.append(name)
        if not name.isalpha():
            raise TypeError("Firstname contain only letters")
        
        
    def phonenumber_verification(self):
        number=input("Enter Phonenumber:")
        if type(number) == str:
            if (len(str(number)) == 10):
                con.append(number)
                print("valid phonenumber")
            else:
                raise TypeError ("phonenumber not valid")   
        
    
    def groups_verification(self):
        input("Enter groups:")
        if type(self.groups) == str:
            if len(self.groups) <= 10:
                con.append(self.groups)
                print(con)
                print("Phone contacts successfully created")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contains only letters")
        print(database)

    
a={}
con=[]

database=[{"Firstname":"Abi","Lastname":"Rithinyaa","Phno":9854268725,"Groups":"Family"},            
       {"Firstname":"Anu","Lastname":"priyaa","Phno":9987968234,"Groups":"Friends"},
       {"Firstname":"Aarthi","Lastname":"M","Phno":9172653411,"Groups":"Friends"},
       {"Firstname":"Abiani","Lastname":"Kumar","Phno":9813245678,"Groups":"Friends"},]
       

database.append(con)

Indhu=phone_Contacts("Indhu","mathi","9003085387","Family")
Indhu.open_phcontacts()
Indhu.firstname_verification()
Indhu.lastname_verification()
Indhu.phonenumber_verification()
Indhu.groups_verification()
