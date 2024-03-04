from pynput import keyboard
import time

LOG_FILE = "key_log.txt"

key_press_times = {}
previous_event_time = None
recording = False

def on_press(key):
    global recording, previous_event_time
    current_time = time.time()

    if key == keyboard.Key.f12:
        if not recording:
            # Start recording
            recording = True
            previous_event_time = current_time  # Set the start time for latency calculation
            with open(LOG_FILE, "a") as f:
                f.write(f"Recording started at {time.ctime()}\n")
            print("Recording started.")
        else:
            # Stop recording
            recording = False
            with open(LOG_FILE, "a") as f:
                f.write("Recording stopped\n")
            print("Recording stopped.")
            return False  # Stop listener
        return

    if recording:
        key_press_times[key] = current_time
        latency = (current_time - previous_event_time) * 1000 if previous_event_time else 0
        key_name = str(key).replace("'", "").replace("Key.", "")
        with open(LOG_FILE, "a") as f:
            f.write(f"latency {latency:.2f} ms\n")
            f.write(f"{key_name} down\n")
        previous_event_time = current_time

def on_release(key):
    global previous_event_time
    current_time = time.time()

    if recording and key in key_press_times:
        down_time = key_press_times[key]
        up_time = current_time
        duration = (up_time - down_time) * 1000  # Convert to milliseconds
        latency = (current_time - previous_event_time) * 1000  # Latency to the next event
        key_name = str(key).replace("'", "").replace("Key.", "")

        # Write key down and up times, duration, and latency to log   
        with open(LOG_FILE, "a") as f: 
            f.write(f"latency {latency:.2f} ms\n")
            f.write(f"{key_name} up\n")
        
        previous_event_time = current_time
        # Remove the key from the dictionary once released
        del key_press_times[key]

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
