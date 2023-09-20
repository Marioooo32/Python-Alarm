import tkinter as tk
import time
import winsound

def set_alarm(hours, minutes):
    current_time = time.localtime()
    alarm_time = time.strptime(f"{current_time.tm_year} {current_time.tm_mon} {current_time.tm_mday} {hours} {minutes}", "%Y %m %d %H %M")
    alarm_timestamp = time.mktime(alarm_time)
    current_timestamp = time.mktime(current_time)
    time.sleep(alarm_timestamp - current_timestamp)
    frequency = 2500  # Feel the piercing sound of doom
    duration = 2000  # Endure the torment for 2 seconds
    winsound.Beep(frequency, duration)
    print("Wake up, pathetic human!")

def set_alarm_gui():
    root = tk.Tk()
    root.title("Mario's Alarm")
    
    width = 300
    height = 200
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    
    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
    
    hour_label = tk.Label(root, text="Enter hour (0-23):")
    hour_label.pack()
    hour_entry = tk.Entry(root)
    hour_entry.pack()
    
    minute_label = tk.Label(root, text="Enter minute (0-59):")
    minute_label.pack()
    minute_entry = tk.Entry(root)
    minute_entry.pack()
    
    def set_alarm_handler():
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        set_alarm(hour, minute)
    
    set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm_handler)
    set_alarm_button.pack()
    
    root.mainloop()

set_alarm_gui()