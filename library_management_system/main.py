import tkinter as tk
import mysql.connector as mysql
from datetime import datetime

mydb = mysql.connect(host='localhost', user='root', password='', database='library')
mycursor = mydb.cursor()

root=tk.Tk()
root.geometry("1555x675")
root.config(bg="#FEFAE0")
root.title("Library Management System")

def login():
    def login_account():
        uid = user_id_entry.get()
        password = password_entry.get()
        if "" in (uid, password):
            err_win = tk.Toplevel(login_)
            err_win.geometry("150x80")
            err_win.title("Error")
            output = tk.Label(err_win, text="Fill the Entry Properly", font=("Arial",10))
            output.pack()
            ok_btn = tk.Button(err_win, text="OK", font=("Arial", 11), command=err_win.destroy)
            ok_btn.pack()
        else:
            user_data = (uid,)
            query = "SELECT password FROM users WHERE Userid=%s"
            mycursor.execute(query,user_data)
            db_pass = mycursor.fetchone()

            if ( db_pass == None or password != db_pass[0] ):
                err_win = tk.Toplevel(login_)
                err_win.geometry("200x80")
                err_win.title("Error")
                output = tk.Label(err_win, text="Invalid Password or User ID", font=("Arial",10))
                output.pack()
                ok_btn = tk.Button(err_win, text="OK", font=("Arial", 11), command=err_win.destroy)
                ok_btn.pack()
            else:
                root.deiconify()
                login_.destroy()
    
    # -------Login (GUI)-------
    root.withdraw()
    login_ = tk.Toplevel(root)
    login_.geometry("750x500")
    login_.config(bg="#FEFAE0")
    login_.title("Login")

    heading = tk.Label(login_, text="LIBRARY MANAGEMENT SYSTEM", font=("Arial", 25), bg="brown", fg="white")
    heading.place(x=80, y=25)
    l1 = tk.Label(login_, text="LOGIN TO LIBRARY MANAGEMENT SYSTEM", font=("Arial", 18), bg="#FFBD31")
    l1.place(x=95, y=100)

    user_id = tk.Label(login_, text="User ID", font=("Arial", 15), bg="#FFBD31")
    user_id.place(x=80, y=180)
    user_id_entry = tk.Entry(login_, font=("Arial", 15))
    user_id_entry.place(x=300, y=180)

    password = tk.Label(login_, text="Password", font=("Arial", 15), bg="#FFBD31")
    password.place(x=80, y=250)
    password_entry = tk.Entry(login_, font=("Arial", 15), show="*")
    password_entry.place(x=300, y=250)

    login_btn = tk.Button(login_, text="LOGIN TO ACCOUNT", font=("Arial", 14, "bold"), bg="#95B9C7", command=login_account)
    login_btn.place(x=250, y=325)

    #signin_btn = tk.Button(login_, text="CREATE NEW ACCOUNT", font=("arial", 14,"bold"), bg="#95B9C7")
    #signin_btn.place(x=400, y=420)

login()

def err_window(message):
    err_win = tk.Toplevel(root)
    err_win.geometry("300x100")
    err_win.title("Error")
    output = tk.Label(err_win, text=message, font=("Arial", 10))
    output.pack()
    ok_btn = tk.Button(err_win, text="OK", font=("Arial", 11), command=err_win.destroy)
    ok_btn.pack()

# ------- ADD DETAILS -------    
def add_details():
    ids = stu_id_entry.get()
    name = name_entry.get()
    phn = phn_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()
    clg = clg_entry.get()
    course = crs_entry.get()

    book_id = book_id_entry.get()
    book_name = book_name_entry.get()
    hsn = hsn_entry.get()
    author = author_entry.get()
    issue_date = issue_date_entry.get()
    return_date = return_date_entry.get()
    per_day_price = per_day_price_entry.get()

    stu_data = (ids, name, phn, email, dob, clg, course) # student
    book_data=(book_id, book_name, hsn, author, issue_date, return_date, per_day_price, ids) # book
    
    if "" in (ids, name, phn, email, dob, clg, course, book_id, book_name, hsn, author, issue_date, return_date, per_day_price, ids):
        err_window("Error Occured! Fill the Empty Entries")
    else:
        # -------CHECKING STUDENT IN DATABASE-------
        query="SELECT Student_ID FROM student where Student_ID = %s"
        student = (ids,)
        mycursor.execute(query, student)
        student = mycursor.fetchone()

        if student != None:
            err_window("Only 1 Book per Student")
            clear_entries()
            return
        # -------CHECKING BOOK_ID IN DATABASE-------
        query="SELECT Book_ID FROM book_issue where Book_ID = %s"
        book = (book_id,)
        mycursor.execute(query, book)
        book = mycursor.fetchone()

        if book != None:
            err_window("Book is not available")
            clear_entries()
            return
        #-------INSERTING DATA IN DATABASE-------
        query = "INSERT INTO student( Student_ID, Name, Phone, Email, DOB, College, Course ) VALUES (%s,%s,%s,%s,%s,%s,%s) "
        mycursor.execute(query, stu_data)
        query = "INSERT INTO book_issue(Book_ID, Book_Name, Book_HSN_Code, book_Author, Issue_Date, Return_Date, Per_Day_Fine, Student_ID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" 
        mycursor.execute(query, book_data)
        mydb.commit()
        #----- Sucess Window-----
        add_win = tk.Toplevel(root)
        add_win.title("Sucess")
        add_win.geometry("300x100")
        output = tk.Label(add_win, text="Data Added Successfully...!", font=("Arial",15))
        output.pack()
        ok_btn = tk.Button(add_win, text="OK", command=add_win.destroy)
        ok_btn.pack()

