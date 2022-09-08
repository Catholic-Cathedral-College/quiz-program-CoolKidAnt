import dic
import points
score=0

loop=True
while loop:
 print("do you want to participate in a quiz yes/no?")
 answer=input("")
 if answer.lower() == "no":
  print("no quiz then \n")
 elif answer.lower() == "yes":
  print("Ok lets see if you'll survive an alien apocalypse")
  loop=False
 else:
   print("invalid input")


print(dic.scene.get(1))
answer=input("")
valid_input = False
while not valid_input:
  if answer.lower() == ("a"):
    score+=10
    valid_input = True
  elif answer.lower()== ("b"):
    score+=7
    valid_input = True
  elif answer.lower() == ("c"):
    score+=5
    valid_input = True
  else: 
    print("invalid")
    answer = input()

print(dic.scene.get(2))
answer=input("")
valid_input = False
while not valid_input:
  if answer.lower() == ("a"):
    score+=10
    valid_input = True
  elif answer.lower()== ("b"):
    score+=7
    valid_input = True
  elif answer.lower() == ("c"):
    score+=5
    valid_input = True
  else: 
    print("invalid")
    answer = input()

print(score)





