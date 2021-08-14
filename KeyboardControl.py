from djitellopy import tello

import KeyPressModule as key

from time import sleep

key.init()

me = tello.Tello()

me.connect()

print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50

    if key.getKey("LEFT"):
        lr = -speed

    elif key.getKey("RIGHT"):
        lr = speed

    if key.getKey("UP"):
        fb = speed

    elif key.getKey("DOWN"):
        fb = -speed

    if key.getKey("w"):
        ud = speed

    elif key.getKey("s"):
        ud = -speed

    if key.getKey("a"):
        yv = -speed

    elif key.getKey("d"):
        yv = speed

    if key.getKey("q"): me.land(); sleep(3)

    if key.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()

    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    sleep(0.05)
