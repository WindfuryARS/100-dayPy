import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = tkinter.Label(text="0")
km_result.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

cal_button = tkinter.Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=1, row=2)

window.mainloop()
