var_a = int(input("Enter another integer a:"))
var_b = int(input("Enter another integer b:"))

if var_b > var_a:
    print("b is greater than a")
#or you can write "elif" which means "else if" if you want to add another option/statement
elif var_a > var_b:
    print("a is greater than b")
else:
    print("a == b")