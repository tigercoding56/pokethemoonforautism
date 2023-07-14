import subprocess
import time

def minimize_window(window_title):
    # Get the window ID using xdotool
    cmd = f"xdotool search --name '{window_title}'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    window_id = result.stdout.strip()

    if window_id:
        # Minimize the window using xdotool
        #cmd = f"xdotool windowminimize {window_id}"
        #subprocess.run(cmd, shell=True)
        
        # Wait for the window to minimize
        #time.sleep(1)
        
        # Send the "Enter" key input to the window using xdotool
        cmd = f"xdotool key --window {window_id} Return"
        subprocess.run(cmd, shell=True)
        cmd = f"xdotool key --window {window_id} W"
        subprocess.run(cmd, shell=True)
        cmd = f"xdotool key --window {window_id} F"
        subprocess.run(cmd, shell=True)
        
    else:
        print(f"Window '{window_title}' not found")

# Wait for user to focus on the desired window
time.sleep(1)

# Call the function to minimize the window and send the "Enter" key input
while True:
    time.sleep(0.1)
    minimize_window("Learn to Fly 3")
cmd = f"xdotool keyup --window {window_id} F"
subprocess.run(cmd, shell=True)
cmd = f"xdotool keyup --window {window_id} W"
subprocess.run(cmd, shell=True)
cmd = f"xdotool keyup --window {window_id} Return"
subprocess.run(cmd, shell=True)