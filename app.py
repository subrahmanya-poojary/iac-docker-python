from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)
#app.run(host="0.0.0.0", port=5000)
# Game state variables
player_score = 0
computer_score = 0
player_wins = 0
computer_wins = 0

@app.route('/in-game-session')
def index():
    return render_template('main.html', player_score=player_score, computer_score=computer_score, player_wins=player_wins, computer_wins=computer_wins)

@app.route('/')
def start_game():
    global player_wins, computer_wins, player_score, computer_score
    player_wins = 0
    computer_wins = 0
    player_score = 0
    computer_score = 0
    return render_template('start_game.html')

@app.route('/play', methods=['POST'])
def play():
    global player_score, computer_score, player_wins, computer_wins

    # Get the player's choice from the form
    player_choice = request.json.get('choice')
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
        winner = "Tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
        winner = "Player"
        player_score += 1
    else:
        result = "You lose!"
        winner = "Computer"
        computer_score += 1

    # Update star indicators
    if winner == "Player":
        player_wins += 1
    elif winner == "Computer":
        computer_wins += 1

    # Check if someone has won 3 points
    if player_wins == 3:
        return jsonify({
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result,
            "winner": winner,
            "game_over": True,
            "final_winner": "Player"
        })
    elif computer_wins == 3:
        return jsonify({
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result,
            "winner": winner,
            "game_over": True,
            "final_winner": "Computer"
        })

    # If no one has won yet, continue the game
    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
        "winner": winner,
        "game_over": False
    })

@app.route('/game_over')
def game_over():
    return render_template('game_over.html', player_wins=player_wins, computer_wins=computer_wins)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
