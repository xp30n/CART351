# # num = 5
# # for i in range (num):
# #     print(i) # this prints the number 0-4 because 0 counts as one number

# sum = 0
# for i in range(0, 20, 2):
#     sum = sum + i
# print(sum)
# # output 90

# # you can also use an else in the for loop >

# for index in range(20):
#   print(index)
# else:
#   print("finished for loop!")

#   #BREAK

#   # the break keyword is used to break out a for loop or a while loop

#   for index in range(10):
#      print(f"look index: {index}")
#      if index==3:
#         break

# def test_break_else(num):
#   #go through loop
#   for index in range(num):
#     print(f"for loop :) {index}")
#     #condition for break
#     if index == 30:
#       print(f"breaking out")
#       break
#   #come here if we DO NOT break
#   else:
#     print("finished for loop - num is less than 30!")

#   #out of for loop clause
#   print(f"out of the foor loop")

# # test_break_else(20)
# test_break_else(40)

# ::::::::::::::::::::::::::::::::::::::::::::::::
# ::               WHILE LOOPS                  ::
# ::::::::::::::::::::::::::::::::::::::::::::::::

# Condition of the while loop
number =int(input("Please input number: ")) 
while number < 20 :  
    print(f"in while loop: number is {number}\n")
    # Increment the value of the variable "number by 1"
    number = number+1
print(f"after the while loop: number is: {number}")