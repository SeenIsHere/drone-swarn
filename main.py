from codrone_edu.swarm import *
from codrone_edu.drone import *
from threading import Thread
from hb import play_hb
from rand_move import random_drone_sequence
from pynput.keyboard import Key, Listener
import time

#connects to drone
swarm = Swarm()
swarm.auto_connect()

#if there are less than 3 drones, exit
if len(swarm.drone_objects) < 3:
    print("Please connect 3 drones")
    exit()

#checks battery
if not all([drone.get_battery() > 70 for drone in swarm.drone_objects]):
    print("Please charge all drones")
    exit()

#sets drone colors to match controller colors
swarm.drone_objects[0].set_drone_LED(255, 0, 0, 100)
swarm.drone_objects[0].set_controller_LED(255, 0, 0, 100)
swarm.drone_objects[1].set_drone_LED(0, 255, 0, 100)
swarm.drone_objects[1].set_controller_LED(0, 255, 0, 100)
swarm.drone_objects[2].set_drone_LED(0, 0, 255, 100)
swarm.drone_objects[2].set_controller_LED(0, 0, 255, 100)


#when backspace is pressed, all drones will land
def on_press(key):
    print(key)
    if key == Key.backspace:
        for drone in swarm.drone_objects:
            drone: Drone = drone
            drone.emergency_stop()
        swarm.close_all()
        return False

#function loop to check for on_press
def kill_drone():
    while True:
        with Listener(
            on_press=on_press) as listener:
            listener.join()

#function to control drone1
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

#function to control drone2
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

#function to control drone3
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

#drone movement functions
drone_funcs = [drone1, drone2, drone3]

#assigns drone function and drone instance to a thread
drone_threads = [Thread(target=func, args=(drone,)) for drone, func in zip(swarm.drone_objects, drone_funcs)]

#assigns kill_drone function to a thread
kill = Thread(target=kill_drone)

#start all threads
t = swarm.start_threading(*drone_threads, kill)