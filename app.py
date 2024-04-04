from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.ttk import Combobox
import mysql.connector


def open_election_window():
    election_window = Toplevel(window)
    election_window.title("Election Table")
    election_window.geometry("900x500")
    Label(election_window, text="testing").pack()
    election_window.grab_set()

def open_committee_window():
    committee_window = Toplevel(window)
    committee_window.title("Committee Table")
    committee_window.geometry("900x500")
    Label(committee_window, text="testing").pack()
    committee_window.grab_set()

def open_candidate_window():
    candidate_window = Toplevel(window)
    candidate_window.title("Candidate Table")
    candidate_window.geometry("900x500")
    Label(candidate_window, text="testing").pack()
    candidate_window.grab_set()

def open_contribution_window():
    contribution_window = Toplevel(window)
    contribution_window.title("Contribution Table")
    contribution_window.geometry("900x500")
    Label(contribution_window, text="testing").pack()
    contribution_window.grab_set()

def open_expenditure_window():
    expenditure_window = Toplevel(window)
    expenditure_window.title("Expenditure Table")
    expenditure_window.geometry("900x500")
    Label(expenditure_window, text="testing").pack()
    expenditure_window.grab_set()

def open_filing_window():
    filing_window = Toplevel(window)
    filing_window.title("Filing Table")
    filing_window.geometry("900x500")
    Label(filing_window, text="testing").pack()
    filing_window.grab_set()

def exit_program():
    window.destroy()


window = Tk()
window.title("FEC Database")
window.geometry("1280x720+0+0")

label_title = Label(window, text="Federal Election Committee Management System", font=("", 40, "bold"))
label_title.pack(side=TOP, fill=X)

# ==================== Tables Frame ====================
TablesFrame = Frame(window)
TablesFrame.place(x=0, y=120, width=1280, height=400)
tableFrame = LabelFrame(TablesFrame, font=("", 20, "bold"), text="Select a Table")
tableFrame.grid(row=0, column=0)

election_button = Button(tableFrame, text="Election", font=("", 20),
                         width=40, height=3, command=open_election_window)
election_button.grid(row=1, column=0)
committee_button = Button(tableFrame, text="Committee", font=("", 20),
                                  width=40, height=3, command=open_committee_window)
committee_button.grid(row=2, column=0)
candidate_button = Button(tableFrame, text="Candidate", font=("", 20),
                          width=40, height=3, command=open_candidate_window)
candidate_button.grid(row=3, column=0)
contribution_button = Button(tableFrame, text="Contribution", font=("", 20),
                          width=40, height=3, command=open_contribution_window)
contribution_button.grid(row=1, column=1)
expenditure_button = Button(tableFrame, text="Expenditure", font=("", 20),
                          width=40, height=3, command=open_expenditure_window)
expenditure_button.grid(row=2, column=1)
filing_button = Button(tableFrame, text="Filing", font=("", 20),
                          width=40, height=3, command=open_filing_window)
filing_button.grid(row=3, column=1)


# ==================== Exit Frame ====================
ExitFrame = Frame(window)
ExitFrame.place(x=0, y=550, width=1280, height=400)
exitFrame = LabelFrame(ExitFrame)
exitFrame.grid(row=0, column=0)

exit_button = Button(exitFrame, text="Exit", font=("", 20), command=exit_program)
exit_button.grid(row=1, column=0)


window.mainloop()
