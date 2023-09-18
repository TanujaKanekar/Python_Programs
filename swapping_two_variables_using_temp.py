#program to swap two numbers using temporary variable

x = input("Enter the value of x: ") #Taking the input from the user
y = input("Enter the value of y: ")

#Using temporary variable to swap the two numbers
temp = x
x    = y
y    = temp

print("Before swapping the x value: {}".format(x))
print("After swapping the y value: {}".format(y))
