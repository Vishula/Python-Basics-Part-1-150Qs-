vish = 1
# # Write a Python program to print the following string in a specific format
# # Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
#
# # Output :
# # Twinkle, twinkle, little star,
# # 	How I wonder what you are!
# # 		Up above the world so high,
# # 		Like a diamond in the sky.
# # Twinkle, twinkle, little star,
# # 	How I wonder what you are
# # use \n for new line and \t for tab space and \t\t for two tab spaces
#
#
# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n \t \t Up above the world so high, \n "
#       "Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are  ")
#
# print("-" * 50)
#
# # --------------------------------------------------------------------------
#
# #  Write a Python program to get the Python version you are using.
#
# import sys
#
# print(sys.version)
# print(sys.version_info)
#
# print("-" * 50)
#
# # --------------------------------------------------------------------------
#
# # Write a Python program to display the current date and time.
#
# import datetime
#
# #
# date = datetime.datetime.now()
# # time = datetime.datetime.now().time()
# #
# # print(date)
# # print(time)
#
# print(date.strftime("%Y-%m-%d %H:%M:%S"))
#
# print("-" * 50)
#
# # --------------------------------------------------------------------------
# # import math to access pi value.
# import math
#
# enter_radius = float(input("= "))
# area = math.pi * enter_radius ** 2
# print("area = ", area)
#
# print("-" * 50)
#
# # --------------------------------------------------------------------------
# # using string concatenation:  (" ") = space
#
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# print(last_name + " " + first_name)
#
# print("-" * 50)
#
# # --------------------------------------------------------------------------
# # python program which accepts a sequence of comma separated numbers from uer and generate a list and a tuple with those numbers
# # numbers_input = int(input("Enter nums with comma: "))
# #listy = []
# a = listy.append(numbers_input)
# sample data: 3 , 5, 7, 23
# values = input("Input numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print('list: ', list)
# print('Tuple', `tuple)

# print("-" * 50)

# ---------------------------------------------------------------------------

vish = 2


# val = input("(E)nter numbers: ")
# list = val.split(",")
# tuple = tuple(list)
# print('list: ', list)
# print('Tuple: ', tuple)

# Write a Python program to accept
# a filename from the user and print
# the extension of that. Go to the
# editor
# Sample filename : abc.java

# python expects file name as an argument
# python file.py your_fule.asm


# # accept a filename from user
# filename = input("Input the (F)ile N(a)me: ")
# f_extns = filename.split(".")
#
# # print the extension
# print("Extension of the filename is: " +
#       repr(f_extns[-1]))
#
# print("-" * 50)

# ---------------------------------------------------------------------------
# Python program to display the first and last color from the following list.
# color_list = ["Red", "Green", "White", "Black"]
#
# print("First color: " + color_list[0])
# print("Last color: " + color_list[-1])
# print("%s %s" % (color_list[0], color_list[-1]))
#
# name = "vish"
# age = 24
# print("Hello my name is %s and I'm %d years old." % ((name), (age)))

# print("-" * 50)

# ---------------------------------------------------------------------------

# Python program to display the examination schedule.

# exam_st_date = (11, 12, 2020)
# print("Exam start date: %i/%i/%i" % exam_st_date)
# print("Exam start date: %d/%d/%d" % exam_st_date)

# print("-" * 50)

# ---------------------------------------------------------------------------

# Python program that accepts an integer (n) and computes the value of n+nn+nnn

# print(5+55+555)
# n_value = int(input("Enter (n) value: "))
# n1 = int("%d" % n_value)
# n2 = int("%d%i" % (n_value, n_value))
# n3 = int("%s%s%s" % (n_value, n_value, n_value))
# print(n1+n2+n3)


# print("-" * 50)

# ---------------------------------------------------------------------------

# print the documents (syntax, descriptions) of built-in functions
# .__doc__ provides documentation of the object.
# print(help(abs))
# print(abs.__doc__)
# print(input.__doc__)
# print(help(__doc__))


# print("-" * 50)

# ---------------------------------------------------------------------------
# print calendar of given month and year
# use calendar module

# import calendar
#
# year = 2020
# month = 5
#
# # display the calendar
#
# print(calendar.month(year, month))

# print("-" * 50)

# ---------------------------------------------------------------------------

# print("""a string that you don't have to escape
#     this
#     is a multi-line
#     heredoc string -----> example
#     """)

# print("-" * 50)

# ---------------------------------------------------------------------------
# calculate number of days between two dates.

# import datetime
#
# d_one = datetime.date(2020, 5, 10)
# d_two = datetime.date(2020, 5, 1)
#
# dexter = d_one-d_two
# print(dexter.days)

# print("-" * 50)

# ---------------------------------------------------------------------------
# from math import pi
#
# r = 6
# volume = 4/3 * pi * r**3
# print(volume)

# print("-" * 50)

# ---------------------------------------------------------------------------
# number = 17
# enter_num = int(input("Enter a number: "))
#
# if enter_num > number:
#     print(abs(number-enter_num)*2)
# else:
#     print(number-enter_num)

# print("-" * 50)

# ---------------------------------------------------------------------------

# TEST if a number is close to 1000 or 2000

# def numb(n):
#     return ((abs(1000-n)<=100) or (abs(2000-n)<=100))
#
#
# print(numb(1000))
# print(numb(900))
# print(numb(800))
# print(numb(2200))

# print("-" * 50)

# ---------------------------------------------------------------------------
# calculate the sum of three given numbers
# if the values are equal then return three times of their sum

# def three_nums(a, b, c):
#     if a == b == c:
#         print("(EQ)Sum of 3 numbers = ", (a + b + c)*3)
#     else:
#         print("(NEQ)Sum of 3 numbers = ", a + b + c)
#
# print(three_nums(10,100,1000))
# print(three_nums(10,10,10))
# print(three_nums(5,5,5))

# print("-" * 50)

# ---------------------------------------------------------------------------

# def strings(a):
#     if a
# SOLUTION 1
# a = "isVish"
# if a[0:2] == 'IS' or 'is':
#     print(a)
# else:
#     n = ["IS" + a]
#     print(n)


# SOLUTION 2
# def new_string(str):
#     if len(str) >= 2 and str[:2] == "Is":
#         return str
#     return "Is" + str
#
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))

# print("-" * 50)

# ---------------------------------------------------------------------------

# def string_prints(line, num):
#     res = ''
#
#     for i in range(num):
#     gdfxc v    res = res + line
#     return res
#
# print(string_prints("coke", 2))
#  'abc' * num = 'abcabcabc'
# def convo(line, num):
#    emptystring = ""


# print("-" * 50)
# Q 20- 23 check again later
# ---------------------------------------------------------------------------
# Q 24

# Check whether passed letter is a vowel or not

# def isvowel(c):
#     vowels = 'aeiou'
#     return c in vowels
#
#
# print(isvowel("e"))
# print(isvowel("z"))

# ---------------------------------------------------------------------------
# Q 25

# check if specified val is contained in groups of values
# 3 -> [3,4,5] -> T
# 3 -> [4,1,9] -> F

# def iscontained(values, x):
#     if x in values:
#         return True
#     else:
#         return False
#
#
# print(iscontained([2, 5, 3, 4], 3))
# print(iscontained([1, 2, 4, 19],19))

# ---------------------------------------------------------------------------
# Q 26

# create a histrogram from a given list of integers

def histogram(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
          output += 'x'
          times = times -1
        print(output)

histogram([2, 3, 6, 5])
