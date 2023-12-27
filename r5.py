from tkinter import Tk, Label, Button, Frame, messagebox, Entry
from datetime import datetime, time, timedelta

class Subject:
    def __init__(self, name):
        self.name = name
        self.attendance = False


class AttendanceManager:
    # Class to manage attendance data
    attendance_data = {}

    @classmethod
    def add_attendance(cls, day, data):
        if day not in cls.attendance_data:
            cls.attendance_data[day] = []
        cls.attendance_data[day].append(data)


class StudentAttendanceApp:
    def __init__(self, master, display_gui = True):
        self.master = master
        self.current_username = None  # Variable to store the currently logged-in username

        if self.master:
            self.master.title("Student Attendance System")
            self.master.geometry("700x400")
            self.master.configure(bg="#fff")
        # Common starting time for all subjects
        # self.common_start_time = time(9, 0)
        # Interval for each subject (30 minutes)
        self.subject_interval = timedelta(minutes=1)
        # Timetable
        self.timetable = {
            'Monday':    [Subject('FLA'), Subject('JAVA'), Subject('SE'), Subject('MP'), Subject('CN'), Subject('ADA')],
            'Tuesday':   [Subject('JAVA'), Subject('ADA'), Subject('FLA'), Subject('SE'), Subject('MP'), Subject('CN')],
            'Wednesday': [Subject('SE'), Subject('FLA'), Subject('ADA'), Subject('JAVA'), Subject('MP'), Subject('CN')],
            'Thursday':  [Subject('MP'), Subject('FLA'), Subject('JAVA'), Subject('SE'), Subject('ADA'), Subject('CN')],
            'Friday':    [Subject('ADA'), Subject('CN'), Subject('FLA'), Subject('JAVA'), Subject('SE'), Subject('MP')]
        }

        # Time ranges
        # self.time_ranges = {
        #     'FLA': (0, 30),  # Generic time range in minutes
        #     'JAVA': (30, 60),
        #     'SE': (60, 90),
        #     'MP': (90, 120),
        #     'CN': (120, 150),
        #     'ADA': (150, 180)
        # }

        # GUI setup
        if display_gui:
            self.setup_gui()
        self.current_day_index = 0
        self.current_subject_index = 0
        self.next_button_scheduled = False

    def setup_gui(self):
        max_day_name_length = max(len(day) for day in self.timetable.keys())
        current_day = self.get_current_day()

        for day, subjects in self.timetable.items():
            frame = Frame(self.master, bg="#fff")
            frame.pack(pady=10)

            Label(frame, text=day, font=('Calibri', 14, 'bold'), bg="#fff", width=max_day_name_length + 2).grid(row=0, column=0, padx=10)

            for col, subject in enumerate(subjects, start=1):
                button = Button(frame, text=subject.name, width=10, height=2,
                                command=lambda d=day, s=subject: self.open_next_button(d, s),
                                state='normal' if day == current_day else 'disabled')
                button.grid(row=0, column=col, padx=10)

    def get_current_day(self):
        # Use the datetime module to get the current day
        return datetime.now().strftime('%A')

    # Modify the open_next_button method
    def open_next_button(self, day, subject):
        # Create a new top-level window for entering name and roll number
        entry_window = Tk()
        entry_window.title("Enter Name and Roll Number")

        # Labels and Entries for name and roll number
        name_label = Label(entry_window, text="Enter Your Name:")
        name_label.pack(pady=10)
        name_entry = Entry(entry_window)
        name_entry.pack(pady=10)

        roll_number_label = Label(entry_window, text="Enter Roll Number:")
        roll_number_label.pack(pady=10)
        roll_number_entry = Entry(entry_window)
        roll_number_entry.pack(pady=10)

        # Submit button callback function
        def submit_info():
            name = name_entry.get()
            roll_number = roll_number_entry.get()
            entry_window.destroy()  # Close the entry window

            # Now you can use the name and roll_number variables as needed
            self.process_attendance_submission(day, subject, name, roll_number)

        # Submit button
        submit_button = Button(entry_window, text="Submit", command=submit_info)
        submit_button.pack(pady=10)


    def process_attendance_submission(self, day, subject, name, roll_number):
        # Check if the entered name matches the currently logged-in username
        if name != self.current_username:
            messagebox.showerror("Invalid Name", "Entered name does not match the currently logged-in username.")
            return

        current_time = datetime.now().time()

        # Store the attendance data using the class variable
        # if day not in StudentAttendanceApp.attendance_data:
        #     StudentAttendanceApp.attendance_data[day] = []

        AttendanceManager.add_attendance(day, {'Name': name, 'Roll Number': roll_number, 'Subject': subject.name})

        self.current_username = name  # Add this line

        # Calculate the end time based on the subject's interval
        end_time = datetime.combine(datetime.today(), time(23, 59, 59))  # Set end time to the last second of the day

        if not subject.attendance:
            subject.attendance = True
            messagebox.showinfo("Attendance", f"Attendance Submitted for {subject.name} on {day}.\nRoll Number: {roll_number}")
            self.disable_button(day, subject)
            if not self.next_button_scheduled:
                self.next_button_scheduled = True
                self.master.after(int(self.subject_interval.total_seconds() * 1000), lambda: self.open_next_subject_or_day(day))
        else:
            messagebox.showerror("Attendance", f"Attendance for {subject.name} on {day} is already submitted.")


    def disable_button(self, day, subject):
        for child in self.master.winfo_children():
            if isinstance(child, Frame):
                for button in child.winfo_children():
                    if isinstance(button, Button) and button.cget("text") == subject.name:
                        button.config(state='disabled')


    def open_next_day(self):
        self.current_day_index += 1

        if self.current_day_index < len(self.timetable):
            self.open_button(list(self.timetable.keys())[self.current_day_index], self.timetable[list(self.timetable.keys())[self.current_day_index]][self.current_subject_index])
        else:
            # End of timetable
            messagebox.showinfo("Attendance", "Attendance for all subjects has been submitted.")

    def open_button(self, day, subject):
        for child in self.master.winfo_children():
            if isinstance(child, Frame):
                for button in child.winfo_children():
                    if isinstance(button, Button) and button.cget("text") == subject.name:
                        button.invoke()

def run_student_app():
    root = Tk()
    app = StudentAttendanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_student_app()