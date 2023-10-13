import tkinter as tk
from tkinter import ttk  # ttk provides access to the Tk themed widget set
from tools.autocubing import main as autocubing_main
import threading

def autocubing_toggle():
    if "Start" in autocubing_button.cget("text"):
        start_autocubing()
        autocubing_button.configure(text="Stop", command=stop_autocubing)
    else: 
        stop_autocubing()
        
def start_autocubing():
    global autocubing_thread
    global stop_event
    selected_potential = potential_var.get()
    input_lines = radio_var.get()
    check_box_select = check_True_var.get()

    stop_event = threading.Event()
    stop_event.clear()
    autocubing_thread = threading.Thread(target=autocubing_main, args=(selected_potential, input_lines,check_box_select,stop_event))
    autocubing_thread.start()

def stop_autocubing():
    global stop_event
    if stop_event:
        stop_event.set()
    autocubing_thread.join()  
    autocubing_button.configure(text="Start", command=autocubing_toggle)

# press F12 to start auto cubing
def on_press_f12(event):
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



# select drop down
potential_var = tk.StringVar(value="Select potential")
potential_options = ["select potential","力量", "敏捷", "智力", "幸運", "ATT", "MATT", "掉率", "金幣獲取"]
option_menu = ttk.OptionMenu(main_frame, potential_var, *potential_options)
option_menu.grid(row=1, column=0, padx=(10,100))

def update_checkbox_state(*args):
    if potential_var.get() in ["力量", "敏捷", "智力", "幸運"]:
        Check_True3["state"] = tk.NORMAL
    else:
        Check_True3["state"] = tk.DISABLED
potential_var.trace_add("write", update_checkbox_state)

# radio button group
radio_var = tk.IntVar()
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



# submit button
autocubing_button = ttk.Button(main_frame, text="Start", command=autocubing_toggle)
autocubing_button.grid(row=4, column=0, pady=10, columnspan=3,padx=(100,0))

update_checkbox_state()

root.bind("<F12>", on_press_f12)
root.mainloop()