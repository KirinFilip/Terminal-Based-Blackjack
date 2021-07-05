# Terminal-Based-Blackjack
Simple terminal based blackjack game for one player

1 deck of 52 cards

player and dealer (computer)

Card values:

King = Queen = Jack = 10

Numbered cards (2-10) = retain face value

Ace = 1 or 11 depending which value advanteges the player

Win conditions:
Player gets 21 - player wins
Dealer gets 21 - dealer wins
Player and Dealer get 21 - draw (also known as Push)

Player decisions:

HIT = request another card from the dealer,
    add the value of the card to your total card value,
    if third card gives you 21 you immediately win -> Blackjack,
    if third card gives you a total of more than 21 -> you lose,
    if not you may continue hitting until satisfied

STAND = satisfied with your current hand

SURRENDER = you surrender to the dealer and lose, another round commences
    is offered when the dealer's upcard (the card you can see)
    is either an ace or a ten value (Ace, King, Queen, Jack, Ten)

One round of blackjack:
- Player receives one card
- Dealer receives one card - upcard (player can see)
- Player receives another card
- Dealer receives another card - player can not see the card
- Player decides to either HIT, STAND or SURRENDER
- If HIT, player receives another card and 
  the value of the card is added to the total
  he then decides either to HIT again or STAND
- If STAND, player is satisfied with his had and the dealer reveals his card
- If Player has more total than Dealer -> Player wins
- If Dealer has more total than Player -> Dealer wins
- If Both Player and Dealer have the same total -> Draw

Functions:
deal
hit
surrender
total
result
