user_input = input("Enter the number you want : ")
user_input = user_input.split(" ")
# 78 56 45 7 88 9 

count = 0
for i in user_input:
    count += 1
print(count)    

for int_value in range(count):
    user_input[int_value] = int(user_input[int_value])
    
max_num = user_input[0]

for number in user_input:
    if number < int(max_num):
        max_num = number
        
print(number)
    

