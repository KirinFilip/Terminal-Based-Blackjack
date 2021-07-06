import random

# ---------------------------------------------------------------------------------
# Deck:

# 1 deck of 52 cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# Deals two cards to a hand
def deal():
    hand = []
    for i in range(2):
        card = random.choice(deck)
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand

# ---------------------------------------------------------------------------------
# Player decisions:

# hit = request another card from the dealer
def hit(hand):
    card = random.choice(deck)
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)

    return hand

# surrender = you surrender, only if dealer has A, K, Q, J or 10
def surrender(dealer_hand):
    check_surrender = ( 
        dealer_hand[0] == "A"
        or dealer_hand[0] == "K"
        or dealer_hand[0] == "Q"
        or dealer_hand[0] == "J"
        or dealer_hand[0] == 10
    )
    if check_surrender:
        print("Player surrendered")
        play_again()
    else:
        print("You can not surrender!")

# ---------------------------------------------------------------------------------
# Keeping score:

# return total value of cards
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K": 
            card = 10
        elif card == "A":
            if total < 11: card = 11
            else: card = 1
        total += card
    return total

# check for blackjack
def check_blackjack(hand):
    if total(hand) == 21:
        print("Player wins, Blackjack!")
        play_again()

# compare player and dealer results and print winner
def check_result(player_hand, dealer_hand):
    if total(player_hand) == 21:
        print_result(player_hand, dealer_hand)
        print("You win!, Blackjack")
        play_again()

    elif total(dealer_hand) == 21:
        print_result(player_hand, dealer_hand)
        print("Dealer wins, Blackjack")
        play_again()

    elif total(player_hand) > 21:
        print_result(player_hand, dealer_hand)
        print("You busted, you lose.")
        play_again()

    elif total(dealer_hand) > 21:
        print_result(player_hand, dealer_hand)
        print("Dealer busts, You win!")
        play_again()

    elif total(player_hand) > total(dealer_hand):
        print_result(player_hand, dealer_hand)
        print("You win!")
        play_again()

    elif total(player_hand) < total(dealer_hand):
        print_result(player_hand, dealer_hand)
        print("Dealer wins!")
        play_again()

    elif total(player_hand) == total(dealer_hand):
        print_result(player_hand, dealer_hand)
        print("It's a Draw (Push)!")
        play_again()

# ---------------------------------------------------------------------------------
# Game functions:

# ask user to play again
def play_again():
    answer = input("\nWould you like to play again? (yes/no): ").lower()
    if answer == "yes":
        main()
    else:
        print("Thank you for playing!")
        exit()

# display hands and totals
def print_result(player_hand, dealer_hand):
    print(f"\nPlayer hand: {player_hand}, total: {total(player_hand)}")
    print(f"Dealer hand: {dealer_hand}, total: {total(dealer_hand)}")

# ---------------------------------------------------------------------------------
def main():
    pass
    print("\n\n\n----------BLACKJACK----------")

    #1 deal two hands
    player_hand = deal()
    dealer_hand = deal()

    #2 show player hand and one dealer card
    print(f"Your hand: {player_hand}, total: {total(player_hand)}")
    print(f"Dealers hand: [{dealer_hand[0]}]")

    #3 evaluate total for blackjack
    check_blackjack(player_hand)

    #5 ask for player decision (HIT, STAND, SURRENDER)
    print("Player move:")
    while total(player_hand) < 21 and total(dealer_hand) < 21:
        player_decision = input("Would you like to hit, stand or surrender? (hit/stand/surrender): ").lower()

    #6 if HIT add another card to player hand and evaluate the total player hand
        if player_decision == "hit":
            while total(player_hand) < 21:
                hit(player_hand)
                while total(dealer_hand) < 17:
                    hit(dealer_hand)
                check_result(player_hand, dealer_hand)
                play_again()

    #11 if STAND evaluate the total of player and dealer hand
        elif player_decision == "stand":
            while total(dealer_hand) < 17:
                    hit(dealer_hand)
            check_result(player_hand, dealer_hand)
            play_again()

    #12 if SURRENDER than print player loses
        elif player_decision == "surrender":
            surrender(dealer_hand)


if __name__ == "__main__":
    main()
