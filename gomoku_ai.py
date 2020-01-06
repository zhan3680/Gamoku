"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy, Machi(Yipeng Li) and George(Yifan Zhang) with tests contributed by Siavash Kazemian.  Last modified: november. 13, 2016
"""
import random
def is_empty(board):
    for i in range(len(board)):             #assume 8X8
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True
    
def left_bounded(board,y,x):
    if  x==0:
        return True
    if x!=0:
        if board[y][x-1] != " ":      #also board[y][x-1] != mark 
            return True
        else:
            return False
         
def right_bounded(board,y,x):
    if  x==7:
        return True
    
    if x!=7:
        
        if board[y][x+1] != " ":      #also board[y][x+1] != mark 
            return True
        else:
            return False
        
def bounded_up(board,y,x):
    if y==0:
        return True
    if y!=0:
        if board[y-1][x] != " ":      #also board[y-1][x] != mark 
            return True
        else:
            return False
def bounded_below(board,y,x):
    if y==7:
        return True
    if y!=7:
        
        if board[y+1][x] != " ":      #also board[y+1][x] != mark 
            return True
        else:
            return False
       
def bounded_upperleft(board,y,x):
    if (y,x)==(0,0):
       return True
    elif y==0 or x==0:
        return True
    if y!=0 and x!=0:
        if board[y-1][x-1] != " ":
            return True
        else:
            return False 
            
def bounded_lowerright(board,y,x):
    if (y,x)==(7,7):
       return True
    elif y==7 or x==7:
        return True
    if y!=7 and x!=7:
        if board[y+1][x+1] != " ":
            return True
        else:
            return False 
def bounded_upperright(board,y,x):
    if (y,x)==(0,7):
       return True
    elif y==0 or x==7:
        return True
    if y!=0 and x!=7:
        if board[y-1][x+1] != " ":
            return True
        else:
            return False 
 
def bounded_lowerleft(board,y,x):
    if (y,x)==(7,0):
       return True
    elif y==7 or x==0:
       return True
    if y!=7 and x!=0:
        if board[y+1][x-1] != " ":
            return True
        else:
            return False    

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    
    if d_y==1 and d_x==0:
        if bounded_below(board,y_end,x_end) and bounded_up(board,y_end-length+1,x_end):
           return "CLOSED"
        elif (not bounded_below(board,y_end,x_end) and bounded_up(board,y_end-length+1,x_end)) or (bounded_below(board,y_end,x_end) and not bounded_up(board,y_end-length+1,x_end)):
           return "SEMIOPEN"
        else:
           return "OPEN"
    elif d_y==0 and d_x==1:
        if right_bounded(board,y_end,x_end) and left_bounded(board,y_end,x_end-length+1):
            return "CLOSED"
        elif (right_bounded(board,y_end,x_end) and not left_bounded(board,y_end,x_end-length+1)) or (not right_bounded(board,y_end,x_end) and left_bounded(board,y_end,x_end-length+1)):
            return "SEMIOPEN"
        else:
            return "OPEN"
    elif d_y==d_x==1:
        if bounded_lowerright(board,y_end,x_end) and bounded_upperleft(board,y_end-length+1,x_end-length+1):
           return "CLOSED"
        elif (bounded_lowerright(board,y_end,x_end) and not bounded_upperleft(board,y_end-length+1,x_end-length+1)) or (not bounded_lowerright(board,y_end,x_end) and bounded_upperleft(board,y_end-length,x_end-length+1)):
            return "SEMIOPEN"
        else:
            return "OPEN"
    elif d_y==1 and d_x==-1:
        if bounded_lowerleft(board,y_end,x_end) and bounded_upperright(board,y_end-length+1,x_end+length-1):
           return "CLOSED"
        elif (bounded_lowerleft(board,y_end,x_end) and not bounded_upperright(board,y_end-length+1,x_end+length-1)) or (not bounded_lowerleft(board,y_end,x_end) and bounded_upperright(board,y_end-length+1,x_end+length-1)):
            return "SEMIOPEN"
        else:
            return "OPEN"

    

         
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    col_length=0
    open_seq_count=0
    semi_open_seq_count=0
    i=0
    counter=0
    while i < min((8-x_start),(8-y_start)):
        counter+=1
        while board[y_start+i*d_y][x_start+i*d_x]==col:
              col_length+=1
              i+=1
              
        i=max(i,counter)
        if col_length==length:
           if is_bounded(board,y_start+(col_length-1)*d_y, x_start+(col_length-1)*d_x, length, d_y, d_x)=="OPEN":
              open_seq_count+=1
              col_length=0
           elif is_bounded(board,y_start+(col_length-1)*d_y, x_start+(col_length-1)*d_x, length, d_y, d_x)=="SEMIOPEN":
              semi_open_seq_count+=1
              col_length=0
           else:
              col_length=0
        else:
            col_length=0
    result=(open_seq_count, semi_open_seq_count)    
    return result   
    
def constraint(board,col,y, x,length,d_y, d_x):
    constraint=8
    if d_y==d_x==1:
       constraint=min(8-y,8-x)
    elif d_y==1 and d_x==-1:
       constraint=min(8-y,x+1)
    return constraint
       
def detect_rowB(board, col, y, x, length, d_y, d_x):

    col_length=0
    open_seq_count=0
    semi_open_seq_count=0
    j=0
    counter=0
    ranging=constraint(board,col,y, x,length,d_y, d_x)
    while j < ranging:
        counter=j+1
        while board[y+j*d_y][x+j*d_x]==col:
              col_length+=1
              j+=1
              if y+j*d_y > 7 or x+j*d_x > 7 or x+j*d_x < 0:
                 break 
        j=max(j,counter)
        if col_length==length:
           if is_bounded(board,y+(j-1)*d_y, x+(j-1)*d_x, length, d_y, d_x)=="OPEN":
              open_seq_count+=1
              col_length=0
           elif is_bounded(board,y+(j-1)*d_y, x+(j-1)*d_x, length, d_y, d_x)=="SEMIOPEN":
              semi_open_seq_count+=1
              col_length=0
           else:
              col_length=0
        else:
           col_length=0
    result=(open_seq_count, semi_open_seq_count)    
    return result        
           
           
  
    
def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowB(board, col, y_origin+i, x_origin, length, 0, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowB(board, col, y_origin, x_origin+i, length, 1, 0)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowB(board, col, y_origin+i, x_origin, length, 1, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    x_origin=0
    y_origin=0
    for i in range(1,8):
        res=detect_rowB(board, col, y_origin, x_origin+i, length, 1, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    x_origin=7
    y_origin=0
    for i in range(8):
        res=detect_rowB(board, col, y_origin+i, x_origin, length, 1, -1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    x_origin=7
    y_origin=0
    for i in range(1,8):
        res=detect_rowB(board, col, y_origin, x_origin-i, length, 1, -1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
    return open_seq_count, semi_open_seq_count
    
    
def detect_rowC(board, col, y, x, length, d_y, d_x):

    col_length=0
    open_seq_count=0
    semi_open_seq_count=0
    closed_seq_count=0
    j=0
    counter=0
    ranging=constraint(board,col,y, x,length,d_y, d_x)
    while j < ranging:
        counter=j+1
        
        while board[y+j*d_y][x+j*d_x]==col:
              col_length+=1
              j+=1
              if y+j*d_y > 7 or x+j*d_x > 7 or x+j*d_x < 0:
                 break 
        j=max(j,counter)
        if col_length==length:
           if is_bounded(board,y+(j-1)*d_y, x+(j-1)*d_x, length, d_y, d_x)=="OPEN":
              open_seq_count+=1
              col_length=0
           elif is_bounded(board,y+(j-1)*d_y, x+(j-1)*d_x, length, d_y, d_x)=="SEMIOPEN":
              semi_open_seq_count+=1
              col_length=0
           else:
              closed_seq_count+=1
              col_length=0
        else:
           col_length=0
    result=(open_seq_count, semi_open_seq_count,closed_seq_count)    
    return result        

def detect_rowsC(board, col, length):
    
    open_seq_count, semi_open_seq_count,closed_seq_count = 0, 0, 0
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowC(board, col, y_origin+i, x_origin, length, 0, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowC(board, col, y_origin, x_origin+i, length, 1, 0)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    x_origin=0
    y_origin=0
    for i in range(8):
        res=detect_rowC(board, col, y_origin+i, x_origin, length, 1, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    x_origin=0
    y_origin=0
    for i in range(1,8):
        res=detect_rowC(board, col, y_origin, x_origin+i, length, 1, 1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    x_origin=7
    y_origin=0
    for i in range(8):
        res=detect_rowC(board, col, y_origin+i, x_origin, length, 1, -1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    x_origin=7
    y_origin=0
    for i in range(1,8):
        res=detect_rowC(board, col, y_origin, x_origin-i, length, 1, -1)
        open_seq_count+=res[0]
        semi_open_seq_count+=res[1]
        closed_seq_count+=res[2]
    return open_seq_count, semi_open_seq_count,closed_seq_count
    
    
def is_win_white(board):
    current_situation=detect_rowsC(board, "w", 5)
    if current_situation[0]+current_situation[1]+current_situation[2]>0:
       return True
    else:
       return False
def is_win_black(board):
    current_situation=detect_rowsC(board, "b", 5)
    if current_situation[0]+current_situation[1]+current_situation[2]>0:
       return True
    else:
       return False
def board_is_full(board):
    for j in range(8):
        for i in range(8):
            if board[j][i]==" ":
                return False
    return True
#######################################################################################    
def get_free_squares(board):
    free_squares=[]
    for j in range(8):
        for i in range(8):
            if board[j][i]==" ":
               free_squares.append((j,i))
    return free_squares



def search_max(board):
     
     max_score=0
     best_choices=[]
     free = get_free_squares(board)
     score1=0
     
     for move in free:
         
         board[move[0]][move[1]]="b"   #assume this function is written for the computer
         score1=score(board)
         board[move[0]][move[1]]=" " 
         max_score=max(max_score,score1)
         
     for move2 in free:
         board[move2[0]][move2[1]]="b"  
         score2=score(board)
         board[move2[0]][move2[1]]=" " 
         if score2==max_score:
            best_choices.append(move2)
     if best_choices!=[]:
        move_y, move_x=random.choice(best_choices)
     else:
        free2=get_free_squares(board)
        move_y,move_x=random.choice(free2)
     
     return  move_y, move_x      
            
         
     
    
    
    
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def score_move(board,col,move):
    open_b = {}
    semi_open_b = {}
    closed_b ={}
    open_w = {}
    semi_open_w = {}
    closed_w ={}
    open_b2 = {}
    semi_open_b2 = {}
    closed_b2 ={}
    open_w2 = {}
    semi_open_w2 = {}
    closed_w2 ={}

    for i in range(2, 6):
        open_b[i],semi_open_b[i],closed_b[i] = detect_rowsC(board, "b", i)
        open_w[i],semi_open_w[i],closed_w[i] = detect_rowsC(board, "w", i)
    row, column = move[0],move[1]
    board[row][column] = "b"
    for i in range(2, 6):
        open_b2[i],semi_open_b2[i],closed_b2[i]  = detect_rowsC(board, "b", i)
        
    board[row][column] = "w"
    for i in range(2, 6):
        open_w2[i],semi_open_w2[i],closed_w2[i] = detect_rowsC(board, "w", i)
    board[row][column] = " "
    if col=="w":
       score=10**13*(semi_open_w2[5]-semi_open_w[5])+10**13*(open_w2[5]-open_w[5])+10**13*(closed_w2[5]-closed_w[5])+10**12*(semi_open_b2[5]-semi_open_b[5])+10**12*(open_b2[5]-open_b[5])+10**12*(closed_b2[5]-closed_b[5])+10**11*(open_w2[4]-open_w[4])+10**10*(open_b2[4]-open_b[4])+ 10**9*(semi_open_w2[4]-semi_open_w[4])+10**8*(open_w2[3]-open_w[3])+10**7*(open_b2[3]-open_b[3])+10**6*(semi_open_b2[4]-semi_open_b[4])+10**5*(semi_open_w2[3]-semi_open_w[3])+10**4*(semi_open_b2[3]-semi_open_b[3])+10**3*(open_w2[2]-open_w[2])+10**2*(open_b2[2]-open_b[2])+10**1*(semi_open_b2[2]-semi_open_b[2])+1*(semi_open_w2[2]-semi_open_w[2])
    elif col=="b":
         score=10**13*(semi_open_b2[5]-semi_open_b[5])+10**13*(open_b2[5]-open_b[5])+10**13*(closed_b2[5]-closed_b[5])+10**12*(semi_open_w2[5]-semi_open_w[5])+10**12*(open_w2[5]-open_w[5])+10**12*(closed_w2[5]-closed_w[5])+10**11*(open_b2[4]-open_b[4])+10**10*(open_w2[4]-open_w[4])+ 10**9*(semi_open_b2[4]-semi_open_b[4])+10**8*(open_b2[3]-open_b[3])+10**7*(open_w2[3]-open_w[3])+10**6*(semi_open_w2[4]-semi_open_w[4])+10**5*(semi_open_b2[3]-semi_open_b[3])+10**4*(semi_open_w2[3]-semi_open_w[3])+10**3*(open_b2[2]-open_b[2])+10**2*(open_w2[2]-open_w[2])+10**1*(semi_open_w2[2]-semi_open_w[2])+1*(semi_open_b2[2]-semi_open_b[2])
    
    return score
    
def get_move(board, col):
    '''Return a tuple which contains the coordinates of the move the AI wants
    to make for colour col on board board'''
    if board[4][4]==" ":
       return(4,4)
    
       
    max_score=0
    best_choices=[]
    free = get_free_squares(board)
    score1=0
    for move in free:
        score1=score_move(board,col,move)
        max_score=max(max_score,score1)
    for move2 in free:
        score2=score_move(board,col,move2)
        if score2==max_score:
            best_choices.append(move2)
    if best_choices!=[]:
        move_y, move_x=random.choice(best_choices)
    else:
        free2=get_free_squares(board)
        move_y, move_x=random.choice(free2)
    return  move_y, move_x      
    
def is_win(board):
    if is_win_black(board):
       return  "Black won"
    elif is_win_white(board):
        return "White won"
    elif not is_win_black(board) and not is_win_white(board) and board_is_full(board):
        return "Draw"
    else:
        return "Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz) 
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y,move_x=get_move(board,"w")
        
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5
    
    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w",y,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")
        
        
def test_detect_rowsB():
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 1; d_y = 0; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    x = 5; y = 0; d_x = 1; d_y = 0; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
   
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()
    play_gomoku(8)
    