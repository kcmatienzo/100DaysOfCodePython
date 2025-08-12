import random

ASCII = {
    "rock": r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}

CHOICES = ("rock", "paper", "scissors")

comp = random.choice(CHOICES)

# print(ASCII[comp])

def decide_winner(player: str, comp: str):
    if player == comp:
        return "tie"
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "win" if (player, comp) in wins else "lose"

def prompt_player() -> str:
    while True:
        choice = input("Choose (rock/paper/scissors) or 'q' to quit: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            return "quit"
        if choice in CHOICES:
            return choice
        print("Invalid choice. Try again.")

def main():
    print("Welcome to Rock - Paper - Scissors (ASCII)!\n")
    player_score = 0
    comp_score = 0
    rounds = 0

    try:
        while True:
            player = prompt_player()
            