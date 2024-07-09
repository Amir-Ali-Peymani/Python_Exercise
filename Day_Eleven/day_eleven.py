#black jack game
# 1-objective ->  over 21 you lose
# 2-objective -> user first get 2 card
# 3-objective -> three 10 number
# 4-objective -> 
import random

# List of card values
cards_number = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dealer and player hands
dealer = []
player = []

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards_number)

def calculate_score(hand):
    """Calculates the score of a hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_scores(player_score, dealer_score):
    """Compares the scores of the player and dealer."""
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "Dealer has blackjack! You lose."
    elif player_score == 0:
        return "You have blackjack! You win."
    elif player_score > 21:
        return "You went over. You lose."
    elif dealer_score > 21:
        return "Dealer went over. You win."
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."

def game_player():
    """Plays a round of blackjack for the player."""
    player.append(deal_card())
    player.append(deal_card())
    dealer.append(deal_card())
    dealer.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == 'y':
                player.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)

    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

def game_menu():
    """Displays the game menu and starts the game."""
    print("Welcome to Blackjack!")

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        player.clear()
        dealer.clear()
        game_player()

    print("Good Bye!!")

# Start the game
game_menu()
