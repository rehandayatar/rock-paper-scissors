import random
import signal
import sys

def handler(sig, frame):
    print("\nProgram stopped by user")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

options = ["rock","paper","scissors"]
running = True
while running:
    
    computer = random.choice(options)

    player = input("Enter your choice(rock,paper,scissors):").lower()

    if player not in ["rock","paper","scissors"]:
        print("invalid choice")
        continue
    
    print(f"player : {player}")
    print(f"computer : {computer}")    

    if  player == computer:
        print("Its a draw")
    elif player == "rock" and computer == "scissors":
        print("You win")         
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You Lose!")    
    play_again = input("Do you wanna play again (y/n):").lower()    
    if  play_again != "y":
        running = False
    
    
    print()
print("Thanks for playing!")    








import random
import signal
import sys

def handler(sig, frame):
    print("\nProgram stopped by user")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

options = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
rounds_to_win = 2   # Best of 3 → first to 2 wins

while player_score < rounds_to_win and computer_score < rounds_to_win:
    computer = random.choice(options)
    player = input("Enter your choice (rock, paper, scissors): ").lower()

    if player not in options:
        print("Invalid choice\n")
        continue

    print(f"Player   : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a draw")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win this round")
        player_score += 1

    else:
        print("Computer wins this round")
        computer_score += 1

    print(f"Score → You: {player_score} | Computer: {computer_score}\n")

# Final result
if player_score == rounds_to_win:
    print("🎉 You won BEST OF 3!")
else:
    print("❌ Computer won BEST OF 3!")

print("Thanks for playing!")
