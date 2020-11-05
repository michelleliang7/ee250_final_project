import sys
import time
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
import grovepi
from grovepi import *
from grove_rgb_lcd import *

if __name__ == '__main__':
    thresh = 400
    PORT = 4
    sound_sensor = 0
    # for calculating sensor threshold: grovepi.pinMode(sound_sensor,"INPUT")
    grovepi.pinMode(sound_sensor,"INPUT")
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        try:
            dist = grovepi.ultrasonicRead(PORT)
        except TypeError:
            print ("Error") # maybe do something else?
        except IOError:
            print ("Error")

        #json_body[0]['fields']['Float_value'] = dist
        #client.write_points(json_body)
        try: 
         sensor_value = grovepi.analogRead(sound_sensor)
        except: 
           print ("Sensor failed")
        if sensor_value>thresh:
          print("sound heard")
