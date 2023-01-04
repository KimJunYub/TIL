import time
import sys

sys.stdout = open('stdout.txt','w')

pin = 4

try:	
    while True :        
        h, t = Adafruit_DHT.read_retry(sensor, pin)        
        if h is not None and t is not None :
            #print("Time="+time.strftime('%Y.%m.%d-%H:%M:%S')+"|Temperature={0:0.1f}*C|Humidity={1:0.1f}%".format(t, h))
            print("Time="+time.strftime('%H:%M')+"|Temperature={0:0.1f}*C|Humidity={1:0.1f}%".format(t, h))
            time.sleep(60)
        else :
            print('Read error')
            time.sleep(100)
except KeyboardInterrupt:
    print("End")    
finally:
    sys.stdout.close()