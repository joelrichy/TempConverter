from tkinter import *
import random


class Convertor:
    def __init__(self):
        print("Hello world")

        #formatting variables...
        background_colour = "light blue"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_colour)
        self.converter_frame.grid()

        # Tempurature Conversion Heading (row 0)
        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Arial", 16, "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tempurature Convertor")
    something = Convertor()
    root.mainloop()