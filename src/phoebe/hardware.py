import pyfirmata import Arduino, util
import smbus

class Vector3:
	@classmethod
	def Zero():
		return Vector3(0, 0, 0)

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
    	def __eq__(self, other):
    	    if other is not Vector3:
    	        return false
    	    return other.x == self.x && other.y == self.y && other.z == self.z

        def __ne__(self, other):
        	return not (self == other)

class IMUState:
	def __init__(self, accelerometer, gyroscope, magnetometer):
		self.accelerometer = accelerometer
		self.gyroscope = gyroscope
		self.magnetometer = magnetometer

        def __eq__(self, other):
            if other is not IMUState:
                return false
            return other.accelerometer == self.accelerometer &&
                   other.gyroscope == self.gyroscope &&
                   other.magnetometer == self.magnetometer

            def __ne__(self, other):
                return not (self == other)

class Hardware:
	def __init__(self, board, bus):
		self.board = board
		self.bus = bus
		bus.open()
# 		self.analogIterator = util.Iterator(board)
# 		self.anologIterator.start()

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