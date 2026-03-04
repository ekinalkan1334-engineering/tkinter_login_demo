import tkinter as tk
from tkinter import messagebox

correct_email= "ekin@gmail.com"
correct_password= "ekin123"

#login start
def login():                  
    email=email_entry.get() 
    password=password_entry.get()


     # Check for empty fields first
    if (not email and not passwoard):
        messagebox.showerror("Error", "Please enter your email and password")

    elif not email:
        messagebox.showerror("Error", "Please enter your email")

    elif not password:
        messagebox.showerror("Error", "Please enter your password")

    else:
        # Check if email and password are correct
        if (email==correct_email and password==correct_password):
             messagebox.showinfo("Success","Login Successful")

        else:
            messagebox.showerror("Error","Email or password is incorrect")

def forgot_password():
    messagebox.showinfo("Info", "Password reset process (demo)")

def continue_as_guest():
    messagebox.showinfo("Info", "Continuing without registration")

#window
window=tk.Tk()
window.title("Sign In")
window.geometry("400x500")
window.configure(bg="#CFD6F3")  #for background color

#for small window
frame = tk.Frame(window, bg="#D1ADE8", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)


#for email
tk.Label(frame, text="Email Address:", bg="#E6D1EB").pack(pady=(30,5))
email_entry = tk.Entry(frame, width=30)
email_entry.pack(pady=5)

#for password
tk.Label(frame, text="Password:", bg="#E6D1EB").pack(pady=5)
password_entry = tk.Entry(frame, width=30, show=".")  #show hides
password_entry.pack(pady=5)

tk.Button(frame, text="Login", width=20, command=login, bg="#ADD8E6").pack(pady=(20,5))
tk.Button(frame, text="Forgot Password", width=20, command=forgot_password, bg="#B0E0E6").pack(pady=5)
tk.Button(frame, text="Continue as Guest", width=20, command=continue_as_guest, bg="#B0E0E6").pack(pady=5)

window.mainloop()  #keep the window open
