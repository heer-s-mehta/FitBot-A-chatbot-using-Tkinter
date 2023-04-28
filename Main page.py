import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
photo = PhotoImage(file=r"C:\Users\heerm\OneDrive\Desktop\PYTHON\MINI PROJECT\workout.png")
frame = tk.Frame(master = root)
frame.pack(expand=True,fill="both")

#to open new page
import subprocess
def run_program():
    subprocess.call(["python",r"C:\Users\heerm\OneDrive\Desktop\PYTHON\MINI PROJECT\workoutbot.py"])
    
#photo as a button 

button = tk.Button(frame, command=run_program,image=photo)
button.image=photo
button.pack(expand=True,fill="both")

root.mainloop()



