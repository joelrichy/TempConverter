from tkinter import *
from functools import partial  # to prevent unwanted additional windows
import random


class Convertor:
    def __init__(self, parent):
        # formatting variables
        background_colour = "light blue"

        # converter frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # tempurature Converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then select "
                                                  "one of the buttons below",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_colour,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3) orchid3 / khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)


        #  Answer Label (row4)
        self.converted_label = Label(self.converter_frame,
                                     text="Conversion goes here",
                                     font="Arial 14 bold",
                                     fg="purple",
                                     bg=background_colour, pady=10)
        self.converted_label.grid(row=4)

        #  History/Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       text="Calculation History",
                                       font="Arial 12 bold",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame,
                                  text="Help", font="Arial 12 bold",
                                  width=5, padx=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, to):
        print(to)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Convertor(root)
    root.mainloop()