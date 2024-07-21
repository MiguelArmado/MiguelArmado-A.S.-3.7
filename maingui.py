"""
Title: Foreign Exchange
Written by: Miguel Armado
Date Written: 25/06/2024
Purpose of the program: To allow the user to convert currencies through the use of a GUI
V1: Create a GUI for my main menu where the user can convert currencies
"""
# Import the necessary library/ies
from tkinter import *

# Variables

# Font styles
sub_headings = ("Helvetica", 9, "bold")

# Colors
gray = "#E6E6E6"
orange = "FFB570"
blue = "#8282FF"

# Create a GUI class
class Forex:
    def __init__(self):
        self.amount_num = IntVar()
        self.from_num = IntVar()
        self.left_frame = Frame()
        self.left_frame.config(bg=gray)
        self.left_frame.grid()

        self.forex_lbl1 = Label(self.left_frame,
                                text="Currency Converter",
                                bg=gray,
                                font=("Helvetica", 18, "bold"))
        self.forex_lbl1.grid(ipadx=30, ipady=20,
                             sticky=S)
        
        self.amount_lbl2 = Label(self.left_frame,
                                 text="Amount:",
                                 bg=gray,
                                 font=sub_headings)
        self.amount_lbl2.grid(row=1, column=0,
                              ipadx=10, ipady=10,
                              sticky=W)
        
        self.amount_num = Entry(self.left_frame,
                                textvariable=self.amount_num,

                                )
        
        self.from_lbl3 = Label(self.left_frame,
                               text="From:",
                               bg=gray,
                               font=sub_headings)
        self.from_lbl3.grid(row=2, column=0,
                            ipadx=10, ipady=5,
                            sticky=W)

# Main Program
root = Tk()
root.title("Foreign Exchange")
root.configure(bg=gray)
root.geometry("580x310")
root.resizable(0, 0)
Forex()
root.mainloop()