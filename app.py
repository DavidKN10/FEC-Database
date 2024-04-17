from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Scrollbar, Treeview
import mysql.connector


# ======================================== Table Windows ========================================
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="database name"
)

cursor = connection.cursor()
# ==================== Election Window ====================
def election_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM election")
        rows = cursor.fetchall()
        if len(rows) != 0:
            election_table.delete(*election_table.get_children())
            for row in rows:
                election_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = election_table.focus()

    # ==================== Button Windows ====================
    def election_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Election (ElectionID, ElectionName, Date, State) VALUES (%s, %s, %s, %s)"
            election_data = (election_ID_entry.get(), election_name_entry.get(),
                             election_date_entry.get(), election_state_entry.get())
            cursor.execute(insert_query, election_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

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

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def election_update_window():
        def submit_query():
            update_query = "UPDATE Election SET ElectionName=%s, Date=%s, State=%s WHERE ElectionID=%s"
            cursor.execute(update_query, (election_name_entry.get(), election_date_entry.get(),
                                          election_state_entry.get(), election_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

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

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def election_delete_window():
        def submit_query():
            electionID = election_ID_entry.get()
            delete_dependent_rows(electionID)
            delete_query = "DELETE FROM Election WHERE ElectionID=%s"

            cursor.execute(delete_query, (electionID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        def delete_dependent_rows(electionID):
            delete_query = "DELETE FROM candidate WHERE ElectionID=%s"
            cursor.execute(delete_query, (electionID,))
            connection.commit()

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

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

    # ==================== Main Election Window ====================
    election_window = Toplevel(window)
    election_window.title("Election Table")
    election_window.geometry("900x500")
    Label(election_window, font=("", 20, "bold"), text="Election").pack()
    election_window.grab_set()


    # ==================== Actions Frame ====================
    ActionFrame = Frame(election_window)
    ActionFrame.place(x=650, y=50, height=200, width=200)
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
    InfoFrame.place(x=10, y=50, height=700, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Election Info")
    infoFrame.grid(row=0, column=0)


    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    election_table = ttk.Treeview(infoFrame, columns=("electionID", "electionName", "date", "state"),
                                  yscrollcommand=scroll_y.set, height=18)

    election_table.column("#0", width=100)
    election_table.column("electionID", anchor=CENTER, width=100)
    election_table.column("electionName", anchor=W, width=200)
    election_table.column("date", anchor=CENTER, width=100)
    election_table.column("state", anchor=CENTER, width=60)


    election_table.heading("electionID", text="Election ID")
    election_table.heading("electionName", text="Election Name")
    election_table.heading("date", text="Date")
    election_table.heading("state", text="State")

    election_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=election_table.yview)

    election_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Committee Window ====================
def committee_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM committee")
        rows = cursor.fetchall()
        if len(rows) != 0 :
            committee_table.delete(*committee_table.get_children())
            for row in rows:
                committee_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = committee_table.focus()

    # ==================== Button Windows ====================
    def committee_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Committee (CommitteeID, CommitteeName, Treasurer, CommitteeType, State) VALUES (%s, %s, %s, %s, %s)"
            committee_data = (committee_ID_entry.get(), committee_name_entry.get(),
                              treasurer_entry.get(), committee_type_entry.get(), state_entry.get())
            cursor.execute(insert_query, committee_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

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

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def committee_update_window():
        def submit_query():
            update_query = """
            UPDATE Committee
            SET CommitteeName = %s, 
                Treasurer = %s, 
                CommitteeType = %s,
                State = %s
            WHERE CommitteeID = %s;
            """
            cursor.execute(update_query, (committee_name_entry.get(), treasurer_entry.get(),
                                          committee_type_entry.get(), state_entry.get(), committee_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

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

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def committee_delete_window():
        def submit_query():
            committeeID = committee_ID_entry.get()
            delete_query = "DELETE FROM Committee WHERE CommitteeID = %s;"

            cursor.execute(delete_query, (committeeID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Committee Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 15, "bold"), text="Delete Committee").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=1, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

    # ==================== Main Committee Window ====================
    committee_window = Toplevel(window)
    committee_window.title("Committee Table")
    committee_window.geometry("900x500")
    Label(committee_window, font=("", 20, "bold"), text="Committee").pack()
    committee_window.grab_set()


    # ==================== Actions Frame ====================
    ActionFrame = Frame(committee_window)
    ActionFrame.place(x=700, y=50, height=500, width=500)
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
    InfoFrame.place(x=10, y=50, height=700, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Committee Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    committee_table = ttk.Treeview(infoFrame, columns=("committeeID", "committeeName", "treasurer", "committeeType", "state"),
                                   yscrollcommand=scroll_y.set, height=18)

    committee_table.column("#0", width=100)
    committee_table.column("committeeID", anchor=CENTER, width=100)
    committee_table.column("committeeName", anchor=W, width=200)
    committee_table.column("treasurer", anchor=W, width=100)
    committee_table.column("committeeType", anchor=W, width=100)
    committee_table.column("state", anchor=CENTER, width=60)

    committee_table.heading("committeeID", text="Committee ID")
    committee_table.heading("committeeName", text="Committee Name")
    committee_table.heading("treasurer", text="Treasurer")
    committee_table.heading("committeeType", text="Committee Type")
    committee_table.heading("state", text="State")

    committee_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=committee_table.yview)

    committee_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Candidate Window ====================
def candidate_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM candidate")
        rows = cursor.fetchall()
        if len(rows) != 0:
            candidate_table.delete(*candidate_table.get_children())
            for row in rows:
                candidate_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click in
    def get_cursor():
        cursor_row = candidate_table.focus()

    # ==================== Button Windows ====================
    def candidate_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Candidate (CandidateID, CandidateName, PartyAffiliation, Office, State, CommitteeID, ElectionID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            candidate_data = (candidate_ID_entry.get(), candidate_name_entry.get(), party_affiliation_entry.get(),
                              office_entry.get(), state_entry.get(), committee_ID_entry.get(), election_ID_entry.get())
            cursor.execute(insert_query, candidate_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Candidate Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Candidate").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        candidate_name_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name", height=1)
        candidate_name_label.grid(row=2, column=0)
        candidate_name_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_name_entry.grid(row=2, column=1)

        party_affiliation_label = Label(infoFrame, font=("", 15), text="Enter Party Affiliation", height=1)
        party_affiliation_label.grid(row=3, column=0)
        party_affiliation_entry = Entry(infoFrame, font=("", 15), width=18)
        party_affiliation_entry.grid(row=3, column=1)

        office_label = Label(infoFrame, font=("", 15), text="Enter Office", height=1)
        office_label.grid(row=4, column=0)
        office_entry = Entry(infoFrame, font=("", 15), width=18)
        office_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=6, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=6, column=1)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=7, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=7, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def candidate_update_window():
        def submit_query():
            update_query = """
            UPDATE Candidate
            SET CandidateName = %s, 
                PartyAffiliation = %s, 
                Office = %s,
                State = %s,
                CommitteeID = %s,
                ElectionID = %s
            WHERE CandidateID = %s;
        """
            cursor.execute(update_query, (candidate_name_entry.get(), party_affiliation_entry.get(), office_entry.get(),
                                          state_entry.get(), committee_ID_entry.get(), election_ID_entry.get(),
                                          candidate_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Candidate Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Candidate").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        candidate_name_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name", height=1)
        candidate_name_label.grid(row=2, column=0)
        candidate_name_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_name_entry.grid(row=2, column=1)

        party_affiliation_label = Label(infoFrame, font=("", 15), text="Enter Party Affiliation", height=1)
        party_affiliation_label.grid(row=3, column=0)
        party_affiliation_entry = Entry(infoFrame, font=("", 15), width=18)
        party_affiliation_entry.grid(row=3, column=1)

        office_label = Label(infoFrame, font=("", 15), text="Enter Office", height=1)
        office_label.grid(row=4, column=0)
        office_entry = Entry(infoFrame, font=("", 15), width=18)
        office_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=6, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=6, column=1)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=7, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=7, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def candidate_delete_window():
        def submit_query():
            candidateID = candidate_ID_entry.get()
            delete_query = "DELETE FROM Candidate WHERE CandidateID=%s;"

            cursor.execute(delete_query, (candidateID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Candidate Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Candidate").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

    # ==================== Main Candidate Window ====================
    candidate_window = Toplevel(window)
    candidate_window.title("Candidate Table")
    candidate_window.geometry("900x500")
    Label(candidate_window, font=("", 20, "bold"), text="Candidate").pack()
    candidate_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(candidate_window)
    ActionFrame.place(x=725, y=50, height=500, width=500)
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
    InfoFrame.place(x=10, y=50, height=700, width=700)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Candidate Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    candidate_table = ttk.Treeview(infoFrame, columns=("candidateID", "candidateName", "partyAffiliation", "office",
                                                       "state", "committeeID", "electionID"),
                                   yscrollcommand=scroll_y.set, height=18)

    candidate_table.column("#0", width=100)
    candidate_table.column("candidateID", anchor=W, width=100)
    candidate_table.column("candidateName", anchor=W, width=100)
    candidate_table.column("partyAffiliation", anchor=W, width=100)
    candidate_table.column("office", anchor=W, width=100)
    candidate_table.column("state", anchor=CENTER, width=60)
    candidate_table.column("committeeID", anchor=W, width=100)
    candidate_table.column("electionID", anchor=W, width=100)

    candidate_table.heading("candidateID", text="Candidate ID")
    candidate_table.heading("candidateName", text="Candidate Name")
    candidate_table.heading("partyAffiliation", text="Party Affiliation")
    candidate_table.heading("office", text="Office")
    candidate_table.heading("state", text="State")
    candidate_table.heading("committeeID", text="Committee ID")
    candidate_table.heading("electionID", text="Election ID")

    candidate_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=candidate_table.yview)

    candidate_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Contribution Window ====================
def contribution_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM contribution")
        rows = cursor.fetchall()
        if len(rows) != 0:
            contribution_table.delete(*contribution_table.get_children())
            for row in rows:
                contribution_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = contribution_table.focus()

    # ==================== Button Windows ====================
    def contribution_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Contribution (ContributionID, DonorName, CommitteeID, Amount, Date) VALUES (%s, %s, %s, %s, %s)"
            contribution_data = (contribution_ID_entry.get(), donor_name_entry.get(), committee_ID_entry.get(),
                                 amount_entry.get(), date_entry.get())
            cursor.execute(insert_query, contribution_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Contribution Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Contribution").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        donor_name_label = Label(infoFrame, font=("", 15), text="Enter Donor Name", height=1)
        donor_name_label.grid(row=2, column=0)
        donor_name_entry = Entry(infoFrame, font=("", 15), width=18)
        donor_name_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=5, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=5, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def contribution_update_window():
        def submit_query():
            update_query = """
            UPDATE Contribution
            SET DonorName = %s, 
                CommitteeID = %s, 
                Amount = %s,
                Date = %s
            WHERE ContributionID = %s;
        """
            cursor.execute(update_query, (donor_name_entry.get(), committee_ID_entry.get(), amount_entry.get(),
                                          date_entry.get(), contribution_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Contribution Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Contribution").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"))
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        donor_name_label = Label(infoFrame, font=("", 15), text="Enter Donor Name", height=1)
        donor_name_label.grid(row=2, column=0)
        donor_name_entry = Entry(infoFrame, font=("", 15), width=18)
        donor_name_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=5, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=5, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def contribution_delete_window():
        def submit_query():
            contributionID = contribution_ID_entry.get()
            delete_query = "DELETE FROM Contribution WHERE ContributionID = %s;"
            cursor.execute(delete_query, (contributionID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Contribution Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Contribution").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()


    # ==================== Main Contribution Window ====================
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
    InfoFrame.place(x=0, y=50, height=700, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Contribution Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    contribution_table = ttk.Treeview(infoFrame, columns=("contributionID", "donorName", "committeeID", "amount", "date"),
                                      yscrollcommand=scroll_y, height=18)

    contribution_table.column("#0", width=100)
    contribution_table.column("contributionID", anchor=W, width=100)
    contribution_table.column("donorName", anchor=W, width=100)
    contribution_table.column("committeeID", anchor=W, width=100)
    contribution_table.column("amount", anchor=W, width=100)
    contribution_table.column("date", anchor=W, width=100)

    contribution_table.heading("contributionID", text="Contribution ID")
    contribution_table.heading("donorName", text="Donor Name")
    contribution_table.heading("committeeID", text="Committee ID")
    contribution_table.heading("amount", text="Amount")
    contribution_table.heading("date", text="Date")

    contribution_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=contribution_table.yview)

    contribution_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Expenditure Window ====================
def expenditure_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM expenditure")
        rows = cursor.fetchall()
        if len(rows) != 0:
            expenditure_table.delete(*expenditure_table.get_children())
            for row in rows:
                expenditure_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = expenditure_table.focus()

    # ==================== Button Windows ====================
    def expenditure_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Expenditure (ExpenditureID, Payee, CommitteeID, Amount, Purpose, Date) VALUES (%s, %s, %s, %s, %s, %s)"
            expenditure_data = (expenditure_ID_entry.get(), payee_entry.get(), committee_ID_entry.get(),
                                amount_entry.get(), purpose_entry.get(), date_entry.get())
            cursor.execute(insert_query, expenditure_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Expenditure Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Expenditure").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        payee_label = Label(infoFrame, font=("", 15), text="Enter Payee Name", height=1)
        payee_label.grid(row=2, column=0)
        payee_entry = Entry(infoFrame, font=("", 15), width=18)
        payee_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        purpose_label = Label(infoFrame, font=("", 15), text="Enter Purpose", height=1)
        purpose_label.grid(row=5, column=0)
        purpose_entry = Entry(infoFrame, font=("", 15), width=18)
        purpose_entry.grid(row=5, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=6, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=6, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def expenditure_update_window():
        def submit_query():
            update_query = """
            UPDATE Expenditure
            SET Payee = %s, 
                CommitteeID = %s, 
                Amount = %s,
                Purpose = %s,
                Date = %s
            WHERE ExpenditureID = %s;
        """
            cursor.execute(update_query, (payee_entry.get(), committee_ID_entry.get(), amount_entry.get(),
                                          payee_entry.get(), date_entry.get(), expenditure_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Expenditure Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Expenditure").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        payee_label = Label(infoFrame, font=("", 15), text="Enter Payee Name", height=1)
        payee_label.grid(row=2, column=0)
        payee_entry = Entry(infoFrame, font=("", 15), width=18)
        payee_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        purpose_label = Label(infoFrame, font=("", 15), text="Enter Purpose", height=1)
        purpose_label.grid(row=5, column=0)
        purpose_entry = Entry(infoFrame, font=("", 15), width=18)
        purpose_entry.grid(row=5, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=6, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=6, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def expenditure_delete_window():
        def submit_query():
            expenditureID = expenditure_ID_entry.get()
            delete_query = "DELETE FROM Expenditure WHERE ExpenditureID = %s;"
            cursor.execute(delete_query, (expenditureID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Expenditure Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Expenditure").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

    expenditure_window = Toplevel(window)
    expenditure_window.title("Expenditure Table")
    expenditure_window.geometry("900x500")
    Label(expenditure_window, font=("", 20, "bold"), text="Expenditure").pack()
    expenditure_window.grab_set()
    # ==================== Actions Frame ====================
    ActionFrame = Frame(expenditure_window)
    ActionFrame.place(x=725, y=50, height=500, width=500)
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
    InfoFrame.place(x=0, y=50, height=700, width=700)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Expenditure Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    expenditure_table = ttk.Treeview(infoFrame, columns=("expenditureID", "payee", "committeeID",
                                                         "amount", "purpose", "date"),
                                     yscrollcommand=scroll_y, height=18)

    expenditure_table.column("#0", width=100)
    expenditure_table.column("expenditureID", anchor=W, width=100)
    expenditure_table.column("payee", anchor=W, width=100)
    expenditure_table.column("committeeID", anchor=W, width=100)
    expenditure_table.column("amount", anchor=W, width=100)
    expenditure_table.column("purpose", anchor=W, width=100)
    expenditure_table.column("date", anchor=W, width=100)

    expenditure_table.heading("expenditureID", text="Expenditure ID")
    expenditure_table.heading("payee", text="Payee")
    expenditure_table.heading("committeeID", text="Committee ID")
    expenditure_table.heading("amount", text="Amount")
    expenditure_table.heading("purpose", text="Purpose")
    expenditure_table.heading("date", text="Date")

    expenditure_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=expenditure_table.yview)

    expenditure_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Filing Window ====================
def filing_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM filing")
        rows = cursor.fetchall()
        if len(rows) != 0:
            filing_table.delete(*filing_table.get_children())
            for row in rows:
                filing_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = filing_table.focus()

    # ==================== Button Windows ====================
    def filing_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Filing (FilingID, ReportType, ReportPeriod, DateFiled, CommitteeID) VALUES (%s, %s, %s, %s, %s)"
            filing_data = (filing_ID_entry.get(), report_type_entry.get(), report_period_entry.get(),
                           date_filed_entry.get(), committee_ID_entry.get())
            cursor.execute(insert_query, filing_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Filing Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Filing").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        report_type_label = Label(infoFrame, font=("", 15), text="Enter Report Type", height=1)
        report_type_label.grid(row=2, column=0)
        report_type_entry = Entry(infoFrame, font=("", 15), width=18)
        report_type_entry.grid(row=2, column=1)

        report_period_label = Label(infoFrame, font=("", 15), text="Enter Report Period", height=1)
        report_period_label.grid(row=3, column=0)
        report_period_entry = Entry(infoFrame, font=("", 15), width=18)
        report_period_entry.grid(row=3, column=1)

        date_filed_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_filed_label.grid(row=4, column=0)
        date_filed_entry = Entry(infoFrame, font=("", 15), width=18)
        date_filed_entry.grid(row=4, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=5, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=5, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def filing_update_window():
        def submit_query():
            update_query = """
                    UPDATE Filing
                    SET ReportType = %s, 
                        ReportPeriod = %s, 
                        DateFiled = %s,
                        CommitteeID = %s
                    WHERE FilingID = %s;
            """
            cursor.execute(update_query, (report_type_entry.get(), report_period_entry.get(), date_filed_entry.get(),
                                          committee_ID_entry.get(), filing_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Filing Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Filing").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        report_type_label = Label(infoFrame, font=("", 15), text="Enter Report Type", height=1)
        report_type_label.grid(row=2, column=0)
        report_type_entry = Entry(infoFrame, font=("", 15), width=18)
        report_type_entry.grid(row=2, column=1)

        report_period_label = Label(infoFrame, font=("", 15), text="Enter Report Period", height=1)
        report_period_label.grid(row=3, column=0)
        report_period_entry = Entry(infoFrame, font=("", 15), width=18)
        report_period_entry.grid(row=3, column=1)

        date_filed_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_filed_label.grid(row=4, column=0)
        date_filed_entry = Entry(infoFrame, font=("", 15), width=18)
        date_filed_entry.grid(row=4, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=5, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=5, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def filing_delete_window():
        def submit_query():
            filingID = filing_ID_entry.get()
            delete_query = "DELETE FROM Filing WHERE FilingID = %s;"
            cursor.execute(delete_query, (filingID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Filing Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Filing").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

    # ==================== Main Filing Window ====================
    filing_window = Toplevel(window)
    filing_window.title("Filing Table")
    filing_window.geometry("900x500")
    Label(filing_window, font=("", 20, "bold"), text="Filing").pack()
    filing_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(filing_window)
    ActionFrame.place(x=610, y=50, height=500, width=500)
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
    InfoFrame.place(x=10, y=50, height=500, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Filing Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    filing_table = ttk.Treeview(infoFrame, columns=("filingID", "reportType", "reportPeriod",
                                                    "dateFiled", "committeeID"),
                                 yscrollcommand=scroll_y.set, height=18)

    filing_table.column("#0", width=100)
    filing_table.column("filingID", anchor=W, width=100)
    filing_table.column("reportType", anchor=W, width=100)
    filing_table.column("reportPeriod", anchor=W, width=100)
    filing_table.column("dateFiled", anchor=W, width=100)
    filing_table.column("committeeID", anchor=W, width=100)

    filing_table.heading("filingID", text="Filing ID")
    filing_table.heading("reportType", text="Report Type")
    filing_table.heading("reportPeriod", text="Report Period")
    filing_table.heading("dateFiled", text="Date")
    filing_table.heading("committeeID", text="Committee ID")

    filing_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=filing_table.yview)

    filing_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Filing Window ====================
def other_window():
    def committee_transactions_window():
        def fetch_data():
            cursor.execute("""
            SELECT CommitteeID, 'Contribution' AS TransactionType, Amount AS Amount, Date AS TransactionDate FROM Contribution
            UNION ALL
            SELECT CommitteeID, 'Expenditure' AS TransactionType, -Amount AS Amount, Date AS TransactionDate FROM Expenditure
            ORDER BY CommitteeID, TransactionDate;
            """)
            rows = cursor.fetchall()
            if len(rows) !=0:
                CT_table.delete(*CT_table.get_children())
                for row in rows:
                    CT_table.insert("", END, values=row)
                connection.commit()

        def get_cursor():
            cursor_row = CT_table.focus()

        CT_window = Toplevel(window)
        CT_window.title("Committee Transactions")
        CT_window.geometry("550x500")
        Label(CT_window, font=("", 20, "bold"), text="Committee Transactions").pack()
        CT_window.grab_set()


        CT_InfoFrame = Frame(CT_window)
        CT_InfoFrame.place(x=60, y=50, height=500, width=500)
        ctInfoFrame = LabelFrame(CT_InfoFrame, font=("", 15, "bold"), text="Transaction Info")
        ctInfoFrame.grid(row=0, column=0)

        note = Label(CT_InfoFrame, font=("", 13), text="Note: + amount = contribution, - amount = expenditure")
        note.grid(row=1, column=0)

        scroll_y = ttk.Scrollbar(ctInfoFrame, orient=VERTICAL)
        CT_table = ttk.Treeview(ctInfoFrame, columns=("committeeID", "transactionType", "amount", "transactionDate"),
                                yscrollcommand=scroll_y.set, height=18)

        CT_table.column("#0", width=100)
        CT_table.column("committeeID", anchor=CENTER, width=100)
        CT_table.column("transactionType", anchor=CENTER, width=100)
        CT_table.column("amount", anchor=CENTER, width=100)
        CT_table.column("transactionDate", anchor=CENTER, width=100)

        CT_table.heading("committeeID", text="Committee ID")
        CT_table.heading("transactionType", text="Transaction Type")
        CT_table.heading("amount", text="Amount")
        CT_table.heading("transactionDate", text="Transaction Date")

        CT_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=CT_table.yview)

        CT_table.pack(fill=BOTH, expand=1)

        fetch_data()


    def republican_window():
        def fetch_data():
            cursor.execute("SELECT * FROM Candidate WHERE PartyAffiliation IN ('Republican Party');")
            rows = cursor.fetchall()
            if len(rows) !=0:
                candidate_table.delete(*candidate_table.get_children())
                for row in rows:
                    candidate_table.insert("", END, values=row)
                connection.commit()


        def get_cursor():
            cursor_row = candidate_table.focus()


        republican_window = Toplevel(window)
        republican_window.title("Republican Candidates")
        republican_window.geometry("900x500")
        Label(republican_window, font=("", 20, "bold"), text="Republican Candidates").pack()
        republican_window.grab_set()

        candidate_info_frame = Frame(republican_window)
        candidate_info_frame.place(x=60, y=50, height=700, width=800)
        candidateInfoFrame = LabelFrame(candidate_info_frame, font=("", 15, "bold"), text="Candidate Info")
        candidateInfoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(candidateInfoFrame, orient=VERTICAL)
        candidate_table = ttk.Treeview(candidateInfoFrame, columns=("candidateID", "candidateName", "partyAffiliation",
                                                                    "office", "state", "committeeID", "electionID"),
                                       yscrollcommand=scroll_y.set, height=18)

        candidate_table.column("#0", width=100)
        candidate_table.column("candidateID", anchor=W, width=100)
        candidate_table.column("candidateName", anchor=W, width=130)
        candidate_table.column("partyAffiliation", anchor=W, width=110)
        candidate_table.column("office", anchor=W, width=110)
        candidate_table.column("state", anchor=W, width=50)
        candidate_table.column("committeeID", anchor=W, width=100)
        candidate_table.column("electionID", anchor=W, width=100)
        
        candidate_table.heading("candidateID", text="Candidate ID")
        candidate_table.heading("candidateName", text="Candidate Name")
        candidate_table.heading("partyAffiliation", text="Party Affiliation")
        candidate_table.heading("office", text="Office")
        candidate_table.heading("state", text="State")
        candidate_table.heading("committeeID", text="Committee ID")
        candidate_table.heading("electionID", text="Election ID")

        candidate_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=candidate_table.yview)

        candidate_table.pack(fill=BOTH, expand=1)

        fetch_data()


    def democrat_window():
        def fetch_data():
            cursor.execute("SELECT * FROM Candidate WHERE PartyAffiliation IN ('Democratic Party');")
            rows = cursor.fetchall()
            if len(rows) != 0:
                candidate_table.delete(*candidate_table.get_children())
                for row in rows:
                    candidate_table.insert("", END, values=row)
                connection.commit()

        def get_cursor():
            cursor_row = candidate_table.focus()

        republican_window = Toplevel(window)
        republican_window.title("Democrat Candidates")
        republican_window.geometry("900x500")
        Label(republican_window, font=("", 20, "bold"), text="Democrat Candidates").pack()
        republican_window.grab_set()

        candidate_info_frame = Frame(republican_window)
        candidate_info_frame.place(x=60, y=50, height=700, width=800)
        candidateInfoFrame = LabelFrame(candidate_info_frame, font=("", 15, "bold"), text="Candidate Info")
        candidateInfoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(candidateInfoFrame, orient=VERTICAL)
        candidate_table = ttk.Treeview(candidateInfoFrame, columns=("candidateID", "candidateName", "partyAffiliation",
                                                                    "office", "state", "committeeID", "electionID"),
                                       yscrollcommand=scroll_y.set, height=18)

        candidate_table.column("#0", width=100)
        candidate_table.column("candidateID", anchor=W, width=100)
        candidate_table.column("candidateName", anchor=W, width=130)
        candidate_table.column("partyAffiliation", anchor=W, width=110)
        candidate_table.column("office", anchor=W, width=110)
        candidate_table.column("state", anchor=W, width=50)
        candidate_table.column("committeeID", anchor=W, width=100)
        candidate_table.column("electionID", anchor=W, width=100)

        candidate_table.heading("candidateID", text="Candidate ID")
        candidate_table.heading("candidateName", text="Candidate Name")
        candidate_table.heading("partyAffiliation", text="Party Affiliation")
        candidate_table.heading("office", text="Office")
        candidate_table.heading("state", text="State")
        candidate_table.heading("committeeID", text="Committee ID")
        candidate_table.heading("electionID", text="Election ID")

        candidate_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=candidate_table.yview)

        candidate_table.pack(fill=BOTH, expand=1)

        fetch_data()


    def personal_funds_window():
        def fetch_data():
            cursor.execute("""
            SELECT DISTINCT c.CandidateID, c.CandidateName, cc.CommitteeName
            FROM Candidate c
            JOIN Contribution co ON c.CommitteeID = co.CommitteeID
            JOIN Committee cc ON c.CommitteeID = cc.CommitteeID
            WHERE c.CandidateName = co.DonorName;
            """)
            rows = cursor.fetchall()
            if len(rows) != 0:
                personal_funds_table.delete(*personal_funds_table.get_children())
                for row in rows:
                    personal_funds_table.insert("", END, values=row)
                connection.commit()

        def get_cursor():
            cursor_row = personal_funds_table.focus()

        personal_funds_window = Toplevel(window)
        personal_funds_window.title("Personal Funds")
        personal_funds_window.geometry("550x500")
        Label(personal_funds_window, font=("", 20, "bold"), text="Personal Funds").pack()
        personal_funds_window.grab_set()

        personal_funds_frame = Frame(personal_funds_window)
        personal_funds_frame.place(x=50, y=50, height=500, width=500)
        personalFundsFrame = LabelFrame(personal_funds_frame, font=("", 15, "bold"), text="Personal Funds")
        personalFundsFrame.grid(row=0, column=0)

        note = Label(personal_funds_frame, font=("", 12), text="Candidates who have made contributions to their own campaign")
        note.grid(row=1, column=0)

        scroll_y = ttk.Scrollbar(personalFundsFrame, orient=VERTICAL)
        personal_funds_table = ttk.Treeview(personalFundsFrame, columns=("candidateID", "candidateName",
                                                                           "committeeName"),
                                            yscrollcommand=scroll_y.set, height=18)

        personal_funds_table.column("#0", width=100)
        personal_funds_table.column("candidateID", anchor=W, width=100)
        personal_funds_table.column("candidateName", anchor=W, width=100)
        personal_funds_table.column("committeeName", anchor=W, width=150)

        personal_funds_table.heading("candidateID", text="Candidate ID")
        personal_funds_table.heading("candidateName", text="Candidate Name")
        personal_funds_table.heading("committeeName", text="Committee Name")

        personal_funds_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=personal_funds_table.yview)

        personal_funds_table.pack(fill=BOTH, expand=1)

        fetch_data()


    # ==================== Main Other Functions Window ====================
    other_window = Toplevel(window)
    other_window.title("Other Features")
    other_window.geometry("900x500")
    Label(other_window, font=("", 20, "bold"), text="Other Features").pack()
    other_window.grab_set()

    # ==================== Buttons Frame ====================
    ButtonFrame = Frame(other_window)
    ButtonFrame.place(x=60, y=50, height=500, width=500)
    buttonFrame = LabelFrame(ButtonFrame, font=("", 15, "bold"), text="Select a Feature")
    buttonFrame.grid(row=0, column=0)

    committee_transactions = Button(buttonFrame, text="Committee Transactions", font=("", 15), width=20, height=1,
                                    command= committee_transactions_window)
    committee_transactions.grid(row=1, column=0)

    republican_button = Button(buttonFrame, text="Republican Candidates", font=("",15), width=20, height=1,
                               command=republican_window)
    republican_button.grid(row=2, column=0)

    democrat_button = Button(buttonFrame, text="Democrat Candidates", font=("",15), width=20, height=1,
                               command=democrat_window)
    democrat_button.grid(row=3, column=0)

    personal_funds_button = Button(buttonFrame, text="Personal Funds", font=("",15), width=20, height=1,
                                   command=personal_funds_window)
    personal_funds_button.grid(row=4, column=0)


def exit_program():
    cursor.close()
    connection.close()
    window.destroy()


# ======================================== Main Window ========================================
window = Tk()
window.title("FEC Database")
window.geometry("1280x720+0+0")

label_title = Label(window, text="Federal Election Committee Management System", font=("", 40, "bold"))
label_title.pack(side=TOP, fill=X)

# ==================== Tables Frame ====================
TablesFrame = Frame(window)
TablesFrame.place(x=60, y=120, width=1280, height=400)
tableFrame = LabelFrame(TablesFrame, font=("", 20, "bold"), text="Select a Table")
tableFrame.grid(row=0, column=0)

election_button = Button(tableFrame, text="Election", font=("", 20),
                         width=35, height=2, command=election_window)
election_button.grid(row=1, column=0)

committee_button = Button(tableFrame, text="Committee", font=("", 20),
                          width=35, height=2, command=committee_window)
committee_button.grid(row=2, column=0)

candidate_button = Button(tableFrame, text="Candidate", font=("", 20),
                          width=35, height=2, command=candidate_window)
candidate_button.grid(row=3, column=0)

contribution_button = Button(tableFrame, text="Contribution", font=("", 20),
                             width=35, height=2, command=contribution_window)
contribution_button.grid(row=1, column=1)

expenditure_button = Button(tableFrame, text="Expenditure", font=("", 20),
                            width=35, height=2, command=expenditure_window)
expenditure_button.grid(row=2, column=1)

filing_button = Button(tableFrame, text="Filing", font=("", 20),
                       width=35, height=2, command=filing_window)
filing_button.grid(row=3, column=1)

other_button = Button(tableFrame, text="Other Features", font=("", 20),
                      width=35, height=2, command=other_window)
other_button.grid(row=4, column=0)


# ==================== Exit Frame ====================
ExitFrame = Frame(window)
ExitFrame.place(x=60, y=550, width=1280, height=400)
exitFrame = LabelFrame(ExitFrame)
exitFrame.grid(row=0, column=0)

exit_button = Button(exitFrame, text="Exit", font=("", 20), command=exit_program, width=10)
exit_button.grid(row=1, column=0)


window.mainloop()