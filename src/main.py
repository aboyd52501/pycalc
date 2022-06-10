from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator 🧮")


current_number_string = ""
current_number_string_var = StringVar()
current_operator = None

secondary_expression = ""

def press_key(num):
    def return_function():
        global current_number_string
        current_number_string = current_number_string + str(num)
        global current_number_string_var
        current_number_string_var.set(current_number_string)

    return return_function


ROOT_HEIGHT = 400
ROOT_WIDTH = 250

root.geometry(f"{ROOT_HEIGHT}x{ROOT_WIDTH}")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid()

# Create rows
screen_row = ttk.Frame(mainframe)
screen_row.pack(side=TOP)

display = ttk.Label(screen_row, textvariable=current_number_string_var, font=("Helvetica", 20))
display.pack(side=RIGHT, fill=X, expand=True)

first_row = ttk.Frame(mainframe)
first_row.pack(side=TOP)

second_row = ttk.Frame(mainframe)
second_row.pack(side=TOP)

third_row = ttk.Frame(mainframe)
third_row.pack(side=TOP)

fourth_row = ttk.Frame(mainframe)
fourth_row.pack(side=TOP)

fifth_row = ttk.Frame(mainframe)
fifth_row.pack(side=TOP)

# Create the buttons

# Number buttons
sign_button = ttk.Button(fifth_row, text="+/-", command=press_key('!'))
sign_button.pack(side=LEFT)

zero_button = ttk.Button(fifth_row, text='0', command=press_key(0))
zero_button.pack(side=LEFT)

decimal_button = ttk.Button(fifth_row, text='.', command=press_key('.'))
decimal_button.pack(side=LEFT)

def create_number_button(num):
    rows = [first_row, second_row, third_row, fourth_row, fifth_row]
    this_row = rows[3 - ((num-1) // 3)]
    return ttk.Button(this_row, text=str(num), command=press_key(num)).pack(side=LEFT)

for i in range(1, 9+1):
    create_number_button(i)

# Enter button
enter_button = ttk.Button(fifth_row, text="Enter", command = lambda: print(current_number_string))
enter_button.pack(side=RIGHT)


# Function buttons

plus_button = ttk.Button(fourth_row, text="+", command=press_key('+'))
plus_button.pack(side=LEFT)

minus_button = ttk.Button(third_row, text='-', command=press_key('-'))
minus_button.pack(side=LEFT)

times_button = ttk.Button(second_row, text='x', command=press_key('*'))
times_button.pack(side=LEFT)

divide_button = ttk.Button(first_row, text='/', command=press_key('/'))
divide_button.pack(side=RIGHT)

ce_button = ttk.Button(first_row, text='CE', command=press_key('CE'))
ce_button.pack(side=LEFT)

c_button = ttk.Button(first_row, text='C', command=press_key('C'))
c_button.pack(side=LEFT)

back_button = ttk.Button(first_row, text='<-', command=press_key('<'))
back_button.pack(side=LEFT)



root.mainloop()