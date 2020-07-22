# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect
from datetime import datetime
# -- Initialization section --
app = Flask(__name__)
def ace():
    if 'A of Spades' in player_hand or 'A of Hearts' in player_hand or 'A of Clubs' in player_hand or 'A of Diamonds' in player_hand:
            sum1 = sum1 - 10
            props = {
            "message": "your hand is " + str(player_hand) ,
            "message2": "the dealer's hand is " + str(dealer_hand),
            "pcard1": deck_pic[player_hand[0]],
            "pcard2": deck_pic[player_hand[1]],
            "dcard1": deck_pic[dealer_hand[0]],
            "dcard2": deck_pic[dealer_hand[1]],
            } 
    else:
        props = {
        "message": "you lose",
        "pcard1": deck_pic[player_hand[0]],
        "pcard2": deck_pic[player_hand[1]],
        "dcard1": deck_pic[dealer_hand[0]],
        "dcard2": deck_pic[dealer_hand[1]],
        }
#______DECK_______
deck_pic = {
    '2 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Atlas_deck_2_of_spades.svg/540px-Atlas_deck_2_of_spades.svg.png",
    '2 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Atlas_deck_2_of_hearts.svg/540px-Atlas_deck_2_of_hearts.svg.png",
    '2 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Atlas_deck_2_of_clubs.svg/800px-Atlas_deck_2_of_clubs.svg.png",
    '2 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Atlas_deck_2_of_diamonds.svg/800px-Atlas_deck_2_of_diamonds.svg.png",
    '3 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Atlas_deck_3_of_spades.svg/800px-Atlas_deck_3_of_spades.svg.png",
    '3 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Atlas_deck_3_of_hearts.svg/800px-Atlas_deck_3_of_hearts.svg.png",
    '3 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Atlas_deck_3_of_clubs.svg/800px-Atlas_deck_3_of_clubs.svg.png",
    '3 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Atlas_deck_3_of_diamonds.svg/800px-Atlas_deck_3_of_diamonds.svg.png",
    '4 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Atlas_deck_4_of_spades.svg/80px-Atlas_deck_4_of_spades.svg.png",
    '4 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Atlas_deck_4_of_hearts.svg/800px-Atlas_deck_4_of_hearts.svg.png",
    '4 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Atlas_deck_4_of_clubs.svg/80px-Atlas_deck_4_of_clubs.svg.png",
    '4 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Atlas_deck_4_of_diamonds.svg/800px-Atlas_deck_4_of_diamonds.svg.png",
    '5 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Atlas_deck_5_of_spades.svg/800px-Atlas_deck_5_of_spades.svg.png",
    '5 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Atlas_deck_5_of_hearts.svg/800px-Atlas_deck_5_of_hearts.svg.png",
    '5 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Atlas_deck_5_of_clubs.svg/800px-Atlas_deck_5_of_clubs.svg.png",
    '5 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Atlas_deck_5_of_diamonds.svg/800px-Atlas_deck_5_of_diamonds.svg.png",
    '6 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Atlas_deck_6_of_spades.svg/80px-Atlas_deck_6_of_spades.svg.png",
    '6 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Atlas_deck_6_of_hearts.svg/80px-Atlas_deck_6_of_hearts.svg.png",
    '6 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Atlas_deck_6_of_clubs.svg/80px-Atlas_deck_6_of_clubs.svg.png",
    '6 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Atlas_deck_6_of_diamonds.svg/800px-Atlas_deck_6_of_diamonds.svg.png",
    '7 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Atlas_deck_7_of_spades.svg/80px-Atlas_deck_7_of_spades.svg.png",
    '7 of Hearts': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Atlas_deck_7_of_hearts.svg/80px-Atlas_deck_7_of_hearts.svg.png',
    '7 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Atlas_deck_7_of_clubs.svg/80px-Atlas_deck_7_of_clubs.svg.png",
    '7 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Atlas_deck_7_of_diamonds.svg/80px-Atlas_deck_7_of_diamonds.svg.png",
    '8 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Atlas_deck_8_of_spades.svg/80px-Atlas_deck_8_of_spades.svg.png",
    '8 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Atlas_deck_8_of_hearts.svg/80px-Atlas_deck_8_of_hearts.svg.png",
    '8 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Atlas_deck_8_of_clubs.svg/80px-Atlas_deck_8_of_clubs.svg.png",
    '8 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Atlas_deck_8_of_diamonds.svg/80px-Atlas_deck_8_of_diamonds.svg.png",
    '9 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Atlas_deck_9_of_spades.svg/80px-Atlas_deck_9_of_spades.svg.png",
    '9 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Atlas_deck_9_of_hearts.svg/80px-Atlas_deck_9_of_hearts.svg.png",
    '9 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Atlas_deck_9_of_clubs.svg/80px-Atlas_deck_9_of_clubs.svg.png",
    '9 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Atlas_deck_9_of_diamonds.svg/80px-Atlas_deck_9_of_diamonds.svg.png",
    '10 of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Atlas_deck_10_of_spades.svg/80px-Atlas_deck_10_of_spades.svg.png",
    '10 of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Atlas_deck_10_of_hearts.svg/80px-Atlas_deck_10_of_hearts.svg.png",
    '10 of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Atlas_deck_10_of_clubs.svg/80px-Atlas_deck_10_of_clubs.svg.png",
    '10 of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Atlas_deck_10_of_diamonds.svg/800px-Atlas_deck_10_of_diamonds.svg.png",
    'J of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Jack_of_spades_en.svg/83px-Jack_of_spades_en.svg.png",
    'J of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Jack_of_hearts_en.svg/83px-Jack_of_hearts_en.svg.png",
    'J of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Jack_of_clubs_en.svg/800px-Jack_of_clubs_en.svg.png",
    'J of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Jack_of_diamonds_en.svg/83px-Jack_of_diamonds_en.svg.png",
    'Q of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Queen_of_spades_en.svg/83px-Queen_of_spades_en.svg.png",
    'Q of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Queen_of_hearts_en.svg/83px-Queen_of_hearts_en.svg.png",
    'Q of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Queen_of_clubs_en.svg/83px-Queen_of_clubs_en.svg.png",
    'Q of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Queen_of_diamonds_en.svg/83px-Queen_of_diamonds_en.svg.png",
    'K of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/King_of_spades_en.svg/83px-King_of_spades_en.svg.png",
    'K of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/King_of_hearts_en.svg/83px-King_of_hearts_en.svg.png",
    'K of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/King_of_clubs_en.svg/83px-King_of_clubs_en.svg.png",
    'K of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/King_of_diamonds_en.svg/83px-King_of_diamonds_en.svg.png",
    'A of Spades': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Ace_of_spades.svg/800px-Ace_of_spades.svg.png",
    'A of Hearts': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Ace_of_hearts.svg/83px-Ace_of_hearts.svg.png",
    'A of Clubs': "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Ace_of_clubs.svg/83px-Ace_of_clubs.svg.png",
    'A of Diamonds': "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Ace_of_diamonds.svg/83px-Ace_of_diamonds.svg.png"
    }

