from doctest import master
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):

    # Control Variables 
    WIDTH = 1280
    HEIGHT = 720

    mission_progress = 0
    
    

    def __init__(self):
        super().__init__()

        self.forward_value = tkinter.DoubleVar()
        self.forward_value.set(0.0)
        self.backward_value = tkinter.DoubleVar()
        self.left_value = tkinter.DoubleVar()
        self.right_value = tkinter.DoubleVar()

        self.title("Explorer Rover - Mission Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing())  # call .on_closing() when app gets closed

        #============ Set Frames =============
        self.grid_columnconfigure(0, minsize=400)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
       
        self.grid_rowconfigure(0, minsize=90)

        self.frame_header = customtkinter.CTkFrame(master=self, fg_color=None)
        self.frame_header.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nswe")

        self.frame_objetives = customtkinter.CTkFrame(master=self)
        self.frame_objetives.grid(row=1, column=0, rowspan=2, padx=(20, 8), pady=(0, 20), sticky="nswe")

        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.grid(row=1, column=1, columnspan=2, padx=(8, 20), pady=(0, 8), sticky="nswe")

        self.frame_gripper = customtkinter.CTkFrame(master=self)
        self.frame_gripper.grid(row=2, column=1, padx=8, pady=(8, 20), sticky="nswe")

        self.frame_sensor = customtkinter.CTkFrame(master=self)
        self.frame_sensor.grid(row=2, column=2, padx=(8, 20), pady=(8, 20), sticky="nswe")


        #============ Set Header =============
        self.obj_title = customtkinter.CTkLabel(self.frame_header, 
                                                text="EXPLORER ROVER MISSION CONTROL",
                                                text_font=("Roboto Bold", -18)
                                                )
        self.obj_title.grid(row=0, column=0, sticky="w", pady=0)

        self.obj_subtitle = customtkinter.CTkLabel(self.frame_header, 
                                                text="KSCIA - International Space Academy",
                                                text_font=("Roboto regular", -12),
                                                justify=tkinter.LEFT
                                                )
        self.obj_subtitle.grid(row=1, column=0, sticky="w")


        logo = Image.open(PATH + "/images/logoKSCIA.png").resize((50,50))
        self.logo_image = ImageTk.PhotoImage(logo)

        self.logo_label = customtkinter.CTkLabel(master=self.frame_header, image=self.logo_image)
        self.logo_label.place(x=1140, y=0)

        #============== Frame Objetives ================
        self.frame_objetives.grid_rowconfigure(1, minsize=20) # spacing row
        self.frame_objetives.grid_rowconfigure(4, minsize=20) # spacing row
        self.frame_objetives.grid_rowconfigure(12, minsize=20) # spacing row

        self.obj_title = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="MISSION OBJETIVES",
                                                text_font=("Roboto Bold", -16))
        self.obj_title.grid(row=0, column=0, padx=16, pady=16, sticky="sw")

        # Progressbar
        self.progressbar_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Progress: ",
                                                text_font=("Roboto Bold", -16))
        self.progressbar_txt.grid(row=2, column=0, padx=16, sticky="snw")

        self.progressbar_value = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="00%",
                                                text_font=("Roboto medium", -16),
                                                width=80,
                                                anchor="e")
        self.progressbar_value.grid(row=2, column=1, columnspan=3, padx=16, sticky="sne")

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_objetives,)
        self.progressbar.grid(row=3, column=0, columnspan=4, sticky="snwe", padx=16, pady=16)
        self.progressbar.set(0)

        # Mission Objetives
        self.obj_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Objetives:",
                                                text_font=("Roboto Bold", -16))
        self.obj_txt.grid(row=5, column=0, padx=16, pady=16, sticky="snw")

        # Item 1
        self.item1_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="1. Free access to Habitat",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item1_txt.grid(row=7, column=0, padx=16, pady=10, sticky="snw")

        self.item1_check = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item1_check, 0.2))
        self.item1_check.grid(row=7, column=1,  sticky="sne")

        # Item 2
        self.item2_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="2. Find and Collect Water",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item2_txt.grid(row=8, column=0, padx=16, pady=10, sticky="snw")

        self.item2_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check1, 0.05))
        self.item2_check1.grid(row=8, column=1,  sticky="sne")
        self.item2_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check2, 0.05))
        self.item2_check2.grid(row=8, column=2, pady=10, sticky="sne")
        self.item2_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item2_check3, 0.05))
        self.item2_check3.grid(row=8, column=3, pady=10, sticky="sne")

        # Item 3
        self.item3_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="3. Collect Food",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item3_txt.grid(row=9, column=0, padx=16, pady=10, sticky="snw")

        self.item3_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check1, 0.05))
        self.item3_check1.grid(row=9, column=1,  sticky="sne")
        self.item3_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check2, 0.05))
        self.item3_check2.grid(row=9, column=2, pady=10, sticky="sne")
        self.item3_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item3_check3, 0.05))
        self.item3_check3.grid(row=9, column=3, pady=10, sticky="sne")


        # Item 4
        self.item4_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="4. Collect soil samples",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item4_txt.grid(row=10, column=0, padx=16, pady=10, sticky="snw")

        self.item4_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check1, 0.05))
        self.item4_check1.grid(row=10, column=1,  sticky="sne")
        self.item4_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check2, 0.05))
        self.item4_check2.grid(row=10, column=2, pady=10, sticky="sne")
        self.item4_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item4_check3, 0.05))
        self.item4_check3.grid(row=10, column=3, pady=10, sticky="sne")


        # Item 5
        self.item5_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="5. Share fuel with other team",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item5_txt.grid(row=11, column=0, padx=16, pady=10, sticky="snw")

        self.item5_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item5_check1, 0.20))
        self.item5_check1.grid(row=11, column=1, pady=10, sticky="sne")

        # Item 6
        self.item6_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="6. Fuel the Launch Vehicle",
                                                text_font=("Roboto regular", -14),
                                                anchor="w")
        self.item6_txt.grid(row=12, column=0, padx=16, pady=10, sticky="snw")

        self.item6_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="",
                                                        command= lambda : self.progressbar_callback(self.item6_check1, 0.15))
        self.item6_check1.grid(row=12, column=1, pady=10, sticky="sne")
        
    

        #============== Frame Control ================
        self.frame_control.grid_columnconfigure(0, minsize=50) 
        self.frame_control.grid_columnconfigure(1, minsize=100)
        self.frame_control.grid_columnconfigure(2, minsize=300)

        self.frame_control.grid_rowconfigure(1, minsize=30) # spacing row
        #self.frame_control.grid_rowconfigure(6, minsize=20) # spacing row

        self.control_title = customtkinter.CTkLabel(self.frame_control, 
                                                text="MISSION CONTROL",
                                                text_font=("Roboto Bold", -16))
        self.control_title.grid(row=0, column=0, columnspan=3, padx=16, pady=16, sticky="sw")


        # Forward control
        self.forward_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="FORWARD",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.forward_txt.grid(row=2, column=1, padx=8, pady=10, sticky="snw")

        self.forward_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.forward_value)
        self.forward_slider.grid(row=2, column=2, padx=8, pady=10, sticky="we")
        self.forward_slider.set(0)

        self.forward_entry = customtkinter.CTkEntry(master=self.frame_control, 
                                                    height=30,
                                                    textvariable=self.forward_value)
        self.forward_entry.grid(row=2, column=3, padx=8, pady=10, sticky="nswe")

        self.forward_btn = customtkinter.CTkButton(master=self.frame_control, text="SEND", height=30)
        self.forward_btn.grid(row=2, column=4, padx=8, pady=10, sticky="nswe")

        # Backward control
        self.backward_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="BACKWARD",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.backward_txt.grid(row=3, column=1, padx=8, pady=10, sticky="snw")
        
        self.backward_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.backward_value)
        self.backward_slider.grid(row=3, column=2, padx=8, pady=10, sticky="we")
        self.backward_slider.set(0)

        self.backward_entry = customtkinter.CTkEntry(master=self.frame_control,  
                                                    height=30,
                                                    textvariable=self.backward_value)
        self.backward_entry.grid(row=3, column=3, padx=8, pady=10, sticky="nswe")

        self.backward_btn = customtkinter.CTkButton(master=self.frame_control, text="SEND", height=30)
        self.backward_btn.grid(row=3, column=4, padx=8, pady=10, sticky="nswe")

        # Left control
        self.left_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="TURN LEFT",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.left_txt.grid(row=4, column=1, padx=8, pady=10, sticky="snw")
        
        self.left_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.left_value)
        self.left_slider.grid(row=4, column=2, padx=8, pady=10, sticky="we")
        self.left_slider.set(0)

        self.left_entry = customtkinter.CTkEntry(master=self.frame_control,
                                                height=30,
                                                textvariable=self.left_value)
        self.left_entry.grid(row=4, column=3, padx=8, pady=10, sticky="nswe")

        self.left_btn = customtkinter.CTkButton(master=self.frame_control, text="SEND", height=30)
        self.left_btn.grid(row=4, column=4, padx=8, pady=10, sticky="nswe")

        # Right control
        self.right_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="TURN LEFT",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.right_txt.grid(row=5, column=1, padx=8, pady=10, sticky="snw")
        
        self.right_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=2,
                                                number_of_steps=200,
                                                variable=self.right_value)
        self.right_slider.grid(row=5, column=2, padx=8, pady=10, sticky="we")
        self.right_slider.set(0)

        self.right_entry = customtkinter.CTkEntry(master=self.frame_control,
                                                height=30,
                                                textvariable=self.right_value)
        self.right_entry.grid(row=5, column=3, padx=8, pady=10, sticky="nswe")

        self.right_btn = customtkinter.CTkButton(master=self.frame_control, text="SEND", height=30)
        self.right_btn.grid(row=5, column=4, padx=8, pady=10, sticky="nswe")




        #============== Frame Gripper ================
        self.frame_gripper.grid_columnconfigure(1, minsize=10) 

        self.frame_gripper.grid_rowconfigure(1, minsize=10) # spacing row
        #self.frame_control.grid_rowconfigure(6, minsize=20) # spacing row

        self.gripper_title = customtkinter.CTkLabel(self.frame_gripper, 
                                                text="GRIPPER CONTROL",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w")
        self.gripper_title.grid(row=0, column=0, columnspan=3, padx=16, pady=16, sticky="sw")

        # Gripper control
        self.status1_txt = customtkinter.CTkLabel(self.frame_gripper, 
                                                text="Claw Control: ",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.status1_txt.grid(row=2, column=0, padx=20, sticky="w")

        self.status1_txt = customtkinter.CTkLabel(self.frame_gripper, 
                                                text="OPEN",
                                                width=50,
                                                text_font=("Roboto medium", -16),
                                                anchor="e")
        self.status1_txt.grid(row=2, column=2, padx=8, pady=10, sticky="e")

        self.arm_switch = customtkinter.CTkSwitch(master=self.frame_gripper, 
                                                    text="  CLOSE",
                                                    text_font=("Roboto medium", -16))
        self.arm_switch.grid(row=2, column=3, padx=8, pady=10, sticky="w")

        # Arm control
        self.status2_txt = customtkinter.CTkLabel(self.frame_gripper, 
                                                text="Arm Control: ",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.status2_txt.grid(row=3, column=0, padx=20, pady=10, sticky="snw")

        self.status1_txt = customtkinter.CTkLabel(self.frame_gripper, 
                                                text="UP",
                                                width=50,
                                                text_font=("Roboto medium", -16),
                                                anchor="e")
        self.status1_txt.grid(row=3, column=2, padx=8, pady=10, sticky="e")

        self.arm_switch = customtkinter.CTkSwitch(master=self.frame_gripper, 
                                                    text="  DOWN",
                                                    text_font=("Roboto medium", -16))
        self.arm_switch.grid(row=3, column=3, padx=8, pady=10, sticky="w")


        #============== Frame Sensors ================
        #self.frame_sensor.grid_columnconfigure(0, minsize=50) 

        self.frame_sensor.grid_rowconfigure(1, minsize=20) # spacing row
        self.frame_sensor.grid_rowconfigure(4, minsize=20) # spacing row
        #self.frame_control.grid_rowconfigure(6, minsize=20) # spacing row

        self.sensor_title = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="SENSORS",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w")
        self.sensor_title.grid(row=0, column=0, padx=16, pady=16, sticky="w")

        # Distance
        self.distancebar_txt = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="Distance: ",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w")
        self.distancebar_txt.grid(row=2, column=0, padx=20, sticky="snw")

        self.distancebar_value = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="00 cm",
                                                text_font=("Roboto medium", -16),
                                                width=80,
                                                anchor="e")
        self.distancebar_value.grid(row=2, column=1, columnspan=3, padx=16, sticky="sne")

        self.distancebar = customtkinter.CTkProgressBar(master=self.frame_sensor,
                                                        width=380)
        self.distancebar.grid(row=3, column=0, columnspan=4, padx=20, pady=16, sticky="snwe")


        # Color
        self.color_sensor_txt = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="Color Sensor: ",
                                                text_font=("Roboto Bold", -16),
                                                anchor="w")
        self.color_sensor_txt.grid(row=5, column=0, padx=20, sticky="nw")

        self.color_sensor_label = customtkinter.CTkLabel(self.frame_sensor, 
                                                text="",
                                                anchor="w",
                                                height=40,
                                                fg_color="red",
                                                corner_radius=10)
        self.color_sensor_label.grid(row=5, column=1, padx=20, sticky="snwe")


    # Metods

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
    
    
        

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
