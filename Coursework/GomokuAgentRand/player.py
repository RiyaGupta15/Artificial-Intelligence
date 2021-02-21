import numpy as np

from misc import legalMove
from gomokuAgent import GomokuAgent

class Player(GomokuAgent):
    def move(self, board):
        while True:
            moveLoc = tuple(np.random.randint(self.BOARD_SIZE, size=2))
            if legalMove(board, moveLoc):
                return moveLoc


#player_loc = [[],[]]

    #def player_move(self, board):
     #   while True:
      #      moveLoc = input('Enter the coordinates you want to move to')
       #     if legalMove(board, moveLoc):
        #        return moveLoc

#players = []

 #   def Qualification(self, players):
  #      count = 0
   #     time = 5