# -------CLEAR ENTRIES-------
def clear_entries():
    stu_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    phn_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    clg_entry.delete(0, tk.END)
    crs_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    book_name_entry.delete(0, tk.END)
    hsn_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    issue_date_entry.delete(0, tk.END)
    return_date_entry.delete(0, tk.END)
    per_day_price_entry.delete(0, tk.END)    

# ------- SHOWING DETAILS --------
def show_details():
    detail = tk.Toplevel(root)
    detail.geometry("1200x650")
    detail.title("Student Records")
    heading = tk.Label(detail, text="Student and Book Records", font=('Arial', 22, 'bold'), bg="#95B9C7")
    heading.pack()
    output = tk.Text(detail, font=('Arial', 11), width=175, height=40)
    output.pack()
    query = "SELECT * FROM student, book_issue WHERE student.Student_ID = book_issue.Student_ID "
    mycursor.execute(query)
    result = mycursor.fetchall()

    if len(result) == 0:
        output.insert(tk.END, "No Data Found...")
        return
    output.insert(tk.END, 'Student_ID | Name | Phone_No | Email | DOB | College | Course | Book_ID | Book_Name | HSN_Code | Author | Issue_Date | Return_Date | Per_Day_Fine \n\n')
    output.insert(tk.END, '-' * 225 + '\n\n')
    for row in result:
        for i in range(len(row)):
            output.insert(tk.END, str(row[i]) + " | ")
        output.insert(tk.END, "\n")

# ------- UPDATE DETAILS --------
def update_details():
    ids = stu_id_entry.get()

    if (ids == ""):
        err_window("Enter Student ID to Update")
        return
    query = "SELECT Student_ID FROM student WHERE Student_ID=%s"
    data = (ids,)
    mycursor.execute(query, data)
    student = mycursor.fetchone()

    if student == None:
        err_window("Student Not Found")
        return
    name = name_entry.get()
    phn = phn_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()
    clg = clg_entry.get()
    course = crs_entry.get()
    book_id = book_id_entry.get()
    book_name = book_name_entry.get()
    hsn = hsn_entry.get()
    author = author_entry.get()
    issue_date = issue_date_entry.get()
    return_date = return_date_entry.get()
    per_day_price = per_day_price_entry.get()

    if "" in (name, phn, email, dob, clg, course, book_id, book_name, hsn, author, issue_date, return_date, per_day_price):
        err_window("Fill All the Entries Properly")
        return
    stu_data = (name, phn, email, dob, clg, course, ids)
    book_data = (book_id, book_name, hsn, author, issue_date, return_date, per_day_price, ids)
    query = "UPDATE student SET Name = %s, Phone = %s, Email = %s, DOB = %s, College = %s, Course = %s WHERE Student_ID = %s;"
    mycursor.execute(query, stu_data)
    query = "UPDATE book_issue SET Book_ID = %s, Book_Name = %s, Book_HSN_Code = %s, Book_Author = %s, Issue_Date = %s, Return_Date = %s, Per_Day_Fine = %s WHERE Student_ID = %s;"
    mycursor.execute(query, book_data)
    mydb.commit()

    up_win = tk.Toplevel(root)
    up_win.title("Sucess")
    up_win.geometry("350x120")
    output = tk.Label(up_win,text="Data Updated Successfully...!", font=("Arial", 15))
    output.pack()
    ok_btn = tk.Button(up_win, text="OK", font=("Arial", 11), command=up_win.destroy)
    ok_btn.pack()
    clear_entries()

