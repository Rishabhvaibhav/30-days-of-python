# pizza order program 

size = input("Enter the size you want S/M/L :  ")

if size == "s" or size == "S":
    cost = 100
    print("you choose small pizza ")
elif size == "m" or size == "M":
    cost = 200
    print("you choose medium pizza ")
elif size == "l" or size == "L":
    cost = 300
    print("you choose large pizza ")
else:
    print("Invalid Entry ")
    exit()

addon = input("if want to add peperroni enter Y / N ")

if addon == "y" or addon =="Y":
    if cost == 100:
         cost = cost + 30
         print(f"Your current cost is {cost}")
    elif cost == 200:
         cost = cost + 50
         print(f"Your current cost is {cost}")
    elif cost == 300:
         cost = cost + 80
         print(f"Your current cost is {cost}")
    else: 
        pass
cheese = input("you want extra cheese :Y / N")   
if cheese == "y" or cheese == "Y":
    cost = cost + 20

else:
    pass
print(f"Your current pizza Cost is {cost}")
