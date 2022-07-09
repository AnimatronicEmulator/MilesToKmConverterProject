import tkinter


def miles_to_km_calc():
    miles = float(val_in_miles.get())
    val_in_km_label["text"] = miles * 1.60934


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=15, pady=15)

val_in_miles = tkinter.Entry(width=13)
val_in_miles.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=3)

equal_label = tkinter.Label(text="is equal to ")
equal_label.grid(row=1, column=0)

val_in_km_label = tkinter.Label(text=0)
val_in_km_label.grid(row=1, column=1)
val_in_km_label.config(padx=13, pady=3)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = tkinter.Button(text="Calculate", command=miles_to_km_calc)
calc_button.grid(row=2, column=1)

tkinter.mainloop()