deck_back = {
    '2 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '2 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '2 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '2 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '3 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '3 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '3 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '3 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '4 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '4 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '4 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '4 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '5 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '5 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '5 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '5 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '6 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '6 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '6 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '6 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '7 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '7 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '7 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '7 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '8 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '8 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '8 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '8 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '9 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '9 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '9 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '9 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '10 of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '10 of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '10 of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    '10 of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'J of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'J of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'J of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'J of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'Q of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'Q of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'Q of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'Q of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'K of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'K of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'K of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'K of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'A of Spades': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'A of Hearts': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'A of Clubs': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png",
    'A of Diamonds': "https://i.pinimg.com/originals/10/80/a4/1080a4bd1a33cec92019fab5efb3995d.png"
    }

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
player_image = []
dealer_hand = []
dealer_image = []
dealer_revealed = []
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
        player_image.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        player_hand.append(deck[0])
        player_image.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        dealer_image.append(deck_pic[deck[0]])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        dealer_image.append(deck_back[deck[0]])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
    else:
        while len(player_hand) > 0:
            deck.append(player_hand[0])
            player_hand.remove(player_hand[0])
            player_image.remove(player_image[0])
        while len(dealer_hand) > 0:
            deck.append(dealer_hand[0])
            dealer_hand.remove(dealer_hand[0])
            dealer_image.remove(dealer_image[0])
            dealer_revealed.remove(dealer_revealed[0])
        random.shuffle(deck)
        player_hand.append(deck[0])
        player_image.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        player_hand.append(deck[0])
        player_image.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        dealer_image.append(deck_pic[deck[0]])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        dealer_image.append(deck_back[deck[0]])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
    props = {
        "pcards": player_image,
        "dcards": dealer_image
        }
    print(player_image)
    return render_template('index.html', props = props, time = datetime.now())
