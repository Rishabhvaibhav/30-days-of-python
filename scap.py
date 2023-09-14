import random
Name = input("Enter name as a sepreted commas : ")
Name = Name.split(",")
member = len(Name)

toss = random.randint(1,member)

who_will_pay = Name[toss]
print(who_will_pay) 