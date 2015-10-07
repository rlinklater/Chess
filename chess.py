import copy
import sys
from OffenseTest import *
choice=""
draw=False
stalemate=False
checkmate=False
player="0"
text=open("gameResult.txt","w")
def FileRead():
        testCase = "TestCase1: "
        with open("testCase.txt", 'r') as f:
                
                for line in f:
                        if line[0] == "x":
                                # PlayerX piece coordinate
                                # PlayerX - King Piece
                                xK = tuple([int(line[4])-1, int(line[6])-1]) # Creates tuple for PlayerX's King
                                        #               PlayerX - Rook Piece
                                xR = tuple([int(line[14])-1, int(line[16])-1]) #               Creates tuple for PlayerX's Rook   
                                # PlayerY - King Piece
                                yK = tuple([int(line[24])-1, int(line[26])-1]) #       Creates tuple for PlayerY's King
                        else:
                                # Print "Coordinate format unrecognized"
                                pass
                
        return xK,xR,yK, testCase
#determines heuristic value for player 2
def heuristic2(test):
        hval=abs(float(test[0])-3.5)+abs(float(test[1])-3.5)+float(test[2])
        return(hval)

#automated player 2 move
def player2(board,K,R,k):
        possible=moves(board,K,R,k,2)
        global stalemate
        global checkmate
        global draw
        #if it is a draw king takes Rook
        if draw:
                print("HELLO")
                return(R)
        #check if a checkmate or stalemate has occurred
        if possible==[]:
                stalemate=True
                if R[0]==k[0] or R[1]==k[1]:
                        checkmate=True
                        stalemate=False
                return k

        p2=[]
        #create a tuple with x and y coordinates of player 2 with their heuristic value
        for i in possible:
                p2.append(tuple([i[0],i[1],heuristic2(i)]))
        return(p2)

#defines possible rook moves
def rookMoves(board,board1,board2,K,R,k):
        for i in range(8):
                if board[R[0]][i] =="-" and board2[R[0]][i] !="O":
                        if R[0]==K[0] and R[0]==k[0]:
                                if abs(R[1]-K[1]) < abs(R[1]-k[1]):
                                        block=K[1]
                                if (R[1]>block and i>block) or (R[1]<block and i<block):
                                        if board1[R[0]][i]=="Z":
                                                board1[R[0]][i]="Y"
                                        else:
                                                board1[R[0]][i]="X"
                        elif R[0]==K[0]:
                                if (R[1]>K[1] and i>K[1]) or (R[1]<K[1] and i<K[1]):
                                        if board1[R[0]][i]=="Z":
                                                board1[R[0]][i]="Y"
                                        else:
                                                board1[R[0]][i]="X"     
                        elif R[0]==k[0]:
                                if (R[1]>k[1] and i>k[1]) or (R[1]<k[1] and i<k[1]):
                                        if board1[R[0]][i]=="Z":
                                                board1[R[0]][i]="Y"
                                        else:
                                                board1[R[0]][i]="X"
                        else:
                                if board1[R[0]][i]=="Z":
                                                board1[R[0]][i]="Y"
                                else:
                                        board1[R[0]][i]="X" 
                if board[i][R[1]]=="-" and board2[i][R[1]]!="O":
                        if R[1]==K[1] and R[1]==k[1]:
                                if abs(R[0]-K[0]) < abs(R[0]-k[0]):
                                        block=K[0]
                                if (R[0]>block and i>block) or (R[0]<block and i<block):
                                        if board1[i][R[1]]=="Z":
                                                board1[i][R[1]]="Y"
                                        else:
                                                board1[i][R[1]]="X"
                        elif R[1]==K[1]:
                                if (R[0]>K[0] and i>K[0]) or (R[0]<K[0] and i<K[0]):
                                        if board1[i][R[1]]=="Z":
                                                board1[i][R[1]]="Y"
                                        else:
                                                board1[i][R[1]]="X"     
                        elif R[1]==k[1]:
                                if (R[0]>k[0] and i>k[0]) or (R[0]<k[0] and i<k[0]):
                                        if board1[i][R[1]]=="Z":
                                                board1[i][R[1]]="Y"
                                        else:
                                                board1[i][R[1]]="X"
                        else:
                                if board1[i][R[1]]=="Z":
                                                board1[i][R[1]]="Y"
                                else:
                                        board1[i][R[1]]="X" 
