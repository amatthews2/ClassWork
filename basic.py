#basics
x = input("Enter a letter: ")
print("you entered {}".format(x))

#print(x)


#the double == is a compare
#the = is assign
# the colon the start of the block of code (indented 4 spaces)
if x== "a":
    a = 1
    b = 2
    c = a + b
    print(" {} + {} = {}".format(a, b, c))
elif x == "s":
    a = 20
    b = - 3
    c = a - b
    print (" {} - {} = {}".format(a, b, c))
elif x == "m":
    a = 2
    b = 3
    c = a*b
    print (" {} * {} = {}".format(a, b, c))
else:
    print("The {} command is not recognized".format(x))
