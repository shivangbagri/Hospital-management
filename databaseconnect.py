"""
Author: Shivang
Date: 16/3/20
Purpose: Hospital management project through Python Data-connectivity

"""
import mysql.connector
import random
import time

# must install python-mysql connector
# this code may lack try-catch block, I rest this on the contributors.

med_list = ['X12', 'X32', 'Y12', 'X44']
mydb = mysql.connector.connect(user='shivangbagri', password='hivang26', database='wisdom', autocommit=True)

cur = mydb.cursor()

print("WELCOME TO HIVANG HOSPITAL DATABASE")
print("\n""FILL THE REQUIRED ENTRIES TO ACCESS YOUR INFO")
run = True
account = False
while run:
    print("\n""1: REGISTER YOURSELF" "\n""2: LOG IN""\n")
    x = int(input("Select your choice "))
    if x == 1:
        name = input("Enter Patient name ")
        age = int(input("Enter age "))
        dis = input("Enter Disease ")
        phone = int(input("Enter your phone no. "))
        med = random.choice(med_list)
        command = "insert into hivang_hospital values('" + name + "','" + str(age) + "','" + dis.upper() + "', '" + str(
            phone) + "','" + med + "')"
        try:
            print("REGISTERED SUCCESSFULLY! ""\n")
            account = True

        except Exception as e:
            print("Error occured! ")
        cur.execute(command)
        break
    elif x == 2:
        e_name = input("Enter your name ")
        command2 = ("select Patient_name from hivang_hospital where Patient_name= '" + e_name + "'")
        cur.execute(command2)
        pot = cur.fetchone()
        if pot is not None:
            print("Logined Successfully! ")
            account = True
            details = input("Do you want to fetch your details? (y/n) ")
            if details == 'y':
                print(" Name  Age  Disease  Phone No.  Meds ")
                command3 = ("select*from hivang_hospital where Patient_name='" + e_name + "'")
                cur.execute(command3)
                result = cur.fetchall()
                for i in result:
                    print(i)
            else:
                print("Operation cancelled")
        else:
            print("Account not found, Try creating a new account")
            account = False
    break
while True and account:
    print("\n3: DOCTOR's VIEW""\n""4: Paymemt""\n""5: Exit")
    y = int(input("Select your choice "))
    if y == 3:
        print("Here is our Doctor's view on your health")
        with open("hospital.txt", 'r+') as file:
            data = file.readlines()
            for j in data:
                print(j, end="")
    elif y == 4:
        name = input("Enter your name ")
        print("Enter payment method ""\n""1:Card only""\n")
        pay = int(input("Enter your choice "))
        if pay == 1:
            card_det = input("Enter card details ")
            card_pwd = int(input("Enter card pin "))
            card_amount = int(input("Enter amount pending($) "))
            print("Sending...")
            time.sleep(2)
            print("Amount Sent! \/")
    elif y == 5:
        print("Thanks for visiting ""\n""----HIVANG HOSPITAL")
        print("Logged out")
        break
