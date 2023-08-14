# Poker Game Implementation

This project implements a simple version of the Texas Hold'em poker game using Python. This includes classes for managing players, cards, decks, the game table, and the dealer buttons. The project demonstrates how to simulate the different stages of a poker game, such as dealing cards, betting rounds and community cards.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Classes](#classes)
- [Remaining Work and Planned Additions](#remaining-work-and-planned-additions)
- [Contributing](#contributing)

## Description

This Python project simulates a poker game. It includes the following key components:

- `Player`: Represents a poker player with attributes such as name, hand, stack size, and actions.
- `Card`: Represents a playing card with a suit and rank.
- `Deck`: Manages a deck of playing cards, allowing shuffling and dealing.
- `DealerButton`: Manages the dealer button's position in the game.
- `Table`: Represents the poker table, including players, community cards, and the pot.
- `Game`: Orchestrates the poker game, handling rounds, bets, and actions.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the `game.py` script to start the poker game.

In the `game.py` script, you can customize the game setup and interactions. Here are some examples of how you can interact with the game:

- Add Players: In the `if __name__ == '__main__':` block, you can add players to the game using the `add_player` method of the `Game` class. For example:

    ```python
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Carol")
    
    the_game.add_player(player1)
    the_game.add_player(player2)
    the_game.add_player(player3)
    ```

- Modify Player Stacks: You can change the stack sizes of players by using the `add_to_stack` and `sub_from_stack` methods of the `Player` class. For example:

    ```python
    player1.add_to_stack(200)  # Add 200 chips to player's stack
    player2.sub_from_stack(50)  # Subtract 50 chips from player's stack
    ```

- Remove Players: You can remove players from the game using the `remove_player` method of the `Table` class. For example:

    ```python
    the_game.table.remove_player(player3)  # Remove Carol from the game
    ```

Remember to adjust the interactions according to the current state of your project and the specific features you've implemented.


## Usage

The project simulates a poker game with simplified rules. Players are automatically added to the table, and the game progresses through different stages:

1. Preflop: Players receive two private cards.
2. Flop: Three community cards are dealt face-up.
3. Turn: An additional community card is dealt.
4. River: The final community card is dealt.
5. Showdown: Players reveal their hands, and the winner is determined.

During each round, players take turns performing actions such as calling, raising, checking, and folding. The game implements basic betting logic and tracks the pot size.

## Classes

### Player

Represents a player in the poker game with attributes and actions.

- Attributes:
  - `name`: Player's name.
  - `hand`: List of cards in the player's hand.
  - `stack`: Available chips.
  - `curent_in_pot`: Chips bet in the current round.
  - `still_in_hand`: Indicates if the player is still in the hand.

- Actions:
  - `bet_call_raise(amount)`: Perform a bet, call, or raise.
  - `fold()`: Fold the player's hand.
  - `check()`: Check if the player can check.

### Card

Represents a playing card with a suit and rank.

- Attributes:
  - `suit`: Card's suit.
  - `rank`: Card's rank.

### Deck

Manages a deck of playing cards.

- Attributes:
  - `suits`: List of card suits.
  - `ranks`: List of card ranks.
  - `stack`: List of cards in the deck.

- Actions:
  - `shuffle()`: Shuffle the deck.
  - `deal_card()`: Deal a card from the deck.

### DealerButton

Manages the position of the dealer button.

- Attributes:
  - `position`: Current position of the dealer button.

- Actions:
  - `forward_position(num_of_players)`: Move the button's position forward.

### Table

Represents the poker table.

- Attributes:
  - `places`: Dictionary of player positions.
  - `community_cards`: List of community cards.
  - `pot`: Current pot size.
  - `last_bet_size`: Size of the last bet.
  - `last_player`: Player who made the last action.

- Actions:
  - Various methods to manage players, community cards, and pot size.

### Game

Orchestrates the poker game.

- Attributes:
  - `deck`: Instance of the `Deck` class.
  - `table`: Instance of the `Table` class.
  - `dealer_button`: Instance of the `DealerButton` class.
  - `players`: List of players in the game.

- Actions:
  - `add_player(player)`: Add a player to the game.
  - `set_dealer()`: Set the dealer button's position.
  - `deal_cards()`: Deal cards to players.
  - `start()`: Start the poker game.
  - `start_hand()`: Start a new hand.
  - `round(occupied_seats, start_position)`: Perform a betting round.
  - Other methods to handle player actions, bets, and rounds.

# Remaining Work and Planned Additions

## Showdown Functionality
- Implement the `showdown` function to reveal the remaining players' cards.
- Determine the winning hand based on hand strength evaluation.

## Hand Strength Evaluation
- Develop functions to evaluate the strength of players' hands.
- Identify various combinations such as straight flush, four of a kind, full house, flush, straight, three of a kind, two pairs, one pair, and high card.

## End of Hand Handling
- Create an `end_hand` method within the `Game` class to handle the conclusion of a hand.
- Reset player states, pot size, and community cards to their initial values.
- Move the dealer's button to the next seat in a circular manner.
- Update the dealer's position for the next hand using the new method.

## Testing and Refinement
- Thoroughly test the game for various scenarios to ensure proper functionality.
- Address any bugs, glitches, or issues that may arise during testing.
- Review and refactor the codebase to improve readability, modularity, and maintainability.
- Consider breaking down the code into separate modules or classes for better organization.

## User Interaction and Interface
- Consider creating a user-friendly interface to facilitate player interactions.
- Allow players to input their actions using a command-line interface or graphical buttons.

## Documentation and Instructions
- Provide clear documentation on how to run and interact with the game.
- Include instructions for players to understand the game's rules and mechanics.

## Scalability and Multiplayer
- Consider adding network functionality to enable multiplayer gameplay over the internet.

## Graphics and Visualization
- If desired, enhance the game's appearance with graphics and visual elements.
- Display cards, player stacks, pot size, and community cards in a visually appealing way.

## Error Handling and Input Validation
- Implement robust error handling and input validation to prevent crashes or unexpected behavior.
- Handle cases where players input invalid actions or incorrect values.


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to create a pull request or submit an issue.
