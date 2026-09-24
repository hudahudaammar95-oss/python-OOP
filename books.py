import random
import time
import os
game=("""      
                >---<  
                      |
                      | 
                      |
                      |
                      |
                =========== ""","""

                >---< 
                  |   |
                      | 
                      |
                      |
                      |
                =========== ""","""

                 >---<
                  |   |
                  O   | 
                  |   |
                      |
                      |""","""

                 >---<
                  |   |
                  O   |
                 /|\  |
                      |
                      |""","""
           
                 >---<
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |""","""
           
                 >---<
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
           """)
def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
while True: 
    print(game[0])
    words=['glass','bad','gay']
    random_word=random.choice(words)
    guessed_letters=[]
    display=["_"]*len(random_word)
    print(' '.join(display))
    lives=5
    while "_" in display and lives>0:
        guess=input('guess a letter: ')
        if guess in guessed_letters:
            print('\n💢you already guess this letter 💢')
            time.sleep(1)
        elif guess not in random_word :
            lives-=1
            print(f'\n💥you have {lives} tries left!!💥 ')
            print(game[5-lives])
            guessed_letters.append(guess)
        else:
            for position in range(len(random_word)):
                if  random_word[position] in guess:
                    display[position]=guess
                    guessed_letters.append(guess)   
                    print('good job😍😍')    
                    print('***************************************************')  
        print(" ".join(display))

    if lives==0:
        print('--------------\nlose❌🤦‍♀️\n--------------')
    else:
        print('analizing...........')
        time.sleep(2)
        print('\n-------------\nYOU WIN😀🤑\n-------------')
    #اللعب مره اخرى
    if lives==0 or "_" not in display:
            another_game=input('do u want to play again ? y/n: ').lower()
            if another_game=='y':
                clear()
                continue
            else:
                print('game finished')
                exit()