from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.ttk import Combobox
import mysql.connector


# ======================================== Table Windows ========================================

# ==================== Election Window ====================
def open_election_window():
    election_window = Toplevel(window)
    election_window.title("Election Table")
    election_window.geometry("900x500")
    Label(election_window, font=("", 20, "bold"), text="Election").pack()
    election_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(election_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1
                           ,command=election_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=election_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=election_delete_window)
    delete_button.grid(row=3, column=0)


    # ==================== Table Info Frame ====================
    InfoFrame = Frame(election_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Election Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def election_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Election Insert")
    insert_window.geometry("500x400")
    Label(insert_window, font=("", 15, "bold"), text="Insert Election").pack()

    InfoFrame = Frame(insert_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
    election_ID_label.grid(row=1, column=0)
    election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    election_ID_entry.grid(row=1, column=1)

    election_name_label = Label(infoFrame, font=("", 15), text="Enter Election name", height=1)
    election_name_label.grid(row=2, column=0)
    election_name_entry = Entry(infoFrame, font=("", 15), width=18)
    election_name_entry.grid(row=2, column=1)

    election_date_label = Label(infoFrame, font=("", 15), text="Enter Election date", height=1)
    election_date_label.grid(row=3, column=0)
    election_date_entry = Entry(infoFrame, font=("", 15), width=18)
    election_date_entry.grid(row=3, column=1)

    election_state_label = Label(infoFrame, font=("", 15), text="Enter Election state", height=1)
    election_state_label.grid(row=4, column=0)
    election_state_entry = Entry(infoFrame, font=("", 15), width=18)
    election_state_entry.grid(row=4, column=1)


    SubmitFrame = Frame(insert_window)
    SubmitFrame.place(x=0, y=300, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    insert_window.grab_set()


def election_update_window():
    update_window = Toplevel(window)
    update_window.title("Election Update")
    update_window.geometry("500x400")
    Label(update_window, font=("", 15, "bold"), text="Update Election").pack()

    InfoFrame = Frame(update_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
    election_ID_label.grid(row=1, column=0)
    election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    election_ID_entry.grid(row=1, column=1)

    election_name_label = Label(infoFrame, font=("", 15), text="Enter Election name", height=1)
    election_name_label.grid(row=2, column=0)
    election_name_entry = Entry(infoFrame, font=("", 15), width=18)
    election_name_entry.grid(row=2, column=1)

    election_date_label = Label(infoFrame, font=("", 15), text="Enter Election date", height=1)
    election_date_label.grid(row=3, column=0)
    election_date_entry = Entry(infoFrame, font=("", 15), width=18)
    election_date_entry.grid(row=3, column=1)

    election_state_label = Label(infoFrame, font=("", 15), text="Enter Election state", height=1)
    election_state_label.grid(row=4, column=0)
    election_state_entry = Entry(infoFrame, font=("", 15), width=18)
    election_state_entry.grid(row=4, column=1)

    SubmitFrame = Frame(update_window)
    SubmitFrame.place(x=0, y=300, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    update_window.grab_set()


def election_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Election Delete")
    delete_window.geometry("400x300")
    Label(delete_window, font=("", 15, "bold"), text="Delete Election").pack()

    InfoFrame = Frame(delete_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
    election_ID_label.grid(row=1, column=0)
    election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    election_ID_entry.grid(row=1, column=1)


    SubmitFrame = Frame(delete_window)
    SubmitFrame.place(x=0, y=150, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    delete_window.grab_set()


# ==================== Committee Window ====================
def open_committee_window():
    committee_window = Toplevel(window)
    committee_window.title("Committee Table")
    committee_window.geometry("900x500")
    Label(committee_window, font=("", 20, "bold"), text="Committee").pack()
    committee_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(committee_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=committee_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=committee_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=committee_delete_window)
    delete_button.grid(row=3, column=0)
    # ==================== Table Info Frame ====================
    InfoFrame = Frame(committee_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Committee Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def committee_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Committee Insert")
    insert_window.geometry("500x400")
    Label(insert_window, font=("", 15, "bold"), text="Insert Committee").pack()

    InfoFrame = Frame(insert_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
    committee_ID_label.grid(row=1, column=0)
    committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_ID_entry.grid(row=1, column=1)

    committee_name_label = Label(infoFrame, font=("", 15), text="Enter Committee name", height=1)
    committee_name_label.grid(row=2, column=0)
    committee_name_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_name_entry.grid(row=2, column=1)

    treasurer_label = Label(infoFrame, font=("", 15), text="Enter Treasurer", height=1)
    treasurer_label.grid(row=3, column=0)
    treasurer_entry = Entry(infoFrame, font=("", 15), width=18)
    treasurer_entry.grid(row=3, column=1)

    committee_type_label = Label(infoFrame, font=("", 15), text="Enter Committee type", height=1)
    committee_type_label.grid(row=4, column=0)
    committee_type_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_type_entry.grid(row=4, column=1)

    state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
    state_label.grid(row=5, column=0)
    state_entry = Entry(infoFrame, font=("", 15), width=18)
    state_entry.grid(row=5, column=1)


    SubmitFrame = Frame(insert_window)
    SubmitFrame.place(x=0, y=300, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    insert_window.grab_set()


def committee_update_window():
    update_window = Toplevel(window)
    update_window.title("Committee Update")
    update_window.geometry("500x400")
    Label(update_window, font=("", 15, "bold"), text="Update Committee").pack()

    InfoFrame = Frame(update_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
    committee_ID_label.grid(row=1, column=0)
    committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_ID_entry.grid(row=1, column=1)

    committee_name_label = Label(infoFrame, font=("", 15), text="Enter Committee name", height=1)
    committee_name_label.grid(row=2, column=0)
    committee_name_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_name_entry.grid(row=2, column=1)

    treasurer_label = Label(infoFrame, font=("", 15), text="Enter Treasurer", height=1)
    treasurer_label.grid(row=3, column=0)
    treasurer_entry = Entry(infoFrame, font=("", 15), width=18)
    treasurer_entry.grid(row=3, column=1)

    committee_type_label = Label(infoFrame, font=("", 15), text="Enter Committee type", height=1)
    committee_type_label.grid(row=4, column=0)
    committee_type_entry = Entry(infoFrame, font=("", 15), width=18)
    committee_type_entry.grid(row=4, column=1)

    state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
    state_label.grid(row=5, column=0)
    state_entry = Entry(infoFrame, font=("", 15), width=18)
    state_entry.grid(row=5, column=1)


    SubmitFrame = Frame(update_window)
    SubmitFrame.place(x=0, y=300, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    update_window.grab_set()


def committee_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Committee Delete")
    delete_window.geometry("400x300")
    Label(delete_window, font=("", 15, "bold"), text="Delete Committee").pack()

    InfoFrame = Frame(delete_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
    infoFrame.grid(row=0, column=0)

    election_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
    election_ID_label.grid(row=1, column=0)
    election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
    election_ID_entry.grid(row=1, column=1)


    SubmitFrame = Frame(delete_window)
    SubmitFrame.place(x=0, y=150, height=250, width=250)
    submitFrame = LabelFrame(InfoFrame)
    submitFrame.grid(row=0, column=0)

    submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10)
    submit_button.grid(row=1, column=0)

    delete_window.grab_set()


# ==================== Candidate Window ====================
def open_candidate_window():
    candidate_window = Toplevel(window)
    candidate_window.title("Candidate Table")
    candidate_window.geometry("900x500")
    Label(candidate_window, font=("", 20, "bold"), text="Candidate").pack()
    candidate_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(candidate_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=candidate_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=candidate_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=candidate_delete_window)
    delete_button.grid(row=3, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(candidate_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Candidate Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def candidate_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Candidate Insert")
    insert_window.geometry("700x400")
    Label(insert_window, font=("", 20, "bold"), text="Insert Candidate").pack()
    insert_window.grab_set()


def candidate_update_window():
    update_window = Toplevel(window)
    update_window.title("Candidate Update")
    update_window.geometry("700x400")
    Label(update_window, font=("", 20, "bold"), text="Update Candidate").pack()
    update_window.grab_set()


def candidate_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Candidate Delete")
    delete_window.geometry("700x400")
    Label(delete_window, font=("", 20, "bold"), text="Delete Candidate").pack()
    delete_window.grab_set()


# ==================== Contribution Window ====================
def open_contribution_window():
    contribution_window = Toplevel(window)
    contribution_window.title("Contribution Table")
    contribution_window.geometry("900x500")
    Label(contribution_window, font=("", 20, "bold"), text="Contribution").pack()
    contribution_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(contribution_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=contribution_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=contribution_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=contribution_delete_window)
    delete_button.grid(row=3, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(contribution_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Contribution Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def contribution_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Contribution Insert")
    insert_window.geometry("700x400")
    Label(insert_window, font=("", 20, "bold"), text="Insert Contribution").pack()
    insert_window.grab_set()


def contribution_update_window():
    update_window = Toplevel(window)
    update_window.title("Contribution Update")
    update_window.geometry("700x400")
    Label(update_window, font=("", 20, "bold"), text="Update Contribution").pack()
    update_window.grab_set()


def contribution_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Contribution Delete")
    delete_window.geometry("700x400")
    Label(delete_window, font=("", 20, "bold"), text="Delete Contribution").pack()
    delete_window.grab_set()


# ==================== Expenditure Window ====================
def open_expenditure_window():
    expenditure_window = Toplevel(window)
    expenditure_window.title("Expenditure Table")
    expenditure_window.geometry("900x500")
    Label(expenditure_window, font=("", 20, "bold"), text="Expenditure").pack()
    expenditure_window.grab_set()
    # ==================== Actions Frame ====================
    ActionFrame = Frame(expenditure_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=expenditure_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=expenditure_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=expenditure_delete_window)
    delete_button.grid(row=3, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(expenditure_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Expenditure Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def expenditure_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Expenditure Insert")
    insert_window.geometry("700x400")
    Label(insert_window, font=("", 20, "bold"), text="Insert Expenditure").pack()
    insert_window.grab_set()


def expenditure_update_window():
    update_window = Toplevel(window)
    update_window.title("Expenditure Update")
    update_window.geometry("700x400")
    Label(update_window, font=("", 20, "bold"), text="Update Expenditure").pack()
    update_window.grab_set()


def expenditure_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Expenditure Delete")
    delete_window.geometry("700x400")
    Label(delete_window, font=("", 20, "bold"), text="Delete Expenditure").pack()
    delete_window.grab_set()


# ==================== Filing Window ====================
def open_filing_window():
    filing_window = Toplevel(window)
    filing_window.title("Filing Table")
    filing_window.geometry("900x500")
    Label(filing_window, font=("", 20, "bold"), text="Filing").pack()
    filing_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(filing_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=filing_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=filing_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=filing_delete_window)
    delete_button.grid(row=3, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(filing_window)
    InfoFrame.place(x=0, y=50, height=500, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Filing Info")
    infoFrame.grid(row=0, column=0)


# ==================== Button Windows ====================
def filing_insert_window():
    insert_window = Toplevel(window)
    insert_window.title("Filing Insert")
    insert_window.geometry("700x400")
    Label(insert_window, font=("", 20, "bold"), text="Insert Filing").pack()
    insert_window.grab_set()


def filing_update_window():
    update_window = Toplevel(window)
    update_window.title("Filing Update")
    update_window.geometry("700x400")
    Label(update_window, font=("", 20, "bold"), text="Update Filing").pack()
    update_window.grab_set()


def filing_delete_window():
    delete_window = Toplevel(window)
    delete_window.title("Filing Delete")
    delete_window.geometry("700x400")
    Label(delete_window, font=("", 20, "bold"), text="Delete Filing").pack()
    delete_window.grab_set()


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

exit_button = Button(exitFrame, text="Exit", font=("", 20), command=exit_program, width=10)
exit_button.grid(row=1, column=0)


window.mainloop()