#defines possible moves for the offensive king
def oKingMoves(board,board1,board2,K,R,k):
        for i in range(8):
                for j in range(8):
                        if (board[i][j]=="-" or board[i][j]=="R")  and i<=K[0]+1 and i>=K[0]-1 and j<=K[1]+1 and j>=K[1]-1:
                                if board1[i][j]=="X":
                                        board1[i][j]="Y"
                                elif board[i][j]=="R":
                                        #print("Protected")
                                        board2[i][j]="r"
                                elif board2[i][j]=="O":
                                        board1[i][j]="s"
                                else:
                                        board1[i][j]="Z"
#defines moves for the defensive king
def dKingMoves(board,board1,board2,K,R,k):
        global draw
        for i in range(8):
                for j in range(8):
                        if (board1[i][j]=="-" or board1[i][j]=="R") and i<=k[0]+1 and i>=k[0]-1 and j<=k[1]+1 and j>=k[1]-1:
                                if board2[i][j]=="-":
                                        board2[i][j]="O"
                                elif board2[i][j]=="R":
                                        board2[i][j]="D"
#finds possible moves using rookMoves,oKingMoves,dKingMoves, and possible moves
def moves(board, K,R,k,turn):
        global player
        board1 = createboard(K,R,k)
        board2 = createboard(K,R,k)

        if turn==2:
                #creates a board of possible moves for player 2
                rookMoves(board,board1,board2,K,R,k)
                oKingMoves(board,board1,board2,K,R,k)
                dKingMoves(board,board1,board2,K,R,k)
                #printboard(board2)
                return possiblemoves(board2,"2")
                #return(board2)
        elif turn==1:
                #creates a board of possible moves for player 1
                if player != "1":
                        dKingMoves(board,board1,board2,K,R,k)
                rookMoves(board,board1,board2,K,R,k)
                oKingMoves(board,board1,board2,K,R,k)
                #printboard(board1)
                return possiblemoves(board1,"1")
                #return(board1)

#takes a board of possible moves and returns a list of tuples of possible moves
def possiblemoves(board,c):
        #possible moves for player 2 (x,y,whether or not you can take the rook)
        if c == "2":
                p2=[]
                for j in range(len(board)):
                        for i in range(len(board[j])):
                                if board[i][j]=="O":
                                        p2.append(tuple([i,j,10]))
                                elif board[i][j]=="D":
                                        p2.append(tuple([i,j,0]))
                                        draw=True
                return p2
        #possible moves for player 1 (x,y, piece that made the move)
        elif c == "1":
                p1=[]
                for j in range(len(board)):
                        for i in range(len(board[j])):
                                if board[i][j]=="X" or board[i][j]=="s":
                                        p1.append(tuple([i,j,"R"]))
                                elif board[i][j]=="Z":
                                        p1.append(tuple([i,j,"K"]))
                                elif board[i][j]=="Y":
                                        p1.append(tuple([i,j,"R"]))
                                        p1.append(tuple([i,j,"K"]))
                return p1
#finds the coordinates of the pieces given the board
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
        #print(K,R,k)
        return(K,R,k)
#prints out the board given the board
def createboard(K,R,k):
        board = [[0 for x in range(8)] for x in range(8)] 
        for i in range(8):
                for j in range(8):
                        board[i][j]="-"
        board[k[0]][k[1]]="k"
        board[R[0]][R[1]]="R"
        board[K[0]][K[1]]="K"
        return board
def printboard(board):
        terminal=sys.stdout
        print("Board=>")
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
        sys.stdout=text
        print("Board=>")
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
        sys.stdout=terminal
