import pyautogui
import time

# Get the path to the .exe file
exe_file_path = "./kkkkklik.exe"

# Run the .exe file
pyautogui.run_program(exe_file_path)

# Wait for the program to start up
time.sleep(5)

# Get the size of the program window
window_size = pyautogui.size()

# Loop through each pixel in the program window
for x in range(0, window_size[0]):
    for y in range(0, window_size[1]):
        # Click on the current pixel
        pyautogui.click(x, y)

# Wait for the program to close
time.sleep(5)
