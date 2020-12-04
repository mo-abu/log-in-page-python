#Importing tkinter

from tkinter import *
import os

#Creating my sign up screen

def signup():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("500x500")
    screen1.title("Sign up")

    global username
    global password
    global username_entry
    global password_entry
    global door_number_entry
    global street_name_entry
    global postcode_entry
    global country_entry

    username = StringVar()
    username = IntVar()
    password = StringVar()
    password = IntVar()
    door_number = StringVar()
    door_number = IntVar()
    street_name = StringVar()
    street_name = IntVar()
    postcode = StringVar()
    postcode = IntVar()
    country = StringVar()
    country = IntVar()

    Label(screen1, text = "").pack()
    Label(screen1, text = "Please enter details below to sign up").pack()
    Label(screen1, text = "").pack()
    
    Label(screen1, text = "Username", bg = "light blue").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password", bg = "light blue").pack()
    password_entry = Entry(screen1, textvariable = password, show='*')
    password_entry.pack()
    
    Label(screen1, text = "").pack()
    Label(screen1, text = "Please enter your address").pack()
    Label(screen1, text = "").pack()

    Label(screen1, text = "Door Number", bg = "light blue").pack()
    door_number_entry = Entry(screen1, textvariable = door_number)
    door_number_entry.pack()
    Label(screen1, text = "Street Name", bg = "light blue").pack()
    street_name_entry = Entry(screen1, textvariable = street_name)
    street_name_entry.pack()
    Label(screen1, text = "Postcode", bg = "light blue").pack()
    postcode_entry = Entry(screen1, textvariable = postcode)
    postcode_entry.pack()
    Label(screen1, text = "Country", bg = "light blue").pack()
    country_entry = Entry(screen1, textvariable = country)
    country_entry.pack()
    
    Label(screen1, text = "").pack()
    Label(screen1, text = "Click sign up to complete registration").pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Sign up", width = "10", height = "1", command = sign_user).pack()

#Creating my login screen

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("500x500")
    screen2.title("Login")

    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
        
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
        
    Label(screen2, text = "Username", bg = "light blue").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password", bg = "light blue").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = "10", height = "1", command = login_verify).pack()

#Creating a successful login in screen

def delete3():
    screen3.destroy()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("200x100")
    Label(screen3, text = "Login success").pack()
    Button(screen3,text = "OK", command = delete3).pack()

#Creating a unsuccessful login in screen
        
def delete4():
    screen4.destroy()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Unuccessful login attempt")
    screen4.geometry("200x100")
    Label(screen4,text = "Password not recognised").pack()
    Button(screen4,text = "OK", command = delete4).pack()

#Creating a unsuccessful login in screen
        
def delete5():
    screen5.destroy()
        
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Unuccessful login attempt")
    screen5.geometry("200x100")
    Label(screen5,text = "Username not found").pack()
    Button(screen5,text = "OK", command = delete5).pack()

#Creating a file which stores a single users data and then deleting input after successful sign up

def sign_user():
    username_info = username.get()
    password_info = password.get()
    door_number_entry_info = door_number_entry.get()
    street_name_entry_info = street_name_entry.get()
    postcode_entry_info = street_name_entry.get()
    country_entry_info = street_name_entry.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.write(door_number_entry_info+"\n")
    file.write(street_name_entry+"\n")
    file.write(postcode_entry_info+"\n")
    file.write(country_entry_info+"\n")

    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    door_number_entry.delete(0, END)
    street_name_entry.delete(0, END)
    postcode_entry.delete(0, END)
    country_entry.delete(0, END)

    Label(screen1, text = "Sign up successful", fg = "green", font = ("Calibri", 15)).pack()

#Creating a user verifier which checks if the username and password is correct or incorrect

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
        
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

#Creating the main login/sign up in screen

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Login Page")
    Label(text = "Login Page", bg = "light blue", width = "200", font = ("Calibri", 15)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "50", height = "2", bg = "light blue", command = login).pack()
    Label(text = "").pack()
    Button(text = "Sign up", width = "50", height = "2", bg = "light blue", command = signup).pack()

    screen.mainloop()

main_screen()
