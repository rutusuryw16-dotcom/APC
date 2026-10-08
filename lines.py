with open ("example.txt","r") as file:
 content = file.read()
print("character",len(content))
with open(" sample.txt","r") as file:
  c = file.readlines()
print("lines",len()) 

words = content.split()
print("words",len(words))