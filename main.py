import string
import time
import subprocess
import os
from pathlib import Path

## Prepare tools

# . . .
def dotdotdot():
    time.sleep(1)
    for i in range(0, 3):
        print(".")
        time.sleep(1)

# Big ugly alphanumeric qabbala cipher function
def cipher(in_str):
    cipher_ls = []
    intent_ints = []
    intent_str = []
    in_str.lower()
    # Separate numbers and letters into their own lists
    for i in range(len(in_str)):
        if (in_str[i].isdigit()):
            intent_ints.append(in_str[i])
        elif (in_str[i].isalpha()):
            intent_str.append(in_str[i])
    # Convert letters to numeric value in AQ
    # Ignore special characters in cipher
    for i in intent_str:
        if i.isalpha:
            cipher_val = ord(i) - (ord("a")) + 10
            cipher_ls.append(cipher_val)
        else:
            return
    # Add together integers and append to cipher list
    cipher_ls.append(sum((list(map(int, intent_ints)))))
    # Add everything together for the final total value
    global cipher_sum
    cipher_sum = sum(cipher_ls)
    print(intent + " = " + str(cipher_sum))

# Use the cipher value to forge entropy into a sigil
def sigilize():
    txt_sigil = open("./sigils/" + str(cipher_sum) + ".txt", "w")
    cmd = ['head', '-c', str(cipher_sum), '/dev/urandom']
    sigil = subprocess.call(cmd, stdout=txt_sigil)
    txt_sigil_print = subprocess.Popen(['cat', 'sigils/' + str(cipher_sum) + '.txt'], stdout=subprocess.PIPE).communicate()[0]
    print(str(cipher_sum) + " = " + str(txt_sigil_print))

def charge():
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['stress-ng', '-c', '1', '-t', '1s'], stdout=devnull, stderr=subprocess.STDOUT)

def launch():
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['rm', sigil_path], stdout=devnull, stderr=subprocess.STDOUT)

def altar():
    global intent
    a = True
    while a == True:
        clear_the_screen = subprocess.call('clear', shell=True)
        print(Path('333.txt').read_text())
        intent = input("State your intent: ")
        time.sleep(1)
        print("Ciphering")
        dotdotdot()
        cipher(intent)
        time.sleep(1)
        print('')
        print("Sigilizing")
        dotdotdot()
        sigilize()
        global sigil_path
        sigil_path = str("sigils/" + str(cipher_sum) + ".txt")
        print('')
        print("Charging")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        charge()
        print("Launching")
        dotdotdot()
        launch()
        print("Success!")
        time.sleep(1)
        clear = input("Press Enter to restart")


## Start the ritual
altar()
