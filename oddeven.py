#Python program to check if input number is odd or even

#Take the input from the user
num= int(input("Enter the number: "))

#check if the number is divisible by 2
#if number is divisibel by 2 then the number is even

if(num%2)==0:
   print("even number")
else:
   print("{0} is Odd number".format(num)) #here {} is replacement field for num
