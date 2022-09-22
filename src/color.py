import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)

class ColorSensor:

    def __init__(self) -> None:
        self.s2 = 20
        self.s3 = 16
        self.signal = 21
        self.NUM_CYCLES = 20
        self.colorRead = ""
        self.red_Tr = 19000
        self.green_Tr = 18000
        self.blue_Tr = 24000
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.s2,GPIO.OUT)
        GPIO.setup(self.s3,GPIO.OUT)
        #print("\n")
        print("Start")
    
    def getColor(self, printValues=False):
        
        GPIO.output(self.s2,GPIO.LOW)
        GPIO.output(self.s3,GPIO.LOW)
        #sleep(0.3)
        start = time()

        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time() - start      #seconds to run for loop
        red  = self.NUM_CYCLES / duration   #in Hz
        
        
        GPIO.output(self.s2,GPIO.LOW)
        GPIO.output(self.s3,GPIO.HIGH)
        #sleep(0.3)
        start = time()
        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time() - start
        blue = self.NUM_CYCLES / duration
        

        GPIO.output(self.s2,GPIO.HIGH)
        GPIO.output(self.s3,GPIO.HIGH)
        #sleep(0.3)
        start = time()
        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time() - start
        green = self.NUM_CYCLES / duration
        
        if printValues:
            print(f'red value - {red}')
            print(f'blue value - {blue}')
            print(f'green value - {green}')
        
        if red < 10000 and green < 10500 and blue < 10000:
            self.colorRead = "Black"
        elif red > 20000 and green > 20000 and blue > 20000:
            self.colorRead = "White"
        elif green < red > blue:
            self.colorRead = "Red"
        elif red < blue > green:
            self.colorRead = "Blue"
        elif blue < green > red:
            self.colorRead = "Green"
        
        return self.colorRead
        

    def endprogram(self):
        GPIO.cleanup()
    





