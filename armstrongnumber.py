#Program to find if the number is Armstrong or not

#Take the input from the user
num = int(input("enter the number: "))

#Initialize the sum variable to zero
sum = 0

#assign temp value with the entered number
temp = num

#if the number is greater than zero perfrom following operations
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

#if entered number is equal to sum number then the number is armstrong
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

