# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' likes ' + color )
#
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2026 - int(birth_year)
# print(type(age))
# print('Your age is' ,age)
from idlelib.debugger_r import codetable
from string.templatelib import convert

# weight_pounds = input('What is your weight in pounds ')
# weight_kilograms = 0.45 * int(weight_pounds)
# print('Your weight is',weight_kilograms, 'kilograms')
#
# course = 'Python for Beginners'
# another = course[:]
#
# print(another)

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# # John [Smith] is a coder
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)

# course = 'Python for Beginners'
# print(course.replace('P','Jo'))
# print('python' in course)

# import math
# print(math.floor(2.9))

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")
#
# price_house = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = price_house * 0.10
# else:
#     down_payment = price_house * 0.20
# print(f"Down payment: ${down_payment}")


# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print('Eligible for loan')

# temperature = 20
# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither a hot day nor a cold day")

# name = input('What is your name? ')
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters')
# else:
#     print('Name looks good')

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')

# number = int(input('Enter a number: '))
# even = number % 2
# if even == 0:
#     print('Even number')
# else:
#     print('Odd number')

# age = int(input('Enter your age: '))
#
# if age < 0:
#     print('Invalid age')
# elif age < 13:
#     print('You are a child')
# elif age < 18:
#     print('You are minor')
# elif age < 36:
#     print('You are a young adult')
# elif age < 61:
#     print('You are adult')
# else:
#     print('You are a senior')

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit :
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number :
#         print('You won!')
#         break
#     elif guess_count > guess_limit -1 :
#         print('Sorry you failed')

print()
message = "Forca Barca"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3

print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

professors = ["greg","leo","orlando","kianoosh"]
print(professors[0])
print(professors[-1])
professors.append("alberto")
print(professors)
professors.extend(["richard","jason"])
print(professors)
professors.insert(2,"pedro")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5]) #accessing professors in positions 3 and 4
print(professors[5:]) #starting at 5 all the way to the end
print(professors[:3]) #from 0 all the way to 2
print(professors[:]) #print everything, copy of the original list

x = professors.pop(6)
print(professors)
print(professors.index("mark"))
x = professors.pop(6)
print(professors)
print(x)
print(len(professors))
print(type(professors))
professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for i in professors:
    print(i.title())
print("FIU")

water_data = {
    "temperature":[78,89,92],
    "pH":[6.5,6.7,6.3],
    "oxygen":[7.2,5.6,3.5],
}

print(water_data["oxygen"])

print(water_data.keys())
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)