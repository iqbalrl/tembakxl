﻿import os, sys, time, subprocess, socket, select, threading
from platform import python_version
pv = python_version()

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'


   

try:
    import platform
    from xlpy import *
except Exception as err:
    os.system('pip install --upgrade pip')
    os.system('pkg install php')
    os.system('pip install requests')
    os.system('pip install -r requirements.txt')
    os.system('python dor.py')()
except KeyboardInterrupt:
	  prints (m+"[" + p + "Fail To Import" + m + "]")
	  sys.exit()


       
def print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0 / 90)

def print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)
      
def main_menu():
       clear()
       prints(W + '            -== '+gt+'Zydekenzou'+W+' ==-')
       prints(W + '# ' + str(time.strftime('%a, %d %B %Y')))
       prints(W + '# Hanya Untuk Provider ' + C + str(os.popen('getprop gsm.operator.alpha').read().split('\n')[0]))
       prints(W + '# Python ' + C + str(pv) + W + ', ' + C + str(os.popen('getprop ro.product.device').read().split('\n')[0]) + ' ' + str(os.popen('getprop ro.build.version.release').read().split('\n')[0]) + ' Build SDK ' + str(os.popen('getprop ro.build.version.sdk').read().split('\n')[0]))
       prints(W + '#'*45)
       
       
       prints (gt+"Menu Pilihan:")
       prints (gt+"  ["+p+"1"+gt+"] "+p+"Menu Tembak")
       prints (gt+"  ["+p+"2"+gt+"] "+p+"Waktu")
       prints (gt+"  ["+p+"0"+gt+"] "+p+"Keluar")
      
    
    
       choice = str(input(C+" Masukan Pilihan👉 "))
       exec_menu(choice)
       return
       print(W + '# ' + str(time.strftime('%a, %d %B %Y')))

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
   print("loading")
   os.system('cd xlotp;python app.py')

def menu_2():
    slowprint("loading")
    os.system('sh jam.sh;python app.py')
    return os.system('python app.py')

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
