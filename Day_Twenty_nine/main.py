from tkinter import messagebox
import tkinter
import random
import pyperclip

screen = tkinter.Tk()
screen.title("Create Password")
screen.minsize(350, 110)

def generate_password():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1','2','3','4','5', '6', '7', '8', '9','0']
    symbols = ['!', '@', '$' , '*', '&', '^', '(',')','+','-']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(characters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)

def save_data():
    file = open("D:\Projects\Python\Python_Exercise\Day_Twenty_nine\password.txt", "a")
    website_local = webiste.get()
    email_local = email.get()
    password_local = password_input.get()
    if len(website_local) == 0 or len(password_local) == 0:
        messagebox.showinfo(title="Error", message="fields are empty!!")
    else:
        is_ok =messagebox.askokcancel(title=webiste, message=f"These are the details entered:\n Email:" 
                                    f"{email}\n Password: {password}\n is it ok to save? ")
        if is_ok:
            file.write(f"{email_local} | {website_local} | {password_local}\n")
            webiste.delete(0, 'end')
            password_input.delete(0, 'end')
    file.close()




email_name = tkinter.Label(text="Email: ")
email_name.grid(column=0, row=1)
email = tkinter.Entry(text="email", width=40)
email.grid(column=1, row=1, columnspan=2)
email.insert(0, "amiralipeymanispacelove@gmail.com")


website_name = tkinter.Label(text="Website: ")
website_name.grid(column=0, row=2)
webiste = tkinter.Entry(width=40)
webiste.grid(column=1, row=2, columnspan=2)
webiste.focus()

password = tkinter.Label(text="Password: ")
password.grid(column=0, row=3)
password_input = tkinter.Entry(width=20)
password_input.grid(column=1, row=3)
password_button = tkinter.Button(text="Gnerate pass word", command=generate_password)
password_button.grid(column=2, row=3, columnspan=1)


Add_button = tkinter.Button(text="Add", width=22, command=save_data)
Add_button.grid(column=1, row=4, columnspan=2)
  



screen.mainloop()