import tkinter

window = tkinter.Tk()
window.title("STAR WARS")
window.minsize(300, 300)


jesus = tkinter.Label(text="if the world hates you just remember that i has hated me first")
jesus.pack(side="top")

def change_text():
    new_text = taking_input.get()
    jesus.config(text=new_text)


button = tkinter.Button(text="click for next lesson", command=change_text)
button.pack(side="top")

taking_input = tkinter.Entry(width=10)
taking_input.pack()



window.mainloop()









