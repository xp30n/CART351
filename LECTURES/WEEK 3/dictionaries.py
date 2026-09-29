# A dictionary is like a list, but you don't look up values in a dictionary by their index
# you look them up using a key or a uniqueidentifier for that value

# This is a dictionary with one key (Cart_253_A) associated with a value (Pippin Bar)

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


