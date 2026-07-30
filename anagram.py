#Anagram Check 
#Check whether two strings are anagrams.


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")
