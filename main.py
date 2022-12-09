# Noe Soudi, partner for final: Tiffany Domingo
# CSCI 1620-001, 9/8/2022
# This program is a live gui weather application
# Data is retrieved via API
# Data is parsed using JSON
# API key is necessary for this program to run correctly
# Refer to obtainAPI.txt for instructions on how to get you own free personal API Key

from app_gui import *


def main():
    window = Tk()
    window.title("noe and tiff")
    window.geometry("600x500")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
