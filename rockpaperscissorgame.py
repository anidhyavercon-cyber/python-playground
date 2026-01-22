import random

options = ("Rock" , "Paper", "Scissor") 
running = True

while running:
    
    player = None
    computer = random.choice(options)
        
    while player not in options:
        
        player = input ("Enter a choice (Rock , Paper, Scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "Rock" and computer == "Scissor":
        print("You win")
    elif player == "Paper" and computer == "Rock":
        print("You win")
    elif player == "Scissor" and computer == "Paper":
        print("You win")
    else:
        print("You lose")
        
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
    
print ("Thanks for Playing")