import random

options=("rock","scissor","paper")

running=True

while running:

  player = None
  computer = random.choice(options)


  while player not in options:
    player=input("Enter a choice(rock,paper,scissor) : ")

  if player==computer:
    print("Its a draw")
  elif player=="rock" and computer=="scissor":
    print("you win!!")
  elif player=="scissor" and computer=="paper":
    print("you win!!")
  elif player=="paper" and computer=="rock":
    print("you win!!")
  else:
    print("you lose")

  print(f"your choice : {player}")
  print(f"Computer chocie : {computer}")

  play=input("Play again> (y/n): ").lower
  if not play=="y":
    running=False
print("Thanks for playing")

