from codrone_edu.swarm import *
from codrone_edu.drone import *

swarm = Swarm()
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