# Author: Benyamin Zolfaghari
# Assignment: AI Homework 4

## 🧩 Step 1: Initialize the Game Board ::..................

def initialize_board():
    global board
    board = ["-"] * 9
    return board
game_board = initialize_board()
print(game_board)


## 🧩 Step 2: Display the Game Board ::.....................

def display_board(board):
    
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---------")
display_board(game_board)


## 🧩 Step 3: Define the Players ::..........................

def define_players():
    global player1, player2
    while True:
        player1 = input("Player 1, choose X or O: ").upper()
        if player1 in ["X", "O"]:
            break
        else:
            print("Invalid input. Please choose X or O.")

    if player1 == "X" :
        player2 = "O"
    else :
        player2 = "X"
    print(f"Player 1 is {player1} and Player 2 is {player2}.")
    return player1, player2


player1, player2 = define_players()
current_player = player1 

## 🧩 Step 4: Create a Player Move Function ::.........................

def player_move(board, current_player):
    while True:
        try:
            move = int(input(f"{current_player}, choose a position (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            idx = move - 1
            if board[idx] == "-":
                board[idx] = current_player 
                print("Move registered successfully.")
                break
            else:
                print("This position is already taken. Try another.")
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")


## 🧩 Step 5: Check for a Winner ::......................................

def winner(board):
    
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            print(f"WIN! Row completed by {board[i]}")
            return board[i]
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            print(f"WIN! Column completed by {board[i]}")
            return board[i]
    
    if board[0] == board[4] == board[8] and board[0] != "-":
        print(f"WIN! Diagonal completed by {board[0]}")
        return board[0]
    
    if board[2] == board[4] == board[6] and board[2] != "-":
        print(f"WIN! Diagonal completed by {board[2]}")
        return board[2]
    
    if "-" not in board:
        print("It's a tie!")
        return "Tie"
    
    return None

# Next Steps : Final Loop :::...................................................


while True:
    display_board(board)
    player_move(board, current_player)
    result = winner(board)
    if result in [player1, player2]:
        print(f"Player {result} wins!")
        break
    elif result == "Tie":
        print("Game ended in a tie!")
        break
    if current_player == player1 :
        current_player = player2
    else :
        current_player = player1











