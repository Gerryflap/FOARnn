import numpy as np

from FoarConnection import FoarConnection


class Game(object):
    def __init__(self, foarConn: FoarConnection, playernum):
        self.board = np.matrix(np.zeros([6, 7]))
        self.boardHeights = [0] * 7
        self.foarConn = foarConn
        self.playernum = playernum

    def getPossibleStates(self):
        states = dict()
        for i in range(7):
            if self.boardHeights[i] != 6:
                newBoard = self.board.copy()
                newBoard[self.boardHeights[i], i] = 1
                states[i] = newBoard

    def doMove(self, index, player):
        symbol = 1 if player == self.playernum else -1
        self.board[self.boardHeights[index], index] = symbol
        self.boardHeights[index] += 1
