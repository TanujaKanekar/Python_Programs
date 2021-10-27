# Program to reverse an integer

#Takes the input from the user
num = int(input("Please enter the number: "))

#Initially reverse_num is intialized to 0
reverse_num=0

while num!=0:
     digit=num%10
     reverse_num=reverse_num * 10 + digit
     num //=10
print("Reversed Number is: "+str(reverse_num))
