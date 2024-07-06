import mysql.connector as m
def insert():
    cr=mdb.cursor();
    print("\n**********INSERTING OR ADDING RECORDS**********")
    try:
        d=int(input("\nEnter Flat No. -"))
        qry="select * from Record_Book where Flat_No=%s"%(d,)
        cr.execute(qry)
        q=cr.fetchone()
        if q==None:
            e=input("Enter Owner's name -")
            f=int(input("Enter Owner's contact no. -"))
            g=str(input("Enter Owner's Email ID -"))
            h=input("Enter Self Occupied/Tenant -")
            if h.lower()=="tenant":
                i=input("Enter Tenant's name -")
                j=int(input("Enter Tenant's contact no. -"))
                k=str(input("Enter Tenant's Email ID -"))
                sql="Insert into Record_Book values(%s,'%s',%s,'%s','%s','%s',%s,'%s')"%(d,e,f,g,h,i,j,k,)
            else:
                sql="Insert into Record_Book(Flat_No,OName,OContactNo,OEmailID,Status) values(%s,'%s',%s,'%s','%s')"%(d,e,f,g,h,)
            cr.execute(sql)
            mdb.commit()
            print("Record Inserted succesfully")
        else:
            print('''Sorry that flat detail already exists.
To make any change in the alreay existing data use the update function''')      
    except:
        mdb.rollback()
        print("Record cannot be inserted")
    print("\nDISPLAYING THE RECORDS")
    print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
    cr.execute("Select * from Record_Book") 
    rec=cr.fetchall() 
    for x in rec:
        print(x) 
    return
def search():
    cr=mdb.cursor();
    print("\n**********SEARCHING RECORDS**********")
    try:
        n=input("\nEnter the flat no to be searched - ")
        qry="select * from Record_Book where Flat_No=%s"%(n,)
        cr.execute(qry)
        rec=cr.fetchall()
        if rec!=[]:
            for x in rec:
                print("\nDISPLAYING THE SEARCHED RECORD")
                print("\nFlat No -",x[0])
                print("Owner's Name -",x[1])
                print("Owner's Contact No -",x[2])
                print("Owner's Email ID -",x[3])
                print("Status -",x[4])
                print("Tenant's Name -",x[5])
                print("Tenant's Contact No -",x[6])
                print("Tenant's Email ID -",x[7])
        else:
            print("Record not found ")
    except:
        mdb.rollback()
        print("Record can't be searched")
    return
def update():
    cr=mdb.cursor();
    print("\n**********UPDATING RECORD**********")
    cr.execute("Select * from record_book")
    rec=cr.fetchall()
    print("\nDISPLAYING THE CURRENT RECORDS")
    print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
    for x in rec:
        print(x)
    try:
        y="yes"
        while y.lower()=="yes":
            f=int(input("\nEnter the flat no to be updated -"))
            qry="select * from Record_Book where Flat_No=%s"%(f,)
            cr.execute(qry)
            d=cr.fetchone()
            if d!=None:
                print('''\nChoose one of the following options to update -\n
(1)Owner's Name
(2)Owner's Contact No
(3)Owner's Email ID
(4)Status
(5)Tenant's Name
(6)Tenant's Contact No
(7)Tenant's Email ID\n''')
                c=int(input("Enter your choice(1-7) -"))
                if c==1:
                    n="OName"
                    a=input("\nEnter the Owner's Name to be updated -")
                elif c==2:
                    n="OContactNo"
                    a=int(input("\nEnter the Owner's Contact No to be updated -"))
                elif c==3:
                    n="OEmailID"
                    a=str(input("\nEnter the Owner's Email ID to be updated -"))
                elif c==4:
                    n="Status"
                    a=input("\nEnter the status to be updated -")
                elif c==5:
                    n="TName"
                    a=input("\nEnter the Tenant's Name to be updated -")
                elif c==6:
                    n="TContactNo"
                    a=int(input("\nEnter the Tenant's Contact No to be updated -"))
                elif c==7:
                    n="TEmailID"
                    a=str(input("\nEnter the Tenant's Email ID to be updated -"))
                else:
                    print("Enter a valid option")
                r=(a,f)
                qry="update record_book set "+n+ "=%s where flat_no=%s"
                cr.execute(qry,r)
                print(cr.rowcount,"Records Updated")
                mdb.commit()
            else:
                print("Sorry no such flat exists")
            y=input('''\nIf you wish to update more records enter "yes"
or if you wish to exit enter "no" --- ''')
        else:
            print("Thankyou")
        print("\nDISPLAYING THE UPDATED RECORDS")
        print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
        cr.execute("Select * from record_book")
        rec=cr.fetchall()
        for x in rec:
            print(x)
        print("\nEXITING")
    except:
        print("Record not found or cannnot be updated")
        mdb.rollback()
    return
def delete():
    cr=mdb.cursor();
    print("\n**********DELETING RECORD**********")
    cr.execute("Select * from Record_Book")
    rec=cr.fetchall()
    print("\nTable records are -")
    print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
    for x in rec:
        print(x)    
    a=input("\nEnter the Flat No. to be deleted::")
    try:
        qry="delete from Record_Book where Flat_No=%s"%(a,)
        cr.execute(qry)
        print(cr.rowcount,"Records Deleted")
        mdb.commit()
        cr.execute("Select * from Record_Book")
        rec=cr.fetchall()
        print("\nUpdated table records are -")
        print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
        for x in rec:
            print(x)
    except:
        print("Record not found or cannnot be deleted")
        mdb.rollback()
    return
def display():
    cr=mdb.cursor();
    print("\n**********DISPLAYING RECORD**********")
    cr.execute("Select * from record_book")
    rec=cr.fetchall()
    print('''\nFlat No | Owner's Name | Owner's Contact No. | Owner's Email ID |
Status | Tenant's Name | Tenant's Contact No | Tenant's Email ID\n''')
    for x in rec:
        print(x)
    return
def main():
    print("\n**********WELCOME**********")
    p="yes"
    while p.lower()=="yes":
        print('''\nChoose any of the below functions to perform -
(1)Insert or add record
(2)Search records
(3)Update records
(4)Delete records
(5)Display records''')
        c=int(input("\nEnter your choice(1-4) - "))
        if c==1:
            insert()
        elif c==2:
            search()
        elif c==3:
            update()
        elif c==4:
            delete()
        elif c==5:
            display()
        else:
            print("Please choose a valid option")
        p=input('''\nIf you wish to continue enter "yes"
or if you wish to exit enter "no" --- ''')
    else:
        print("\n************Thank you************")
mdb=m.connect(host="localhost",user="root", passwd="21102003", database="anjali")
print(mdb)
main()
