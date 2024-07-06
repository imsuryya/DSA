# Write a Python function to check if a given string is a palindrome or not.

palindrome = str(input("Enter the palindrome word: "))
if palindrome[::-1] == palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


   
