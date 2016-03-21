import numpy as np
import socket as skt
import time
import threading

from Game import Game
from NNbot import playGame


def sendString(socket, string):
    socket.send(bytes(string + "\n", 'UTF-8'))



def receiveThread(foarConn):
    while 1:
        try:
            s = str(foarConn.socket.recv(4096))
            s = s
            command = s.split(" ")[:-1]
            print(command)

            foarConn.handleCommand(command)

        except Exception as e:
            print(e)



def startReceiveThread(foarConn):
    threading._start_new_thread(receiveThread, (foarConn, ))


class FoarConnection(object):
    def __init__(self, ip, port, name):
        self.socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.socket.settimeout(2)
        self.socket.connect((ip, port))
        self.lobby = set()
        self.name = name
        startReceiveThread(self)
        sendString(self.socket, "CONNECT " + name)
        sendString(self.socket, "LOBBY")

    def send(self, command):
        sendString(self.socket, command)

    def handleCommand(self, command):
        s = command[0]
        if s == "LOBBY":
            self.lobby = []
            for user in command[1:]:
                self.lobby.append(user)
        elif s == "START":
            playerNum = 1 if command[1] == self.name else 2
            playGame(self, playerNum)




if __name__ == "__main__":
    conn = FoarConnection("127.0.0.1", 1337, "Pizza")
    time.sleep(10)
    print(conn)
