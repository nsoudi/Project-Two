from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk, ImageSequence
import requests
import pytemperature

gifCounter = 0


class GUI:
    """
    A class representing tkinter GUI interface window object for weather checking application
    """
    def __init__(self, window):
        """
        Constructor to create the initial state of a window object
        :param window: Name of tkinter instance of class Tk
        """

        font_one = Font(family="Bodoni 72 Smallcaps", size=40, weight="bold")
        instructionfont = Font(family="helvetica", size=12)
        font_two = Font(family="Bangla MN", size=20)
        font_three = Font(family="Bangla MN", size=15)
        font_four = Font(family="Bodoni 72 Smallcaps", size=18)

        self.window = window

        self.iconimg = Image.open("weather.gif")
        resized = self.iconimg.resize((550, 100), Image.ANTIALIAS)
        self.iconimg = ImageTk.PhotoImage(Image.open("weather.gif"))
        self.newiconimg = ImageTk.PhotoImage(resized)
        self.frame_picture = Frame(self.window)
        self.imglabel = Label(self.frame_picture, image=self.newiconimg)
        self.frame_picture.pack(pady=10)
        self.imglabel.pack()

        self.frame_rules = Frame(self.window)
        self.label_rules = Label(self.frame_rules, text="Check The Weather", font=font_one)
        self.label_rules.pack(padx=5)
        self.frame_rules.pack(pady=10)

        self.frame_city = Frame(self.window)  # City is zipcode
        self.label_city = Label(self.frame_city, text="Enter your Zip/Postal Code", font=font_two)
        self.entry_city = Entry(self.frame_city, borderwidth=6)
        self.frame_city.pack(anchor='w', pady=10)
        self.label_city.pack(padx=30, side="left")
        self.entry_city.pack(padx=2, side="left")

        self.frame_area = Frame(self.window)  # Area is countrycode
        self.label_area = Label(self.frame_area, text="Enter your Country Code", font=font_two)
        self.entry_area = Entry(self.frame_area, borderwidth=6)
        self.frame_area.pack(anchor='w', pady=10)
        self.label_area.pack(padx=30, side="left")
        self.entry_area.pack(padx=2, side="left")

        self.frame_submit = Frame(self.window)
        self.btn_submit = Button(self.frame_submit, text="submit", font=font_two, command=self.submitbutton)

        self.frame_errormessage = Frame(self.window)
        self.lbl_message = Label(self.frame_errormessage,
                                 text="Zip code and Country code combition invalid.\n"
                                      " Visit worldpostalcode.com for valid zip and country pairings",
                                 font=font_four)
        self.lbl_message2 = Label(self.frame_errormessage, text="invalid.\n please fill in city and area code",
                                  font=font_four)
        self.lbl_message3 = Label(self.frame_errormessage,
                                  text="invalid.\n do not leave any entries blank. "
                                       "zip must be a int. country code must be an str",
                                  font=font_four)

        self.btn_results = Button(self.frame_submit, text="Weather results ready!\nClick to view Results",
                                  command=self.page1)
        self.frame_submit.pack(anchor="w", padx=30, pady=10)
        self.btn_submit.pack()
        self.bigframe = Frame(self.window)

    def play_gif(self):
        """
        Method to play the "loading animation once validation is complete and submit button is clicked.
        """

        global gifCounter
        gifCounter += 1

        self.img = Image.open("Bar-Preloader-3.gif")
        self.lbl1 = Label(self.window, height=50, width=150)
        self.lbl1.place(x=50, y=400)

        for self.img in ImageSequence.Iterator(self.img):
            self.img = ImageTk.PhotoImage(self.img)
            self.lbl1.config(image=self.img)
            self.window.update()
        self.lbl1.place_forget()

        self.img2 = Image.open("Bar-Preloader-3.gif")
        self.lbl2 = Label(self.window, height=50, width=150)
        self.lbl2.place(x=200, y=400)

        for self.img2 in ImageSequence.Iterator(self.img2):
            self.img2 = ImageTk.PhotoImage(self.img2)
            self.lbl2.config(image=self.img2)
            self.window.update()
        self.lbl2.place_forget()

        self.img3 = Image.open("Bar-Preloader-3.gif")
        self.lbl3 = Label(self.window, height=50, width=150)
        self.lbl3.place(x=350, y=400)

        for self.img3 in ImageSequence.Iterator(self.img3):
            self.img3 = ImageTk.PhotoImage(self.img3)
            self.lbl3.config(image=self.img3)
            self.window.update()
        self.lbl3.place_forget()

        if gifCounter == 3:
            self.btn_submit.pack_forget()  # Code in this if block removes loading
            self.btn_results.pack()        # animation after being played desired amount of times
            self.lbl1.pack_forget()
            self.lbl1.place_forget()
            self.lbl2.pack_forget()
            self.lbl2.place_forget()
            self.lbl3.pack_forget()
            self.lbl3.place_forget()
            return

        self.window.after(1, self.play_gif)

    def window2(self):
        self.window(exit())

    def page1(self):
        """
        Method to raise the second tkinter window. this window displays weather rulst based
        the zip code and country code entered after validation.
        """

        font_five = Font(family="Bodoni 72 Smallcaps", size=18)
        font_six = Font(family="Krungthep", size=20)

        self.bigframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.iconimg2 = Image.open("weather.gif")
        resized = self.iconimg2.resize((550, 100), Image.ANTIALIAS)
        self.iconimg2 = ImageTk.PhotoImage(Image.open("weather.gif"))
        self.newiconimg2 = ImageTk.PhotoImage(resized)
        self.imglabel2 = Label(self.bigframe, image=self.newiconimg)
        self.imglabel2.place(relx=0.0, rely=0.0, x=23, y=10)

        if self.thecurrentemp <= 50.0:
            self.iconimgg = Image.open("coldguy.png")
            resized = self.iconimgg.resize((140, 140), Image.ANTIALIAS)
            self.iconimgg = ImageTk.PhotoImage(Image.open("coldguy.png"))
            self.newiconimgg = ImageTk.PhotoImage(resized)
            self.imgglabell = Label(self.bigframe, image=self.newiconimgg)
            self.imgglabell.place(relx=0.0, rely=0.0, x=420, y=130)

        elif self.thecurrentemp > 50.00:
            self.iconimgg2 = Image.open("goodweatherguy.png")
            resized = self.iconimgg2.resize((140, 140), Image.ANTIALIAS)
            self.iconimgg2 = ImageTk.PhotoImage(Image.open("goodweatherguy.png"))
            self.newiconimgg2 = ImageTk.PhotoImage(resized)
            self.imgglabell2 = Label(self.bigframe, image=self.newiconimgg2)
            self.imgglabell2.place(relx=0.0, rely=0.0, x=420, y=130)

        self.label1 = Label(self.bigframe, text=self.weather_report, font=font_five, borderwidth=6, relief="groove",
                            justify=LEFT)
        self.label1.place(relx=0.0, rely=0.0, x=30, y=125)
        self.btn_exit = Button(self.bigframe, text="exit", font=font_six, command=self.window.destroy)
        self.btn_exit.place(relx=0.0, rely=0.0, x=30, y=300)
        self.btn_again = Button(self.bigframe, text="Check The Weather Again", font=font_six, command=self.retsart)
        self.btn_again.place(relx=0.0, rely=0.0, x=30, y=350)

    def retsart(self):
        """
        Method to clear previous data and go back to home screen is "check weather again" button is clicked.
        """
        global gifCounter
        self.bigframe.place_forget()
        self.btn_results.pack_forget()
        self.btn_submit.pack()
        if gifCounter > 0:
            gifCounter = 0

    def submitbutton(self):
        """
        Method to submit the user's zip code and country code. Validation is done here first before accepting entry.
        zip code may only integers and country code may only be strings. Leaving either entry box blank is not allowed
        """

        while self.entry_area.get() == '':

            self.lbl_message.pack_forget()
            self.frame_errormessage.pack_forget()
            self.lbl_message3.pack()
            self.frame_errormessage.pack()
            #print("Value Error: entry box empty")
            return

        self.api_start = 'https://api.openweathermap.org/data/2.5/weather?zip='

        # API key sharing is prohibited therefor I have left it out of the code.
        # Please obtain your own personal free weather data API from https://openweathermap.org/
        # It is necessary in order for the program to run successfully.
        # I have left further detailed instructions in the "obtainAPI.txt".
        self.api_key = "&appid=c11e530e965174a8742b2b2539aa8a85"

        try:
            zip = int(self.entry_city.get())
            country = str(self.entry_area.get())
            url = self.api_start + str(zip) + ',' + country + self.api_key
            json_data = requests.get(url).json()
            current_temp_k = json_data['main']['temp']
            current_temp_f = pytemperature.k2f(current_temp_k)
            current_pressure = json_data['main']['pressure']
            current_humidity = json_data['main']['humidity']

            self.thecurrentemp = current_temp_f

            expected_low_temp = json_data['main']['temp_min']
            expected_low_temp = pytemperature.k2f(expected_low_temp)
            expected_high_temp = json_data['main']['temp_max']
            expected_high_temp = pytemperature.k2f(expected_high_temp)

            weather_description = json_data['weather'][0]['description']

            self.weather_report = f"Current Temperature in Fahrenheit: {current_temp_f}\n" \
                                  f"Current pressure in HPA: {current_pressure}\n" \
                                  f"Current Humidity: {current_humidity}\n" \
                                  f"Expected Low Temperature in Fahrenheit: {expected_low_temp}\n" \
                                  f"Expected High Temperature in Fahrenheit: {expected_high_temp}\n" \
                                  f"Current conditions: {weather_description}"

            self.frame_errormessage.pack_forget()
            self.lbl_message.pack_forget()
            self.entry_city.delete(0, END)
            self.entry_area.delete(0, END)
            self.play_gif()

        except ValueError:

            if len(self.entry_city.get()) == 0:
                self.lbl_message.pack_forget()
                self.frame_errormessage.pack_forget()
                self.lbl_message3.pack()
                self.frame_errormessage.pack()
            else:
                self.lbl_message3.pack_forget()
                self.frame_errormessage.pack(anchor="e", pady=10)
                self.lbl_message.pack(padx=2, side="right", anchor="e")

        except KeyError:
            self.lbl_message3.pack_forget()
            self.frame_errormessage.pack(anchor="e", pady=10)
            self.lbl_message.pack(padx=2, side="right", anchor="e")

