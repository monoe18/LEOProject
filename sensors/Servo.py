PIN_SERVO = 18

import RPi.GPIO as GPIO
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_SERVO, GPIO.OUT)
    GPIO.output(PIN_SERVO, True)
    pwm=GPIO.PWM(PIN_SERVO, 50) # 50 Hz
    pwm.start(0)
    return pwm
 

def servo_angle(servo_angle,pwm):
    duty = servo_angle / 18 + 2
    GPIO.output(PIN_SERVO, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(PIN_SERVO, False)
    pwm.ChangeDutyCycle(0)


def servo_stop():
    pwm.stop()
    GPIO.cleanup()
