"""
Title: Foreign Exchange
Written by: Miguel Armado
Date Written: 25/06/2024
Purpose of the program: To allow the user to convert currencies through the use of a GUI
V1: Create a GUI for my main menu where the user can convert currencies
V2: Added an exchange rate to the right of the main conversion tool
"""
# Import the necessary library/ies
from tkinter import *
import requests
from tkinter import ttk

# Initialize the API so that I can use the data to get the currencies and conversions
URL = "https://v6.exchangerate-api.com/v6/9e764c29f1f368dc0202e365/latest/USD"

# Request to get the .json file returned by the URL
RESPONSE = requests.get(URL)

# Assign the .json file to a variable
DATA = RESPONSE.json()

# Constants
# List of currencies
CURRENCIES = list(DATA["conversion_rates"].keys())
CURRENCIES.remove("ZWL")

# Font styles
SUB_HEADINGS = ("Helvetica", 9, "bold")

# Colors
GRAY = "#E6E6E6"
BLUE = "#8282FF"
RED = "#FF0000"
BLACK = "#000000"
LIGHT_BLUE = "#ccccfc"

# Maximum amount of money the user can convert
MAX_AMOUNT = 10000


# Create a GUI class
class Forex(Tk):
    def __init__(self):
        super().__init__()
        # Change the title of the program to Foreign Exchange, set the size of the window and make it not resizeable
        self.title("Foreign Exchange"), self.geometry("685x310"), self.resizable(0, 0)
        self.configure(bg=GRAY)

        # Set up the text variable's data types that will constantly change throughout the game.
        self.amount_num = StringVar()
        self.currencies = CURRENCIES
        self.from_currency = StringVar()
        self.to_currency = StringVar()
        self.converted_value = DoubleVar()

        # Setting the default amounts for the amount to be converted
        # and converted to 0
        self.amount_num.set("")

        # Label for the title of the program
        self.currency_converter_lbl1 = Label(self,
                                             text="Currency Converter",
                                             bg=GRAY,
                                             font=("Helvetica", 18, "bold"))
        self.currency_converter_lbl1.grid(ipadx=10, ipady=15,
                                          sticky=S)

        # Label for the amount the user wants to convert
        self.amount_lbl2 = Label(self,
                                 text="Amount:",
                                 bg=GRAY,
                                 font=("Helvetica", 12, "bold"))
        self.amount_lbl2.grid(row=1, column=0,
                              ipadx=6, ipady=5,
                              sticky=W)

        # Entry box for the amount the user wants to convert
        self.amount_num_entry1 = Entry(self,
                                       textvariable=self.amount_num,
                                       bg=LIGHT_BLUE,
                                       font=SUB_HEADINGS,
                                       width=23)
        self.amount_num_entry1.grid(row=1, column=0,
                                    sticky=E, ipady=5)

        # Label for the currency the user wants to convert from
        self.from_lbl3 = Label(self,
                               text="From:",
                               bg=GRAY,
                               font=SUB_HEADINGS)
        self.from_lbl3.grid(row=2, column=0,
                            ipadx=10, ipady=5,
                            sticky=W)

        # a Combobox that will display the currencies the user wants to convert from
        # This ComboBox also has a feature to autocomplete or change the contents
        # of the combobox to display the currencies that start with the letter the user
        # inputted when the user releases a key. It also does not allow the input of special characters and
        # numbers, decreasing the possibilities of errors in the program.
        self.from_currency_combo1 = ttk.Combobox(self,
                                                 width=23,
                                                 textvariable=self.from_currency,
                                                 values=self.currencies,
                                                 validate='key',
                                                 validatecommand=(self.register(self.__validate_combo_input), '%d', '%P'))
        self.from_currency_combo1.bind('<KeyRelease>', self.__update_combo, '+')
        self.from_currency_combo1.bind('<KeyRelease>', lambda _: self.capitalize_currency(self.from_currency), '+')
        self.from_currency_combo1.bind('<KeyRelease>', lambda _: self.update_exchange_rate(), '+')
        self.from_currency_combo1.bind('<ButtonPress-1>', lambda _: self.update_exchange_rate())
        self.from_currency_combo1.grid(row=2, column=0,
                                       sticky=E)

        # Space between Combo-boxes
        self.spacer1 = Label(self, text="",
                             bg=GRAY)
        self.spacer1.grid(row=3, column=0)

        # Label for the currency the user wants to convert to
        self.to_lbl4 = Label(self,
                             text="To: ",
                             width=8,
                             bg=GRAY,
                             font=SUB_HEADINGS)
        self.to_lbl4.grid(row=4, column=0,
                          sticky=W)

        # Same with the first combobox, it does the same but this time it will contain the currency the user wants to
        # converts to
        self.to_currency_combo2 = ttk.Combobox(self,
                                               width=23,
                                               textvariable=self.to_currency,
                                               values=self.currencies,
                                               validate='key',
                                               validatecommand=(self.register(self.__validate_combo_input), '%d', '%P'))
        self.to_currency_combo2.bind('<KeyRelease>', self.__update_combo, '+')
        self.to_currency_combo2.bind('<KeyRelease>', lambda _: self.capitalize_currency(self.to_currency), '+')
        self.to_currency_combo2.bind('<KeyRelease>', lambda _: self.update_exchange_rate(), '+')
        self.to_currency_combo2.bind('<ButtonPress-1>', lambda _: self.update_exchange_rate())
        self.to_currency_combo2.grid(row=4, column=0,
                                     sticky=E)
        # Label for the error message
        self.error_lbl5 = Label(self,
                                text="",
                                bg=GRAY,
                                fg=RED,
                                font=SUB_HEADINGS,
                                justify=CENTER)
        self.error_lbl5.grid(row=5, column=0,
                             sticky="E")

        # Label for the converted amount (text)
        self.converted_lbl6 = Label(self,
                                    text="Converted amount: ",
                                    fg=BLACK,
                                    bg=GRAY,
                                    font=SUB_HEADINGS)
        self.converted_lbl6.grid(row=6, column=0,
                                 ipady=10, sticky="W")

        # Label for the converted amount value
        self.amount_converted_lbl7 = Label(self,
                                           text="",
                                           fg=BLACK,
                                           font=("Helvetica", 12, "bold"),
                                           width=13,
                                           borderwidth=1,
                                           relief=SOLID)
        self.amount_converted_lbl7.grid(row=6, column=0,
                                        ipady=5, sticky="E")

        # Spacer for between the error message and the calculate button
        self.spacer2 = Label(self,
                             text="",
                             bg=GRAY)
        self.spacer2.grid(row=7, column=0)

        # Button to calculate the conversion
        self.button_calculate = Button(self,
                                       width=24,
                                       height=2,
                                       fg=BLACK,
                                       bg=BLUE,
                                       text="Calculate",
                                       font=SUB_HEADINGS,
                                       command=self.calculate,
                                       borderwidth=1,
                                       relief=SOLID
                                       )
        self.button_calculate.grid(row=8, column=0,
                                   sticky="E")
        # Instructions and the label for the instructions
        instructions = "Make sure when choosing currencies that the currencies " \
                       "aren't highlighted in blue when selected." \
                       " You can do this by clicking again on the box when you select a currency.\n\n" \
                       "1. Input the amount first\n" \
                       "2. Select currencies\n" \
                       "3. Calculate!"
        self.instructions_label8 = Label(self,
                                         text=instructions,
                                         font=("Helvetica", 10, "bold"),
                                         wraplength=400,
                                         justify=LEFT,
                                         bg=GRAY)
        self.instructions_label8.grid(column=1, row=0,
                                      rowspan=3)

        # Label for showing where the exchange rate will appear
        exchange_rate_mssg = "Exchange rate will appear below!"
        self.exchange_rate_below_label9 = Label(self,
                                                text=exchange_rate_mssg,
                                                font=("Helvetica", 10, "bold"),
                                                bg=GRAY)
        self.exchange_rate_below_label9.grid(column=1, row=3,
                                             sticky=S)

        # Label for the exchange rate
        self.exchange_rate_label10 = Label(self,
                                           text="",
                                           font=("Helvetica", 20, "bold"),
                                           relief=SOLID,
                                           height=4,
                                           width=24
                                           )
        self.exchange_rate_label10.grid(column=1, row=4,
                                        rowspan=8, padx=11)

        self.mainloop()

    def update_exchange_rate(self):
    # This is the method to update the exchange rate constantly when the user selected currencies
        try:
            # If the both currencies are strings
            if self.from_currency.get().isalpha() and self.to_currency.get().isalpha():
                # Calls the self.validate_currencies method and validate currencies
                if self.validate_currencies():
                    # Calls the self.conversion_to_usd method to convert 1 amount of the from_currency to USD
                    value = self.conversion_to_usd(1)
                    self.exchange_rate_label10.config(text=f"1 {self.from_currency.get()} = {value * DATA['conversion_rates'][self.to_currency.get()]:.4f} {self.to_currency.get()}")
            # If one or both currencies are not strings, clear the exchange rate
            else:
                self.exchange_rate_label10.config(text="")
        except KeyError:
            pass

    def validate_currencies(self):
    # This purpose of this method is to validate if both of the currencies are valid    
            if self.from_currency.get().upper() in self.currencies and self.to_currency.get().upper() in self.currencies:
                return True

    def calculate(self):
    # This method calculates the conversion of the USD conversion of the from_currency to the to_currency,
    # both selected by the user        
        try:
            validate_currency = self.validate_currencies()
            validate_amount = self.validate_amount()
            from_currency_to_usd = self.conversion_to_usd(float(self.amount_num.get()))
            # if the amount is validated (which is done by calling the self.validate_amount method)
            if validate_amount:
                # If the currencies are both valid, change the label for the amount converted to the converted amount and clear the error label box
                if validate_currency:
                    self.converted_value = from_currency_to_usd * DATA["conversion_rates"][self.to_currency.get().upper()]
                    self.error_lbl5.config(text="")
                    self.amount_converted_lbl7.config(text=f"{self.converted_value:.2f}")
                # If one or both of the currencies are invalid, clear the label for the amount converted and display an error message
                else:
                    self.error_lbl5.config(text="Both currencies must be valid")
                    self.amount_converted_lbl7.config(text="")
        # If the user inputs a non-integer in the entry box for the amount, don't display an error message on the terminal
        except ValueError:
            pass

    def conversion_to_usd(self, amount):
    # This method returns the value when the amount of from_currency selected by the user is converted to USD
        # If the program can successfully calculate the conversion, return the value
        try:
            return amount / DATA["conversion_rates"][self.from_currency.get().upper()]
        # If the program cannot do the calculation because of unlike data types or the currency is not valid, return False
        except KeyError or ValueError:
            return False

    def validate_amount(self):
    # This method validates the amount inputted by the user on the entry box for the amount to be converted    
        try:
            amount = float(self.amount_num.get())
            if amount > MAX_AMOUNT:  # If the amount is greater than the MAX_AMOUNT of money that could be converted
                self.amount_converted_lbl7.config(text="")  # Clear the Label for the amount converted
                self.error_lbl5.config(text=f"Amount must be equal to or below {MAX_AMOUNT}")  # Print error message
            elif amount <= 0:  # If the amount is less than or equal to 0
                self.amount_converted_lbl7.config(text="")  # Clear the Label for the amount converted
                self.error_lbl5.config(text="Amount must be greater than 0")  # Print error message
            else:  # If amount is valid
                return True
        except ValueError:  # If user inputted a value that's invalid (letters, spaces, special characters)
            self.error_lbl5.config(text="Amount must be digits, no commas (,)")  # Print error message
            self.amount_converted_lbl7.config(text="")  # Clear Label for amount converted

    # This method is for auto-capitalising the currencies
    @staticmethod
    def capitalize_currency(var):
        var.set(var.get().upper())

    # This static method are just for the autocomplete capability of my two Combo-boxes
    @staticmethod
    def __validate_combo_input(action, text) -> bool:
    # This method is responsible for limiting the input of the user in the comboboxes to three, because all currency codes only have three letters
        if int(action) == 1:
            return text.isalpha() and len(text) <= 3
        else:
            return True

    def __update_combo(self, event):
    # This method is responsible for changing the value of the comboboxes when the user presses a key and the user presses backspace.
        if event.char.isalpha() or event.keysym == 'BackSpace':
            self.from_currency_combo1.configure(values=[i for i in self.currencies if
                                                i.startswith(self.from_currency_combo1.get().upper())])
            self.to_currency_combo2.configure(values=[i for i in self.currencies if
                                              i.startswith(self.to_currency_combo2.get().upper())])

# Main Program


Forex()
