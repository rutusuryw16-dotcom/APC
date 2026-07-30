#Sentence Reversal 
#Reverse the order of words in a sentence without changing the words themselves.
sentence = input("Enter a sentence: ")

words = sentence.split()
reverse = words[::-1]

result = " ".join(reverse)

print("Reversed sentence:", result)
