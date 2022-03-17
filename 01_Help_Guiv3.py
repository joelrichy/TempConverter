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


class Help:
    def __init__(self):
        background = "orange"

        # set up child window (ie help box)
        self.help_box = Toplevel()

        # set up Gui Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font=("Arial", 24, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="Ariel 10 bold",
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tempurature Convertor")
    something = Convertor()
    root.mainloop()