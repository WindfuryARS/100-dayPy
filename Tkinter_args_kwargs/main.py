import tkinter

window = tkinter.Tk()

window.title("Hello World")
window.minsize(width=500, height=800)

# label

my_label = tkinter.Label(text="I'm a label", font=("Arial", 20, "bold"))
my_label.pack()


# my_label["text"] = "zhanma"
# my_label.config(text="zhanma")

def button_clicked():
    print("Button clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()
print(input.get())

window.mainloop()
