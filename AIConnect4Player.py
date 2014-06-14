#from random import randint
import random
import collections
import itertools

class AIConnect4Player(object):
    cache=collections.defaultdict(int)
    gameover=collections.defaultdict(bool)
    
    def __init__(self, player_number):
        """Initializes the Connect4Player. DON'T CHANGE THIS!"""
        self.player_number = player_number
    
    def move(self, board):
        """Returns the next move of the Connect4Player.
        The value returned is an integer from 0-6, specifying
        which column the player's piece should be dropped in
        
        Arguments:
        board -- this is a 6x7 array containing the
            contents of the current game board.
            Each entry will be either 0 (empty),
            1 (occupied by Player 1) or 2 (occupied by Player 2)   
        """
        empty=0
        depth = 6
        for row in board:
            empty+=sum(x==0 for x in row)
        if empty<5:
            depth= 5
        elif empty<10:
            depth= 10
        elif empty<15:
            depth= 13
        elif empty<20:
            depth= 9
        elif empty<30:
            depth= 7
        best_move, value = self.bestMove(depth, board, self.player_number)
        return best_move

    def bestMove (self, depth, board, player_number):
        opp_number=1+(player_number==1)
        legal_moves=collections.defaultdict(int)
        idx=collections.deque()
        idx=collections.deque()
        for j in xrange(7):            
            for i in itertools.ifilter(lambda x: board[x][j]==0, xrange(5,-1,-1)):
                idx.append((i,j))
                break
        for tmp,col in idx:
            # generate new board
            board[tmp][col]=player_number
            # update value
            legal_moves[col]=self.search(depth-1,board,-99999999,99999999,opp_number,player_number)
            board[tmp][col]=0
        #print legal_moves
        maxval=-99999999
        maxidx=-1
        for i,j in legal_moves.iteritems():
            if j>maxval:
                maxval=j
                maxidx=i
            elif (j==maxval) and (abs(i-3)<abs(maxidx-3)):
                maxidx=i
        return (maxidx,maxval)

    def search (self, depth, board, alpha, beta, player_number, best_player):
        opp_number = 1+(player_number==1)
        if(depth==0):
            return self.value(board,best_player,best_player==player_number)-self.value(board,1+(best_player==1),best_player!=player_number)
        
        idx=collections.deque()
        for j in xrange(7):            
            for i in itertools.ifilter(lambda x: board[x][j]==0, xrange(5,-1,-1)):
                idx.append((i,j))
                break
        shuf=range(0,len(idx))
        random.shuffle(shuf)
        idx=[idx[k] for k in shuf]
        
        ok=False
        
        best=alpha if player_number==best_player else beta
        
        for tmp,col in idx:
            ok=True
            board[tmp][col]=player_number
            if self.gameIsOver(board, player_number):
               	board[tmp][col]=0
               	return 30000 if best_player==player_number else -30000
            if player_number==best_player:
                best=max(best,self.search(depth-1,board,best,beta,opp_number,best_player))
                board[tmp][col]=0
                if best>beta:                    
                    return beta
            else:
                best=min(best,self.search(depth-1,board,alpha,best,opp_number,best_player))
                board[tmp][col]=0
                if best<alpha:
                    return alpha
        if ok:  
            return best  
        else:
            return 0
        
    def gameIsOver(self, board, player):
        tup=(player,str(board))
        if tup in self.gameover:
            return self.gameover[tup]
        #row
        for i in xrange(6):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i][j+t]==player:
                        tot+=1
                    elif board[i][j+t]!=0:
                        tot=0
                        break
                if tot==4:
                    self.gameover[tup]=True
                    return True
                
        #column
        for j in xrange(7):
            for i in xrange(3):
                tot=0
                for t in xrange(4):
                    if board[i+t][j]==player:
                        tot+=1
                    elif board[i+t][j]!=0:
                        tot=0
                        break
                if tot==4:
                    self.gameover[tup]=True
                    return True
                    
        for i in xrange(3):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i+t][j+t]==player:
                        tot+=1
                    elif board[i+t][j+t]!=0:
                        tot=0
                        break
                if tot==4:
                    self.gameover[tup]=True
                    return True

        for i in xrange(3):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i+3-t][j+t]==player:
                        tot+=1
                    elif board[i+3-t][j+t]!=0:
                        tot=0
                        break
                if tot==4:
                    self.gameover[tup]=True
                    return True
        self.gameover[tup]=False            
        return False
        
    def value(self, board, player, is_current_player):
        tup=(player,str(board))
        if tup in self.cache:
            return self.cache[tup]
        counter = collections.defaultdict(int)
        idx=[]
        for i in xrange(7):            
            try:
                j=next(itertools.ifilter(lambda x: board[x][i]==0, xrange(6)))
            except StopIteration:
                idx.append(-1)
            idx.append(i)
        
        #row
        for i in xrange(6):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i][j+t]==player:
                        tot+=1
                    elif board[i][j+t]!=0:
                        tot=0
                        break
                    else:
                        if (i-idx[j+t])%2==is_current_player:
                            tot-=0.5
                tot=int(tot)
                if tot>0:
                    counter[tot]+=1
                
        #column
        for j in xrange(7):
            for i in xrange(3):
                tot=0
                for t in xrange(4):
                    if board[i+t][j]==player:
                        tot+=1
                    elif board[i+t][j]!=0:
                        tot=0
                        break
                tot=int(tot)
                if tot>0:
                    counter[tot]+=1
                    
        for i in xrange(3):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i+t][j+t]==player:
                        tot+=1
                    elif board[i+t][j+t]!=0:
                        tot=0
                        break
                    else:
                        if (i+t-idx[j+t])%2==is_current_player:
                            tot-=0.5
                tot=int(tot)
                if tot>0:
                    counter[tot]+=1

        for i in xrange(3):
            for j in xrange(4):
                tot=0
                for t in xrange(4):
                    if board[i+3-t][j+t]==player:
                        tot+=1
                    elif board[i+3-t][j+t]!=0:
                        tot=0
                        break
                    else:
                        if (i+3-t-idx[j+t])%2==is_current_player:
                            tot-=0.5
                tot=int(tot)
                if tot>0:
                    counter[tot]+=1
        tmp=64*counter[3]+32*counter[2]+8*counter[1]+30000*counter[4]         
        self.cache[tup]=tmp
        return tmp
