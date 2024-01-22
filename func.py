import time
from codrone_edu.swarm import Swarm

EvilSwarm: Swarm = Swarm

def logflight():
    year, month, day, hour, min, *_ = time.localtime()
    file1 = open("flight_logs.txt", "a")
    L = [f"{month}/{day}/{year},{hour}:{min},Computer Science Room,BTSJ,Jamie,None"]
    file1.writelines(L)
    file1.close()