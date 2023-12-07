import tkinter as tk
from tkinter import ttk  
from tools.autocubing import main as autocubing_main
import threading
from pynput import keyboard


def autocubing_toggle():
    if "Start" in autocubing_button.cget("text"):
        start_autocubing()
        autocubing_button.configure(text="Stop", command=stop_autocubing)
    else: 
        stop_autocubing()
        
def start_autocubing():
    global autocubing_thread
    global stop_event
    selected_cube = cube_var.get()
    selected_potential = potential_var.get()
    input_lines = radio_var.get()
    True3_box_select = check_True_var.get()
    Above160_box_select = check_Above160_var.get()

    stop_event = threading.Event()
    stop_event.clear()
    autocubing_thread = threading.Thread(target=autocubing_main, args=(selected_cube,selected_potential, input_lines, True3_box_select, Above160_box_select, stop_event))
    autocubing_thread.start()

def stop_autocubing():
    global stop_event
    if stop_event:
        stop_event.set()
    autocubing_thread.join()  
    autocubing_button.configure(text="Start", command=autocubing_toggle)

# press F12 to start auto cubing
def on_press(key):
    if key == keyboard.Key.f12:
        autocubing_toggle()

root = tk.Tk()
root.title("MapleTools")
root.geometry("400x200")

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# label
label = ttk.Label(main_frame, text="Auto Cubing")
label.grid(row=0, column=0, pady=10, columnspan=3,padx=(100,0))



#select cube drop down
cube_var = tk.StringVar(value="Select cube")
cube_options = ["select Cube ","Black","Red"]
cube_menu = ttk.OptionMenu(main_frame, cube_var, *cube_options)
cube_menu.grid(row=1, column=0, padx=(10,100))


# select potential drop down
potential_var = tk.StringVar(value="Select potential")
potential_options = ["select potential","STR", "DEX", "INT", "LUK", "ATT", "Magic ATT", "Item Drop Rate", "Mesos Obtained"]
option_menu = ttk.OptionMenu(main_frame, potential_var, *potential_options)
option_menu.grid(row=2, column=0, padx=(10,100))

def update_checkbox_state(*args):
    if potential_var.get() in ["STR", "DEX", "INT", "LUK","ATT", "Magic ATT"] and radio_var.get() == 3:
        Check_True3["state"] = tk.NORMAL
        Check_Above160["state"] = tk.NORMAL
    else:
        Check_True3["state"] = tk.DISABLED
        Check_Above160["state"] = tk.DISABLED
potential_var.trace_add("write", update_checkbox_state)

# radio button group
radio_var = tk.IntVar()
radio_var.trace_add("write", update_checkbox_state)

R1 = ttk.Radiobutton(main_frame, text=1, variable=radio_var, value=1)
R1.grid(row=1,column=1, padx=5)
R2 = ttk.Radiobutton(main_frame, text=2, variable=radio_var, value=2)
R2.grid(row=2,column=1, padx=5)
R3 = ttk.Radiobutton(main_frame, text=3, variable=radio_var, value=3)
R3.grid(row=3,column=1, padx=5)

# check box
check_True_var = tk.BooleanVar()
Check_True3 = ttk.Checkbutton(main_frame, text='True 3 ',variable= check_True_var, onvalue=True, offvalue=False)
Check_True3.grid(row=1,column=2, padx=(20,5))

check_Above160_var = tk.BooleanVar()
Check_Above160 = ttk.Checkbutton(main_frame, text='Above 160 ',variable= check_Above160_var, onvalue=True, offvalue=False)
Check_Above160.grid(row=2,column=2, padx=(10,5))

# submit button
autocubing_button = ttk.Button(main_frame, text="Start", command=autocubing_toggle)
autocubing_button.grid(row=4, column=0, pady=10, columnspan=3,padx=(100,0))

update_checkbox_state()

listener = keyboard.Listener(on_press=on_press)
listener.start()
root.mainloop()