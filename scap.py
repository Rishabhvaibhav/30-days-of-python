# create a rock paper scissor 
import random
name = input("Enter the Name : ")
while True:
        for i in range():
        user_input = int(input("Choose what your choose \n 0 = Rock \n 1 = paper \n 2 = Scissor  \n Select One :    "))
        print(user_input)
        computer_choose = random.randint(0,2)

        if user_input == computer_choose:
            print("Draw")
        elif (user_input == 0) and ( computer_choose == 1):
            print(f"-----------------{name} win-------------------\n")
        elif (user_input == 2) and ( computer_choose == 1):
            print(f"----------------{name} win--------------------\n")
        elif (user_input == 0) < ( computer_choose == 2):
            print(f"----------------{name} win---------------------\n")
        else:
            print(f"computer choose {computer_choose}")
            print("------------------Computer wins-----------------\n")