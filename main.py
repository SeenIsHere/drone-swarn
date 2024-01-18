from codrone_edu.drone import *
from codrone_edu.swarm import Drone
from threading import Thread
from hb import play_hb
from pynput.keyboard import Key, Listener
import time
from func import logflight, EvilSwarm

program_finished = False

swarm: Drone = EvilSwarm()
swarm.auto_connect()

if len(swarm.drone_objects) < 3:
    print("Please connect 3 drones")
    exit()

if not all([drone.get_battery() > 70 for drone in swarm.drone_objects]):
    print("Please charge all drones")
    exit()

#In order of drone connections
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

for color, drone in zip(colors, swarm.drone_objects):
    drone.set_drone_LED(*color, 100)
    drone.set_controller_LED(*color, 100)

def on_press(key):
    if key == Key.backspace:
        for drone in swarm.drone_objects:
            drone: Drone = drone
            drone.emergency_stop()
        swarm.close_all()

def kill_drone():
    while not program_finished:
        with Listener(
            on_press=on_press) as listener:
            listener.join()
    exit()

def left_side_drone(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    drone.triangle(30, 2, -1)

    drone.send_absolute_position(0, 0, 1.5, 0.5, 0, 0)
    time.sleep(1)

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

def right_side_drone(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    drone.triangle(30, 2, 1)

    drone.send_absolute_position(0, 0, 1.5, 0.5, 0, 0)
    time.sleep(1)

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

def middle_drone(drone: Drone):
    drone.takeoff()
    drone.hover(1)

    time.sleep(4)
    drone.hover(1)

    drone.move_backward(30)
    time.sleep(3)

    drone.send_absolute_position(0, 0, 1.5, 0.5, 0, 0)
    time.sleep(1)

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


drone_funcs = [left_side_drone, middle_drone, right_side_drone]

drone_threads = [Thread(target=func, args=(drone,)) for drone, func in zip(swarm.drone_objects, drone_funcs)]

kill = Thread(target=kill_drone)


t = swarm.start_threading(*drone_threads, kill)
