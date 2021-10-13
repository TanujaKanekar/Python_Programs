#Program to check if two strings are Anagram
""" Two strings are said to be anagram if we can form one string by arranging the characters of another string.
For example, Race and Care. Here, we can form Race by arranging the characters of Care."""

#Take two input strings from the user
str1= str(input("enter string1: "))
str2= str(input("enter string2: "))

#Convert the input string into lowercase
str1 = str1.lower()
str2 = str2.lower()

#If length of string1 is equal to string2 then move to further conditions else print entered strings are not anagram
if(len(str1)== len(str2)):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if (sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram. ")
    else:
        print(str1 + " and " + str2 + " are not anagram. ")

else:
    print(str1 + " and " + str2 + " are not anagram. ")
        
