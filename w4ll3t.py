from tkinter import * 
from tkinter import messagebox
from db import Database

db = Database("pw.db")




def populate_list():
  password_list.delete(0, END)
  for row in db.fetch():
    password_list.insert(END, row)

def add_item():
  if pw_text.get() == "" or acc_text.get() == "":
    messagebox.showerror("Required fields", "Please include all fields")
    return
  db.insert(acc_text.get(), pw_text.get())
  password_list.delete(0, END)
  password_list.insert(END, (acc_text.get(), pw_text.get()))
  clear_text()
  populate_list()


def select_item(event): 
  try:

    global selected_item
    index = password_list.curselection()[0]
    selected_item = password_list.get(index)

    acc_entry.delete(0, END)
    acc_entry.insert(END, selected_item[1])
    pw_entry.delete(0, END)
    pw_entry.insert(END, selected_item[2])
  except IndexError:
    pass

def remove_item():
  db.remove(selected_item[0])
  clear_text()
  populate_list()

def update_item():
  db.update(selected_item[0], acc_text.get(), pw_text.get())
  populate_list()

def clear_text():
  acc_entry.delete(0, END)
  pw_entry.delete(0, END)



# create window object
app = Tk()

# acc
acc_text = StringVar()
acc_label = Label(app, text="account", font=("bold, 14"), pady=5)
acc_label.grid(row=0, column=0, sticky=W, padx=10)
acc_entry = Entry(app, textvariable=acc_text)
acc_entry.grid(row=0, column=1)
# pw
pw_text = StringVar()
pw_label = Label(app, text="password", font=("bold, 14"))
pw_label.grid(row=1, column=0, sticky=W, padx=10)
pw_entry = Entry(app, textvariable=pw_text)
pw_entry.grid(row=1, column=1)

# passwords list (listbox)
password_list = Listbox(app, height=8, width=50)
password_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=10, padx=10)
# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
# set scroll to listbox
password_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=password_list.yview)
# bind select
password_list.bind("<<ListboxSelect>>", select_item)

# buttons
add_btn = Button(app, text="add", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=10)

remove_btn = Button(app, text="remove", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="update", width=12, command=update_item)
update_btn.grid(row=3, column=0)

clear_btn = Button(app, text="clear input", width=12, command=clear_text)
clear_btn.grid(row=3, column=1)



app.title("p0ck3t")
app.geometry("350x300")

# populate data
populate_list()
populate_list()

# start program
app.mainloop()
