t=1
s=2
l=3
d=4
k=5
hb=6
sb=7

def create_board():
    board = [[t,s,l,d,k,l,s,t],
    [0,hb,hb,hb,hb,hb,hb,hb],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [sb,sb,sb,sb,sb,sb,sb,sb],
    [t,s,l,d,k,l,s,t]]
    return board

def print_board(board):
    for b in board:
        print(b)



def take_input():
    print('Give from coordinates:')
    c1 = input()
    print('Give to coordinates:')
    c2 = input()
    return c1, c2

def is_check_mate():
    return False


def make_move(board, c1,c2):
    if validate_move(board, c1, c2):
        board[int(c2[0])][int(c2[1])] = board[int(c1[0])][int(c1[1])]
        board[int(c1[0])][int(c1[1])] = 0
    
def validate_move(board, c1, c2):
    if board[c1[0]][c1[1]] == 1:
        if c2[0] != c1[0] & c2[1] != c1[1]:
            return False

        for i in range(c1[0],c2[0]):
            if board[c2[0]+i][c1[0]] != 0:
                return False

        for i in range(c1[1],c2[1]):
            if board[c2[1]+i][c1[1]] != 0:
                return False
    return True


def main():
    board = create_board()
    check_mate = False
    while not check_mate:
        c1,c2 = take_input()
        x1 = int(c1[0])
        y1 = int(c1[1])
        x2 = int(c2[0])
        y2 = int(c2[1])
        make_move(board, [x1, y1], [x2, y2])
        print(board)

        print_board(board)


main()