# -------- DELETE RECORD --------
def delete_details():
    ids = stu_id_entry.get()

    if (ids == ""):
        err_window("Enter Student ID to Delete")
        return
    query = "SELECT Student_ID FROM student WHERE Student_ID = %s"
    data = (ids,)
    mycursor.execute(query, data)
    student = mycursor.fetchone()

    if student == None:
        err_window("Student Not Found")
        return
    query = "DELETE FROM book_issue WHERE Student_ID = %s"
    mycursor.execute(query, (ids,))
    query = "DELETE FROM student WHERE Student_ID = %s"
    mycursor.execute(query, (ids,))
    mydb.commit()
    del_win = tk.Toplevel(root)
    del_win.title("Sucess")
    del_win.geometry("350x120")
    output = tk.Label(del_win, text="Student Record Deleted Successfully...", font=("Arial",10))
    output.pack()
    ok_btn = tk.Button(del_win, font=("Arial",11), text="OK", command=del_win.destroy)
    ok_btn.pack()
    clear_entries()

# --------- CALCULATE BILL ---------
def calculate_bill():
    ids = stu_id_entry.get()
    allowed_days = 15
    if ids == "":

        err_window("Enter Student ID to Calculate Bill")
        return
    query = "SELECT Issue_Date, Return_Date, Per_Day_Fine FROM book_issue WHERE Student_ID = %s"
    data = (ids,)
    mycursor.execute(query, data)
    book_data = mycursor.fetchone()

    if book_data == None:
        err_window("Book Not Found")
        return
    issue_date = book_data[0]
    return_date = book_data[1]
    per_day_fine = book_data[2]
    issue = datetime.strptime(str(issue_date), "%Y-%m-%d").date()
    return_date = datetime.strptime(str(return_date), "%Y-%m-%d").date()
    total_days = (return_date - issue).days

    if total_days < 0:
        err_window("Invalid Date")
        return
    if total_days <= allowed_days:
        overdue_days = 0
        total_fine = 0
    else:
        overdue_days = total_days - allowed_days
        total_fine = overdue_days * float(per_day_fine)
    
    bill_window = tk.Toplevel(root)
    bill_window.title("Bill")
    bill_window.geometry("320x500")
    bill_window.config(bg="#FEFAE0")
    
    title = tk.Label(bill_window, text="LIBRAY-BILL", font=('Arial', 20, 'bold'), bg="#FEFAE0", fg="#4A4A4A")
    title.pack()
    student_lbl = tk.Label(bill_window, text="Student ID: " + ids, font=('Arial', 15), bg="#FEFAE0")
    student_lbl.pack()
    issue_lbl = tk.Label(bill_window, text="Issue Date: " + str(issue_date), font=('Arial', 15), bg="#FEFAE0")
    issue_lbl.pack()
    return_date_lbl = tk.Label(bill_window, text="Return Date: " + str(return_date), font=('Arial', 15), bg="#FEFAE0")
    return_date_lbl.pack()
    days_lbl = tk.Label(bill_window, text="Total Days: " + str(total_days), font=('Arial', 15), bg="#FEFAE0")
    days_lbl.pack()
    allowed_lbl = tk.Label(bill_window, text="Allowed Days: " + str(allowed_days), font=('Arial', 15), bg="#FEFAE0")
    allowed_lbl.pack()
    overdue_days_lbl = tk.Label(bill_window, text="Overdue Days: " + str(overdue_days), font=('Arial', 15), bg="#FEFAE0")
    overdue_days_lbl.pack()
    total_fine_lbl = tk.Label(bill_window, text="Total Fine: " + str(total_fine), font=('Arial', 15), bg="#FEFAE0")
    total_fine_lbl.pack()
    ok_btn = tk.Button(bill_window, text="OK", font=("Arial", 11,"bold"), command=bill_window.destroy)
    ok_btn.pack()

# ---------------------- MAIN BODY(GUI) ---------------------- 

title=tk.Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=("Arial",45), bg="#FEFAE0", fg="#BC6C25")
title.place(x="300",y="30")
# ---------------------- Student Details ----------------------
l1=tk.Label(root, text="Student Details", font=("Arial",35), bg="#FEFAE0", fg="#606C38")
l1.place(x="125",y="100")

stu_id_lbl = tk.Label(root, text = 'Student ID ', font=("Arial",25), bg="#FEFAE0" )
stu_id_lbl.place(x='100', y='175')
stu_id_entry= tk.Entry(font=("Arial",20))
stu_id_entry.place(x='275', y='175')
    
