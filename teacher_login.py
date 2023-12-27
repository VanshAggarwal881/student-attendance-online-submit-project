from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from r5 import StudentAttendanceApp, AttendanceManager


class TeacherWindow:
    def __init__(self):
        self.img = None

    def display_attendance_data(self, app):
        display_window = Toplevel()
        display_window.title("Attendance Data")

        tree = ttk.Treeview(display_window)
        tree["columns"] = ("Name", "Roll Number", "Subject", "Day")
        tree.heading("Name", text="Name")
        tree.heading("Roll Number", text="Roll Number")
        tree.heading("Subject", text="Subject")
        tree.heading("Day", text="Day")

        for day, data in AttendanceManager.attendance_data.items():
            for entry in data:
                tree.insert("", "end", values=(entry['Name'], entry['Roll Number'], entry['Subject'], day))

        tree.pack(expand=True, fill="both")

    def login_window(self):
        root = Tk()
        root.title('Login')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False, False)

        def signin():
            username = user.get()
            password = code.get()

            subjects = ['fla', 'ada', 'mp', 'se', 'java', 'cn']

            if username in subjects and password == 'teacher':
                app = StudentAttendanceApp(root, display_gui=False)  # Create instance when needed
                self.display_attendance_data(app)  # Call the method to display attendance data
                root.iconify()  # Close the login window
            else:
                messagebox.showerror('invalid', 'invalid username or password')

        # self.img = PhotoImage(file='b1_img.png')
        # root.img_lbl = Label(root, image=self.img, bg='white')
        # root.img_lbl.place(x=500, y=70)
        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=300, y=80)

        heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'password')

        code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(frame, width=39, pady=7, text="Sign in", bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,
                                                                                                                  y=204)

        root.mainloop()


if __name__ == "__main__":
    t_obj = TeacherWindow()
    t_obj.login_window()
