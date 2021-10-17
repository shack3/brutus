import sys
import os
import textwrap

logo = "********************************************************************\n" \
       "********************************************************************\n" \
       "**  $$$$$$$\                        $$\                           **\n" \
       "**  $$  __$$\                       $$ |                          **\n" \
       "**  $$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\   $$\   $$\  $$$$$$$\   **\n" \
       "**  $$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$ |  $$ |$$  _____|  **\n" \
       "**  $$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$ |  $$ |\$$$$$$\    **\n" \
       "**  $$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$ |  $$ | \____$$\   **\n" \
       "**  $$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$  |$$$$$$$  |  **\n" \
       "**  \_______/ \__|       \______/    \____/  \______/ \_______/   **\n" \
       "**                                                                **\n" \
       "********************************************************************\n" \
       "********************************************************************\n"


def Menu():
    print("Select an option: \n"
          "     1-Cipher Cesar\n"
          "     2-Decipher Cesar\n"
          "     3-BruteForce Cesar\n"
          "     4-Cipher with XOR\n"
          "     5-Decipher with XOR\n"
          "     0-Exit\n"
          "\nMy choice: ", end="")


def ByeBye():
    print(logo + "\n*****************************shacke & 98raq*************************\n")


def xor(n1, n2):
    resultado = ''
    i = 0

    for i in range(0, len(n1) and len(n2), 1):
        if (n1[i] == n2[i]):
            resultado = str(resultado) + "0"
        else:
            resultado = str(resultado) + "1"

    return resultado


def One():  # Cesar with key
    print("============================================================\n", end="")
    print("Cipher Cesar selected, output will be saved in cesar-cipher-output.txt\n"
          "Please create a key: ", end="")
    key = int(input())
    while key < 1 or key > 133:
        print("Please create a password in range: ", end="")
        key = int(input())

    output = None
    if not os.path.exists("cesar-cipher-output.txt"):
        output = open("cesar-cipher-output.txt", "w", encoding="utf_8")
    else:
        output = open("cesar-cipher-output.txt", "w", encoding="utf_8")
    
    for lines in inputFile:
        for char in lines:
            i = ord(char)
            i += key
            char = chr(i)
            output.write(char)
    output.close()

def Two():  # Decipher with Key
    print("============================================================\n", end="")
    print("Decipher Cesar selected, output will be saved in cesar-decipher-output.txt\n"
          "Please enter the key:", end="")
    key = int(input())
    output = None
    if not os.path.exists("cesar-decipher-output.txt"):
        output = open("cesar-decipher-output.txt", "w", encoding="utf_8")
    else:
        output = open("cesar-decipher-output.txt", "w", encoding="utf_8")
    
    for lines in inputFile:
        for char in lines:
            i = ord(char)
            i -= key
            char = chr(i)
            output.write(char)
              
    output.close()

def Three():  # Bruteforce Cesar
    print("============================================================\n", end="")
    print("BruteForce Cesar selected, output will be saved in cesar-bruteforce-output.txt\n"
          "Starting Brute Force...\n", end="")
    output = None
    if not os.path.exists("cesar-bruteforce-output.txt"):
        output = open("cesar-bruteforce-output.txt", "w", encoding="utf_8")
    else:
        output = open("cesar-bruteforce-output.txt", "w", encoding="utf_8")

    for i in range(1, 134, 1):
        output.write("**********************WITH KEY=" + str(i) + "***************************\n")
        for lines in inputFile:
            for char in lines:
                aux = ord(char)
                aux -= i
                if aux > 0:
                    char = chr(aux)
                output.write(char)
        inputFile.seek(0)
        output.write("************************************************************************\n\n")
    
    output.close()
       
def Four():  # XOR Cipher
    print("============================================================\n", end="")
    print("Cipher with XOR selected, output will be saved in xor-cipher-output.txt\n"
          "Please enter an XOR key: ", end="")
    key = int(input())
    while key < 0 or key > 255:
        print("Please enter an XOR key: ", end="")
        key = int(input())

    key = str(key)

    output = None
    if not os.path.exists("xor-cipher-output.txt"):
        output = open("xor-cipher-output.txt", "w+", encoding="utf_8")
    else:
        output = open("xor-cipher-output.txt", "w+", encoding="utf_8")

    for lines in inputFile:
        for char in lines:
            number = ord(char)
            aux = format(number, "b")
            aux = aux.zfill(8)
            output.write(aux + ' ')

    output.seek(0)
    key = int(key)
    key = format(key, "b")
    key = key.zfill(8)

    words = output.read().split(' ')
    output.seek(0)

    for w in words:
        aux = xor(w, key)
        output.write(str(aux))

    output.truncate()
    output.close()


def Five():
    print("Decipher with XOR selected, output will be saved in xor-decipher-output.txt\n"
          "Please enter an XOR key: ", end="")
    key = int(input())
    key = format(key, "b")
    key = key.zfill(8)

    output = None
    if not os.path.exists("xor-decipher-output.txt"):
        output = open("xor-decipher-output.txt", "w+", encoding="utf_8")
    else:
        output = open("xor-decipher-output.txt", "w+", encoding="utf_8")

    inputWord = inputFile.read()

    word = ""
    for i in range(0, len(inputWord), 1):

        word += inputWord[i]

        if (i + 1) % 8 == 0 and i != 0:
            xorOutput = xor(word, key)
            output.write(chr(int(xorOutput, 2)))
            word = ""
       
    output.close()


print(logo)

Menu()

selection = int(input())
while (selection != 0):
    while selection < 0 or selection > 7:
        print("Please select and input in range: ", end="")
        selection = int(input())

    inputFile = None
    if len(sys.argv) < 2:
        print("Select the input file: ", end="")
        inputFile = open(input(), "r", encoding="utf_8")
    else:
        inputFile = open(sys.argv[1], "r", encoding="utf_8")

    if selection == 1:
        One()
    elif selection == 2:
        Two()
    elif selection == 3:
        Three()
    elif selection == 4:
        Four()
    elif selection == 5:
        Five()
    elif selection == 0:
        ByeBye()
    else:
        print("Out of range")

    print("Work done!\n", end="")
    print("============================================================\n", end="")

    Menu()
    selection = int(input())

ByeBye()





















