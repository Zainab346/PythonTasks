#   /////// SIMPLE CALCULATOR /////////

print("Which operation you want to perform ?")
print("1 : ADDITION(+)")
print("2 : SUBTRACTION(-)")
print("3 : MULTIPLICATION(*)")
print("4 : DIVISION(/)")
print("5 : MODULUS(%)")
print("6 : EXPONENTIAL(**)")

choice=input("Enter you choice:")
while True:
    if choice=='1':
         x=int(input("Enter 1st number:"))
         y=int(input("Enter 2nd number:"))
         print(f"Addition is : {x+y}")

    elif choice=='2':
         x=int(input("Enter 1st number:"))
         y=int(input("Enter 2nd number:"))
         print(f"Subtion is : {x-y}")

    elif choice=='3':
         x=int(input("Enter 1st number:"))
         y=int(input("Enter 2nd number:"))
         print(f"Multiplition is : {x*y}")
    elif choice=='4':
        x=int(input("Enter 1st number:"))
        y=int(input("Enter 2nd number:"))
        print(f"Division is : {x/y}")

    elif choice=='5':
        x=int(input("Enter 1st number:"))
        y=int(input("Enter 2nd number:"))
        print(f"Modulus is : {x%y}")

    elif choice=='6':
         x=int(input("Enter 1st number:"))
         y=int(input("Enter 2nd number:"))
         print(f"{x} power {y} is : {x**y}")   
    else:
     print("Please enter a valid choice!!!!")

    status=input("Do you want to select another option ? Y/N:")
    if status=='Y'or status == 'y':
         continue
    elif  status=='N'or status == 'n':
         print("Exit!!!!!")
         break


    
