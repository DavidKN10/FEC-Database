from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.ttk import Combobox
import mysql.connector


def open_election_window():
    election_window = Toplevel(window)
    election_window.title("Election Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def open_committee_window():
    election_window = Toplevel(window)
    election_window.title("Committee Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def open_candidate_window():
    election_window = Toplevel(window)
    election_window.title("Candidate Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def open_contribution_window():
    election_window = Toplevel(window)
    election_window.title("Contribution Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def open_expenditure_window():
    election_window = Toplevel(window)
    election_window.title("Expenditure Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def open_filing_window():
    election_window = Toplevel(window)
    election_window.title("Filing Table")
    election_window.geometry("500x500")
    Label(election_window, text="testing").pack()

def exit_program():
    return


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


window.mainloop()
