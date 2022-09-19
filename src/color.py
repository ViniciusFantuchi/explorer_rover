import RPi.GPIO as GPIO
from time import sleep, time

class colorSensor:

    def __init__(self) -> None:
        self.s2 = 20
        self.s3 = 16
        self.signal = 21
        self.NUM_CYCLES = 20
        self.colorRead
        self.red_Tr = 19000
        self.green_Tr = 18000
        self.blue_Tr = 24000
        self.GPIO.setwarnings(False)
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.s2,GPIO.OUT)
        GPIO.setup(self.s3,GPIO.OUT)
        print("\n")
        print("Start")
    
    def getColor(self, printValues=False):
        
        GPIO.output(self.s2,GPIO.LOW)
        GPIO.output(self.s3,GPIO.LOW)
        sleep(0.3)
        start = time()

        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time() - start      #seconds to run for loop
        red  = self.NUM_CYCLES / duration   #in Hz
        
        
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time() - start
        blue = self.NUM_CYCLES / duration
        

        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time()
        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(self.signal, GPIO.FALLING)
        duration = time.time() - start
        green = self.NUM_CYCLES / duration
        
        if printValues:
            print(f'red value - {red}')
            print(f'blue value - {blue}')
            print(f'green value - {green}')
        
        if red > 19000 and green > 19000 and blue > 19000:
            colorRead = "White"
        elif red < 9000 and green < 9000 and blue < 9000:
            colorRead = "Black"
        else:
            if red > green and red > blue:
                colorRead = "Red"
            elif blue > green and blue > red:
                colorRead = "Blue"
            else:
                colorRead = "Green"
            
    #    if red > 19000 and green > 19000 and blue > 19000:
    #        colorRead = "White"
    #    elif red > red_Tr and green < green_Tr and blue < blue_Tr:
    #        colorRead = "Red"
    #    elif red < red_Tr and green < green_Tr and blue > blue_Tr:
    #        colorRead = "Blue"
    #    elif red < red_Tr and green > green_Tr and blue < blue_Tr:
    #        colorRead = "Green"
    #    else:
    #        colorRead = "Black"
        
        return colorRead
        

    def endprogram(self):
        GPIO.cleanup()
    





