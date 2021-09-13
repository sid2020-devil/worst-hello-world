from random import randrange as rand
from time import sleep


# A very beautiful function which will keep printing a string with a random character, until the expected character is drawn
def printHelloWorld(current_str, expectedChar):
    while True:
        tempChar = rand(0, 127)
        print("\r" + current_str + chr(tempChar), end="")
        sleep(0.1)  # Comment this line to see the result instantly
        if chr(tempChar) == expectedChar:
            break


output_str = "Hello World"
present_str = ""

# Try to get the matching character for every character in the string. Good Luck!
for char in output_str:
    printHelloWorld(present_str, char)
    present_str += char