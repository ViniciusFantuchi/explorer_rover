import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        super().__init__()
        self.title("Explorer Rover - Mission Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing())  # call .on_closing() when app gets closed

        #============ Set Frames =============
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_rowconfigure(2, weight=6)
        self.grid_rowconfigure(0, weight=1)

        self.frame_header = customtkinter.CTkFrame(master=self, fg_color=None)
        self.frame_header.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="nswe")

        self.frame_objetives = customtkinter.CTkFrame(master=self)
        self.frame_objetives.grid(row=1, column=0, rowspan=2, padx=(20, 10), pady=(10, 20), sticky="nswe")

        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.grid(row=1, column=1, columnspan=2, padx=(10, 20), pady=10, sticky="nswe")

        self.frame_gripper = customtkinter.CTkFrame(master=self)
        self.frame_gripper.grid(row=2, column=1, padx=10, pady=(10, 20), sticky="nswe")

        self.frame_sensor = customtkinter.CTkFrame(master=self)
        self.frame_sensor.grid(row=2, column=2, padx=(10, 20), pady=(10, 20), sticky="nswe")


        #============ Set Header =============
        self.obj_title = customtkinter.CTkLabel(self.frame_header, 
                                                text="EXPLORER ROVER MISSION CONTROL",
                                                text_font=("Roboto Bold", -20)
                                                )
        self.obj_title.grid(row=0, column=0, sticky="sw")

        self.obj_subtitle = customtkinter.CTkLabel(self.frame_header, 
                                                text="KSCIA - International Space Academy",
                                                text_font=("Roboto regular", -14),
                                                justify=tkinter.LEFT
                                                )
        self.obj_subtitle.grid(row=1, column=0, sticky="nw")


        logo = Image.open(PATH + "/images/logoKSCIA.png")
        self.logo_image = ImageTk.PhotoImage(logo)

        self.logo_label = customtkinter.CTkLabel(master=self.frame_header, image=self.logo_image)
        self.logo_label.place(x=1130, y=0)

    #============ Frame ============



    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
