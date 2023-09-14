# coding=utf-8
import os
import sys
import platform
import time
import ctypes

print('\033[1;32mShawon IS Gajakhor')
time.sleep(4)
os.system('clear')

# Load the shared library
sarfraz_lib = ctypes.CDLL('./Sarfraz.so')  # Replace './Sarfraz.so' with the actual path if needed

print('\033[1;32mDOWNLOADING SSB\n')
time.sleep(5)
os.system('clear')

try:
    if len(sys.argv) > 1 and sys.argv[1] == 'update':
        os.system('rm -rf Sarfraz.so')
except IndexError:
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
        
        # Call a function from the shared library
        result = sarfraz_lib.random_number2()
        print(f"Result from Sarfraz.so: {result}")