#body of the program, makes sure that you may not go past the allowed amount of moves
#also checks for draw, stalemate, and checkmate
def play(movmax):
        movnum=movmax
        global player
        global stalemate
        global checkmate
        global draw
        global text
        #to switch between player 1 and player 2
        player1move=True
        
        
        #creates the coordinates for the board
        K,R,k,line=FileRead()

        #builds the board
        board=createboard(K,R,k)


        #calling offenseive class
        player1=Offense(K,R,k)

        terminal=sys.stdout
        print("================================")
        print("Game started.....")  
        if player=="0":
                print("Test case",end=" ") 
        print("x.K",K," x.R", R, " y.K", k)
        print("================================")
        sys.stdout=text
        print("================================")
        print("Game started.....")  
        if player=="0":
                print("Test case",end=" ") 
        print("x.K",K," x.R", R, " y.K", k)
        print("================================")
        sys.stdout=terminal
        #K,R,k=coord(board)
        printboard(board)
        movnum=movmax
        while draw==False and stalemate==False and checkmate==False and movnum!=0:
                if player1move:
                        #makes sure player 2 goes next
                        player1move=False
                        #if player 1 is the human (or other program) input
                        if player=="1":
                                piece=""
                                while piece != "R" and piece != "K":
                                        piece=input("Are you using the (R)ook or the (K)ing?:")
                                        piece=piece.upper()
                                        if piece == "ROOK":
                                                piece="R"
                                        elif piece == "KING":
                                                piece="K"
                                #takes care of rook moves
                                if piece=="R":
                                        x=R[0]
                                        y=R[1]
                                        possible=moves(board,K,R,k,1)
                                        board[R[0]][R[1]]="-"
                                        illegal=True
                                        while illegal:
                                                x=int(input("Enter Rooke x position:"))
                                                y=int(input("Enter Rooke y position:"))
                                                for i in possible:
                                                        if i[2]=="R":
                                                                if i[0]== x and i[1]==y:
                                                                        illegal=False

                                        R=tuple([x,y])
                                #takes care of king moves
                                elif piece=="K":
                                        x=K[0]
                                        y=K[1]
                                        possible=moves(board,K,R,k,1)
                                        board[K[0]][K[1]]="-"
                                        illegal=True
                                        while illegal:
                                                x=int(input("Enter King x position:"))
                                                y=int(input("Enter King y position:"))
                                                for i in possible:
                                                        if i[2]=="K":
                                                                if i[0]== x and i[1]==y:
                                                                        illegal=False

                                        K=tuple([x,y])
                        else:
                                #where the AI for player 1 goes
                                #min_max_p1(board,K,R,k)
                                print("No AI for player 1")
                        #checks for stalemates or checkmates
                        if moves(board,K,R,k,2) == []:
                                stalemate=True
                                if k[0]==R[0] or k[1]==R[1]:
                                        stalemate=False
                                        checkmate=True
                else:
                        #decrements number of moves left
                        movnum-=1
                        #eliminates k from the board till it gets replaced
                        board[k[0]][k[1]]="-"
                        if player=="2":
                                #does validation for player 2 human input
                                x=k[0]
                                y=k[1]
                                possible=moves(board,K,R,k,2)
                                illegal=True
                                while illegal:
                                        x=int(input("Enter king x position:"))
                                        y=int(input("Enter king y position:"))
                                        for i in possible:
                                                if i[0]== x and i[1]==y:
                                                        illegal=False

                                k=tuple([x,y])
                        else:
                                #player 2 AI
                                #kprime=min_max_p2(board,K,R,k)
                                p2=player2(board,K,R,k)
                                H=1000
                                for i in p2:
                                        if H> i[2]:
                                                H=i[2]
                                                kprime=i
                                k=tuple([kprime[0],kprime[1]])
                        #makes sure that player 1 goes next
                        player1move=True
                        if k==R:
                                draw=True
                        print("Moves =", movmax-movnum)
                #makes sure that the pieces are on the board
                board[R[0]][R[1]]="R"
                board[K[0]][K[1]]="K"
                board[k[0]][k[1]]="k"
                player1.setKingCoord(K)
                player1.setRookCoord(R)
                player1.setOpp_KingCoord(k)
                #prints the board after the move
                printboard(board)

                #prints number of moves
                 
        #prints out the result of the game

        if stalemate or draw:
                print("STALEMATE")
        elif checkmate:
                print("CHECKMATE")
        elif movnum==0:
                print("Ran out of moves")
        sys.stdout=text
        if stalemate or draw:
                print("STALEMATE")
        elif checkmate:
                print("CHECKMATE")
        elif movnum==0:
                print("Ran out of moves")
        sys.stdout=terminal
                
#gets initial input from the user 
while choice !="Y" and choice != "N":
        #decides if there will be human input
        choice=input("Is this a test?: ")
        choice=choice.upper()
        if choice=="NO":
                choice="N"
        elif choice=="YES":
                choice="Y"
        #gets the max number of moves in the game
        try:
                movmax=int(input("Enter the maximum number of moves: (default is 35) "))
        except:
                print("No number entered, default of 35 will be used")
                movmax=35
#gets who the human will be playing as
while choice=="N" and player!="1" and player!="2":
        if choice=="N":
                player=input("Will you be player (1) or player (2)? ")
#starts the main program
play(movmax)
