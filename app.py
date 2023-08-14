from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='templates') 

def draw_two_cards(deck, num_participants):
    """
    Randomly selects two unique cards for each player from the deck of cards.

    Parameters:
        deck (list of lists): A two-dimensional list representing the deck of cards.
            Each cell in the deck should initially contain a boolean value (False),
            indicating that the corresponding card has not been used.

    Returns:
        list of lists: A two-dimensional list representing the cards selected for each player.
            Each element of the outer list represents a player and contains a list of two tuples,
            each tuple representing the position (suit_index, card_index) of the selected card.

    Notes:
        - The `deck` parameter should be a list of size 4 (representing suits) where each element
          is a list of size 13 (representing card values), initially containing False.
        - The function ensures that each card is selected only once for each player.
    """
    players = num_participants
    cards_per_player = 2
    player_cards = [[] for _ in range(players)]  # Array to store each player's two cards

    for _ in range(cards_per_player):
        for player in range(players):
            while True:
                suit_index = random.randint(0, 3)
                card_index = random.randint(0, 12)
                position = (suit_index, card_index)

                if not deck[suit_index][card_index]:
                    deck[suit_index][card_index] = True
                    player_cards[player].append(position)
                    break

    return player_cards

def get_card_value(card_index):
    """
    Maps the card index to the corresponding card value.

    Parameters:
        card_index (int): The index of the card (0 to 12).

    Returns:
        str: The corresponding card value (A, 2, 3, ..., 10, J, Q, K).
    """
    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return card_values[card_index]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    num_participants = int(request.args.get('num_participants', 6))  # Set a default value of 6 if not provided
    if 4 <= num_participants <= 9:
        deck_of_cards = [
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False]
        ]

        player_cards = draw_two_cards(deck_of_cards, num_participants)
        results = []

        for index, cards in enumerate(player_cards, start=1):
            player_number = index
            cards_info = []

            for position in cards:
                suit_index, card_index = position
                suit_values = ['h', 's', 'd', 'c']
                card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

                suit = suit_values[suit_index]
                card_value = get_card_value(card_index)
                card_text = card_values[card_index]
                if card_index == 10:
                    card_text = 'J'
                elif card_index == 11:
                    card_text = 'Q'
                elif card_index == 12:
                    card_text = 'K'
                elif card_index == 0:
                    card_text = 'A'

                if card_index == 9:
                    card_text = '10'

                cards_info.append(f"{card_text}{suit}")

            results.append(f"Player {player_number} gets {', '.join(cards_info)} cards.")

        return render_template('results.html', results=results)
    else:
        return "Invalid number of participants. Please enter a number between 4 and 9."

if __name__ == '__main__':
    app.run(debug=True)