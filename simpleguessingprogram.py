import random

def game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    print("Guess the number if you're correct you win!")
    print(f"You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        print("\nProvide your guess number: ")
        try:
            guess = int(input())
            attempts += 1
            
            remaining = max_attempts - attempts
            
            if secret_number == guess:
                print(f"Your guess was correct, you win in {attempts} attempt(s)!")
                break
            elif secret_number > guess:
                print(f"Your guess is too low! Attempts remaining: {remaining}")
            else:
                print(f"Your guess is too high! Attempts remaining: {remaining}")
                
            if remaining == 0:
                print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
        except ValueError:
            print("Please enter a valid number!")
    
    print("Press 1 to play again or any other key to exit.")
    try:
        replay = int(input())
        if replay == 1:
            game()
        else:
            print("Thanks for playing, see you again!")
    except ValueError:
        print("Thanks for playing, see you again!")

game()
