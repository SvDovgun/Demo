# 1
# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = bool(input("Is your account active? "))

# print(type(name))
# print(type(email))
# print(type(age))
# print(type(height))
# print(type(is_active))


# 2
# length = float(input("length: "))
# width = float(input("width: "))
# area = length * width
# print(area)

# 3 
# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False
# print(is_next)

# 4 
# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 5 :
#     developer_type = "Senior"
# elif work_experience > 1:
#     developer_type = "Middle"
# else:
#     developer_type = "Junior"

# print(developer_type)

# 5
# num = int(input("Enter a number: "))

# if num > 0:
#     result = "Positive number"
# elif num < 0 :
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)

# 6
# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)

# 7 
# numbers = [10, 4, 201, 21, 12, 2, 132, 7, 1, 18, 3, 12, 6, 15, 4, 27]
# sum_num = 0

# for number in numbers:
#     if number % 3 == 0:
#         print(number)
#         sum_num += number

# print(numbers)
# print(sum_num)

# 8 
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum += num
#     print(num)
#     num -= 1    

# print(sum)

# 9
# def greeting():
#     print('Hello world!')

# greeting()

# 10 
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

print(invite_to_event("Tobby"))