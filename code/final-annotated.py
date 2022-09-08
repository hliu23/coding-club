import random

# keep starting new rounds of rock, paper, scissors
while True:
  # print the prompt
  print("Rock, Paper, Scissors!")

  # receive input from the user
  input1 = input()

  # check if user input is same as one of the accepted values
  if input1 == "rock" or input1 == "paper" or input1 == "scissors": 

    # generate the opponent's move randomly
    input2 = random.choice(["rock", "paper", "scissors"])
    print(input2)

    # player: rock
    if input1 == "rock":
      # opponent: scissors
      if input2 == "scissors": print("You won!")
      # opponent: paper
      elif input2 == "paper": print("You lost!")
      # opponent: rock
      else: print("You tied!")

    # player: paper
    elif input1 == "paper":
      # opponent: rock
      if input2 == "rock": print("You won!")
      # opponent: scissors
      elif input2 == "scissors": print("You lost!")
      # opponent: paper
      else: print("You tied!")

    # player: scissors
    else:
      # opponent: paper
      if input2 == "paper": print("You won!")
      # opponent: rock
      elif input2 == "rock": print("You lost!")
      # opponent: scissors
      else: print("You tied!")

  # user input is not one of the accepted values, so start a new round of the game
  else: print("invalid input")