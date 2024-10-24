import serial
import pyautogui
import time

# Replace 'COM3' with your Arduino's COM port
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # Give some time to establish the connection

while True:
    line = ser.readline().decode('utf-8').strip()

    if line == "play":
        # Simulate pressing the Play/Pause key
        pyautogui.press('playpause')
    elif line == "next":
        # Simulate pressing the Next Track key
        pyautogui.press('nexttrack')
    elif line == "back":
        # Simulate pressing the Previous Track key
        pyautogui.press('prevtrack')

ser.close()