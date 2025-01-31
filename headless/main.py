import pyautogui
import time
import random

# Set the duration of the loop (in seconds)
duration = int(input("How long would you like to set the duration to be?(in seconds) :"))  

# Set the delay between mouse moves (in seconds)
delay = int(input("How much delay do you want:")) 
# Get the start time
start_time = time.time()

# Run the loop for the specified duration
while time.time() - start_time < duration:
    # Move the mouse to a random position on the screen
    pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080))
    
    # Wait for the specified delay
    time.sleep(delay)

print("Time is up!")