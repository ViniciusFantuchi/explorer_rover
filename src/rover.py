from gpiozero import Robot, DistanceSensor, Servo, LED
from time import sleep
from color import colorSensor

class Explorer:

    myCorrection = 0.45
    maxPW = (2.0+myCorrection)/1000
    minPW = (1.0-myCorrection)/1000

    move_power = 0.6
    turn_power = 1
    
    def __init__(self):
        
        self.color = colorSensor()
        self.robot = Robot(left=(7,8), right=(9,10))
        self.distanceSensor = DistanceSensor(23, 24)



        self.servo1 = Servo(19,
                            min_pulse_width=explorer.minPW,
                            max_pulse_width=explorer.maxPW)

        self.servo2 = Servo(26,
                            min_pulse_width=explorer.minPW,
                            max_pulse_width=explorer.maxPW)

        self.servoInitialposition()
        
        self.ledR = LED(4)
        self.ledG = LED(17)
        self.ledB = LED(27)


    def servoInitialposition(self):
        self.servo1.max()
        self.servo2.max()
        sleep(0.2)
        self.servo1.detach()
        self.servo2.detach()


    def moveForward(self, power: float, t: float):
        print("forward", t)
        self.robot.forward(power)
        sleep(float(t))
        self.robot.stop()

    def moveBackward(self, power: float, t: float):
        print("backward", t)
        explorer.backward(v)
        sleep(float(textboxB.value))
        explorer.stop()
        
    def turnLeft(self, power: float, t: float):
        print("Turn Left", t)
        self.robot.left(power)
        sleep(float(t))
        self.robot.stop()
        
    def turnRight(self, power: float, t: float):
        print("Turn Right", t)
        explorer.right(power)
        sleep(float(t))
        self.robot.stop()
    
    
    ####servo    
    def openGripper(self):
        self.servo1.mid()
        sleep(0.2)
        self.servo1.detach()

    def closeGripper(self):
        self.servo1.max()
        sleep(0.2)
        self.servo1.detach()

    def upGripper(self):
        self.servo2.mid()
        sleep(0.2)
        self.servo2.detach()
        
    def downGripper(self):
        self.servo2.max()
        sleep(0.2)
        self.servo2.detach()

