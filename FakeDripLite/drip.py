import requests
from termcolor import colored
import time
import sys
import os
import psutil

def DripLite():
                     print(colored("""
                     
	     _     _        _ _ _       
	  __| |_ _(_)_ __  | (_) |_ ___ 
	 / _` | '_| | '_ \ | | |  _/ -_)
	 \__,_|_| |_| .__/ |_|_|\__\___|
	            |_|   FAKE!    v1.0                                           
	            
	         dll injector by: raz
	            Undetectable!
	                                   
""", 'red'))
DripLite()
print(colored("         Downloading DLL's and etc", 'blue'))
toolbar_width = 40
	# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

# hard part, get it to find the process named "Minecraft"
listOfProcessObjects = ["Minecraft", "Badlion Client", "Lunar Client"]
def findProcessIdByName(processName):
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
			if processName.lower() in pinfo['name'].lower():
				print("Found MC! PID: " + pid)
				listOfProcessObjects.append(pinfo)
		except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess):
			print("Uh oh! No processes found. Launch MC first.")
			pass


for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    
    sys.stdout.write(colored('-', 'red'))
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

os.system('clear')

DripLite()
print(colored("            Injecting...", 'blue'))
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.2) # do real work here
    # update the bar
    
    sys.stdout.write(colored('-', 'red'))
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
