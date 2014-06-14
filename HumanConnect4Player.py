from random import randint

class HumanConnect4Player(object):
    """A Connect4Player that asks the user for a move"""
    
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
    
        return int(raw_input("Player " + str(self.player_number) + ", enter your move (0-6): "))