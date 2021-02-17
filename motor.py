import time
from adafruit_crickit import crickit
 
print("1 Servo 4 demo!")

print("Dual motor demo!")
motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2
 
while True:
    motor_1.throttle = 0.1 # full speed forward
    time.sleep(0.5)
    crickit.servo_4.angle = 90     # middle
    time.sleep(1)
    exit()
    
    motor_1.throttle = 0.9 # full speed forward
    time.sleep(0.5)
    #crickit.servo_4.angle = 90      # right
    
    motor_1.throttle = 0  # stopped
    #crickit.servo_4.angle = 90     # middle
    
    time.sleep(1)
    motor_1.throttle = 0.9 # full speed forward
    time.sleep(0.5)
    #crickit.servo_4.angle = 90
    time.sleep(5)
    motor_1.throttle = 0