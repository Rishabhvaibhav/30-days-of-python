# pizza order program 

size = input("Enter the size you want \n Small = s \n Medium = m \n Large= l \n Pick Any pizza You want :  ")

if size == "s" or"S":
    cost = 100
    print("you choose small pizza ")
elif size == "m" or "M":
    cost = 200
    print("you choose medium pizza ")
elif size == "l" or "L":
    cost = 300
    print("you choose large pizza ")
else:
    exit()

addon = input("if want to add peperroni enter Y / N ")

if addon == "y" or "Y":
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
if cheese == "y" or "Y":
    cost = cost + 20
    print(f"current code is : {cost}")
