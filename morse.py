from machine import Pin # type: ignore
from time import sleep

def showDot():
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    
def showLine():
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(0.5)
    
def convertToMorse(message, key):
    morse = []
    
    for letter in message:
        if letter in key:
            morse.append(key[letter])
    
    morse_convertion = " ".join(morse)
    print(f"Sending message: {morse_convertion} ({message})")
    
    return (morse_convertion)
    
def showMorseMessage(message):
    for code in message:
        if code == '.':
            showDot()
        elif code == '-':
            showLine()
        else:
            sleep(0.5)

key = {'A': '.-',
       'B': '-...',
       'C': '-.-.',
       'D': '-..',
       'E': '.',
       'F': '..-.',
       'G': '--.',
       'H': '....',
       'I': '..',
       'J': '.---',
       'K': '-.-',
       'L': '.-..',
       'M': '--',
       'N': '-.',
       'O': '---',
       'P': '.--.',
       'Q': '--.-',
       'R': '.-.',
       'S': '...',
       'T': '-',
       'U': '..-',
       'V': '...-',
       'W': '.--',
       'X': '-..-',
       'Y': '-.--',
       'Z': '--..',
       '0': '-----', '1': '.----', '2': '..---',
       '3': '...--', '4': '....-', '5': '.....',
       '6': '-....', '7': '--...', '8': '---..',
       '9': '----.'}

led = Pin(25, Pin.OUT)

while True:
    message = input("Insert a message: ").upper()
    
    morse_message = convertToMorse(message, key)
    
    showMorseMessage(morse_message)
    
    print("Message sent!")
    
    option = int(input("Do you want to send a new message? "))
    
    if not option:
        print("Shuting down...")
        break