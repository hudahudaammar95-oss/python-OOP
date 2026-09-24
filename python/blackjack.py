import random

def deal_cards():
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10,]
    random_card=random.choice(card)
    return random_card

def calculate(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def results(user_score,computer_score):
    if user_score==computer_score:
        return "Draw✔💥"
    elif user_score==0:
        return 'you got blackjack🤑'
    elif computer_score==0:
        return 'computer got blackjack😭 , you LOSE'
    elif user_score>21:
        return 'you went over 21 ,you lose😢'
    elif computer_score>21:
        return 'computer went over 21,you WIN🤩'
    elif user_score >computer_score:
        print('YOU WIN😍')
    else:
        print('computer scores is higher than yours ,you LOSE😢')

def game():
    game=input(''' Choose the number of the game you want to play:\n1-Snake\n2-Blackjack\n3-turtle\n--------------\n''')
    user_cards=[deal_cards(),deal_cards()]
    computer_cards=[deal_cards(), deal_cards()]
    game_continue=True
    while game_continue:
        user_score=calculate(user_cards)
        computer_score=calculate(computer_cards)
        print(f'\nyou have these cards {user_cards} it equals {user_score}')
        print(f'computer first card is {computer_cards[0]}\n')
        if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
            game_continue=False
        else:
            another_card=input('do you want to draw another card?y/n: ').lower()
            if another_card=='y':
                user_cards.append(deal_cards())
            else:
                game_continue=False
    while computer_score!= 0 and computer_score<17:
            computer_cards.append(deal_cards())
            computer_score=calculate(computer_cards)
    print(f'\nyour final: {user_cards} with score {user_score}')
    print(f"Computer's Final hand: {computer_cards} with score {computer_score}\n")

    print(results(user_score,computer_score))
game()