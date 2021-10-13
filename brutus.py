import sys
import os
import textwrap

logo = "============================================================\n" \
       "$$$$$$$\                        $$\                         \n" \
       "$$  __$$\                       $$ |                        \n" \
       "$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\   $$\   $$\  $$$$$$$\ \n" \
       "$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$ |  $$ |$$  _____|\n" \
       "$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$ |  $$ |\$$$$$$\  \n" \
       "$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$ |  $$ | \____$$\ \n" \
       "$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$  |$$$$$$$  |\n" \
       "\_______/ \__|       \______/    \____/  \______/ \_______/ \n" \
       "============================================================\n"







print(logo)
inputFile = None
if len(sys.argv)<2:
      print("Select the input file: ", end="")
      inputFile = open(input(), "r", encoding="utf_8")
else:
      inputFile = open(sys.argv[1], "r", encoding="utf_8")

print("With '" + inputFile.name + "', select an option: \n"
      "     1-Cipher Cesar\n"
      "     2-Decipher Cesar\n"
      "     3-BruteForce Cesar\n"
      "     4-Cipher with XOR\n"
      "     5-Decipher with XOR\n"
      "     6-Cipher with Brutus\n"
      "     7-Decipher with Brutus\n"
      "My choice: ", end="")

def ByeBye():
      print(logo+ "\n===================Work done, bye bye!======================")

def One(): #Cesar with key
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
                  i +=key
                  char = chr(i)
                  output.write(char)
      ByeBye()

def Two():
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
      ByeBye()

def Three():
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
                        char = chr(aux)
                        output.write(char)
            inputFile.seek(0)
            output.write("************************************************************************\n")
      ByeBye()


def Four():
      print("Cipher with XOR selected, output will be saved in xor-cipher-output.txt\n"
            "Please enter an XOR key: ", end="")
      key = input()

      output = None
      if not os.path.exists("xor-cipher-output.txt"):
            output = open("xor-cipher-output.txt", "w", encoding="utf_8")
      else:
            output = open("xor-cipher-output.txt", "w", encoding="utf_8")

      for lines in inputFile:
            for char in lines:
                  number = ord(char)
                  if number != 10:
                        aux = format(number, "b")
                        output.write(aux)
                  else:
                        output.write(char)

def Five():
      print("Five selected")

def Six():
      print("Six selected")

def Seven():
      print("Seven selected")









selection = int(input())
while selection < 1 or selection > 7:
      print("Please select and input in range: ", end="")
      selection = int(input())

if selection ==1:
      One()
elif selection == 2:
      Two()
elif selection == 3:
      Three()
elif selection == 4:
      Four()
elif selection == 5:
      Five()
elif selection == 6:
      Six()
elif selection == 7:
      Seven()
else:
      print("Out of range")





















