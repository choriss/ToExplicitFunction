# Import required libraries
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import threading

# Use TkAgg in the backend of tkinter application
matplotlib.use('TkAgg')

# Create an instance of tkinter frame
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Set the title of the window
win.title("LaTex Viewer")

# Define a function to get the figure output
def graph():
    # Get the Entry Input

    if entry.get() != "":
        try:
            tmptext = entry.get() 
            tmptext = "$"+tmptext+"$"
            # Clear any previous Syntax from the figure
            wx.clear()
            wx.text(-0.15, 0.4, tmptext, fontsize = 15)
            canvas.draw()
            print(entry.get())
        except:
            pass
        finally:
            canvas.draw()
    else:
        wx.clear()
        canvas.draw()
    win.after(50,graph)

# Create a Frame object
frame = Frame(win)
frame.grid(row=1,column=1)
# Create an Entry widget
var = StringVar()
entry = Entry(frame, width=70, textvariable=var)
entry.grid(row=2,column=1)

# Add a label widget in the frame
label = Label(frame)
label.grid(row=3,column=1)

# Define the figure size and plot the figure
fig = matplotlib.figure.Figure(figsize=(7, 0.7), dpi=100)
wx = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().grid(row=4,column=1)
canvas._tkcanvas.grid(row=4,column=1)

# Set the visibility of the Canvas figure
wx.get_xaxis().set_visible(False)
wx.get_yaxis().set_visible(False)
wx.spines['right'].set_visible(False)
wx.spines['left'].set_visible(False)
wx.spines['top'].set_visible(False)
wx.spines['bottom'].set_visible(False)

# Add Scrollbars
vscrollbar = Scrollbar(frame, orient=VERTICAL)
vscrollbar.grid(row=4, column=2, sticky=N+S)
vscrollbar.config(command=canvas.get_tk_widget().yview)

hscrollbar = Scrollbar(frame, orient=HORIZONTAL)
hscrollbar.grid(row=5, column=1, sticky=E+W)
hscrollbar.config(command=canvas.get_tk_widget().xview)



graph()
win.mainloop()