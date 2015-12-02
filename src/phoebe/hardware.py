import pyfirmata import Arduino, util

class Vector3:
    @classmethod
    def Zero():
        return Vector3(0, 0, 0)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class IMUState:
    def __init__(self, accelerometer, gyroscope, magnetometer):
        self.accelerometer = accelerometer
        self.gyroscope = gyroscope
        self.magnetometer = magnetometer

class Hardware:
    def __init__(self, board):
        self.board = board
        self.analogIterator = util.Iterator(board)
        self.anologIterator.start()

    def setForwardSpeed(self, speed):
        self.board.analog[0].write(speed)

    def setSteering(self, steering):
        self.board.analog[1].write(steering)

    def distanceSensors(self):
        left = self.board.digital[2].read()
        right = self.board.digital[3].read()
        return (left, right)

    def imuState(self):
        return IMUState(Vector3.Zero(), Vector3.Zero(), Vector3.Zero())
