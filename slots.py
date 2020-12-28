#initialize

import random
player1turns = 0
player2turns = 0
player1wallet = 5
player2wallet = 5

#player 1 -------------------------

player1name = str(input("welcome to slots! what's player 1's name? "))
print("this is more complicated than your average game of slots. you get three turns to play, and you start off with $5. if all the reels match, you lose all your money. if the sum of the reels is a multiple of 3, you win half of your money. if the sum of the reels is even but not a multiple of 3, you lose half your money. otherwise (if the reels are not the same, not even when added, and not a multiple of 3), you win the amount of the sum of the reels. you win by getting more money than your opponent at the end of the game.")
player1play = str(input("press y to play slots, or n to give up your turns. "))

while player1play == "y" and player1turns < 3:

    player1reel1 = random.randint(0,2)
    player1reel2 = random.randint(0,2)
    player1reel3 = random.randint(0,2)

    print("spinning...")
    print(str(player1reel1) + " " + str(player1reel2) + " " + str(player1reel3))

    if player1reel1 == player1reel2 == player1reel3:
        print("sorry " + player1name + ", all the reels are the same. you lose all your money!")
        player1wallet = 0
        print("you have $" + str(player1wallet) + " in your wallet, " + player1name + ".")
        
        player1turns = player1turns + 1

    elif ((player1reel1 + player1reel2 + player1reel3) % 3 == 0):
        print("the sum of the reels is a multiple of 3. you win half your money!")
        player1halfmoney = player1wallet // 2
        player1wallet = player1wallet + player1halfmoney
        print("you have $" + str(player1wallet) + " in your wallet, " + player1name + ".")
        
        player1turns = player1turns + 1

    elif (((player1reel1 + player1reel2 + player1reel3) % 2 == 0) and ((player1reel1 + player1reel2 + player1reel3) % 3 != 0)):
        print("the sum of the reels is even, and not a multiple of 3. you lose half your money!")
        player1halfmoney = player1wallet // 2
        player1wallet = player1wallet - player1halfmoney
        print("you have $" + str(player1wallet) + " in your wallet, " + player1name + ".")
        
        player1turns = player1turns + 1

    else:
        print("the reels are not the same, not even, and not a multiple of 3. you win the amount of the sum of the reels!")
        player1wallet = player1wallet + player1reel1 + player1reel2 + player1reel3
        print("you have $" + str(player1wallet) + " in your wallet, " + player1name + ".")
        
        player1turns = player1turns + 1

    if player1turns < 3:
        player1play = str(input("do you want to play again? y/n: "))

print("that's all your turns, " + str(player1name) + ". you have $" + str(player1wallet) + " in your wallet.")

#player 2 -------------------------

player2name = str(input("now for player 2's turn. what's your name, player 2? "))
print("remember, you get three turns to play, and you start off with $5. if all the reels match, you lose all your money. if the sum of the reels is a multiple of 3, you win half of your money. if the sum of the reels is even but not a multiple of 3, you lose half your money. otherwise (if the reels are not the same, not even when added, and not a multiple of 3), you win the amount of the sum of the reels. you need to get more than $" + str(player1wallet) + " to win.")
player2play = str(input("press y to play slots, or n to give up your turns. "))

while player2play == "y" and player2turns < 3:

    player2reel1 = random.randint(0,2)
    player2reel2 = random.randint(0,2)
    player2reel3 = random.randint(0,2)

    print("spinning...")
    print(str(player2reel1) + " " + str(player2reel2) + " " + str(player2reel3))

    if player2reel1 == player2reel2 == player2reel3:
        print("sorry " + player2name + ", all the reels are the same. you lose all your money!")
        player2wallet = 0
        print("you have $" + str(player2wallet) + " in your wallet, " + player2name + ".")
        
        player2turns = player2turns + 1

    elif ((player2reel1 + player2reel2 + player2reel3) % 3 == 0):
        print("the sum of the reels is a multiple of 3. you win half your money!")
        player2halfmoney = player2wallet // 2
        player2wallet = player2wallet + player2halfmoney
        print("you have $" + str(player2wallet) + " in your wallet, " + player2name + ".")
        
        player2turns = player2turns + 1

    elif (((player2reel1 + player2reel2 + player2reel3) % 2 == 0) and ((player2reel1 + player2reel2 + player2reel3) % 3 != 0)):
        print("the sum of the reels is even, and not a multiple of 3. you lose half your money!")
        player2halfmoney = player2wallet // 2
        player2wallet = player2wallet - player2halfmoney
        print("you have $" + str(player2wallet) + " in your wallet, " + player2name + ".")
        
        player2turns = player2turns + 1

    else:
        print("the reels are not the same, not even, and not a multiple of 3. you win the amount of the sum of the reels!")
        player2wallet = player2wallet + player2reel1 + player2reel2 + player2reel3
        print("you have $" + str(player2wallet) + " in your wallet, " + player2name + ".")
        
        player2turns = player2turns + 1

    if player2turns < 3:
        player2play = str(input("do you want to play again? y/n: "))

print("that's all your turns, " + str(player2name) + ". you have $" + str(player2wallet) + " in your wallet.")

#end -------------------------

if player1wallet > player2wallet:
    print(player1name + " has won! they have $" + str(player1wallet) + ", while " + player2name + " only has $" + str(player2wallet) + " in their wallet. thanks for playing!")

elif player2wallet > player1wallet:
    print(player2name + " has won! they have $" + str(player2wallet) + ", while " + player1name + " only has $" + str(player1wallet) + " in their wallet. thanks for playing!")

elif player1wallet == player2wallet and player1wallet > 0 and player2wallet > 0:
    print("wow, it's a tie! both " + player1name + " and " + player2name + " have $" + str(player1wallet) + " in their wallets. thanks for playing!")

else:
    print("aw, looks like you both lost all your money. both " + player1name + " and " + player2name + " have $" + str(player1wallet) + " in their wallets. thanks for playing!")
