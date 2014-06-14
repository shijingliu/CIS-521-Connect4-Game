from copy import deepcopy

class Connect4Game(object):
	"""Plays a game of Connect 4 between two players"""
	
	def __init__(self, player1, player2):
		"""Sets up the game between two players"""
		
		self.player1 = player1
		self.player2 = player2
		self.board = [7*[0] for i in range(6)]
	
	def play(self):
		"""Runs the game"""
		
		while True:
			self.print_board()
			# Move a player
			move = self.player1.move(deepcopy(self.board))
			if not self.is_valid(move):
				print "ERROR: invalid move by player 1"
				return -1
			print "Player 1 move: " + str(move)
			# Update the board
			self.update_board(1, move)
			if self.player_wins(1) or self.board_full():
				break
				
			self.print_board()
			# Move a player
			move = self.player2.move(deepcopy(self.board))
			if not self.is_valid(move):
				print "ERROR: invalid move by player 2"
				return -2
			print "Player 2 move: " + str(move)
			# Update the board
			self.update_board(2, move)	
			if self.player_wins(2) or self.board_full():
				break
		
		# The game is over!
		print "GAME OVER"
		print "-----------"
		self.print_board()
		if self.player_wins(1):
			print "Player 1 wins!"
			return 1
		elif self.player_wins(2):
			print "Player 2 wins!"
			return 2
		else:
			print "It's a draw!"
			return 0
			
	def update_board(self, p, move):
		"""Updates the board given a player and a move.
		
		ASSUMTION: the move is assumed to be valid.
			
		"""
		idx = 5
		while self.board[idx][move] != 0:
			idx = idx - 1
		self.board[idx][move] = p
	
	def is_valid(self, move):
		"""Checks whether a given move is valid"""
		return self.board[0][move]==0
		
	def player_wins(self, p):
		"""Checks if player p has won"""
		# For every position on the board
		for i in range(6):
			for j in range(7):
				if self.board[i][j] == p:
					# See if it has 3 more in any direction starting here
					if i<=2 and self.board[i+1][j]==p and self.board[i+2][j]==p and self.board[i+3][j]==p:
						return True
					if i>=3 and self.board[i-1][j]==p and self.board[i-2][j]==p and self.board[i-3][j]==p:
						return True
					if j<=3 and self.board[i][j+1]==p and self.board[i][j+2]==p and self.board[i][j+3]==p:
						return True
					if j>=3 and self.board[i][j-1]==p and self.board[i][j-2]==p and self.board[i][j-3]==p:
						return True
					if i<=2 and j<=3 and self.board[i+1][j+1]==p and self.board[i+2][j+2]==p and self.board[i+3][j+3]==p:
						return True
					if i<=2 and j>=3 and self.board[i+1][j-1]==p and self.board[i+2][j-2]==p and self.board[i+3][j-3]==p:
						return True
					if i>=3 and j<=3 and self.board[i-1][j+1]==p and self.board[i-2][j+2]==p and self.board[i-3][j+3]==p:
						return True
					if i>=3 and j>=3 and self.board[i-1][j-1]==p and self.board[i-2][j-2]==p and self.board[i-3][j-3]==p:
						return True
		return False
	
	def print_board(self):
		print ""
		print "0  1  2  3  4  5  6"
		print "-------------------"
		"""Prints out the game board"""
		for row in self.board:
			for el in row:
				print str(el) + " ",
			print ""
		print ""
	
	def board_full(self):
		"""Indicates whether the board is completely full of pieces"""
		for row in self.board:
			for el in row:
				if el==0:
					return False
		return True
		
		
				
			
		
		