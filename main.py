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
        self.title("Explorer Rover - Mission Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing())  # call .on_closing() when app gets closed

        #============ Set Frames =============
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)

        #self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_rowconfigure(2, weight=6)
       
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

        self.obj_title = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="MISSION OBJETIVES",
                                                text_font=("Roboto Bold", -16))
        self.obj_title.grid(row=0, column=0, padx=16, pady=16, sticky="sw")

        # Progressbar
        self.progressbar_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Progress: ",
                                                text_font=("Roboto medium", -16))
        self.progressbar_txt.grid(row=1, column=0, padx=16, sticky="snw")

        self.progressbar_value = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="00%",
                                                text_font=("Roboto medium", -16),
                                                width=80,
                                                anchor="e")
        self.progressbar_value.grid(row=1, column=1, columnspan=3, padx=16, sticky="sne")

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_objetives,)
        self.progressbar.grid(row=2, column=0, columnspan=4, sticky="snwe", padx=16, pady=16)

        # Mission Objetives
        self.progressbar_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="Mission Objetives",
                                                text_font=("Roboto medium", -16))
        self.progressbar_txt.grid(row=3, column=0, padx=16, pady=16, sticky="snw")

        # Item 1
        self.item1_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="1. Free access to Habitat",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item1_txt.grid(row=4, column=0, padx=16, pady=8, sticky="snw")

        self.item1_check = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item1_check.grid(row=4, column=1,  sticky="sne")

        # Item 2
        self.item2_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="2. Find and Collect Water",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item2_txt.grid(row=5, column=0, padx=16, pady=8, sticky="snw")

        self.item2_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item2_check1.grid(row=5, column=1,  sticky="sne")
        self.item2_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item2_check2.grid(row=5, column=2, pady=8, sticky="sne")
        self.item2_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item2_check3.grid(row=5, column=3, pady=8, sticky="sne")

        # Item 3
        self.item3_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="3. Collect Food",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item3_txt.grid(row=6, column=0, padx=16, pady=8, sticky="snw")

        self.item3_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item3_check1.grid(row=6, column=1,  sticky="sne")
        self.item3_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item3_check2.grid(row=6, column=2, pady=8, sticky="sne")
        self.item3_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item3_check3.grid(row=6, column=3, pady=8, sticky="sne")


        # Item 4
        self.item4_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="4. Collect soil samples",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item4_txt.grid(row=7, column=0, padx=16, pady=8, sticky="snw")

        self.item4_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item4_check1.grid(row=7, column=1,  sticky="sne")
        self.item4_check2 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item4_check2.grid(row=7, column=2, pady=8, sticky="sne")
        self.item4_check3 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item4_check3.grid(row=7, column=3, pady=8, sticky="sne")


        # Item 5
        self.item5_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="5. Share fuel with other team",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item5_txt.grid(row=8, column=0, padx=16, pady=8, sticky="snw")

        self.item5_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item5_check1.grid(row=8, column=1,  sticky="sne")

        # Item 6
        self.item6_txt = customtkinter.CTkLabel(self.frame_objetives, 
                                                text="6. Fuel the Launch Vehicle",
                                                text_font=("Roboto regular", -16),
                                                anchor="w")
        self.item6_txt.grid(row=9, column=0, padx=16, pady=8, sticky="snw")

        self.item6_check1 = customtkinter.CTkCheckBox(self.frame_objetives, text="")
        self.item6_check1.grid(row=9, column=1,  sticky="sne")
        
    

        #============== Frame Control ================

        self.control_title = customtkinter.CTkLabel(self.frame_control, 
                                                text="MISSION CONTROL",
                                                text_font=("Roboto Bold", -16))
        self.control_title.grid(row=0, column=0, padx=16, pady=16, sticky="sw")




        self.forward_txt = customtkinter.CTkLabel(self.frame_control, 
                                                text="FORWARD",
                                                text_font=("Roboto medium", -16),
                                                anchor="w")
        self.forward_txt.grid(row=1, column=0, padx=16, pady=8, sticky="snw")

        self.forward_slider = customtkinter.CTkSlider(master=self.frame_control,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.forward_slider.grid(row=1, column=1, columnspan=2, pady=10, padx=20, sticky="we")





    def progressbar_callback(switch, value):
        App.mission_progress

        val = switch.get()
        if val == 1:
            App.mission_progress += value
        else:
            App.mission_progress -= value
        print(App.mission_progress)
    
   

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
