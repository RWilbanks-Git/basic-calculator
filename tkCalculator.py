
from tkinter import *
import tkinter as tk
import math

window = Tk()
window.title("Calculator")
window.geometry("250x350")
window.resizable(False, False)

x = None
y = None
operator = None
complete = False


def button_click(number):
#    global complete, count
    current = lbl_value["text"]

    # If the calculation is complete, reset the display for the next number
    if current == "0" or current == "0.":
        lbl_value["text"] = str(number)
    else:
        # If it's a decimal, check if there's already one in the number
        if number == ".":
            if "." not in current:
                lbl_value["text"] = current + str(number)
        else:
            lbl_value["text"] = current + str(number)


def set_operator(op):
    global x, operator
    x = float(lbl_value["text"])
    operator = op
    lbl_value["text"] = ""


def clear():
    global x, y, operator
    lbl_value["text"] = "0"
    x = None
    y = None
    operator = None
    complete = False


def calculation():
    global x, y, operator, complete
    y = float(lbl_value["text"])
    result = y

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "x":
        result = x * y
    elif operator == "/":
        if y == 0:
            result = "Error"
        else:
            result = x/y

    lbl_value["text"] = "{:.6f}".format(result) if isinstance(result, float) else str(result)
    x = result
    complete = True


def sroot():
    global x
    x = float(lbl_value["text"])
    result = math.sqrt(x)
    lbl_value["text"] = str(result)
    complete = True


def square():
    try:
        value = float(lbl_value["text"])
        result = value ** 2
        lbl_value["text"] = "{:.6f}".format(result)
    except ValueError:
        lbl_value["text"] = "Error"

    complete = True




# display label
lbl_value = tk.Label(master=window, text="0", width=16, height=2, anchor="e", font=("Arial", 16), relief = "sunken")
lbl_value.grid(row=0, column=0, columnspan=4, pady = 10)

# number buttons
btn_7 = tk.Button(master=window, text="7", command=lambda: button_click(7), width=5, height=2)
btn_7.grid(row=2, column=0, padx = 5, pady = 5, sticky = "nsew")

btn_8 = tk.Button(master=window, text="8", command=lambda: button_click(8), width=5, height=2)
btn_8.grid(row=2, column=1, padx = 5, pady = 5, sticky = "nsew")

btn_9 = tk.Button(master=window, text="9", command=lambda: button_click(9), width=5, height=2)
btn_9.grid(row=2, column=2, padx = 5, pady = 5, sticky = "nsew")

btn_4 = tk.Button(master=window, text="4", command=lambda: button_click(4), width=5, height=2)
btn_4.grid(row=3, column=0, padx = 5, pady = 5, sticky = "nsew")

btn_5 = tk.Button(master=window, text="5", command=lambda: button_click(5), width=5, height=2)
btn_5.grid(row=3, column=1, padx = 5, pady = 5, sticky = "nsew")

btn_6 = tk.Button(master=window, text="6", command=lambda: button_click(6), width=5, height=2)
btn_6.grid(row=3, column=2, padx = 5, pady = 5, sticky = "nsew")

btn_1 = tk.Button(master=window, text="1", command=lambda: button_click(1), width=5, height=2)
btn_1.grid(row=4, column=0, padx = 5, pady = 5, sticky = "nsew")

btn_2 = tk.Button(master=window, text="2", command=lambda: button_click(2), width=5, height=2)
btn_2.grid(row=4, column=1, padx = 5, pady = 5, sticky = "nsew")

btn_3 = tk.Button(master=window, text="3", command=lambda: button_click(3), width=5, height=2)
btn_3.grid(row=4, column=2, padx = 5, pady = 5, sticky = "nsew")

btn_0 = tk.Button(master=window, text="0", command=lambda: button_click(0), width=5, height=2)
btn_0.grid(row=5, column=0, padx = 5, pady = 5, sticky = "nsew")



#Non-Number buttons

btn_off = tk.Button(master=window, text="OFF", command=window.quit, width=5, height=2)
btn_off.grid(row=1, column=0, padx = 5, pady = 5, sticky = "nsew")

btn_clear = tk.Button(master=window, text="CE", command=clear, width=5, height=2)
btn_clear.grid(row=1, column=1, padx = 5, pady = 5, sticky = "nsew")

btn_root = tk.Button(master=window, text="√x", command=sroot, width=5, height=2)
btn_root.grid(row=1, column=2, padx = 5, pady = 5, sticky = "nsew")

btn_square = tk.Button(master=window, text="x²", command=square, width=5, height=2)
btn_square.grid(row=1, column=3, padx = 5, pady = 5, sticky = "nsew")

btn_divide = tk.Button(master=window, text="/", command=lambda: set_operator("/"), width=5, height=2)
btn_divide.grid(row=2, column=3, padx = 5, pady = 5, sticky = "nsew")

btn_mult = tk.Button(master=window, text="x", command=lambda: set_operator("x"), width=5, height=2)
btn_mult.grid(row=3, column=3, padx = 5, pady = 5, sticky = "nsew")

btn_sub = tk.Button(master=window, text="-", command=lambda: set_operator("-"), width=5, height=2)
btn_sub.grid(row=4, column=3, padx = 5, pady = 5, sticky = "nsew")

btn_point = tk.Button(master=window, text=".", command=lambda: button_click("."), width=5, height=2)
btn_point.grid(row=5, column=1, padx = 5, pady = 5, sticky = "nsew")

btn_equal = tk.Button(master=window, text="=", command=calculation, width=5, height=2)
btn_equal.grid(row=5, column=2, padx = 5, pady = 5, sticky = "nsew")

btn_add = tk.Button(master=window, text="+", command=lambda: set_operator('+'), width=5, height=2)
btn_add.grid(row=5, column=3, padx = 5, pady = 5, sticky = "nsew")

window.mainloop()
