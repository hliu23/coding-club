import random

while True:
  print("Rock, Paper, Scissors!")
  input1 = input()
  if input1 == "rock" or input1 == "paper" or input1 == "scissors": 
    input2 = random.choice(["rock", "paper", "scissor"])
    print(input2)
    if input1 == "rock":
      if input2 == "scissor": print("You won!")
      elif input2 == "paper": print("You lost!")
      else: print("You tied!")
    elif input1 == "paper":
      if input2 == "rock": print("You won!")
      elif input2 == "scissor": print("You lost!")
      else: print("You tied!")
    else:
      if input2 == "paper": print("You won!")
      elif input2 == "rock": print("You lost!")
      else: print("You tied!")

  else: print("invalid input")