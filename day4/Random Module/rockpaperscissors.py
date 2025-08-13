import random #Import the module Random

#r""" means raw string, backslashes inside the art are treated literally
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

# Winner logic function. 
def decide_winner(player: str, comp: str):
    if player == comp:
        return "tie"
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "win" if (player, comp) in wins else "lose"

# Player input logic function.
def prompt_player() -> str:
    while True:
        choice = input("Choose (rock/paper/scissors) or 'q' to quit: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            return "quit"
        if choice in CHOICES:
            return choice
        print("Invalid choice. Try again.")

# Game Loop
def main():
    print("Welcome to Rock - Paper - Scissors (ASCII)!\n")
    player_score = 0
    comp_score = 0
    rounds = 0

    try:
        while True:
            player = prompt_player()
            if player == "quit":
                break

            comp = random.choice(CHOICES)
            result = decide_winner(player, comp)
            rounds += 1
            
            #Showing Results
            print(f"\nYou chose: {player}")
            print(ASCII[player])
            print(f"Computer chose: {comp}")
            print(ASCII[comp])

            if result == "win":
                player_score += 1
                print("You win this round!")
            elif result == "lose":
                comp_score += 1
                print("You lose this round.")
            else:
                print("It's a tie!")
            
            print(f"Score -- You: {player_score}  Computer: {comp_score}  (Rounds: {rounds})\n")

    #Exiting with friendly message instead of crashing
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. Exiting...")

    # Shows final results after quitting
    print("\nFinal Score:")
    print(f"You: {player_score}  Computer: {comp_score}  Rounds played: {rounds}")
    if player_score > comp_score:
        print("Overall winner: YOU!")
    elif player_score < comp_score:
        print("Overall winner: Computer")
    else:
        print("Overall: It's a tie!")
    print("Thanks for playing!")    
    
# Runs the main function
if __name__ == "__main__":
    main()