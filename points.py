

def points():
    score=0
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