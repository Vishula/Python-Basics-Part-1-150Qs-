import fact as fact

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

# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while(times > 0):
#           output += 'x'
#           times = times -1
#         print(output)
#
# histogram([2, 3, 6, 5])

# ---------------------------------------------------------------------------
# Q 27]]
# emptystring
# list to a string

# print
# def lststring(lisa):
#     emptystring = ""
#     for x in lisa:
#
#         convertedinput = str(x)
#         emptystring += convertedinput
#     print(emptystring, end=".")  # add "." to end after one loop.
#
#
# lststring(["vish", "got", 1, "Wright"])

# ---------------------------------------------------------------------------
# Q 28 & 29 & 30 already done. find and add

# ---------------------------------------------------------------------------
# Q 31 already done. find and add

#

# def gcd(x, y):
#     xval = int(input("Enter x value: "))
#     yval = int(input("Enter y value: "))
#
#     while xval > 0:
import math
# def factos(a):
# #     if a > 0:
# #         return a * math.factorial(a-1)
# #     else:
# #         return 1
# #
# #
# # print(factos(4))
# # print(factos(3))
# # print(factos(2))
# # print(factos(1))
# # print(factos(0))

# import numbers
# import fibonacci
# def fibon(n, index):
#     if index[n] != 0:
#         return index[n]
#     if n == 2 or n == 1:
#         result = 1
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#     return result
#
# print(fibon(5), 6)

# ---------------------------------------------------------------------------
# Q 32 find lcm of two (+) integers

# def gcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y,x%y)
#
# def lcm(a, b):
#     lcm = (a * b)/gcd(a, b)
#     return lcm
#
# print(lcm(50, 65))


# def lcm(x, y):
#    if x > y:
#        z = x
#    else:
#        z = y
#
#    while(True):
#        if((z % x == 0) and (z % y == 0)):
#            lcm = z
#            break
#        z += 1
#
#    return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

# ---------------------------------------------------------------------------
# Q 33 program sum of 3 given integers
# if 2 values are same sum = 0

# def summ(a, b, c):
#
#     if a == b or b == c or a ==c:
#         summ = 0
#
#     else:
#         summ = a + b + c
#     return summ
#
#
#
# print(summ(10,20,30))
# print(summ(20,50,20))


# ---------------------------------------------------------------------------
# Q 34 program sum of 3 given integers

# def twosome(a, b):
#     sum = a + b
#     if sum in range(15,20):
#         return 20
#     else:
#         return sum
#
# print(twosome(10,6))
# print(twosome(10,2))
# print(twosome(10,12))

# ---------------------------------------------------------------------------
# Q 35
# two integers are equal or difference = 5
# or sum is 5
# def program(a, b):
#     if a == b or a + b == 5 or a - b == 5:
#         return True
#     else:
#         return False
#
# print(program(5,5))
# print(program(10, 5))
# print(program(10,0))

# ---------------------------------------------------------------------------
# Q 36

# def uzi(objectA, objectB):
#     if isinstance(objectA, int) and isinstance(objectB, int):
#         return objectA + objectB
#     else:
#
#         return "Error"
#
# print(uzi(10,20))
# print(uzi(1.3,5))
# print(uzi("a", "b"))

# ---------------------------------------------------------------------------
# Q 37


# name = input("Enter name: ")
# age = int(input("Enter age: "))
# adde = input("Enter Address: ")
#
# print(name, age, adde)

# ---------------------------------------------------------------------------
# Q 38
# (x*y) * (x*y)

# def mult(x, y):
#     a = x ** 2 + y **2 + 2*x*y
#     print("({} + {}) ^ 2) = {}".format(x, y, a))
#
# mult(4,3)

# ---------------------------------------------------------------------------
# Q 39

# amt = 10000
# int = 3.5
# years = 7
#
# future_value  = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

# ---------------------------------------------------------------------------
# Q 40
# calculating distance between two points
# pythagoras theorem used for final equation
# import math
# p1 = [4, 0]
# p2 = [6, 6]
#
# # use index to refer to x1 and x2 and y1 and y2
# distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)
# print(distance)

# ---------------------------------------------------------------------------
# Q 41
# program to check if a file exist in a current folder

# import os.path
#
# print(os.path.isfile('abc.txt'))
# print(os.path.isfile("PageOne.py"))

# ---------------------------------------------------------------------------
# Q 42 later

# ---------------------------------------------------------------------------
# Q 43
# program to get os name
# platform and release info
# import platform
# import os
#
# print(os.name)
# print(platform.system())
# print(platform.release())

# ---------------------------------------------------------------------------
# Q 44
# locate py site packages
# import site;
# print(site.getsitepackages())
# ---------------------------------------------------------------------------
# Q 45
# program to call an external command in py

# from subprocess import call
# call(['ls', '-l'])

# ---------------------------------------------------------------------------
# Q 46
# program to get the path
# and name of the file currently executing

# import os
# print("current file name: ", os.path.realpath(__file__))

# ---------------------------------------------------------------------------
# Q 47
# program to find out number of CPU's using
import multiprocessing

print(multiprocessing.cpu_count())


# ---------------------------------------------------------------------------
# Q 48
# program to parse/send a string to
# float or integer
# word = float(input("Enter a string: "))
# float = float(word)
# integer = int(word)
# print("Float: ", float)
# print("Integer: ", integer)


# def string2fi(word):
#
#     convertedfloat = float(word)
#     convertedint = int(float(word))
#     print(convertedfloat)
#     print(convertedint)
#
# string2fi("246.231")

# ---------------------------------------------------------------------------
# Q 49
#

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/Vishula/Desktop') if isfile(join('/Users/Vishula/Desktop', f))]
print(files_list);
