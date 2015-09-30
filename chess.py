# from FileRead import *
import copy

# Variable Declarations
## General Purpose
choice = None
player = "0"
# workfile = 'testCase.txt'
## Game State Flags
draw = False
stalemate = False
checkmate = False

def heuristic2(p2):
        hlist=[]
        for i in range(len(p2)):
                hval=0
                for j in range(len(p2[1])):
                        hval+=abs(float(p2[i][j])-3.5)
                hlist.append(hval)
        print(p2[hlist.index(min(hlist))])
        return(p2[hlist.index(min(hlist))])

def player2(board,K,R,k):
        possible=moves(board,K,R,k,2)
        global stalemate
        global checkmate
        if draw:
                return(R)
        p2=[]
        for j in range(len(board)):
                for i in range(len(board[j])):
                        if possible[i][j]=="O":
                                p2.append(tuple([i,j]))
        print(p2)
        if p2==[]:
                stalemate=True
                if R[0]==k[0] or R[1]==k[1]:
                        checkmate=True
                        stalemate=False
                return k
        return(heuristic2(p2))


def rookeMoves(board,board1,board2,K,R,k):
        for i in range(8):
                if board[R[0]][i] =="-" and board2[R[0]][i] !="O":
                        if board1[R[0]][i]=="Z":
                                board1[R[0]][i]="Y"
                        else:
                                board1[R[0]][i]="X"            
                if board[i][R[1]]=="-" and board2[i][R[1]]!="O":
                        if board1[i][R[1]]=="Z":
                                board1[i][R[1]]="Y"
                        else:
                                board1[i][R[1]]="X"
def oKingMoves(board,board1,board2,K,R,k):
        for i in range(8):
                for j in range(8):
                        if (board[i][j]=="-" or board[i][j]=="R") and board2[i][j]!="O" and i<=K[0]+1 and i>=K[0]-1 and j<=K[1]+1 and j>=K[1]-1:
                                if board1[i][j]=="X":
                                        board1[i][j]="Y"
                                elif board[i][j]=="R":
                                        board2[i][j]="r"
                                else:
                                        board1[i][j]="Z"
def dKingMoves(board,board1,board2,K,R,k):
        global draw
        for i in range(8):
                for j in range(8):
                        if (board1[i][j]=="-" or board1[i][j]=="R") and i<=k[0]+1 and i>=k[0]-1 and j<=k[1]+1 and j>=k[1]-1:
                                if board2[i][j]=="-":
                                        board2[i][j]="O"
                                elif board2[i][j]=="R":
                                        board2[i][j]="D"
                                        draw=True
def moves(board, K,R,k,player):
        board1 = [[0 for x in range(8)] for x in range(8)]
        board2 = [[0 for x in range(8)] for x in range(8)]
        for i in range(8):
                for j in range(8):
                        board1[i][j]="-"
                        board2[i][j]="-"
                        
        '''
        # Code Block to read in coordinates from
        # workfile('testCase.txt')

        coordinates = FileRead(workfile)
        K = coordinates[0]
        R = coordinates[1]
        k = coordinates[2]

        '''
        board1[K[0]][K[1]]="K"
        board1[R[0]][R[1]]="R"
        board1[k[0]][k[1]]="k"
        board2[K[0]][K[1]]="K"
        board2[R[0]][R[1]]="R"
        board2[k[0]][k[1]]="k"

        if player==2:
                rookeMoves(board,board1,board2,K,R,k)
                oKingMoves(board,board1,board2,K,R,k)
                dKingMoves(board,board1,board2,K,R,k)
                printboard(board2)
                return(board2)
        elif player==1:
                dKingMoves(board,board1,board2,K,R,k)
                rookeMoves(board,board1,board2,K,R,k)
                oKingMoves(board,board1,board2,K,R,k)
                printboard(board1)



        #for Rooke
        rookeMoves(board,board1,board2,K,R,k)
        #for King
        oKingMoves(board,board1,board2,K,R,k)
        #for king
        dKingMoves(board,board1,board2,K,R,k)
                
#    printboard(board1)
#    printboard(board2)
def coord(board):
        for i in range(len(board)):
                try:
                        K=tuple([i,board[i].index("K")])
                except ValueError:
                        continue
        for i in range(len(board)):
                try:
                        R=tuple([i,board[i].index("R")])
                except ValueError:
                        continue
        for i in range(len(board)):
                try:
                        k=tuple([i,board[i].index("k")])
                except ValueError:
                        continue
        print(K,R,k)
        return(K,R,k)

def printboard(board):
        counter=0
        for j in range(8):
                print(counter, end=" ")
                for i in range(8):
                        print (board[i][j], end=" ")
                print()
                counter+=1
        counter=0
        print(" ",end=" ")
        for i in range(8):
                print(counter,end=" ")
                counter+=1
        print()
def play(movmax):
        movnum=movmax
        global player
        player1move=True
        board = [[0 for x in range(8)] for x in range(8)] 
        for i in range(8):
                for j in range(8):
                        board[i][j]="-"
        k=tuple([0,0])
        R=tuple([4,3])
        K=tuple([2,6])
        board[k[0]][k[1]]="k"
        board[R[0]][R[1]]="R"
        board[K[0]][K[1]]="K"

        K,R,k=coord(board)
        printboard(board)
        movnum=movmax
        while draw==False and stalemate==False and checkmate==False and movnum!=0:
                if player1move:
                        player1move=False
                else:
                        board[k[0]][k[1]]="-"
                        if player=="2":
                                x=k[0]
                                y=k[1]
                                while x>=k[0]+2 or x<=k[0]-2 or y<=k[1]-2 or k>=k[1]+2 or x>7 or x<0 or y<0 or y>7 or (x==k[0] and y==k[1]):
                                        x=int(input("Enter king x position:"))
                                        y=int(input("Enter king y position:"))
                                k=tuple([x,y])
                        else:
                                k=player2(board,K,R,k)
                        player1move=True
                board[R[0]][R[1]]="R"
                board[K[0]][K[1]]="K"
                board[k[0]][k[1]]="k"
                printboard(board)
                movnum-=1
                print("Moves =", movmax-movnum) 
        if draw:
                print("DRAW")
        elif stalemate:
                print("STALEMATE")
        elif checkmate:
                print("CHECKMATE")
        elif movnum==0:
                print("Ran out of moves")
                
# For Debugging purposes, check if the user wants to run a test, or actually play the game
# "Yes" to run the test, "No" to play a normal game.
while choice !="Y" and choice != "N":
        choice=input("Is this a test?(Y/N): ")
        choice=choice.upper()

        # Play Case       
        if choice=="NO" or "N":
                choice="N"
        # Test Case
        elif choice=="YES" or "Y":
                choice="Y"

        # Total number of moves to allow/execute
        movmax=int(input("Enter the maximum number of moves: (default is 35) "))
        if movmax=="":
                movmax=35


# Player vs Player Code Block
while choice=="N" and player!="1" and player!="2":
        # If this is not a test
        if choice=="N":
                # User must decide to be whether player 1(Offensive) or player 2(Defensive)
                player=input("Will you be player (1) or player (2)? ")

play(movmax)
