theBoard = {'7': ' ' , '8': ' ' , '9': ' ',
            '4': ' ' , '5': ' ' , '6': ' ',
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game_over():
    printBoard(theBoard)
    print("\nGame Over.\n")

def game():
    turn = 'X'
    count = 0

    for i in range(9):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input("A value b/w 1 to 9")
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            game_over()
            print("****" +turn + "won. ****")
            
        elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ' or theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ' or theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
            game_over()
            print("****" +turn + "won. ****")
            
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
            game_over()
            print("****" +turn + "won. ****")
            
    
    if count == 9:
        game_over()
        print("It's a Tie!")
    
restart = input("Do you wanna play?(y/n)")
if restart.lower == "y":
    for key in board_keys:
        theBoard[key] = " "
    
    game()

if __name__ == "__main__":
    game()
            
            
