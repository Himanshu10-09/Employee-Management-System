import mysql.connector as x
from tabulate import tabulate
con=x.connect(host ="host_info", user ="User_Info", password="Your_password", database ="employee")
c=con.cursor()

#Functions to add data ====================================================================

def addempinfo():
    empid = int(input("Enter employee Id ="))
    empname = input("Enter employee Name =")
    empPhNo = int (input("Enter employee Phone number ="))
    empaddr = input("Enter employee address =")
    empemail = input("Enter employee's email =")
    print("Date of Birth Format:(YYYY/MM/DD)")
    empdob = input("Enter employee's Date of Birth =")
    empgender = input("Enter employee's Gender =")
    empdesgn = input("Enter employee's designation =")
    c.execute("Insert into Employeeinfo values(%s,%s,%s,%s,%s,%s,%s,%s)",(empid,empname,empPhNo,empaddr,empemail,empdob,empgender,empdesgn))
    ch = input("Do you want to add this record (y/n)=")
    if ch=='y' or ch=='Y':
        con.commit()
        print("Data added successfully!!!")
    else:
        print("Data not added!!!!")

def adddeptinfo():
    deptid = int(input("Enter department id ="))
    deptname = input("Enter department name =")
    c.execute("Insert into Department values(%s,%s)",(deptid,deptname))
    ch = input("Do you want to add this record (y/n)=")
    if ch=='y' or ch=='Y':
        con.commit()
        print("Data added successfully!!!")
    else:
        print("Data not added!!!")

def addsalaryinfo():
    salaryid = int(input("Enter Salary id ="))
    print("Date Format:-(DD-MM-YYYY)")
    salarydate = input("Enter salary date =")
    print("Salary month should be in words(Ex:- January,February, etc.) ")
    salarymonth = input("Enter salary month =")
    c.execute("Insert into Salaryinfo values(%s,%s,%s)",(salaryid,salarydate,salarymonth))
    ch = input("Do you want to add this record (y/n)= ")
    if ch=='y' or ch=='Y':
        con.commit()
        print("Data added successfully!!!")
    else:
        print("Data not added!!!")

def addpaydealsinfo():
    basicsalary = int(input("Enter Employee's basic salary ="))
    bonus = int(input("Enter Bonus ="))
    extwrksalary = int(input("Enter Extra work salary ="))
    c.execute("Insert into Paydeals values(%s,%s,%s)",(basicsalary,bonus,extwrksalary))
    ch = input("Do you want to add this record (y/n) =")
    if ch=='y' or ch=='Y':
        con.commit()
        print("Data added successfully!!!")
    else:
        print("Data not added!!!")
#Functions to display Data ===============================================================

def displayemp():
    print("\n\n",120*"=")
    c.execute("Select * from Employeeinfo")
    data = c.fetchall()
    print(tabulate(data,headers=["EmpID","Name","Phone No.","Address","Email","DOB","Gender","Designation"],tablefmt='psql'))
    print("\n\n",120*"=")
    
def displaydept():
    print("\n\n",80*"=")
    c.execute("Select * from Department")
    data = c.fetchall()
    print(tabulate(data,headers=["Department Id","Department Name"],tablefmt='psql'))
    print("\n\n",80*"=")

def displaysalary():
    print("\n\n",80*"=")
    c.execute("Select * from Salaryinfo")
    data = c.fetchall()
    print(tabulate(data,headers=["Salary ID","Salary Date","Salary Month"],tablefmt='psql'))
    print("**(Date Format:-(DD-MM-YYYY))")
    print("\n\n",80*"=")
    

def displaypaydeals():
    print("\n\n",80*"=")
    c.execute("Select * from Paydeals")
    data = c.fetchall()
    print(tabulate(data,headers=["Basic Salary","Bonus","Extrawork Salary"],tablefmt='psql'))
    print("\n\n",80*"=")


#Functions to Search for a record ======================================================================

def searchemp():
    empid = int(input("Enter employee id to be searched ="))
    c.execute("Select * from Employeeinfo where Employeeid=%s",(empid,))
    print("\n\n",140*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["EmpID","Name","Phone No.","Address","Email","DOB","Gender","Designation"],tablefmt='psql'))
    print("\n\n",140*"=")

