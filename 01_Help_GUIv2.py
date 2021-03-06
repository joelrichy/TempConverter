from tkinter import *


class Convertor:
    def __init__(self):

        #formatting variables...
        background_colour = "light blue"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     padx=10, pady=10, bg=background_colour)
        self.converter_frame.grid()

        # Tempurature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", 16, "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", 14),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help :)")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tempurature Convertor")
    something = Convertor()
    root.mainloop()