#
# Copyright (C) Sajjad M- HFA2020
# All Rights Reserved.
#
from tkinter import *
from tkinter import messagebox
from RemoteTeaching import RemoteTeaching, LibraryManagment
from PIL import ImageTk, Image


class AnalogClass:
    # UI settings
    def __init__(self, top):
        # Generate Audio File
        GAF_row = 4
        GAF_col = 0
        # For Broadcast Only
        BO_row = 4
        BO_col = 4
        # Convert Scanned Book to Txt
        SB_row = 14
        SB_col = 0
        # For Library Management
        LM_row = 14
        LM_col = 4

        self.top = top
        # Window Spec
        top.title("Analog Classroom")
        top.geometry("1200x600")

        # Banner config
        self.L1 = Label(top, text="Class Management Platform\nCreate Virtual Analog Classrooms", fg="red",
                   font=("Helvetica", 16)).grid(row=0, column=2)
        self.L1 = Label(top, text=" ", fg="blue", font=("Helvetica", 12)).grid(row=3, column=2)
        self.L1 = Label(top, text=" ", fg="blue", font=("Helvetica", 12)).grid(row=11, column=2)
        self.L1 = Label(top, text=" ", fg="blue", font=("Helvetica", 12)).grid(row=12, column=2)

        # MS log
        imgFile = Image.open("M4Africa.jpg")
        imgFile = imgFile.resize((150, 150), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        mslogo = ImageTk.PhotoImage(imgFile)
        LMS = Label(top, image=mslogo, )
        LMS.image = mslogo  # keep a reference!
        LMS.grid(row=0, column=1, )

        # Mylogo
        myFile = Image.open("VAC.jpg")
        myFile = myFile.resize((150, 150), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        mylogo = ImageTk.PhotoImage(myFile)
        LM = Label(top, image=mylogo, )
        LM.image = mylogo  # keep a reference!
        LM.grid(row=0, column=5, )

        # Generate Audio File
        self.L2 = Label(top, text="List of the Text Books", ).grid(row=GAF_row, column=GAF_col)
        self.L3 = Label(top, text="FM Channel", ).grid(row=GAF_row + 1, column=GAF_col)
        self.L4 = Label(top, text="Teacher Name", ).grid(row=GAF_row + 2, column=GAF_col)
        self.L5 = Label(top, text="Class Name", ).grid(row=GAF_row + 3, column=GAF_col)
        self.L6 = Label(top, text="Message", ).grid(row=GAF_row + 4, column=GAF_col)
        self.E1 = Entry(top, bd=5)
        self.E1.grid(row=GAF_row, column=GAF_col + 1)
        self.E2 = Entry(top, bd=5)
        self.E2.grid(row=GAF_row + 1, column=GAF_col + 1)
        self.E3 = Entry(top, bd=5)
        self.E3.grid(row=GAF_row + 2, column=GAF_col + 1)
        self.E4 = Entry(top, bd=5)
        self.E4.grid(row=GAF_row + 3, column=GAF_col + 1)
        self.E5 = Entry(top, bd=5)
        self.E5.grid(row=GAF_row + 4, column=GAF_col + 1)
        self.txtProcesButton = Button(top, text="Read From Text Book", font=("Helvetica", 12), command=self.txtProces).grid(
            row=GAF_row + 6, column=GAF_col + 1, )

        # For Broadcast Only
        self.L22 = Label(top, text="List of Audio Files", ).grid(row=BO_row, column=BO_col)
        self.L23 = Label(top, text="FM Channel", ).grid(row=BO_row + 1, column=BO_col)
        self.L24 = Label(top, text="Teacher Name", ).grid(row=BO_row + 2, column=BO_col)
        self.L25 = Label(top, text="Class Name", ).grid(row=BO_row + 3, column=BO_col)
        self.L26 = Label(top, text="Message", ).grid(row=BO_row + 4, column=BO_col)
        self.E21 = Entry(top, bd=5)
        self.E21.grid(row=BO_row, column=BO_col + 1)
        self.E22 = Entry(top, bd=5)
        self.E22.grid(row=BO_row + 1, column=BO_col + 1)
        self.E23 = Entry(top, bd=5)
        self.E23.grid(row=BO_row + 2, column=BO_col + 1)
        self.E24 = Entry(top, bd=5)
        self.E24.grid(row=BO_row + 3, column=BO_col + 1)
        self.E25 = Entry(top, bd=5)
        self.E25.grid(row=BO_row + 4, column=BO_col + 1)
        self.auProcesButton = Button(top, text="Broadcast Audio Files", font=("Helvetica", 12), command=self.auProces).grid(row=BO_row + 6,
                                                                                                         column=BO_col + 1, )

        # for Scanned Book
        self.L32 = Label(top, text="List of the Digital Books", ).grid(row=SB_row, column=SB_col)
        self.L33 = Label(top, text="FM Channel", ).grid(row=SB_row + 1, column=SB_col)
        self.L34 = Label(top, text="Teacher Name", ).grid(row=SB_row + 2, column=SB_col)
        self.L35 = Label(top, text="Class Name", ).grid(row=SB_row + 3, column=SB_col)
        self.L36 = Label(top, text="Message", ).grid(row=SB_row + 4, column=SB_col)
        self.E31 = Entry(top, bd=5)
        self.E31.grid(row=SB_row, column=SB_col + 1)
        self.E32 = Entry(top, bd=5)
        self.E32.grid(row=SB_row + 1, column=SB_col + 1)
        self.E33 = Entry(top, bd=5)
        self.E33.grid(row=SB_row + 2, column=SB_col + 1)
        self.E34 = Entry(top, bd=5)
        self.E34.grid(row=SB_row + 3, column=SB_col + 1)
        self.E35 = Entry(top, bd=5)
        self.E35.grid(row=SB_row + 4, column=SB_col + 1)
        self.imgProcesButton = Button(top, text="Read From Scanned Book", font=("Helvetica", 12), command=self.imgProces).grid(
            row=SB_row + 6, column=SB_col + 1, )

        # For Library Management
        self.L42 = Label(top, text="Library Name", ).grid(row=LM_row, column=LM_col)
        self.L43 = Label(top, text="Book Name", ).grid(row=LM_row + 1, column=LM_col)
        self.L44 = Label(top, text="Borrower Name", ).grid(row=LM_row + 2, column=LM_col)
        self.L45 = Label(top, text="Status", ).grid(row=LM_row + 3, column=LM_col)
        self.L46 = Label(top, text="Date", ).grid(row=LM_row + 4, column=LM_col)
        self.E41 = Entry(top, bd=5)
        self.E41.grid(row=LM_row, column=LM_col + 1)
        self.E42 = Entry(top, bd=5)
        self.E42.grid(row=LM_row + 1, column=LM_col + 1)
        self.E43 = Entry(top, bd=5)
        self.E43.grid(row=LM_row + 2, column=LM_col + 1)
        self.E44 = Entry(top, bd=5)
        self.E44.grid(row=LM_row + 3, column=LM_col + 1)
        self.E45 = Entry(top, bd=5)
        self.E45.grid(row=LM_row + 4, column=LM_col + 1)
        self.checkStatusButton = Button(top, text="Search for Book", font=("Helvetica", 12), command=self.statusProces).grid(
            row=LM_row + 6, column=LM_col + 1, )
        self.checkoutButton = Button(top, text="Check Out", font=("Helvetica", 12), command=self.checkoutProces).grid(row=LM_row + 6,
                                                                                                      column=LM_col + 2, )
        self.checkInButton = Button(top, text="Check In", font=("Helvetica", 12), command=self.checkinProces).grid(row=LM_row + 6,
                                                                                                   column=LM_col + 3, )

    # To triger Txt Process
    def txtProces(self):
        try:
            bookListName = Entry.get(self.E1)
            fmChannel = Entry.get(self.E2)
            teacherName = Entry.get(self.E3)
            className = Entry.get(self.E4)
            teacherName = Entry.get(self.E3)
            Entry.delete(self.E5,0,END)
            Entry.insert(self.E5, 0, bookListName)
            print(bookListName)
            Remote_Teaching = RemoteTeaching.getBookListJson(bookListName)
            Remote_Teaching.readBookList()
            #os.system('python3 RemoteTeaching.py ')
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

    # To Trigger audio Process
    def auProces(self):
        try:
            bookListName = Entry.get(self.E21)
            fmChannel = Entry.get(self.E22)
            teacherName = Entry.get(self.E23)
            className = Entry.get(self.E24)
            teacherName = Entry.get(self.E23)
            Entry.delete(self.E5,0,END)
            Entry.insert(self.E5, 0, bookListName)
            print(bookListName)
            Remote_Teaching = RemoteTeaching.getBookListJson(bookListName)
            Remote_Teaching.readBookList()
            #os.system('python3 RemoteTeaching.py ')
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

    # To Trigger Image Process
    def imgProces(self):
        try:
            bookListName = Entry.get(self.E31)
            fmChannel = Entry.get(self.E32)
            teacherName = Entry.get(self.E33)
            className = Entry.get(self.E34)
            teacherName = Entry.get(self.E33)
            Entry.delete(self.E5,0,END)
            Entry.insert(self.E5, 0, bookListName)
            print(bookListName)
            Remote_Teaching = RemoteTeaching.getBookListJson(bookListName)
            Remote_Teaching.readBookList()
            #os.system('python3 RemoteTeaching.py ')
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

    # To Trigger Library search Process
    def statusProces(self):
        try:
            libraryName = Entry.get(self.E41)
            bookName = Entry.get(self.E42)
            Remote_Library = LibraryManagment.getLibraryJson(libraryName)
            [status,borrower,date]=Remote_Library.checkAvailability(bookName)
            Entry.delete(self.E43,0,END)
            Entry.insert(self.E43, 0, borrower)
            Entry.delete(self.E44,0,END)
            Entry.insert(self.E44, 0, status)
            Entry.delete(self.E45,0,END)
            Entry.insert(self.E45, 0, date)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

    # To Trigger check out Process
    def checkoutProces(self):
        try:
            libraryName = Entry.get(self.E41)
            bookName = Entry.get(self.E42)
            borrowerName=Entry.get(self.E43)
            Remote_Library = LibraryManagment.getLibraryJson(libraryName)
            [status,borrower,date]=Remote_Library.checkOut(bookName,borrowerName)
            Entry.delete(self.E43,0,END)
            Entry.insert(self.E43, 0, borrower)
            Entry.delete(self.E44,0,END)
            Entry.insert(self.E44, 0, status)
            Entry.delete(self.E45,0,END)
            Entry.insert(self.E45, 0, date)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

    # To Trigger check IN  Process
    def checkinProces(self):
        try:
            libraryName = Entry.get(self.E41)
            bookName = Entry.get(self.E42)
            Remote_Library = LibraryManagment.getLibraryJson(libraryName)
            [status,borrower,date]=Remote_Library.checkOut(bookName,'')
            Entry.delete(self.E43,0,END)
            Entry.insert(self.E43, 0, borrower)
            Entry.delete(self.E44,0,END)
            Entry.insert(self.E44, 0, status)
            Entry.delete(self.E45,0,END)
            Entry.insert(self.E45, 0, date)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid list")

if __name__ == '__main__':
    top = Tk()
    app_gui = AnalogClass(top)
    top.mainloop()