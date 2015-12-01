import RPi.GPIO as GPIO

DUTY_CYCLE_HZ = 500

class Drive:
    def __init__(self):
        self.steering = GPIO.PWM(12, DUTY_CYCLE_HZ) # example pin output
        self.motor = GPIO.PWM(13, DUTY_CYCLE_HZ) # example pin output

        self.steering.start(50)
        self.motor.start(50)

    def steer(self, rate):
        turn_normalized = (rate + 1) / 2.0
        self.steering.ChangeDutyCycle(turn_normalized * 100)

    def accelerate(self, power):
        forward_normalized = (power + 1) / 2.0
        self.motor.ChangeDutyCycle(forward_normalized * 100)
        

