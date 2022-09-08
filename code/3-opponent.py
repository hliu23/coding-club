import random

while True:
  print("Rock, Paper, Scissors!")
  input1 = input()
  if input1 == "rock" or input1 == "paper" or input1 == "scissors": 
    input2 = random.choice(["rock", "paper", "scissor"])
    print(input2)
  else: print("invalid input")