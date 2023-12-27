# Importing necessary libraries and modules
from tkinter import *                  # Importing the Tkinter library for GUI
from tkinter import messagebox         # Importing the messagebox module for displaying alerts
import ast                             # Importing the ast module for literal evaluation of strings to Python data structures
from r5 import StudentAttendanceApp    # Importing the StudentAttendanceApp class from the 'r5' module

# Creating the main Tkinter window
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Function to handle the sign-in process
def signin():
     username = user.get()
     password=code.get()

     # Reading user data from datasheet.txt file

     file = open('datasheet.txt','r')
     d = file.read()
     r = ast.literal_eval(d)
     file.close()

     if username in r.keys() and password == r[username]:

        # Set the currently logged-in username and launch the main application
        root = Tk()
        app = StudentAttendanceApp(root)
        app.current_username = username
        root.mainloop()
     else:
         messagebox.showerror('invalid','invalid username or password')

##################################################################################################
'''------------------------------Register code begins----------------------------------------- '''

def signup_command():
    window = Toplevel()
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(True, True)
    img = PhotoImage(file='registerpic.png')

    def signup():
        username = user.get()
        password = code.get()
        confirm_p = confirm_password.get()

        if password == confirm_p:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo("Signup", "Successfully Signed Up")

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both password should match")

    def sign():
        window.destroy()

    Label(window, image=img, border=0, bg='white').place(x=50, y=90)
    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    #####----------------------------------------------
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ###################-------------------------
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ######################---------------------------------------
    def on_enter(e):
        confirm_password.delete(0, 'end')

    def on_leave(e):
        if confirm_password.get() == '':
            confirm_password.insert(0, 'Confirm Password')

    confirm_password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_password.place(x=30, y=220)
    confirm_password.insert(0, 'Confirm Password')
    confirm_password.bind("<FocusIn>", on_enter)
    confirm_password.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    ####################--------------------------------
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
                                                                                                              y=280)
    label = Label(frame, text='I have an account.', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)
    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=193, y=340)
    window.mainloop()

'''-----------------------------Register code ends here---------------------------------------'''
####################################################################################################


img= PhotoImage (file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)
frame=Frame (root, width=350, height=350, bg="white")
frame.place(x=480,y=70)

heading= Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
#########----------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place (x=25, y=107)
###########-------------------------------------
def on_enter(e):
    code.delete (0, 'end')

def on_leave (e):
    name=code.get()
    if name=='':
        code.insert(0, 'password')
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place (x=25, y=177)
##########--------------------------------------
# ... (Similar structure for user, code, and sign_up entry widgets)

Button(frame, width=39, pady=7, text="Sign in",bg='#57a1f8',fg='white', border=0,command=signin).place(x=35,y=204)
lbl = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
lbl.place(x=75,y=270)

sign_up = Button(frame, width=6, text="Sign up",border = 0,bg='white',fg='#57a1f8',cursor='hand2',command=signup_command)
sign_up.place(x=215,y=270)

# Start the Tkinter main loop
root.mainloop()


