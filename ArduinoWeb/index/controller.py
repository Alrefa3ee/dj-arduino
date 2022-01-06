import pyfirmata2
try:
    PORT = pyfirmata2.Arduino.AUTODETECT
    board = pyfirmata2.Arduino(PORT)
except:
    print('Port error')


def blueOn():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)

def redOn():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)

def greenOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)


def yellowOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)

def allOff():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)


