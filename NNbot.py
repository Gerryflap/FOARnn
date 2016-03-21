from Game import Game
from nn import NeuralNetwork


class NNtrainer(object):
    def __init__(self, foarConn, playernum):
        self.game = Game(foarConn, playernum)
        self.foarConn = foarConn
        self.nn = NeuralNetwork([5*6,3*4,2*3], 6*7, 2)

    def moveDone(self, index, playerNum):
        self.game.doMove(index, playerNum)

    def moveReq(self):
        maxI = 0
        maxScore = 0
        possibleStates = self.game.getPossibleStates()
        for i in possibleStates:
            score = self.nn.process(possibleStates[i].flatten())[0]
            if maxScore < score:
                maxI = i
                maxScore = score

        self.foarConn.send("MOVE " + maxI)