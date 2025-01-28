import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors")
print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
player_answer = int(input())
computer_answer = random.randint(0, 2)

if player_answer == 0 and computer_answer == 1:
    print("You Lose")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == 1 and computer_answer == 2:
    print("You Lose")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == 2 and computer_answer == 0:
    print("You Lose")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == 1 and computer_answer == 0:
    print("You Win")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == 2 and computer_answer == 1:
    print("You Win")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == 0 and computer_answer == 2:
    print("You Win")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
elif player_answer == computer_answer:
    print(f"Its a Draw: {player_answer} and {computer_answer} ")
    print(game_images[player_answer])
    print("-------------------------------")
    print(game_images[computer_answer])
else:
    print("Invalid Inputs")