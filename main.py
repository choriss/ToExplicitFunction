import ctypes
import tkinter

import easylatex2image
from easylatex2image import latex_to_image
import latex2sympy2
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy

import imgpopup

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

tex_preamble = r"""\usepackage[parfill]{parskip}
\usepackage[german]{varioref}
\usepackage{url}
\usepackage{amsmath} 
\usepackage{dcolumn}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows}
\usetikzlibrary{intersections}
\usepackage[all,cmtip]{xy}
"""

def solve():
    eqs = entry_eq.get().split(",")
    target_letters = target_entry.get().split(",")
    if target_letters != "":
        # latex -> sympy
        eqs_sympy = list(map(latex2sympy2.latex2sympy,eqs))
        # print(eqs)
        # for i in range(len(eqs)):
        #     print(eqs[i])
        #     eqs_sympy[i] = str(latex2sympy2.latex2sympy(eqs[i]))

        print(eqs_sympy)

        print(target_letters)
        solved_answer = sympy.solve(eqs_sympy,target_letters)
        answer_display.delete(0, tkinter.END)
        answer_display.insert(tkinter.END,sympy.latex(solved_answer))
        ans_graph()


def graph():
    # Get the Entry Input

    if entry_eq.get() != "":
        try:
            tmptext = entry_eq.get() 
            tmptext = "$"+tmptext+"$"
            # Clear any previous Syntax from the figure
            wx_eq.clear()
            wx_eq.text(-0.15, 0.4, tmptext, fontsize = 15)
            canvas_eq.draw()
            # print(entry_eq.get())

        except:
            wx_eq.clear()
        finally:
            canvas_eq.draw()
    else:
        wx_eq.clear()
        canvas_eq.draw()
    display.after(50,graph)

def ans_graph():
    if answer_display.get() != "":
        try:
            tmptext = answer_display.get() 
            tmptext = "$"+tmptext+"$"
            # Clear any previous Syntax from the figure
            wx_ans.clear()
            wx_ans.text(-0.15, 0.4, tmptext, fontsize = 15)
            canvas_ans.draw()
            # print(entry_ans.get())

        except:
            pass
        finally:
            canvas_ans.draw()
    else:
        wx_ans.clear()
        canvas_ans.draw()

def eq_tex2img():
    pillow_image = latex_to_image(tex_preamble,"$"+entry_eq.get() +"$","output.png",dpi=500,img_type="PNG")
    imgpopup.open_image_window("output.png")

def ans_tex2img():
    pillow_image = latex_to_image(tex_preamble,"$"+answer_display.get()+"$" ,"output.png",dpi=500,img_type="PNG")
    imgpopup.open_image_window("output.png")

display = tkinter.Tk()


entry_eq_label = tkinter.Label(text="equation here: 0=")
entry_eq_label.grid(row=1,column=1)

entry_eq = tkinter.Entry()
entry_eq.grid(row=1,column=2)

img_btn_eq = tkinter.Button(text="img",command=eq_tex2img)
img_btn_eq.grid(row=1,column=4)


target_label = tkinter.Label(text="target")
target_label.grid(row=2,column=1)

target_entry = tkinter.Entry()
target_entry.grid(row=2,column=2)

answer_label = tkinter.Label(text="Answer")
answer_label.grid(row=3,column=1)

answer_display = tkinter.Entry()
answer_display.grid(row=3,column=2)

img_btn_ans = tkinter.Button(text="img",command=ans_tex2img)
img_btn_ans.grid(row=3,column=4)

answer_btn = tkinter.Button(text="Solve!",command=solve)
answer_btn.grid(row=4,column=1)


# 数式の描画
# equation
# Create a Frame object
frame_eq = tkinter.Frame(display)
frame_eq.grid(row=1,column=3)

# Add a label widget in the frame
label_eq = tkinter.Label(frame_eq)
label_eq.grid(row=1,column=3)

# Define the figure size and plot the figure
fig_eq = matplotlib.figure.Figure(figsize=(7, 0.7), dpi=100)
wx_eq = fig_eq.add_subplot(111)
canvas_eq = FigureCanvasTkAgg(fig_eq, master=label_eq)
canvas_eq.get_tk_widget().grid(row=1,column=3)
canvas_eq._tkcanvas.grid(row=1,column=3)

# Set the visibility of the Canvas figure
wx_eq.get_xaxis().set_visible(False)
wx_eq.get_yaxis().set_visible(False)
wx_eq.spines['right'].set_visible(False)
wx_eq.spines['left'].set_visible(False)
wx_eq.spines['top'].set_visible(False)
wx_eq.spines['bottom'].set_visible(False)

#answer
# Create a Frame object
frame_ans = tkinter.Frame(display)
frame_ans.grid(row=3,column=3)

# Add a label widget in the frame
label_ans = tkinter.Label(frame_ans)
label_ans.grid(row=3,column=3)

# Define the figure size and plot the figure
fig_ans = matplotlib.figure.Figure(figsize=(7, 0.7), dpi=100)
wx_ans = fig_ans.add_subplot(111)
canvas_ans = FigureCanvasTkAgg(fig_ans, master=label_ans)
canvas_ans.get_tk_widget().grid(row=3,column=3)
canvas_ans._tkcanvas.grid(row=3,column=3)

# Set the visibility of the Canvas figure
wx_ans.get_xaxis().set_visible(False)
wx_ans.get_yaxis().set_visible(False)
wx_ans.spines['right'].set_visible(False)
wx_ans.spines['left'].set_visible(False)
wx_ans.spines['top'].set_visible(False)
wx_ans.spines['bottom'].set_visible(False)

graph()
display.mainloop()