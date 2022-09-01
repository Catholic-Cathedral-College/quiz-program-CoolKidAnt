print("do you want to participate in a quiz yes/no?")
block=True

while block:
 answer=input("")
 if answer == "No":
  print("no quiz then \n")
 elif answer == "yes":
  print("Ok lets see if you'll survive a zobie apocalypse")
 else:
  print("invalid input")
   block==False