#_______HANDS_________
@app.route('/hit')
def hit():
    sum1 = 0
    for i in range(0, len(player_hand)):
        sum1 = sum1 + (deck_dict[player_hand[i]])
    player_hand.append(deck[0])
    player_image.append(deck_pic[deck[0]])
    deck.remove(deck[0])
    sum1 = sum1 + (deck_dict[player_hand[-1]])
    props = {
        "pcards": player_image,
        "dcards": dealer_image
        }
    if int(sum1) > 21:
        deck_dict['A of Diamonds'] = 1
        deck_dict['A of Hearts'] = 1
        deck_dict['A of Spades'] = 1
        deck_dict['A of Clubs'] = 1
        if int(sum1) > 21:
            props = {
                "message3": "you lose",
                "pcards": player_image,
                "dcards": dealer_revealed
                }
    return render_template('index.html', props = props, time = datetime.now())

@app.route('/stand')
def stand():
    sum1 = 0
    for i in range(0, len(player_hand)):
        sum1 = sum1 + (deck_dict[player_hand[i]])
    props = {
        "pcards": player_image,
        "dcards": dealer_revealed
        }
    if int(sum1) > 21:
        deck_dict['A of Diamonds'] = 1
        deck_dict['A of Hearts'] = 1
        deck_dict['A of Spades'] = 1
        deck_dict['A of Clubs'] = 1
        if int(sum1) > 21:
            props = {
                "message3": "you lose",
                "pcards": player_image,
                "dcards": dealer_revealed
                }
    sum2 = 0
    for i in range(0, len(dealer_hand)):
        sum2 = sum2 + (deck_dict[dealer_hand[i]])
    while int(sum2) < 17:
        dealer_hand.append(deck[0])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        sum2 = sum2 + (deck_dict[dealer_hand[-1]])
        if int(sum2) > 21:
            deck_dict['A of Diamonds'] = 1
            deck_dict['A of Hearts'] = 1
            deck_dict['A of Spades'] = 1
            deck_dict['A of Clubs'] = 1
            if int(sum1) > 21:
                props = {
                    "message3": "you win",
                    "pcards": player_image,
                    "dcards": dealer_revealed
                    }
    while int(sum1) > int(sum2):
        dealer_hand.append(deck[0])
        dealer_revealed.append(deck_pic[deck[0]])
        deck.remove(deck[0])
        sum2 = sum2 + (deck_dict[dealer_hand[-1]])
        if int(sum2) > 21:
            deck_dict['A of Diamonds'] = 1
            deck_dict['A of Hearts'] = 1
            deck_dict['A of Spades'] = 1
            deck_dict['A of Clubs'] = 1
            if int(sum1) > 21:
                props = {
                    "message3": "you win",
                    "pcards": player_image,
                    "dcards": dealer_revealed
                    }
    if int(sum2) >= int(sum1) and int(sum2) <= 21:
        props = {
            "message3": "you lose!",
            "pcards": player_image,
            "dcards": dealer_revealed
            }
    elif int(sum2) > 21:
        deck_dict['A of Diamonds'] = 1
        deck_dict['A of Hearts'] = 1
        deck_dict['A of Spades'] = 1
        deck_dict['A of Clubs'] = 1
        if int(sum2) > 21:
            props = {
                "message3": "you win!",
                "pcards": player_image,
                "dcards": dealer_revealed  
                }
    return render_template('index.html', props = props, time = datetime.now)