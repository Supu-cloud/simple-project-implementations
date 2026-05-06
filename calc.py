import tkinter

button_values = [
    ["AC", "+/-", "%", "+"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "÷"],
    ["0", ".", "√", "="]
]
right_symbols = ["÷", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) # 5
column_count = len(button_values[0]) # 4

light_blue = "#20bbcf"
dark_green = "#205b7a"
dark_dark_green = "#142f44"
dark_ash = "#1d3849"
black = "#000000"

# window setup
window = tkinter.Tk()
window.title("Suuni Ishara calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background="#000000",
                      foreground="#e9eef0", anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground="#000000", background="#d0d3d9")
        elif value in right_symbols:
            button.config(foreground="#ffffff", background="#d27e10")
        else:
            button.config(foreground="#ffffff", background="#4a4e50")
        
        button.grid(row=row+1, column=column)

frame.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(value):
    value = str(value)
    if value.endswith(".0"):
        return value[:-2]
    return value

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator
    
    # Updated this line to include "√" so the logic below is reachable
    if value in right_symbols or value == "√":
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    if numB != 0:
                        label["text"] = remove_zero_decimal(numA / numB)
                    else:
                        label["text"] = "Error"
                
        elif value in ["+", "-", "x", "÷"]:
            if operator is None:
                A = label["text"]
                operator = value
                label["text"] = "0"
        
        elif value == "√":
            A = label["text"]
            numA = float(A)
            if numA >= 0:
                label["text"] = remove_zero_decimal(numA ** 0.5)
            else:
                label["text"] = "Error"
                
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            label["text"] = str(float(label["text"]) * -1)
            label["text"] = remove_zero_decimal(label["text"])
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(str(result))
            
    elif value == ".":
        if "." not in label["text"]:
             label["text"] += value
             
    elif value in "0123456789":
        if label["text"] == "0":
            label["text"] = value
        else:
            label["text"] += value

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()