name_lbl = tk.Label(root,text="Name ", font=("Arial",25), bg="#FEFAE0")
name_lbl.place(x='100', y='225')
name_entry = tk.Entry(font=('Arial',20))
name_entry.place(x='275', y='225')

phn_lbl = tk.Label(root, text="Phone No. ", font=("Arial",25), bg="#FEFAE0")
phn_lbl.place(x='100', y='275')
phn_entry = tk.Entry(font=('Arial', 20))
phn_entry.place(x='275', y='275')

email_lbl = tk.Label(root, text='E-mail ', font=("Arial",25), bg="#FEFAE0")
email_lbl.place(x='100', y='325')
email_entry = tk.Entry(font=('Arial',20))
email_entry.place(x='275', y='325')
    
dob_lbl = tk.Label(root, text='DOB ', font=("Arial",25), bg="#FEFAE0")
dob_lbl.place(x='100', y='375')
dob_entry = tk.Entry(font=('Arial', 20))
dob_entry.place(x='275', y='375')

clg_lbl = tk.Label(root, text="College ", font=("Arial",25), bg="#FEFAE0")
clg_lbl.place(x='100', y='425')
clg_entry = tk.Entry(font=('Arial', 20))
clg_entry.place(x='275', y='425')

crs_lbl = tk.Label(root, text='Course ', font=('Arial',25), bg='#FEFAE0')
crs_lbl.place(x='100', y='475')
crs_entry = tk.Entry(font=('Arial', 20))
crs_entry.place(x='275', y='475')
# ---------------------- Book Details ----------------------
l2=tk.Label(root, text='Book Details', font=("Arial",35), bg="#FEFAE0", fg="#606C38")
l2.place(x="900",y="100")

book_id_lbl = tk.Label(root, text = 'Book ID ', font=("Arial",25), bg="#FEFAE0" )
book_id_lbl.place(x='925', y='175')
book_id_entry = tk.Entry(font=('Arial',20))
book_id_entry.place(x='1150', y='175')
    
book_name_lbl = tk.Label(root,text="Book Name ", font=("Arial",25), bg="#FEFAE0")
book_name_lbl.place(x='925', y='225')
book_name_entry = tk.Entry(font=('Arial', 20))
book_name_entry.place(x='1150', y='225')

hsn_lbl = tk.Label(root, text="HSN Code ", font=("Arial",25), bg="#FEFAE0")
hsn_lbl.place(x='925',y='275')
hsn_entry = tk.Entry(font=('Arial',20))
hsn_entry.place(x='1150', y='275')

author_lbl = tk.Label(root, text="Author ", font=("Arial",25), bg="#FEFAE0")
author_lbl.place(x='925', y='325')
author_entry = tk.Entry(font=('Arial', 20))
author_entry.place(x='1150', y='325')

issue_date_lbl = tk.Label(root, text="Issue Date", font=("Arial",25), bg="#FEFAE0")
issue_date_lbl.place(x='925', y='375')
issue_date_entry = tk.Entry(font=('Arial', 20))
issue_date_entry.place(x='1150', y='375')

return_date_lbl = tk.Label(root, text="Return Date", font=("Arial",25), bg="#FEFAE0")
return_date_lbl.place(x='925', y='425')
return_date_entry = tk.Entry(font=('Arial', 20))
return_date_entry.place(x='1150', y='425')

per_day_price_lbl = tk.Label(root, text="Per Day Price", font=("Arial",25), bg="#FEFAE0")
per_day_price_lbl.place(x="925",y="475")
per_day_price_entry = tk.Entry(font=('Arial', 20))
per_day_price_entry.place(x='1150', y='475')
# ---------------------- Buttons ----------------------
add_btn = tk.Button(root, text="ADD",font=("Arial", 15), bg="green", fg="white",  command=add_details)
add_btn.place(x='150', y='550')

show_btn = tk.Button(root, text="SHOW", font=("Arial", 15), bg="orange", fg="white", command=show_details)
show_btn.place(x='250', y='550')

update_btn = tk.Button(root, text="UPDATE", font=("Arial",15), bg="blue", fg="white", command=update_details)
update_btn.place(x='365', y='550')

delete_btn = tk.Button(root, text="DELETE", font=("Arial",15), bg="red", fg="white", command=delete_details)
delete_btn.place(x='500', y='550')

calc_btn = tk.Button(root, text="CALCULATE", font=("Arial",15), bg="violet", fg="white", command=calculate_bill)
calc_btn.place(x='635', y='550')

exit_btn = tk.Button(root, text="EXIT", font=("Arial",15), bg="brown", fg="white", command=root.destroy)
exit_btn.place(x='815', y='550')
    
root.mainloop()
mydb.close()