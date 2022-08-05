import psutil
import time

foundVRC = False

while foundVRC == False:
    for process in psutil.process_iter():
        if process.name() == "VRChat.exe":
            foundVRC = True

for process in psutil.process_iter():
    try:
        if process.name() == "EasyAntiCheat_EOS.exe":
            time.sleep(5)
            process.kill()
            print("Terminated EAC process with PID " + str(process.pid))
    except (psutil.AccessDenied):
        print("Access denied")
    except (psutil.NoSuchProcess):
        print("EAC is not running")