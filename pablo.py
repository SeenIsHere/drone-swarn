from codrone_edu.drone import *
from time import sleep

drone = Drone()

drone.check()

drone.pair()
drone.takeoff()

drone.set_throttle(75)
drone.move(1)

drone.circle()
time.sleep(3)

drone.flip("front")
time.sleep(3)

drone.flip("back")
drone.land()


drone.close()

