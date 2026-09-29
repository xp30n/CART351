# A dictionary is like a list, but you don't look up values in a dictionary by their index
# you look them up using a key or a uniqueidentifier for that value

# This is a dictionary with one key (Cart_253_A) associated with a value (Pippin Bar)
# 'key': 'value'

{'Cart_253_A':'Pippin Bar'}

# More entries:

{'Cart_253_A':'Pippin Bar',
'Cart_211':'Brad Todd',
'Cart_214':'Joanna Berzowska', 
'Cart_215':'Jonathan Lessard'}

# Putting a key to a value is sometimes called "mapping"
# In the above example, the key Cart_253_A maps to the value "Pippin Bar"
# You can also assign a dictionary to a variable

class_professors = {'Cart_253_A':'Pippin Bar',
                    'Cart_211':'Brad Todd',
                    'Cart_214':'Joanna Berzowska', 
                    'Cart_215':'Jonathan Lessard'}

# The variable has a type as well
type(class_professors)
# the result will be: <class 'dict'>

# keys and values can be any data type, not only strings
# For example:
# This is a dictionary that maps integers to lists of floating point numbers 
# (A number with a decimal that can have a decimal part)
{17: [1.6, 2.45], 42: [11.6, 19.4], 101: [0.123, 4.89]}

# A dictionary can also be empty with no value/ley
{}

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::           GETTING VALUES OUT OF DICTIONARIES          ::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Our main use of dictionaries will be writing an expression 
# that evaluates to the value for a particular key
# We do it with the same syntax we use to get a value index from a list
# If we want to know who is teacher Cart_253_A, we would write the expression:

class_professors["Cart_253_A"]

# If we put a key that does not exist in the dictionary
# we get an error similar to one we get when trying to access an element of an array past the end
# print(class_professors["Cart_255"])

# the thing you put inside the brackets doesn't have to be a string; it can be any
# Python expression, as long as it evaluates to something that is a key in the dictionary:
cart_class = 'Cart_214'
print(class_professors[cart_class])
# The result will be <Joanna Berzowska >
# it's basically telling python to find whatever is labeled Cart_214 
# and give me the value attached to it

