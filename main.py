#!/usr/bin/env python3
from src.rover import Explorer
from src.color import ColorSensor

from distutils.cmd import Command
import tkinter
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from time import sleep

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Splash(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Set window
        #self.title("Explorer Rover - Mission Control")
        self.geometry('500x300+400+200')
        self.overrideredirect(True)

        logo1 = Image.open(PATH + "/images/logoKSCIA.png").resize((100,100))
        self.logo_image = ImageTk.PhotoImage(logo1)

        self.logo_label = customtkinter.CTkLabel(master=self, image=self.logo_image)
        self.logo_label.pack(pady=(30, 10))

        self.txt = customtkinter.CTkLabel(self, text="EXPLORER ROVER - MISSION CONTROL",
                                            text_font=("Roboto Bold", -22))
        self.txt.pack(pady=20)

        self.count = 0
        
        self.progress = customtkinter.CTkProgressBar(self, width=400, height=5)
        self.progress.set(self.count)
        self.progress.pack(pady=(20, 30))

        self.subtitle = customtkinter.CTkLabel(self, text="KSCIA - International Space Academy",
                                                    text_font=("Roboto regular", -12))
        self.subtitle.pack(pady=0)

        #self.txt.after(2000, self.destroy())

        



    def start(self):
        self.count = self.count + 0.01
        self.progress.set(self.count)
        if self.count <= 1:
            self.progress.after(50, self.start)
        else:
            self.progress.after(100, self.destroy())


class App(customtkinter.CTk):

    # Control Variables 
    WIDTH = 1200
    HEIGHT = 640

    mission_progress = 0
    

    def __init__(self, robot, color):
        super().__init__()
        
        self.robot = robot
        self.color = color


        # Define control variables
        self.status = True
        self.cont = tkinter.IntVar()
        self.cont.set(0)
        self.content = tkinter.StringVar()
        self.forward_value = tkinter.DoubleVar()
        self.forward_value.set(0.0)
        self.backward_value = tkinter.DoubleVar()
        self.left_value = tkinter.DoubleVar()
        self.right_value = tkinter.DoubleVar()

        self.powerForward = 0.5
        self.powerTurn = 1

        self.pd_min = 0
        self.pd_max = 20

        # Set window
        self.title("Explorer Rover - Mission Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing())  # call .on_closing() when app gets closed

        #============ Set Frames =============
        self.grid_columnconfigure(0, minsize=360)
        self.grid_columnconfigure(1, minsize=380)
        self.grid_columnconfigure(2, weight=1, minsize=380)
        

        #self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, minsize=100)
        self.grid_rowconfigure(2, weight=2)
       
        self.grid_rowconfigure(0, minsize=70)

        self.frame_header = customtkinter.CTkFrame(master=self, fg_color=None)
        self.frame_header.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 0), sticky="nswe")

        self.frame_objetives = customtkinter.CTkFrame(master=self)
        self.frame_objetives.grid(row=1, column=0, rowspan=2, padx=(20, 8), pady=(0, 20), sticky="nswe")

        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.grid(row=2, column=1, columnspan=2, padx=(8, 20), pady=(8, 20), sticky="nswe")

        self.frame_sensor = customtkinter.CTkFrame(master=self)
        self.frame_sensor.grid(row=1, column=1, padx=8, pady=(0, 8), sticky="nswe")

        self.frame_send = customtkinter.CTkFrame(master=self)
        self.frame_send.grid(row=1, column=2, padx=(8, 20), pady=(0, 8), sticky="nswe")

        #self.frame_hist = customtkinter.CTkFrame(master=self)
        #self.frame_hist.grid(row=1, column=3, columnspan=2, sticky="nswe")


        #============ Set Header =============
        self.obj_title = customtkinter.CTkLabel(self.frame_header, 
                                                text="EXPLORER ROVER MISSION CONTROL",
                                                text_font=("Roboto Bold", -18)
                                                )
        self.obj_title.grid(row=0, column=0, sticky="ws", pady=0)

        self.obj_subtitle = customtkinter.CTkLabel(self.frame_header, 
                                                text="KSCIA - International Space Academy",
                                                text_font=("Roboto regular", -12),
                                                justify=tkinter.LEFT
                                                )
        self.obj_subtitle.grid(row=1, column=0, pady=0, sticky="wn")


        logo = Image.open(PATH + "/images/logoKSCIA.png").resize((40,40))
        self.logo_image = ImageTk.PhotoImage(logo)

        self.logo_label = customtkinter.CTkLabel(master=self.frame_header, image=self.logo_image)
        self.logo_label.place(x=1060, y=5)

        #============== Frame Objetives ================
        #self.frame_objetives.grid_rowconfigure(1, minsize=0) # spacing row
        #self.frame_objetives.grid_rowconfigure(4, minsize=20) # spacing row
        self.frame_objetives.grid_rowconfigure(12, minsize=20) # spacing row

        self.obj_title = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="MISSION OBJETIVES",
                                                text_font=("Roboto Bold", -16))
        self.obj_title.grid(row=0, column=0, padx=16, pady=16, sticky="sw")

        # Progressbar
        self.progressbar_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Progress: ",
                                                text_font=("Roboto Bold", -16))
        self.progressbar_txt.grid(row=2, column=0, padx=16, pady=0, sticky="snw")

        self.progressbar_value = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="00%",
                                                text_font=("Roboto medium", -16),
                                                width=80,
                                                anchor="e")
        self.progressbar_value.grid(row=2, column=1, columnspan=3, padx=16, sticky="sne")

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_objetives, height=10)
        self.progressbar.grid(row=3, column=0, columnspan=4, sticky="snwe", padx=16, pady=10)
        self.progressbar.set(0)

        # Mission Objetives
        self.obj_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Objetives:",
                                                text_font=("Roboto Bold", -16))
        self.obj_txt.grid(row=5, column=0, padx=16, pady=(16, 10), sticky="snw")

        # Item 1
        self.item1_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="1. Free access to Habitat",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item1_txt.grid(row=7, column=0, padx=16, pady=8, sticky="snw")

        self.item1_check = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item1_check, 0.2))
        self.item1_check.grid(row=7, column=1, padx=0, sticky="sne")

        # Item 2
        self.item2_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="2. Find and Collect Water",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item2_txt.grid(row=8, column=0, padx=16, pady=8, sticky="snw")

        self.item2_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check1, 0.05))
        self.item2_check1.grid(row=8, column=1, padx=0, sticky="sne")
        self.item2_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check2, 0.05))
        self.item2_check2.grid(row=8, column=2, padx=0, pady=8, sticky="sne")
        self.item2_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check3, 0.05))
        self.item2_check3.grid(row=8, column=3, padx=0, pady=8, sticky="sne")

        # Item 3
        self.item3_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="3. Collect Food",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item3_txt.grid(row=9, column=0, padx=16, pady=8, sticky="snw")

        self.item3_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check1, 0.05))
        self.item3_check1.grid(row=9, column=1,  sticky="sne")
        self.item3_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check2, 0.05))
        self.item3_check2.grid(row=9, column=2, pady=8, sticky="sne")
        self.item3_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check3, 0.05))
        self.item3_check3.grid(row=9, column=3, pady=8, sticky="sne")


        # Item 4
        self.item4_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="4. Collect soil samples",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item4_txt.grid(row=10, column=0, padx=16, pady=8, sticky="snw")

        self.item4_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check1, 0.05))
        self.item4_check1.grid(row=10, column=1,  sticky="sne")
        self.item4_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check2, 0.05))
        self.item4_check2.grid(row=10, column=2, pady=8, sticky="sne")
        self.item4_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check3, 0.05))
        self.item4_check3.grid(row=10, column=3, pady=8, sticky="sne")


        # Item 5
        self.item5_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="5. Share fuel with other team",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item5_txt.grid(row=11, column=0, padx=16, pady=8, sticky="snw")

        self.item5_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item5_check1, 0.20))
        self.item5_check1.grid(row=11, column=1, pady=8, sticky="sne")

        # Item 6
        self.item6_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="6. Fuel the Launch Vehicle",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item6_txt.grid(row=12, column=0, padx=16, pady=8, sticky="snw")

        self.item6_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item6_check1, 0.15))
        self.item6_check1.grid(row=12, column=1, pady=8, sticky="sne")
        
        #Sotpwatch

        self.timerbtn = customtkinter.CTkButton(self.frame_objetives, 
                                                text="Start Mission",
                                                width=60,
                                                height=30,
                                                command=self.stopwatch)
        self.timerbtn.grid(row=13, column=0, padx=16, pady=24, sticky="we")

        self.timerTxt = customtkinter.CTkLabel(self.frame_objetives,
                                                text="00:00",
                                                width=80,
                                                bg_color="gray",
                                                corner_radius=10,
                                                text_font=("Roboto Bold", -18))
        self.timerTxt.grid(row=13, column=1, columnspan=3, padx=16, pady=24, sticky="nsw")


        #============== Frame Sensors ================
        #self.frame_sensor.grid_columnconfigure(0, minsize=50) 

        self.frame_sensor.grid_rowconfigure(1, minsize=0) # spacing row
        self.frame_sensor.grid_rowconfigure(4, minsize=20) # spacing row
        #self.frame_control.grid_rowconfigure(6, minsize=20) # spacing row

        self.sensor_title = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="DATA LOGGER",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w",
                                                width=40)
        self.sensor_title.grid(row=0, column=0, padx=16, pady=16, sticky="w")

        # Distance
        self.distancebar_txt = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="Distance: ",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w",
                                                width=40,
                                            )
        self.distancebar_txt.grid(row=2, column=0, padx=20, sticky="snw")

        self.distancebar_value = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="00 cm",
                                                text_font=("Roboto medium", -16),
                                                anchor="e")
        self.distancebar_value.grid(row=2, column=1, columnspan=3, padx=16, sticky="sne")

        self.distancebar = customtkinter.CTkProgressBar(master=self.frame_sensor,
                                                        width=380,
                                                        height=10)
        self.distancebar.grid(row=3, column=0, columnspan=4, padx=20, pady=8, sticky="snwe")


        # Color
        self.color_sensor_txt = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="Color Sensor: ",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w",
                                                width=40)
        self.color_sensor_txt.grid(row=5, column=0, padx=20, sticky="nw")

        self.color_sensor_label = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="",
                                                anchor="w",
                                                height=40,
                                                width=40,
                                                fg_color="red",
                                                corner_radius=10)
        self.color_sensor_label.grid(row=5, column=1, padx=20, sticky="snwe")


        #============== Send data logger ================
        self.frame_send.grid_columnconfigure(0, weight=1) 

        #self.frame_send.grid_rowconfigure(1, minsize=10) # spacing row
        #self.frame_control.grid_rowconfigure(6, maxsize=160) # spacing row

        self.gripper_title = customtkinter.CTkLabel(self.frame_send, 
                                                text="SEND DATA LOGGER",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w")
        self.gripper_title.grid(row=0, column=0, padx=16, pady=16, sticky="sw")

        
        self.canva = customtkinter.CTkCanvas(self.frame_send,
                                                height=120)
        self.canva.create_text(30, 20, 
                                text="Number\t|    last command\t|     value", 
                                anchor="w")
        self.canva.create_line(10, 34, 310, 34)
        self.command_logger = self.canva.create_text(30, 40, text="", anchor="nw")
        self.canva.grid(row=1, column=0, padx=16, pady=(0,16), sticky="nwe")
        


        #============== Frame Control ================
        self.frame_control.grid_columnconfigure(0, minsize=30) 
        self.frame_control.grid_columnconfigure(1, minsize=30)
        self.frame_control.grid_columnconfigure(2, minsize=320)

        self.frame_control.grid_rowconfigure(1, minsize=0) # spacing row
        self.frame_control.grid_rowconfigure(6, minsize=20) # spacing row

        self.control_title = customtkinter.CTkLabel(self.frame_control, 
                                                text="MISSION CONTROL",
                                                text_font=("Roboto Bold", -16))
        self.control_title.grid(row=0, column=0, columnspan=3, padx=(16, 0), pady=16, sticky="sw")


        # Forward control
        self.forward_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="FORWARD",
                                                width=100,
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.forward_txt.grid(row=2, column=1, padx=8, pady=8, sticky="snw")

        self.forward_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0.0,
                                                to=2.0,
                                                number_of_steps=200,
                                                variable=self.forward_value)
        self.forward_slider.grid(row=2, column=2, padx=8, pady=8, sticky="we")
        self.forward_slider.set(0)

        self.forward_entry = customtkinter.CTkEntry(master=self.frame_control, 
                                                    height=30,
                                                    textvariable=self.forward_value)
        self.forward_entry.grid(row=2, column=3, padx=8, pady=8, sticky="nswe")

        self.forward_btn = customtkinter.CTkButton(master=self.frame_control, 
                                                    text="SEND", 
                                                    height=30,
                                                    command= lambda : self.sendCommand('f', self.status))
        self.forward_btn.grid(row=2, column=4, padx=8, pady=8, sticky="nswe")

        # Backward control
        self.backward_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="BACKWARD",
                                                width=100,
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.backward_txt.grid(row=3, column=1, padx=8, pady=8, sticky="snw")
        
        self.backward_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.backward_value)
        self.backward_slider.grid(row=3, column=2, padx=8, pady=8, sticky="we")
        self.backward_slider.set(0)

        self.backward_entry = customtkinter.CTkEntry(master=self.frame_control,  
                                                    height=30,
                                                    textvariable=self.backward_value)
        self.backward_entry.grid(row=3, column=3, padx=8, pady=8, sticky="nswe")

        self.backward_btn = customtkinter.CTkButton(master=self.frame_control, 
                                                    text="SEND", 
                                                    height=30,
                                                    command= lambda : self.sendCommand('b', self.status))
        self.backward_btn.grid(row=3, column=4, padx=8, pady=8, sticky="nswe")

        # Left control
        self.left_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="TURN LEFT",
                                                width=100,
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.left_txt.grid(row=4, column=1, padx=8, pady=8, sticky="snw")
        
        self.left_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.left_value)
        self.left_slider.grid(row=4, column=2, padx=8, pady=8, sticky="we")
        self.left_slider.set(0)

        self.left_entry = customtkinter.CTkEntry(master=self.frame_control,
                                                height=30,
                                                textvariable=self.left_value)
        self.left_entry.grid(row=4, column=3, padx=8, pady=8, sticky="nswe")

        self.left_btn = customtkinter.CTkButton(master=self.frame_control, 
                                                text="SEND", 
                                                height=30,
                                                command= lambda : self.sendCommand('l', self.status))
        self.left_btn.grid(row=4, column=4, padx=8, pady=8, sticky="nswe")

        # Right control
        self.right_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="TURN RIGHT",
                                                width=100,
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.right_txt.grid(row=5, column=1, padx=8, pady=8, sticky="snw")
        
        self.right_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.right_value)
        self.right_slider.grid(row=5, column=2, padx=8, pady=8, sticky="we")
        self.right_slider.set(0)

        self.right_entry = customtkinter.CTkEntry(master=self.frame_control,
                                                height=30,
                                                textvariable=self.right_value)
        self.right_entry.grid(row=5, column=3, padx=8, pady=8, sticky="nswe")

        self.right_btn = customtkinter.CTkButton(master=self.frame_control, 
                                                text="SEND", 
                                                height=30,
                                                command= lambda : self.sendCommand('r', self.status))
        self.right_btn.grid(row=5, column=4, padx=8, pady=8, sticky="nswe")


        #GRIPPER CONTAINER

        self.container = customtkinter.CTkFrame(master=self.frame_control,
                                                height=60,
                                                fg_color=None)
        self.container.grid(row=7, column=1, columnspan=4, pady=0, stick="nswe")

        #content
        self.status1_txt = customtkinter.CTkLabel(self.container, 
                                                text="ARM CONTROL: ",
                                                text_font=("Roboto bold", -16),
                                                anchor="w")
        self.status1_txt.grid(row=0, column=0, padx=10, sticky="w")

        self.status1_txt = customtkinter.CTkLabel(self.container, 
                                                text="CLOSE",
                                                width=50,
                                                text_font=("Roboto medium", -16),
                                                anchor="e")
        self.status1_txt.grid(row=0, column=2, padx=8, pady=10, sticky="e")

        self.claw_switch = customtkinter.CTkSwitch(master=self.container, 
                                                    text="  OPEN",
                                                    text_font=("Roboto medium", -16),
                                                    command= lambda : self.switchStatus(self.claw_switch, "claw"))
        self.claw_switch.grid(row=0, column=3, padx=8, pady=10, sticky="w")

        
        self.status1_txt = customtkinter.CTkLabel(self.container, 
                                                text="DOWN",
                                                width=50,
                                                text_font=("Roboto medium", -16),
                                                anchor="e")
        self.status1_txt.grid(row=0, column=5, padx=8, pady=10, sticky="e")


        self.arm_switch = customtkinter.CTkSwitch(master=self.container, 
                                                    text="  UP",
                                                    text_font=("Roboto medium", -16),
                                                    command= lambda : self.switchStatus(self.arm_switch, "arm"))
        self.arm_switch.grid(row=0, column=6, padx=8, pady=10, sticky="w")

        
        

    #============== METODS ================#

    def progressbar_callback(self, switch, value):
        App.mission_progress

        val = switch.get()
        if val == 1:
            App.mission_progress += value
        else:
            App.mission_progress -= value

        self.progressbar.set(App.mission_progress)
        self.progressbar_value.configure(text=f'{round(App.mission_progress*100)}%')
        #print(App.mission_progress)
    
    def switchStatus(self, value, id):
        val = value.get()
        if id == "claw":
            self.sendCommand('o', self.status) if val else self.sendCommand('c', self.status)
        if id == "arm":
            self.sendCommand('u', self.status) if val else self.sendCommand('d', self.status)
        print(val)


    def sendLogger(self, command, value):
        self.cont.set(self.cont.get() + 1)
        txt_format = f'    {self.cont.get()}\t|        {command}\t|       {value}\n{self.content.get()}'
        self.content.set(txt_format)
        self.canva.itemconfig(self.command_logger, text=self.content.get())
        
    def sendCommand(self, command, status):
        if status:
            if command == 'f':
                f = self.forward_value.get()
                self.sendLogger("Forward", f'{f:.2f}')
                self.robot.moveForward(self.powerForward, f)
            if command == 'b':
                b = self.backward_value.get()
                self.sendLogger("Backward", f'{b:.2f}')
                self.robot.moveBackward(self.powerForward, b)
            if command == 'l':
                l = self.left_value.get()
                self.sendLogger("Turn Left", f'{l:.2f}')
                self.robot.turnLeft(self.powerTurn, l)
            if command == 'r':
                r = self.right_value.get()
                self.sendLogger("Turn Right", f'{r:.2f}')
                self.robot.turnRight(self.powerTurn, r)
            if command == 'o':
                self.sendLogger("Claw control", "open")
                self.robot.openGripper()
            if command == 'c':
                self.sendLogger("Claw control", "close")
                self.robot.closeGripper()
            if command == 'u':
                self.sendLogger("Arm control", "up")
                self.robot.upGripper()
            if command == 'd':
                self.sendLogger("Arm control", "Down")
                self.robot.downGripper()

    def getSensors(self):
        
        c = self.color.getColor(False)
        print(c)
        self.color_sensor_label.configure(fg_color=c)
        
        if c == "Red":
            self.robot.setLed(1,0,0)
        elif c == "Green":
            self.robot.setLed(0,1,0)
        elif c == "Blue":
            self.robot.setLed(0,0,1)
        elif c == "White":
            self.robot.setLed(1,1,1)
        else:
            self.robot.setLed(0,0,0)
        
        
        d = round(self.robot.distanceSensor.distance, 2)
        print(d)
        self.distancebar_value.configure(text=f'{d*100} cm')
        self.distancebar.set(d)
        self.distancebar_value.after(1000, self.getSensors)

    minutes = 4
    seconds = 60


    def stopwatch(self):
        App.seconds = App.seconds - 1
        if App.seconds < 0:
            App.seconds = 59
            App.minutes = App.minutes - 1

        if App.minutes >= 0:
            self.timerTxt.configure(text=f'{App.minutes}:{App.seconds}')
            self.timerTxt.after(100, self.stopwatch)
            if App.minutes == 3 and App.seconds == 0:
                self.timerTxt.configure(bg_color="red")
                messagebox.showwarning(title="Attencion", message="\n3 minutes left\n")
        else:
            self.status = False
            self.canva.itemconfig(self.command_logger, text=f'\tMISSION ACCOMPLISHED \n{self.content.get()}')
            messagebox.showwarning('warning',"\nYour time is over\t\nMISSION ACCOMPLISHED\n")
            print("time is over")

        
        
    def on_closing(self, event=0):
        self.destroy()

colorSensor = ColorSensor()
rover = Explorer()
        
if __name__ == "__main__":
    splash = Splash()
    splash.start()
    splash.mainloop()
    app = App(rover, colorSensor)
    app.getSensors()
    app.mainloop()
