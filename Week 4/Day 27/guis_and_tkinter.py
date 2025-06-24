import tkinter

window = tkinter.Tk()
window.title("First tkinter gui")
window.minsize(500, 300)

#Label

label = tkinter.Label(text="I'm a label!", font=("Arial", 24, "italic"))
label.pack(side="left", expand=True)

window.mainloop()