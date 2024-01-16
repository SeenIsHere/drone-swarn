import time

def logflight():
    year, month, day, hour, min, *_ = time.localtime()
    file1 = open("flight_logs.txt", "a")

    notes = input("Notes: ")

    L = [f"Flight Log: {month}/{day}/{year} {hour}:{min} ||| {notes}\n"]
    file1.writelines(L)
    file1.close()

"""
def detect_wall_and_debug(d, a):
    x = drone.detect_wall(a)
    print("Drone Detected Wall? " + str(x))
    return x

def wall_and_back():
    speed = 3
    blocks = 50
    sleeps = [0.5, 1, 1.5]

    iterations = 0

    drone.takeoff()

    while not drone.get_front_range("cm"): continue

    while not detect_wall_and_debug(drone, blocks * 2):
        drone.move_forward(blocks, "cm", speed)
        iterations += 1
        time.sleep(sleeps[speed - 1] / 2)

    drone.turn_degree(180)
    time.sleep(1)
    
    speed = 2

    drone.move_forward(blocks * (iterations - 1), "cm", speed)
    time.sleep(iterations * sleeps[speed - 1])

    drone.land()

def figure8():
    drone.takeoff()

    drone.circle()

    drone.land()



wall_and_back()

drone.close()

logflight()
    
"""