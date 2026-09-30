from machine import Pin, PWM
from time import sleep

# Motor pins
motor1_speed = PWM(Pin(28))
motor1_direction = Pin(27, Pin.OUT)

motor2_speed = PWM(Pin(26))
motor2_direction = Pin(22, Pin.OUT)

# Motor frequency
motor1_speed.freq(1000)
motor2_speed.freq(1000)

# Settings
SPEED = 30000
FORWARD_TIME = 2.1
TURN_TIME = 0.75


def stop_car():
    motor1_speed.duty_u16(0)
    motor2_speed.duty_u16(0)


def start_car():
    motor1_speed.duty_u16(SPEED)
    motor2_speed.duty_u16(SPEED)


def forward():
    motor1_direction.value(1)
    motor2_direction.value(1)

    start_car()
    sleep(FORWARD_TIME)
    stop_car()
    sleep(0.5)


def backward():
    motor1_direction.value(0)
    motor2_direction.value(0)

    start_car()
    sleep(FORWARD_TIME)
    stop_car()
    sleep(0.5)


def left():
    motor1_direction.value(0)
    motor2_direction.value(1)

    start_car()
    sleep(TURN_TIME)
    stop_car()
    sleep(0.5)


def right():
    motor1_direction.value(1)
    motor2_direction.value(0)

    start_car()
    sleep(TURN_TIME)
    stop_car()
    sleep(0.5)


def turn_back():
    motor1_direction.value(0)
    motor2_direction.value(1)

    start_car()
    sleep(TURN_TIME * 2)
    stop_car()
    sleep(0.5)


# Start
stop_car()
sleep(3)

forward()
left()
forward()
left()
forward()
right()
forward()
right()
forward()
turn_back()
backward()

# Make sure the car stops
stop_car()