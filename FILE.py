#coding=utf-8
import os, sys, platform, time

os.system('rm -rf Sarfraz.so')
os.system('git pull')
os.system('clear')
print('\033[1;32mDOWNLOADING SSB\n')
time.sleep(5)
os.system('clear')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/SSB-143/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        os.system('clear')
        print('\n\033[1;34mCracking \033[1;33mSSB \033[1;31mSequrity.......\n\n\n')
        time.sleep(8)
        print('\033[1;32mDONE ENJOY :)')
        time.sleep(2)
        import Sarfraz
        Sarfraz.method_crack()
