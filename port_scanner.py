#Port Scanner Using Python
#Find more details in the README file
#By Eder Morales

#import the needed modules and/or libraries for the program to run

from queue import Queue
import socket
import threading
import sys
from datetime import datetime

#request input from the user asking for a target
print("")
print("---------------------------------------------")
print("Welcome to the portscanner!\n")
target = input(" Enter a remote host to scan \n(An ip address, or a website following the pattern eg.-> www.website.net): ")


print ("-->Select an option from the following: ")
print (" 1","Select this mode to scan Ports 1 To 1024")
print (" 2","Select This to Scan ports 1 to 49152")
print (" 3","Select thist to scan port 20,21,22,23,25,53,80,110,443")
print (" 4","Select this for Custom port scan")
option = input("")

print (" - Wait a moment while we scan the host to find open ports ")
print ("")


#this part it queues the ports and creates a list of open ports
queue = Queue()
open_ports = []

#sets up the first time of the program
time1 =datetime.now()

#method to know if a port is open or closed
#creates the socket
#connects to the target 
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(option):
    if option == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif option == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif option == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 123, 161, 179, 443, 500, 587, 3389]
        for port in ports:
            queue.put(port)
    elif option == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

#function who adds the open ports to the open_ports variable to print them later

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

#collects the data and prints the list of open ports 
def run_scanner(threads, option):

    get_ports(option)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

#calls the run_scanner function and adds the number of parameters you decided
run_scanner(5000, 1)

#sets up the second time of the program after it finished scanning 
time2 =datetime.now()

#calculates the time it took to complete the task
#and prints it
timetotal= time2-time1

print ("Sanning Completed in : ", timetotal)

print ('This is the stage No. 2 (Scanning) of hacking  ')

print ('Have fun hacking!')