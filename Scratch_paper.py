# for loops are used when you
# want to repeat a block of
# code fixed number of times.

# object type of int has no len()

# for var in range(0,100):
#     print(var, len(var))

#  take a list as a parameter
#  returns the number of items in the list



# colors = ["red", "green", "blue", "purple"]
# for i in range(len(colors)):
#     print(colors[i])

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")

print("--" * 25)

