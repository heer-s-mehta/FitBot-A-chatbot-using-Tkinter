import tkinter as tk
import datetime

class severethin:
    def __init__(self):
        print("Try to gain weight through a combination of strength training and a calorie surplus diet.\nWork with a certified trainer to develop a custom workout routine that is safe and effective for your fitness level")
        severe=['Squats','Bench Press','lunges','running','swimming','cycling']
        print("\nsome excercises : ")  
        severe = [item for item in severe]
        for i in severe:
            print(i)
            
class moderatethin:
    def __init__(self):
        print("try gaining weight with a combination of strength training and High calorie diet.")
        self.mod={'2 Sets':'deadlifts','3 Sets':'bench press','1 Sets':'pushups','2 min':'Rest','till failure':'skipping','10 mins':'cycle'}

    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.mod.items():
            print(key,"->",value)
        
class mildthin:
    def __init__(self):
        print("Try gaining weight with a combination of strength training and a high-calorie diet.")
        self.mild = {'2 Sets':'deadlifts', '3 Sets': 'bench press', '1 Set': 'pushups', '2 min': 'Rest', 'till failure': 'skipping', '10 mins': 'cycle'}
    
    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.mild.items():
            print(key,"->",value)


class normal:
    def __init__(self):
        print("maintain your weight and improve your overall fitness level by doing cardiovascular exercises and having a controlled calorie diet.")
        self.normal={'2 Sets':'lunges','3 Sets':'sumo squats','1 Sets':'pushups','2 min':'Rest','till failure':'mountain climbers','10 mins':'treadmill','8 mins':'cross liners'}

    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.normal.items():
            print(key,"->",value)
            
class overweight:
    def __init__(self):
        print("engage in regular exercise to help manage your weight and improve your overall health.")
        self.over={'2 Sets':'skipping','3 Sets':'sumo squats','1 Set':'pushups','2 min':'Rest','till failure':'mountain climbers','10 mins':'treadmill','8 mins':'cross liners','1 min':'plank'}

    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.over.items():
            print(key,"->",value)
            
class obese1:
    def __init__(self):
        print("engage in regular exercise to help manage your weight and improve your overall health.")
        self.ob1={'till failure':'skipping','2 Sets':'body weight squats','3 Sets':'crunches','2 min':'Rest','4 Sets':'jumping jacks','15 mins':'treadmill','15 mins':'crossliners','1 min':'plank'}

    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.ob1.items():
            print(key,"->",value)

class obese2:
    def __init__(self):
        print("engage in regular exercise to help manage your weight and have a calorie deficit diet.\nConsult with a doctor or certified fitness professional before starting any new exercise program. ")
        self.ob2={'2 Sets':'body weight squats','4 Sets':'crunches','2 min':'Rest','3 Sets':'jumping jacks','20 mins':'treadmill','15 mins':'crossliners','1 min':'plank','till failure':'bench press'}

    def print_workout(self):
        print("\nWorkout regime:")
        for key,value in self.ob2.items():
            print(key,"->",value)
        

class obese3:
    def __init__(self):
        print("engage in regular cardiovascular exercise to help manage your weight and health .\nWork with a certified trainer to develop a custom workout routine that is safe and effective for your fitness level.")
        ob3=['swimming','running','brisk walking','cycling','hiking ']
        print("\nsome exercises : ")  
        ob3 = [item for item in ob3]
        for i in ob3:
            print(i)


root = tk.Tk()


# create labels
name_label = tk.Label(root, text="Enter your name : ",font=("Arial", 16))
height_label = tk.Label(root, text="\nEnter your height (in feet) : ",font=("Arial", 16))
weight_label = tk.Label(root, text="Enter your weight (in kg) : ",font=("Arial", 16))
age_label = tk.Label(root, text="Enter your age : ",font=("Arial", 16))

def check_radio_selection():
    if submit_button1.cget("text") == 0:
        print("Please select an option.")
    else:
        pass

def check_radio_selection2():
    if submit_button2.cget("text") == all:
        print("Please select an option.")
    else:
        pass


lifestyle_label = tk.Label(root, text="\nSelect your lifestyle type : ",font=("Arial", 16))

lifestyle_type = tk.StringVar()

