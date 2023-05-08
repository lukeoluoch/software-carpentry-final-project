import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import homepage


global current_user

def create_login_window():

    # create the login window
    login_window = tk.Tk()
    login_window.geometry('800x600')
    login_window.title("Login")
    
    img = ImageTk.PhotoImage(Image.open("images/login.jpg"))  
    l=tk.Label(image=img)
    l.place(x=0,y=0)
    
    login_frame = tk.Frame(login_window)
    login_frame.place(relx=0.5, rely=0.5, anchor='center')
    

    # create the username and password Entry widgets, login/new account buttons
    welcome_label = tk.Label(login_frame, text="Get In-Saiyan-ly Fit")
    username_label = tk.Label(login_frame, text="Username:")
    username_entry = tk.Entry(login_frame)
    password_label = tk.Label(login_frame, text="Password:")
    password_entry = tk.Entry(login_frame, show="*")
    login_button = tk.Button(login_frame, text="Login")
    new_account_button = tk.Button(login_frame, text="Create New Account")

    # add the widgets to the window
    welcome_label.grid(column=2)
    username_label.grid(row=1,column=1)
    username_entry.grid(row=1,column=2)
    password_label.grid(row=2,column=1)
    password_entry.grid(row=2,column=2)
    login_button.grid(row=3,column=1)
    new_account_button.grid(row=3,column=2)

    login_frame.grid_rowconfigure(0, weight=1)
    login_frame.grid_rowconfigure(4, weight=1)
    login_frame.grid_columnconfigure(0, weight=1)
    login_frame.grid_columnconfigure(3, weight=1)

    # define a function to handle logging in
    def login():
        # get the username and password input from the user
        username = username_entry.get()
        password = password_entry.get()

        # check if the user has an account
        user_file = f"user_files/{username}.txt"
        try:
            with open(user_file) as f:
                # if the file exists, check if the password is correct
                saved_password = f.readline().strip('\n')
                if password == saved_password:
                    # if the password is correct, show the main window
                    
                    global current_user
                    current_user = username
                    
                    login_window.destroy()                    
                    homepage.create_homepage(username)
                    
                    print(username)

                else:
                    # if the password is incorrect, show an error message
                    messagebox.showerror("Error", "Incorrect password")
        except FileNotFoundError:
            # if the file doesn't exist, show an error message
            messagebox.showerror("Error", "Username not found")

    # define a function to handle creating a new account
    def create_account():
        # get the username and password input from the user
        username = username_entry.get()
        password = password_entry.get()

        # create a new file for the user
        user_file = f"user_files/{username}.txt"
        with open(user_file, "w") as f:
            f.write(password)

        # show a message confirming the account was created
        messagebox.showinfo("Success", "Account created successfully")

    # bind the login and create account functions to the buttons
    login_button.config(command=login)
    new_account_button.config(command=create_account)

    # start the event loop
    login_window.mainloop()
    
    return current_user

if __name__ == "__main__":
    create_login_window()