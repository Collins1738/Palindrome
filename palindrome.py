x=""
while x != "exit":
  x=input("Type in a word and I will tell you if this word is a palindrome: \n(type exit to end)\n")
  y=[]
  y.append(x)
  z= x[::-1]
  if x==z:
    print ('This is a palindrome')
  else:  
    print("This is not a palindrome")
  
print("\n\n\n\n\nKeep up!")
