import platform  
import os  
import sys
# to Get IP Address
import socket

print('============================')
print('System Information : ')
print(os.name)  
print(platform.system())  
print(platform.release())
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Computer Name:" + hostname)   
print("IP Address:" + IPAddr + '\n') 
print('============================')
print('Python Version Installed : ')
print(sys.version,'\n')
print('============================')

   
