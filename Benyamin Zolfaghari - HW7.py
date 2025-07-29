# Benyamin Zolfaghari - HW7 ---------------------------------------------------------------


import requests

def start_game():
    url_game = 'https://mastermind.darkube.app/game'
    try:
        response = requests.post(url_game)
        response.raise_for_status()
        game_id = response.json()["game_id"]
        print(f"Your game id is {game_id}.")
        return game_id
    except requests.exceptions.RequestException as e:
        print(f"Error starting game: {e}")
        return None

def send_guess(game_id, guess):
    url_guess = "https://mastermind.darkube.app/guess"
    body = {"game_id": game_id, "guess": guess}
    try:
        response = requests.post(url_guess, json=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending guess: {e}")
        return None

def prompt_guess(game_id):
    while True:
        guess = input("Enter your guess (4 unique digits from 1-6): ").strip()

        if len(guess) != 4:
            print("Guess must be exactly 4 characters long.")
            continue
                
        if not guess.isdigit():
            print("Guess must contain only digits (1-6).")
            continue
            
        if any(digit not in '123456' for digit in guess):
            print("All digits must be between 1 and 6.")
            continue
                
        if len(set(guess)) != 4:
            print("All digits must be unique (no duplicates).")
            continue

        response = send_guess(game_id, guess)
        if not response:
            continue
            
        exact = response.get("black", 0)
        near = response.get("white", 0)
        print(f"Result: {exact} exact, {near} near")
        
        if exact == 4:
            print("Congratulations! You've guessed the correct code!")
            break

def run_game():
    print("Welcome to Mastermind!")
    print("Try to guess the 4-digit code with digits from 1 to 6 (all unique).")
    print("After each guess, you'll get feedback:")
    print("- 'Exact' means correct digit in the correct position")
    print("- 'Near' means correct digit but in the wrong position")
    
    game_id = start_game()
    if game_id:
        prompt_guess(game_id)
    print("Thanks for playing!")

run_game()