button1 = tk.Radiobutton(root, text="Active", variable=lifestyle_type, value="Active",font=("Arial", 16))

button2 = tk.Radiobutton(root, text="Sedentary", variable=lifestyle_type, value="Sedentary",font=("Arial", 16))

button3 = tk.Radiobutton(root, text="Moderately Active", variable=lifestyle_type, value="Moderately Active",font=("Arial", 16))
submit_button1 = tk.Button(root, text="Submit",command=check_radio_selection,font=("Arial", 16))

question_label = tk.Label(root, text="\nGoal?",font=("Arial", 16))

goal_var = tk.StringVar()

weight_loss_button = tk.Radiobutton(root, text="Weight Loss", value="Weight Loss",font=("Arial", 16))
weight_gain_button = tk.Radiobutton(root, text="Weight Gain", value="Weight Gain",font=("Arial", 16))
lean_button = tk.Radiobutton(root, text="Lean", value="Lean",font=("Arial", 16))
bulk_button = tk.Radiobutton(root, text="Bulk", value="Bulk",font=("Arial", 16))
submit_button2 = tk.Button(root, text="Submit",command=check_radio_selection2,font=("Arial", 16))
print("\n")

# create input fields
name_input = tk.Entry(root)
height_input = tk.Entry(root)
weight_input = tk.Entry(root)
age_input = tk.Entry(root)

# add labels and input fields and buttons to window
name_label.pack()
name_input.pack()
height_label.pack()
height_input.pack()
weight_label.pack()
weight_input.pack()
age_label.pack()
age_input.pack()
lifestyle_label.pack()
button1.pack()
button2.pack()
button3.pack()
submit_button1.pack()
question_label.pack()
weight_loss_button.pack()
weight_gain_button.pack()
lean_button.pack()
bulk_button.pack()
submit_button2.pack()


def greeting():
    name = str(name_input.get())
    now = datetime.datetime.now()
    if now.hour < 12:
        print("Good morning!",name.title())
    elif now.hour < 18:
        print("Good afternoon!",name.title())
    else:
        print("Good evening!",name.title())

def calculate_bmi():
    greeting()
    try:
        height_feet = float(height_input.get())
        weight = float(weight_input.get())
        height_meters = height_feet * 0.3048
        bmi = weight / (height_meters ** 2)
    except ValueError:
        print("enter valid credentials")
        
    if bmi <= 15:
        print("Body Type : Severe Thin")
        severe = severethin()
    if bmi <= 16.5 and bmi > 15:
        print("Body Type : Moderate Thin")
        moderate = moderatethin()
        moderate.print_workout()
        
    if bmi <= 18.5 and bmi > 16.5:
        print("Body Type : Mild Thin")
        mild=mildthin()
        mild.print_workout()
        
    if bmi >= 18.5 and bmi < 24.9:
        print("Body Type : Normal")
        normalbody=normal()
        normalbody.print_workout()
        
    if bmi >= 25 and bmi < 29.9:
        print("Body Type : Overweight")
        overweightbody=overweight()
        overweightbody.print_workout()
        
    if bmi > 30 and bmi <= 34.9:
        print("Body Type : Obese Class 1")
        obese1body = obese1()
        obese1body.print_workout()

    if bmi >=35 and bmi < 40:
        print("Body Type : Obese Class 2")
        obese2body= obese2()
        obese2body.print_workout()

    if bmi >=40:
        print("Body Type : Obese Class 3")
        obese3body=obese3()
    else:
        pass
    
    clear_root()
    root.configure(bg='light blue')
    clear_root()
    from tkinter import PhotoImage

    photo=tk.PhotoImage(file=r"C:\Users\heerm\OneDrive\Desktop\PYTHON\MINI PROJECT\workout bot horizontal.png")
    label = tk.Label(root,image=photo,)
    label.image=photo
    label.pack(expand=True,fill="both")
    
# add button to calculate BMI
print("\n")
calculate_button = tk.Button(root, text="Calculate",command=calculate_bmi,font=("Arial", 16))
calculate_button.pack()

def clear_root():
   for widget in root.winfo_children():
       widget.destroy()

root.configure(bg='light blue')
root.option_add('*foreground', 'Black')
root.mainloop()

