 # DOCUMENTATION: https://docs.robolink.com/docs/codrone-edu/python/reference/library/
from codrone_edu.drone import *
import codrone_edu.swarm
from time import sleep
from func import logflight
from random import randint

def random_move(drone):
    random.choice([
        lambda x: drone.move_forward(5),
        lambda x: drone.move_backward(5),
        lambda x: drone.move_left(5),
        lambda x: drone.move_right(5),
        lambda x: drone.flip("front"),
        lambda x: drone.flip("back"),
        lambda x: drone.triangle(),
        lambda x: drone.turn_degree(90),
        lambda x: drone.turn_degree(-90),
])(None)

def random_drone_sequence(drone):
    drone.takeoff()

    randomRGB = [randint(0, 255), randint(0, 255), randint(0, 255)]
    drone.set_drone_LED(*randomRGB, 100)
    drone.set_controller_LED(*randomRGB, 100)

    for _ in range(0, 10000):
        random_move(drone)
        drone.avoid_wall(50)
        drone.circle_turn(50)
        random_move()
        drone.set_throttle(75)

