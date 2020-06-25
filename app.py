# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect



# -- Initialization section --
app = Flask(__name__)


#______DECK_______
deck_dict = {
    '2 of Spades': 2,
    '2 of Hearts': 2,
    '2 of Clubs': 2,
    '2 of Diamonds': 2,
    '3 of Spades': 3,
    '3 of Hearts': 3,
    '3 of Clubs': 3,
    '3 of Diamonds': 3,
    '4 of Spades': 4,
    '4 of Hearts': 4,
    '4 of Clubs': 4,
    '4 of Diamonds': 4,
    '5 of Spades': 5,
    '5 of Hearts': 5,
    '5 of Clubs': 5,
    '5 of Diamonds': 5,
    '6 of Spades': 6,
    '6 of Hearts': 6,
    '6 of Clubs': 6,
    '6 of Diamonds': 6,
    '7 of Spades': 7,
    '7 of Hearts': 7,
    '7 of Clubs': 7,
    '7 of Diamonds': 7,
    '8 of Spades': 8,
    '8 of Hearts': 8,
    '8 of Clubs': 8,
    '8 of Diamonds': 8,
    '9 of Spades': 9,
    '9 of Hearts': 9,
    '9 of Clubs': 9,
    '9 of Diamonds': 9,
    '10 of Spades': 10,
    '10 of Hearts': 10,
    '10 of Clubs': 10,
    '10 of Diamonds': 10,
    'J of Spades': 10,
    'J of Hearts': 10,
    'J of Clubs': 10,
    'J of Diamonds': 10,
    'Q of Spades': 10,
    'Q of Hearts': 10,
    'Q of Clubs': 10,
    'Q of Diamonds': 10,
    'K of Spades': 10,
    'K of Hearts': 10,
    'K of Clubs': 10,
    'K of Diamonds': 10,
    'A of Spades': 11,
    'A of Hearts': 11,
    'A of Clubs': 11,
    'A of Diamonds': 11
    }





        

# -- Routes section --
import random
player_hand = []
dealer_hand = []
deck = []
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for n in numbers:
    for s in suits:
        deck.append(n + " of " + s)
@app.route('/')
def start():
    player_hand = []
    dealer_hand = []
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for n in numbers:
        for s in suits:
            deck.append(n + " of " + s)
    return redirect('/index')
@app.route('/index')
def index():
    if len(player_hand) == 0:
        random.shuffle(deck)
        player_hand.append(deck[0])
        deck.remove(deck[0])
        player_hand.append(deck[0])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])
    else:
        deck.append(player_hand[0])
        player_hand.remove(player_hand[0])
        deck.append(player_hand[0])
        player_hand.remove(player_hand[0])
        deck.append(dealer_hand[0])
        dealer_hand.remove(dealer_hand[0])
        deck.append(dealer_hand[0])
        dealer_hand.remove(dealer_hand[0])
        random.shuffle(deck)
        player_hand.append(deck[0])
        deck.remove(deck[0])
        player_hand.append(deck[0])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])
        
    props = {
        "message": "your hand is " + str(player_hand) ,
        "message2": "the dealer's hand is " + str(dealer_hand)
        }
    return render_template('index.html', props = props)


#_______HANDS_________


@app.route('/hit')
def hit():
    player_hand.append(deck[0])
    deck.remove(deck[0])
    props = {
        "message": "your hand is " + str(player_hand) ,
        "message2": "the dealer's hand is " + str(dealer_hand)
        }
    return render_template('index.html', props = props)

@app.route('/stand')

def stand():
    sum = 0
    for i in range(0, len(player_hand)):
        sum = sum + (deck_dict[player_hand[i]])
    props = {
        "message": "your hand is " + str(player_hand) ,
        "message2": "the dealer's hand is " + str(dealer_hand),
        "message3": "total value in hand = " + str(sum)
        }
    return render_template('index.html', props = props)