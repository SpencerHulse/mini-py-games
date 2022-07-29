import random

def play():
  user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(["r", "p", "s"])

  if user == computer:
    return "Draw!"

  if is_win(user, computer):
    return"You win!"

  return "You lose!"

def is_win(player, opponent):
  if (player == "r" and opponent == "p") or \
  (player == "p" and opponent == "s") or \
  (player == "s" and opponent == "r"):
    return True

print(play())