import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print ("Python number Guessing Game")
print (f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input ("Enter you guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess <lowest_num or guess> highest_num:
             print("Guess is out of the range")
             print (f"Please select a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("To low! Try Again")
        elif guess>answer:
            print("To High! Try Again")
        elif guess==answer:
            print("HOORAYYYY! Your guess is correct")
            print(f"Number of Guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print (f"Please select a number between {lowest_num} and {highest_num}")
        