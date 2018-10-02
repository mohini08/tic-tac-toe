def printboard(board):
    print(board['top-L'] + ' | '  +board['top-M'] + ' | '  +board['top-R'])
    print('----------')
    print(board['med-L'] + ' | ' + board['med-M'] + ' | ' + board['med-R'])
    print('----------')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

def check_winner(board,i):
        if board['top-L']=='X' and board['top-M']=='X' and  board['top-R']=='X' || \
           board['med-L'] == 'X' and board['med-M'] == 'X' and board['med-R'] == 'X' || \
           board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X' || \
           board['top-L'] == 'X' and board['med-M'] == 'X' and board['low-R'] == 'X' || \
           board['low-L'] == 'X' and board['med-M'] == 'X' and board['top-R'] == 'X':
           print('Yay! Player X is winner!!')
           return 1
        elif board['top-L']=='O' and board['top-M']=='O' and  board['top-R']=='O' || \
           board['med-L'] == 'O' and board['med-M'] == 'O' and board['med-R'] == 'O' || \
           board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O' || \
           board['top-L'] == 'O' and board['med-M'] == 'O' and board['low-R'] == 'O' || \
           board['low-L'] == 'O' and board['med-M'] == 'O' and board['top-R'] == 'O':
           print('Yay! Player O is winner!!')
           return 1
        elif i==9:
            print('Oh!No winner')
            return 1

board={'top-L':' ','top-M':' ','top-R':' ','med-L':' ','med-M':' ','med-R':' ','low-L':' ','low-M':' ','low-R':' '}
turn='X'
for i in range(9):
    print('Your turn '+turn+' Where you want to enter: ')
    move=input()
    board[move]=turn
    #print(board)
    if turn=='X':
        turn='O'
    else:
        turn='X'
    printboard(board)
    x=check_winner(board,i)
    if x==1:
        break
