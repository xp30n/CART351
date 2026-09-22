# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                  SYNTAX                    ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# a comment in python is with the pound/hashtag (these are single line comments)
# instead of using curly brackets like in javascript, for python, you put a colon and press enter, and it will automatically indent!!

print("this is correct")
# print(25+30/7) # float division
# print(25+30//7) # integer division

# print(3+2 < 5-7) # this will return a boolean (true or false)
# print(4>2)

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                 VARIABLES                  ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# with variables, you can't indent after each one (like in JavaScript)

bool_var_a = True
bool_var_b = False
bool_var_c = False

# print(bool_var_b)

not_a = not bool_var_a # the output would be false, because we're just making a statement
and_a_b = bool_var_a and bool_var_b # this will give you false because when one answer is false, the whole thing is false. Both variables have to be true

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                 DATA TYPES                 ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# Text Type: str
# Numeric Types: int (whole numbers/no decimals), float (numbers with decimals), complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray
# None Type: NoneType

# to check the type of variable something is you do this:

# testVar = 5
# print(type(testVar))

# testVar_2 = 4.6
# print(type(testVar_2))

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                PRINTING VARS               ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# my_name = "Aliyah"
# my_fav_fruit = "Mango"
# saved_str = f"Hello! my name is {my_name} and my favourite fruit is {my_fav_fruit}"
# print(saved_str)

# the order of variables is important!!

# my_name=input("Name: ") # gives the user an input in which they can type in

my_name = input("Name: ")
my_fav_fruit =  input("Fav Fruit: ")
my_fav_animal = input("Fav Animal: ")
my_fav_veg = input ("Fav Veg: ")
my_fav_color = input ("Fav Color: ")
a_saved_fstring = f"Your fav fruit is {my_fav_fruit}"

print(f"Your name is {my_name}")
print(f"Your favorite color is {my_fav_color} and You also love {my_fav_animal}s")
print(a_saved_fstring)

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                FUNCTIONS                   ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# to write a function, you start with "def"

def least_difference(x1, x2, x3) :
    #abs() returns the absolute value (the positive value of a number (-2 = is an absolute value of 2) )
    # min() returns the minimum value
    diff1 = abs(x1 - x2)
    diff2 = abs(x1 - x3)
    diff3 = abs(x2 - x3)
    return min(diff1,diff2, diff3)

print(least_difference(1,2,3))

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::        LOGICAL IF/ ELSE /ELSE IF           ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

var_a = int(input("Enter another integer a:"))
var_b = int(input("Enter another integer b:"))

if var_b > var_a:
    print("b is greater than a")
#or you can write "elif" which means "else if" if you want to add another option/statement
elif var_a > var_b:
    print("a is greater than b")
else:
    print("a == b")

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                FOR LOOPS                   ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

num = 5
for i in range (num):
    print(i)


# num = 5
# for i in range (num):
#     print(i) # this prints the number 0-4 because 0 counts as one number

sum = 0
for i in range(0, 20, 2):
    sum = sum + i
print(sum)
# output 90

# you can also use an else in the for loop >

for index in range(20):
  print(index)
else:
  print("finished for loop!")

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::                 BREAKS                     ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

  # the break keyword is used to break out a for loop or a while loop

  for index in range(10):
     print(f"look index: {index}")
     if index==3:
        break

def test_break_else(num):
  #go through loop
  for index in range(num):
    print(f"for loop :) {index}")
    #condition for break
    if index == 30:
      print(f"breaking out")
      break
  #come here if we DO NOT break
  else:
    print("finished for loop - num is less than 30!")

  #out of for loop clause
  print(f"out of the foor loop")

# test_break_else(20)
test_break_else(40)

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::               WHILE LOOPS                  ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

