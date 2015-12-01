import unittest
import mock

@patch("RPi.GPIO.PWM", autospec=True)
class TestDrive(unittest.TestClass): # vroom, vroom
    def setup(self, mock):
        self.steer_mock = MagicMock()
        self.drive_mock = MagicMock()

        mock.side_effect = [self.steer_mock, self.drive_mock]

    def test_init(self, mock):
        drive = Drive()
        mock.assert_has_calls([call(12, 500), call(13, 500)])

    def test_steer_left(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.steer(-0.5)
        self.steer_mock.ChangeDutyCycle.assert_called_with(25)

    def test_steer_left_over(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.steer(-1.5)
        self.steer_mock.ChangeDutyCycle.assert_called_with(0)

    def test_steer_right(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.steer(0.5)
        self.steer_mock.ChangeDutyCycle.assert_called_with(75)

    def test_steer_right_over(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.steer(1.5)
        self.steer_mock.ChangeDutyCycle.assert_called_with(100)

    def test_accelerate_forward(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.accelerate(0.5)
        self.drive_mock.ChangeDutyCycle.assert_called_with(75)

    def test_accelerate_forward_over(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.accelerate(1.5)
        self.drive_mock.ChangeDutyCycle.assert_called_with(100)

    def test_accelerate_brake(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.accelerate(-0.5)
        self.drive_mock.ChangeDutyCycle.assert_called_with(25)

    def test_accelerate_brake_over(self, mock):
        drive = Drive()
        mock.reset_mock
        drive.accelerate(-1.5)
        self.drive_mock.ChangeDutyCycle.assert_called_with(0)