def searchdept():
    deptid = int(input("Enter Department id to be searched ="))
    c.execute("select * from Department where Departmentid=%s",(deptid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Department Id","Department Name"],tablefmt='psql'))
    print("\n\n",80*"=")

def searchsalary():
    salaryid = int(input("Enter Salary Id to be Searched ="))
    c.execute("Select * from Salaryinfo where salaryid=%s",(salaryid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Salary ID","Salary Date","Salary Month"],tablefmt='psql')) # type: ignore
    print("\n\n",80*"=")

def searchpaydeals():
    empid = int(input("Enter employee id to search data ="))
    c.execute("Select * from Paydeals where Employeeid=%s",(empid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Basic Salary","Bonus","Extrawork Salary"],tablefmt='psql'))
    print("\n\n",80*"=")

#Function to delete a record from tables ===========================================================

def deleteemp():
    empid = int(input("Enter employee id to be deleted ="))
    c.execute("Select * from Employeeinfo where Employeeid=%s",(empid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["EmpID","Name","Phone No.","Address","Email","DOB","Gender","Designation"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to delete this record? (y/n)=")
    if ch=='y' or ch=='Y':
        c.execute("Delete from Employeeinfo where Employeeid=%s",(empid,))
        con.commit()
        print("Record deleted successfully!!!")
    else:
        print("No record is deleted!!!")

def deletedept():
    Departmentid = int(input("Enter Department id to be deleted ="))
    c.execute("select * from Department where Departmentid=%s",(Departmentid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Department Id","Department Name"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to delete this record? (y/n)=")
    if ch=='y' or ch=='Y':
        c.execute("Delete from Department where Departmentid=%s",(Departmentid,))
        con.commit()
        print("Record deleted successfully!!!")
    else:
        print("No data is deleted!!!")

def deletesalary():
    salaryid = int(input("Enter Salary Id to be deleted ="))
    c.execute("Select * from Salaryinfo where salaryid=%s",(salaryid,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Salary ID","Salary Date","Salary Month"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to delete this record? (y/n)=")
    if ch=='y' or ch=='Y':
        c.execute("Delete from Salaryinfo where salaryid=%s",(salaryid,))
        con.commit()
        print("Record deleted successfully!!!")
    else:
        print("No data is deleted!!!")

def deletepaydeals():
    salary = int(input("Enter salary amount to be deleted from the table:-"))
    c.execute("Select * from Paydeals where Basicsalary=%s",(salary,))
    print("\n\n",80*"=")
    data = c.fetchall()
    print(tabulate(data,headers=["Basic Salary","Bonus","Extrawork Salary"],tablefmt='psql'))
    
    print("\n\n",80*"=")
    ch = input("Do you want to delete this record? (y/n)")
    if ch=='y' or ch=='Y':
        c.execute("Delete from Paydeals where Basicsalary=%s",(salary,))
        con.commit()
        print("Record deleted Successfully!!!")
    else:
        print("No data is deleted!!!")

    

#Function to modify records in a table ===================================================
def modifyemp():
    empid = int(input("Enter employee id to be modified ="))
    c.execute("Select * from Employeeinfo where Employeeid=%s",(empid,))
    data = c.fetchall()
    print("\n\n",80*"=")
    print(tabulate(data,headers=["EmpID","Name","Phone No.","Address","Email","DOB","Gender","Designation"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to modify this record? (y/n) =")
    if ch =='y' or ch =='Y':
        empname = input("Enter new Employee name or press 'Enter' to skip: ")
        if empname =="":
            pass
        else:
            c.execute("Update Employeeinfo set name=%s where Employeeid=%s",(empname,empid))
            con.commit()

        empPhNo = int(input("Enter new employee phone number or Enter '-1' to skip:"))
        if empPhNo == -1:
            pass
        else:
            c.execute("Update Employeeinfo set PhoneNumber=%s where Employeeid=%s",(empPhNo,empid))
            con.commit()

        empaddr = input("Enter new employee adress or press 'Enter' to skip:") 
        if empaddr=="":
            pass
        else:
            c.execute("Update Employeeinfo set Address=%s where Employeeid=%s",(empaddr,empid))
            con.commit()
        
        empemail = input("Enter new employee email or press 'Enter' to skip:")
        if empemail == "":
            pass
        else:
            c.execute("Update Employeeinfo set email=%s where Employeeid=%s",(empemail,empid))
            con.commit()

        print("Date of Birth Format:(YYYY/MM/DD)")
        empdob = input("Enter new employee date of birth or press 'Enter' to skip:")
        if empdob =="":
            pass
        else:
            c.execute("Update Employeeinfo set DateOfBirth=%s where Employeeid=%s",(empdob,empid))
            con.commit()
        
        empgender = input("Enter new employee's gender or press 'Enter' to skip:")
        if empgender =="":
            pass
        else:
            c.execute("Update Employeeinfo set Gender=%s where Employeeid=%s",(empgender,empid))
            con.commit()

        empdesgn = input("Enter new employee designation or press 'Enter' to skip:")
        if empdesgn =="":
            pass
        else:
            c.execute("Update Employeeinfo set Designation=%s where Employeeid=%s",(empdesgn,empid))
            con.commit()

        print("Data modified Successfully!!!")
    else :
        print("No record has been modified!!!")

def modifydept():
    deptid = int(input("Enter department id to be modified ="))
    c.execute("Select * from Department where Departmentid=%s",(deptid,))
    data = c.fetchall()
    print("\n\n",80*"=")
    print(tabulate(data,headers=["Department Id","Department Name"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to modify this record? (y/n) =")
    if ch=='y' or ch=='Y':
        deptname = input("Enter new Department Name or press 'Enter' to skip:")
        if deptname =="":
            deptname = data[1]
        c.execute("Update Department set Departmentname=%s where Departmentid=%s",(deptname,deptid)) # type: ignore
        con.commit()
        print("Data modified successsfully!!!")
    else:
        print("No data has been modified!!!")

def modifysalary():
    salaryid = int(input("Enter salary id to be modified ="))
    c.execute("Select * from Salaryinfo where Salaryid=%s",(salaryid,))
    data = c.fetchall()
    print("\n\n",80*"=")
    print(tabulate(data,headers=["Salary ID","Salary Date","Salary Month"],tablefmt='psql'))
    print("\n\n",80*"=")
    ch = input("Do you want to modify this record? (y/n):")
    if ch=='y' or ch=='Y':
        print("Date Format:-(DD-MM-YYYY)")
        salarydate = input("Enter New salary date or press 'Enter' to skip:")
        if salarydate=="":
            pass
        else:
            c.execute("Update Salaryinfo set Salarydate=%s where Salaryid=%s",(salarydate,salaryid))
            con.commit()

        print("Salary month should be in words(Ex:- January,February, etc.) ")
        salarymonth = input("Enter New salary month or press 'Enter' to skip:")
        if salarymonth=="":
            pass
        else:
            c.execute("Update Salaryinfo set Salarymonth=%s where Salaryid=%s",(salarymonth,salaryid))
            con.commit()
        print("Data modified Successfully!!!")
    else:
        print("NO data has been modified!!!")



#Menu for the Execution of the above defined functions  ==============================================================
while True:
    print("1. Add record in a table")
    print("2. Display records of a table")
    print("3. Search for a record in a table")
    print("4. Delete record in a table")
    print("5. Modify records in a table")
    print("6. Exit")
    ch = int(input("Enter your choice ="))
    if ch==1:
        print("==== In which Table you want to add records? ======")
        print("1. Employee Information Table")
        print("2. Department Table")
        print("3. Salary Table")
        print("4. Pay Deals Table")
        print("5. Exit")
        choice = int(input("Enter your choice ="))
        if choice==1:
            addempinfo()
        elif choice==2:
            adddeptinfo()
        elif choice==3:
            addsalaryinfo()
        elif choice==4:
            addpaydealsinfo()
        elif choice==5:
            pass
    
    elif ch==2:
        print("====  Which Table's record you want to display? ======")
        print("1. Employee Information Table")
        print("2. Department Table")
        print("3. Salary Table")
        print("4. Pay Deals Table")
        print("5. Exit")
        choice = int(input("Enter your choice ="))
        if choice == 1:
            displayemp()
        elif choice ==2:
            displaydept()
        elif choice==3:
            displaysalary()
        elif choice ==4:
            displaypaydeals()
        elif choice ==5:
            pass
    
    elif ch==3:
        print("==== In which Table you want to search records? ======")
        print("1. Employee Information Table")
        print("2. Department Table")
        print("3. Salary Table")
        print("4. Exit")
        choice  = int(input("Enter your choice ="))
        if choice ==1:
            searchemp()
        elif choice ==2:
            searchdept()
        elif choice ==3:
            searchsalary()
        elif choice ==4:
            pass
    
    elif ch==4:
        print("==== In which Table you want to delete records? ======")
        print("1. Employee Information Table")
        print("2. Department Table")
        print("3. Salary Table")
        print("4. PayDeals Table")
        print("5. Exit")
        choice = int(input("Enter your choice ="))
        if choice ==1:
            deleteemp()
        elif choice ==2:
            deletedept()
        elif choice ==3:
            deletesalary()
        elif choice ==4:
            deletepaydeals()
        elif choice==5:
            pass
    
    elif ch==5:
        print("==== Which Table's records you want to modify? ======")
        print("1. Employee Information Table")
        print("2. Department Table")
        print("3. Salary Table")
        print("4. Exit")
        choice = int(input("Enter your choice ="))
        if choice ==1 :
            modifyemp()
        elif choice ==2:
            modifydept()
        elif choice ==3:
            modifysalary()
        elif choice == 4:
            pass
        
    elif ch==6:
        break





























    
