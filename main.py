from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (
            [choice(letters) for _ in range(randint(8, 10))] +
            [choice(symbols) for _ in range(randint(2, 4))] +
            [choice(numbers) for _ in range(randint(2, 4))]
    )
    shuffle(password_list)
    random_password = "".join([char for char in password_list]) #join allows you to concatenate each character to a hole string
    passwrd_entry.delete(0, END)
    passwrd_entry.insert(0, random_password)
    pyperclip.copy(random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
        web = web_entry.get().title()
        email = email_entry.get()
        passwrd = passwrd_entry.get()
        new_data = {
            web: {
                "email": email,
                "password": passwrd,
            }
        }

        if web == "" or passwrd == "":
            messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        else:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
            except FileNotFoundError:
                 with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            passwrd_entry.delete(0, END)

def find_password():
    try:
        with open("data.json", "r") as data_file:
            password_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
            web = web_entry.get().title()
            if web in password_dict:
                messagebox.showinfo(title=web, message=f"email: {password_dict[web]["email"]}\n" 
                                                       f"password: {password_dict[web]["password"]}")
            else:
                messagebox.showwarning(title="Website Not Found", message="No details for the website exits.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo_img)
canvas.grid(row=1, column=1)

#Labels
website = Label(text="Website:")
website.grid(row=2, column=0)

email_user = Label(text="Email/Username:")
email_user.grid(row=3, column=0)

password = Label(text="Password:")
password.grid(row=4, column=0)

#Entries
web_entry = Entry(width=33)
web_entry.grid(row=2, column=1)
web_entry.focus() #to have the cursor ready for typing

email_entry = Entry(width=52)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(0, "antoni.luna0730@gmail.com")

passwrd_entry = Entry(width=33)
passwrd_entry.grid(row=4, column=1)

#Buttons
add = Button(width=44, text="Add", command=save, highlightthickness=0)
add.grid(row=5, column=1, columnspan=2)

generate_password = Button(text="Generate Password", command=password_generator, highlightthickness=0)
generate_password.grid(row=4, column=2)

search = Button(width=10, text="Search", command=find_password, highlightthickness=0)
search.grid(row=2, column=2)

window.mainloop()