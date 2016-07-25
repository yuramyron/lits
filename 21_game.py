import random

class cards(object):
	
	suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
	card_type = ['A', 'K', 'Q', 'V', '10', '9', '8', '7', '6', '5', '4', '3', '2']
	
	def __init__(self):
		pass

	def prepare_deck(self, num=None):
		deck = []
		for card in self.card_type:
			for suite in self.suits:
				deck.append((card, suite))
		return deck

	def shuf(self, deck):
		deck_to_shuffle = deck
		random.shuffle(deck_to_shuffle)
		return deck_to_shuffle

	def hit(self, deck, hand=[]):
			hand.append(deck[0])
			del deck[0]

	def deal(self, deck, hand, num_of_cards):
		while num_of_cards > 0:
			self.hit(deck,hand)
			num_of_cards -= 1

	def count(self, hand, points = 0): 
		for card in hand:
			if card[0] in ['K', 'Q', 'V']:
				points += 10
			elif card[0] == 'A':
				points += 11
			else:
				points += int(card[0])
		return points


#test
#defining variables
game = cards()
dealer_hand = []
playerA_hand = []

#flow
deck = game.prepare_deck()
# print game.count(['A','Q','10','5','V'])
# game.shuffle(deck)
# print deck, len(deck)
# deck = cards.suits
deck = game.shuf(deck)
print deck
game.deal(deck, playerA_hand,2)
dealer_points = game.count(dealer_hand)
playerA_points = game.count(playerA_hand)
game.deal(deck, dealer_hand,2)
print deck

while True:
	print 'Your cards:', playerA_hand
	print 'Total points:', playerA_points
	while True:
		print 'Do you want more?'
		player_will = raw_input()
		print player_will
		if player_will == 'yes':
			game.hit(deck, playerA_hand)
			break
		elif player_will == 'no':
			break
		else:
			print 'Pleaes answer "yes" or "no"'

	continue


# game.hit(deck, playerA_hand)
# game.hit(deck, dealer_hand)
print 'Player A:', playerA_hand
print 'Dealer:', dealer_hand
print 'Deck', deck