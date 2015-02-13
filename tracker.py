import RPi.GPIO as GPIO  
import time  
#from RPIO import PWM

tx = 17;
en = 18;
#af1 = 299;	# 200 max
#af2 = 100;	# 200 max
speed = 0.02;

#PWM.setup()
#PWM.init_channel(0, subcycle_time_us=5500)

# blinking function  
def modulate():  
# Add some pulses to the subcycle
#	PWM.add_channel_pulse(0, tx, 0, af1)
	GPIO.output(tx,GPIO.HIGH)
        time.sleep(speed)  
	GPIO.output(tx,GPIO.LOW)
        time.sleep(speed)  
        return  

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BCM)  
# set up GPIO output channel  
GPIO.setup(tx, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)  

# No Freq adjustment
GPIO.output(tx,GPIO.LOW)

# Silly  startup routine to work around NTX2B bug
GPIO.output(en,GPIO.HIGH)
time.sleep(1)
GPIO.output(en,GPIO.LOW)
time.sleep(0.1)
GPIO.output(en,GPIO.HIGH)

while True:
    modulate()

#PWM.cleanup()
GPIO.cleanup() 
