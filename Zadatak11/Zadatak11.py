from tkinter import *
from datetime import *

class BirthYear:
    def __init__(self, master):
        self.master = master
        self.master.title('Age calculator')
        self.master.geometry('250x180')

        self.entry_label_birth_date = Label(self.master, text='Birth date')
        self.entry_label_birth_date.grid(row=0, column=1)

        self.entry_label_day = Label(self.master, text='Day: ')
        self.entry_label_day.grid(row=1, column=0)

        self.entry_day = Entry(self.master)
        self.entry_day.grid(row=1, column=1)

        self.entry_label_month = Label(self.master, text='Month: ')
        self.entry_label_month.grid(row=2, column=0)

        self.entry_month = Entry(self.master)
        self.entry_month.grid(row=2, column=1)

        self.entry_label_year = Label(self.master, text='Year: ')
        self.entry_label_year.grid(row=3, column=0)

        self.entry_year = Entry(self.master)
        self.entry_year.grid(row=3, column=1)

        self.button = Button(self.master, text='Calculate Age', command=self.calculateAge)
        self.button.grid(row=4, column=1, columnspan=2, pady=(10, 30))

        self.result_label_years = Label(self.master, text='Years old: ')
        self.result_label_years.grid(row=5, column=0)

        self.entry_years = Entry(self.master)
        self.entry_years.grid(row=5, column=1)

    def clearAll(self):
        self.entry_day.delete(0, END)
        self.entry_month.delete(0, END)
        self.entry_year.delete(0, END)
        self.entry_years.delete(0, END)

    def calculateAge(self):
        birth_day = self.entry_day.get()
        birth_month = self.entry_month.get()
        birth_year = self.entry_year.get()

        if birth_day == "" or birth_month == "" or birth_year == "":
            self.clearAll()
        elif not birth_day.isdigit() or not birth_month.isdigit() or not birth_year.isdigit():
            self.clearAll()
        else:
            birth_day = int(self.entry_day.get())
            birth_month = int(self.entry_month.get())
            birth_year = int(self.entry_year.get())
            real_date = None

            try:
                check_if_real_date = date(birth_year, birth_month, birth_day)
                real_date = True
            except ValueError:
                real_date = False

            if not real_date:
                self.clearAll()
            else:
                today = datetime.now()
                calculated_year = int(today.strftime("%Y")) - birth_year
                self.entry_years.delete(0, END)

                if birth_day <= int(today.strftime("%d")) and birth_month <= int(today.strftime("%m")):
                    self.entry_years.insert(10, calculated_year)
                else:
                    self.entry_years.insert(10, calculated_year - 1)

root = Tk()
gui = BirthYear(root)
root.mainloop()