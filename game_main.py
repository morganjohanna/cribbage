import random

hand_player1 = []
hand_player2 = []
cut_card = []

class Prep_Deal():
    """
    Sets up the deck, deals 6 random cards to 2 players, and randomly draws the cut card.
    """
    def __init__(self):
        """
        Initializes class instance
        """

        self.deck = []
        self.available_deck = []

    def create_deck(self):
        """
        Setting up a normal, 52-card deck.

        Returns
        -------
        self.available_deck: list
            A list of all cards in the deck available to be dealt.
        self.deck: list
            A list of all cards in the deck before any have been dealt.
        """

        self.cards = ["Ace of", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack of", "Queen of", "King of"]
        self.suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

        for card in range(len(self.cards)):
            for suit in range(len(self.suits)):
                self.deck.append(self.cards[card] + " " + self.suits[suit])

        self.available_deck = self.deck

        return self.available_deck, self.deck

    def deal_hand(self):
        """
        Deals 6 cards to each of the 2 players and draws a cut card.

        Returns
        -------
        hand_player1: list
            A list of 6 randomly-drawn cards comprising player 1's initial hand.
        hand_player2: list
            A list of 6 randomly-drawn cards comprising player 1's initial hand.
        cut_card: string
            A randomly-drawn card to serve as the cut card.
        """

        global hand_player1
        global hand_player2
        global cut_card

        # self.available_deck = self.deck TODO do I need to reset this here? As self.available_deck is not returned after this, it should be fine, to check

        for i in range(0, 6):
            card = random.choice(self.available_deck)
            hand_player1.append(card)
            self.available_deck = [x for x in self.deck if x not in hand_player1]
            i = i + 1

        for i in range(0, 6):
            card = random.choice(self.available_deck)
            hand_player2.append(card)
            self.available_deck = [x for x in self.deck if x not in hand_player2]
            i = i + 1

        cut_card = random.choice(self.available_deck)

        return hand_player1, hand_player2, cut_card
    
game = Prep_Deal()
game.create_deck()
game.deal_hand()

print(f"Player 1 hand: {hand_player1}")
print(f"Player 2 hand: {hand_player2}")
print(f"Cut card: {cut_card}")

# TODO:
    # class to count value of cards
    # function to discard to crib depending on whose crib
    # function/class to lay out depending on count, pattern (e.g. runs), card-counting based on own hand, visible opponent's hand, and cut_card
    # function to keep score, note wins

    # main game loop function, to Prep_Deal.create_deck, Prep_Deal.deal_hand, TODO count total hand values, TODO discard to crib, TODO lay out, TODO count actual hand and crib values, TODO keep score