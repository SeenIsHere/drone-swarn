from codrone_edu.swarm import *
from codrone_edu.drone import *
from threading import Thread
from hb import play_hb
from rand_move import random_drone_sequence
from pynput.keyboard import Key, Listener
import time

swarm = Swarm()
swarm.auto_connect()

if len(swarm.drone_objects) < 3:
    print("Please connect 3 drones")
    exit()

if not all([drone.get_battery() > 70 for drone in swarm.drone_objects]):
    print("Please charge all drones")
    exit()

swarm.drone_objects[0].set_drone_LED(255, 0, 0, 100)
swarm.drone_objects[0].set_controller_LED(255, 0, 0, 100)
swarm.drone_objects[1].set_drone_LED(0, 255, 0, 100)
swarm.drone_objects[1].set_controller_LED(0, 255, 0, 100)
swarm.drone_objects[2].set_drone_LED(0, 0, 255, 100)
swarm.drone_objects[2].set_controller_LED(0, 0, 255, 100)


def on_press(key):
    print(key)
    if key == Key.backspace:
        for drone in swarm.drone_objects:
            drone: Drone = drone
            drone.emergency_stop()
        swarm.close_all()
        return False

def kill_drone():
    while True:
        with Listener(
            on_press=on_press) as listener:
            listener.join()

def drone1(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    drone.move_forward(30)
    time.sleep(3)

   

    drone.flip("back")
    time.sleep(4)

    drone.set_throttle(65)
    time.sleep(3)

    drone.hover(1)

    drone.turn_degree(180)

    drone.move_forward(30)
    time.sleep(3)
    
    drone.turn_degree(180)
    drone.land()

def drone2(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    drone.move_backward(30)
    time.sleep(3)

    drone.flip("front")
    time.sleep(4)

    drone.set_throttle(65)
    time.sleep(3)

    drone.hover(1)

    drone.turn_degree(180)

    drone.move_backward(30)
    time.sleep(3)

    drone.turn_degree(180)
    drone.land()


def drone3(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    drone.move_forward(30)
    time.sleep(3)


    drone.flip("back")
    time.sleep(4)

    drone.set_throttle(65)
    time.sleep(3)

    drone.hover(1)

    drone.turn_degree(180)

    drone.move_forward(30)
    time.sleep(3)
    
    drone.turn_degree(180)
    drone.land()

drone_funcs = [drone1, drone2, drone3]

drone_threads = [Thread(target=func, args=(drone,)) for drone, func in zip(swarm.drone_objects, drone_funcs)]

kill = Thread(target=kill_drone)

t = swarm.start_threading(*drone_threads, kill)