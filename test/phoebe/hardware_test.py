import doubles
import unittest
import pyfirmata
import smbus

class hardware_test(doubles.unittest.TestClass):
    def setup(self):
        self.board = InstanceDouble('pyfirmata.Arduino')
        self.bus = InstanceDouble('smbus.SMBus')
        expect(self.bus).open
        self.hardware = Hardware(self.board, self.bus)
    
    def testForwardSpeed(self):
        self.hardware.setForwardSpeed(1)
        # TODO: figure out how to write this...

    def testSetSteering(self):
        # TODO: figure out how to write this...
        self.hardware.setSteering(1)

    def testDistanceSensors(self):
        # TODO: mock out reading from analog
        left, right = self.hardware.distanceSensors()
        assert(left == 20)
        assert(right == 25)

    def testIMUState(self):
         # TODO: test that we read the IMU from i2c
        state = self.hardware.imuState()
        accel = Vector3(1, 2, 3)
        gyro = Vector3(2, 3, 4)
        mag = Vector3(3, 4, 5)
        assert(state == IMUState(accel, gyro, mag))