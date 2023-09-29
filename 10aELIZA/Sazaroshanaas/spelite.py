import random
#akmens, skeres, papiruss
moves = ['Skeres', 'akmens', 'papiruss'] #saraksts
while True:
    human_move = input("Input your move: ")
    pc_move = random.choice(moves)
    print("Human: ", human_move, "vs PC: ", pc_move)
    if  human_move == pc_move :
        print("Nobody has won! ")
    elif human_move == 'akmens' and pc_move == 'Skeres': 
        print("Human wins, good job!")
    elif human_move == 'Skeres' and pc_move == 'papiruss':
        print("Human has won PC, good job!")
    elif human_move == 'papiruss' and pc_move == 'akmens':
        print("Human has won once again!")
    else: 
        print("PC has won this time, sorry :(! )")

