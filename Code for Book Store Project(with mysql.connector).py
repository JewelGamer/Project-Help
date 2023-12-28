#Importing module
import mysql.connector as sql

#-------Main Part-------#
#User input for login
user=input("Enter your username(if none then root)>>>")
password=input("Enter the password to login>>>")
mydb=sql.connect(host='localhost',user=user,passwd=password)

#Creating cursor and database
c=mydb.cursor()
c.execute('Create Database IF NOT EXISTS Book_Store')
c.execute('Use Book_Store')
c.execute('Create Table IF NOT EXISTS Stock (Id int PRIMARY KEY,Book_Name varchar(255),Authors_Name varchar(255),Quantity int,Price int)')

#-------Functions-------#
#Defining a function to add data
def Add():
    print("1. To Enter single Value.")
    print("2. To Enter multiple values.")
    a=int(input('Enter your choice:'))

    #Singular input
    if a==1:
        id=int(input("Enter the Book id:"))
        Name=input("Enter the Book Name:")
        Author=input("Enter the name of the Author:")
        Price=int(input("Enter the Price:"))
        Quantity=int(input("Enter the Quantity:"))
        d='Insert into Stock(Id,Book_Name,Authors_Name,Quantity,Price) values(%s,%s,%s,%s,%s)'
        e=(id,Name,Author,Quantity,Price)
        c.execute(d,e)
        mydb.commit()

    #Multiple Inputs
    if a==2:
        b=int(input("Enter the amount entries u wish to make:"))
        for i in range(0,b):
            print('Entry Number:',i+1)
            id=int(input("Enter the Book id:"))
            Name=input("Enter the Book Name:")
            Author=input("Enter the name of the Author:")
            Price=int(input("Enter the Price:"))
            Quantity=int(input("Enter the Quantity:"))
            d='Insert into Stock(Id,Book_Name,Authors_Name,Quantity,Price) values(%s,%s,%s,%s,%s)'
            e=(id,Name,Author,Quantity,Price)
            c.execute(d,e)
            mydb.commit()
    else:
        print('To enter only choose either 1 or 2')

#Defining function to delete values
def Delete():
    print("1. To Enter single Value.")
    print("2. To Enter multiple values.")
    a=int(input('Enter your choice:'))

    #To delete single values
    if a==1:
        d="Delete From stock Where Id = %s"
        e=int(input("Enter the id of the book to delete it:"))
        c.execute(d,(e,))
        mydb.commit()

    #To delete Multiple values at once
    if a==2:
        b=int(input("Enter the amount entries u wish to delete:"))
        for i in range(0,b):
            print("Records Deleted",i+1)
            d="Delete From stock Where Id = %s"
            e=int(input("Enter the id of the book to delete it:"))
            c.execute(d,(e,))
            mydb.commit()
    else:
        print('To delete only choose either 1 or 2')

#Defining function to update esisting data
def Update():
    print("1.To update the Book Name.")
    print("2.To update the Author's Name.")
    print("3.To update the Price of the books.")
    print("4.To update the Quantity of books.")
    f=int(input("Enter your choice:"))

    #To update the Book Name
    if f==1:
        g="Update stock Set Book_Name = %s Where Id = %s"
        h=int(input("Enter the Book ID:"))
        i=input("Enter the Book Name:")
        values=(i,h)
        c.execute(g,values)
        mydb.commit()

    #To update the Author's Name    
    if f==2:
        g="Update stock Set Authors_Name = %s Where Id = %s"
        h=int(input("Enter the Book ID:"))
        i=input("Enter the Author's Name:")
        values=(i,h)
        c.execute(g,values)
        mydb.commit()

    #To update the Price
    if f==3:
        g="Update stock Set Price = %s Where Id = %s"
        h=int(input("Enter the Book ID:"))
        i=input("Enter the Price:")
        values=(i,h)
        c.execute(g,values)
        mydb.commit()

    #To update the Quantity
    if f==4:
        g="Update stock Set Quantity = %s Where Id = %s"
        h=int(input("Enter the Book ID:"))
        i=input("Enter the Quantity:")
        values=(i,h)
        c.execute(g,values)
        mydb.commit()
    else:
        print("Enter one of the choices.")

#Defining function to search through table for suitable data 
def Search():
    print("1.If you want to search according to ID.")
    print("2.If you want to search according to Book Name.")
    print("3.If you want to search according to Author's Name.")
    print("4.If you want search between Prices.")
    print("5.If you want if you want to see all details.")
    j=int(input("Enter your choice:"))

    #To search according to Id
    if j==1:
        k="Select * From stock Where Id = %s"
        m=int(input("Enter the ID:"))
        c.execute(k,(m,))
        result=c.fetchall()
        for row in result:
            print(row)

    #To search according to Book Name
    if j==2:
        k="Select * From stock Where Book_Name = %s"
        m=input("Enter the Book Name:")
        c.execute(k,(m,))
        result=c.fetchall()
        for row in result:
            print(row)

    #To search according to Author's Name
    if j==3:
        k="Select * From stock Where Authors_Name = %s"
        m=input("Enter the Author's Name:")
        c.execute(k,(m,))
        result=c.fetchall()
        for row in result:
            print(row)

    #To search for Price between a certain range
    if j==4:
        k="Select * From stock Where Price Between %s And %s"
        m=input("Enter the Starting Price:")
        n=input("Enter the Ending Price:")
        o=(m,n)
        c.execute(k,o)
        result=c.fetchall()
        for row in result:
            print(row)

    #To show all records
    if j==5:
        c.execute("Select * From Stock")
        result=c.fetchall()
        column_names = c.column_names
        for row in result:
            print(*row,sep="\t")
    else:
        print('Enter one of the choice given above.')

#------Main Loop------#
q=True
while(q):

    #Choices to execute
    print("1.To add to the table.")
    print("2.To delete from the table.")
    print("3.To update values of the table.")
    print("4.To search for data.")
    print("5.Exit/Logout")
    p=int(input("Enter your choice:"))
    if p==1:
        Add()
    if p==2:
        Delete()
    if p==3:
        Update()
    if p==4:
        Search()
    if p==5:
        q=False
        c.close()
        mydb.close()
    else:
        print("Enter the correct choice.")
