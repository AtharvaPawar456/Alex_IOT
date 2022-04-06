from tkinter import *
import os

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text = "Registration Success", fg="green", font=("calibri",11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command=register_user).pack()

def login_verify():

    username1in = (username_verify.get())
    password1 = (password_verify.get())
    username_entry2.delete(0,END)
    password_entry2.delete(0,END)

    username1 = username1in+".txt"
    list_of_files = os.listdir()
    print(list_of_files)
    if username1 in list_of_files:
        with open(username1, 'r') as f:
            data = f.read()
            print(data)
        verify = data.splitlines()
        print(verify)
        if password1 in verify:
            print("login success")
            Label(screen2,text = username1in+" Login Successful", fg="green", font=("calibri",11)).pack()
            import alexMain
        else:
            print("Password has not been recognised")
    else:
        print("User not found !")


def login():
    # print("Login session started")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    global username_entry2
    global password_entry2

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Username * ").pack()
    username_entry2 = Entry(screen2, textvariable= username_verify)
    username_entry2.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry2 = Entry(screen2, textvariable= password_verify)
    password_entry2.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login",width=10,height=1,command=login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Alex(IOT)")
    Label(text = "IOT", bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    Label(text = "").pack()
    Button(text = "Login",height="2",width="30",command=login).pack()
    Label(text = "").pack()
    Button(text = "Register",height="2",width="30",command=register).pack()

    screen.mainloop()

main_screen()