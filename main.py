import random

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

# Player decisions:
def hit(hand):
    card = random.choice(deck)
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)

    return hand

def surrender(dealer_hand):
    if ( 
        dealer_hand[0] == "A"
        or dealer_hand[0] == "K"
        or dealer_hand[0] == "Q"
        or dealer_hand[0] == "J"
        or dealer_hand[0] == 10
    ):
        print("Player surrendered")



# Keeping score:
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

def check_result(player_hand, dealer_hand):
    pass
    # Player Wins - 

    # Player Losses -

    # Dealer Wins -

    # Draw - player_hand = dealer_hand


def play():
    pass
    #1 deal two hands
    #2 show player hand
    #3 evaluate player total, if 21 -> you win print Blackjack
    #4 show dealers one card
    #5 ask for player decision (HIT, STAND, SURRENDER)
    #6 if HIT add another card to player hand
    #7 evaluate the total player hand
    #8 if over 21 print you lose
    #9 if under 21 ask for player decision (HIT, STAND)
    #10 if HIT repeat #5, #6, #7 and #8
    #11 if STAND evaluate the total of player and dealer hand
    #12 print player and dealer hand
    #13 print who wins
    #14 ask if player want to play again


hand = deal()
print(hand)
print(total(hand))
hit(hand)
print(hand)
print(total(hand))
