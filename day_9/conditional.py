# Exercises: Level 1
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

"""
age = int(input('Enter the age :'))
if age >= 18 :
    print("You are old enough to drive ")
else :
    print("You are old enough to learn to drive")

"""






# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
# 
# Output:
# Enter your age: 30
# You are 5 years older than me.
'''
my_age = 21
your_age =int(input('Enter you age '))

if my_age == your_age:
    print('Both age is same ')
elif my_age < your_age:
    age_gap = (your_age - my_age)
    print(f"you are {age_gap} year older than me ")
elif my_age > your_age:
    age_gap = (my_age - your_age)
    print(f"you are {age_gap} year elder than you  ")
else : 
    print('Invalid input ')


'''
    



# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

"""
a = int(input('Enter the first number : '))
b = int(input('Enter the first number : '))

if a > b :
    print(f"{a} is greater than {b}")
elif a < b :
    print(f"{b} is greater than {a}")
else:
    print("Both are equal")

"""



# ### Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
'''
score = (int(input("Enter the marks you get : ")))

if score <= 49:
    print("F")89
elif score <= 59:
    print('D')
elif score <= 69:
    print('C')
elif score <= 89:
    print('B')
elif score <= 100:
    print('A')
else : 
    TypeError
'''





# Check if the season is Autumn, Winter, Spring or Summer.  
# December, January or February, the season is Winter. 
# March, April or May,  the season is Spring 
# June, July or August, the season is Summer
# If the user input is: September, October or November, the season is Autumn.

"""
season = input("Enter the season : ")
season = season.upper()
x = NameError

if season == ("DECEMBER" or "JANUARY" or "FEBRUARY"):
    print("the Season is Winter ")
elif season == ("MARCH" or "APRIL" or "MAY"):
    print("the Season is spring ")
elif season == ("JUNE" or "JULY" or "AUGUST"):
    print("the Season is summer ")
elif season == ("SEPTEMBER" or "OCTOBER" or "NOVEMBER") :
    print("the Season is Autumn ")
else:
    print("Invalid input : " ,x)

"""





# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
"""
i = 0
while True : 
    fruits = ['banana', 'orange', 'mango', 'lemon']
    find = input("Enter food you find : ")
    if find in fruits :
            print("That fruit is already exist in the list ")
    else:
        fruits[-1] = find
        print("your food is not exist, it added sucessfully   ")
        i += 1
        if i > 5:
            break
"""

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format: