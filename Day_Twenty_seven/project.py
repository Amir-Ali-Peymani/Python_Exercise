import tkinter

def miles_to_km():
    miles = float(milest_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

screen = tkinter.Tk()
screen.title("Converter")
screen.config(padx=20, pady=20)

milest_input = tkinter.Entry(width=11)
milest_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
screen.mainloop()