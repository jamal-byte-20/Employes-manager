from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
import data
from employ import *
from re import match


idSelected = 0
v = ["id","nom","departement","hoursTravail","salaire"]


def checkEmpty():
    # nom v
    name_valid = match(r"^[a-zA-Z]{2,}$",input_nom.get())
    if not name_valid:
        input_nom.configure(border_color="red")
        messagebox.showerror("","name is not valid")
        return False
    else:
        input_nom.configure(border_color="")
    #age v
    age_valid = match(r"^\d{2}$",input_age.get())
    if not age_valid:
        input_age.configure(border_color="red")
        messagebox.showerror("","age is not valid")
        return False
    else:
        if int(input_age.get()) < 18:
            input_age.configure(border_color="red")
            messagebox.showerror("age error", "age should be great than or equal 18")
            return False
        else:
            input_age.configure(border_color="")
    
    #s v
    salair_valid = match(r"^[0-9]{4,}$",input_salair.get())
    if not salair_valid:
        input_salair.configure(border_color="red")
        messagebox.showerror("","salair is not valid")
        return False
    else:
        if float(input_salair.get()) <= 0:
            input_salair.configure(border_color="red")
            messagebox.showerror("salair error", "salair should be great than 0")
            return False
        else:
            input_salair.configure(border_color="")

    #dep v
    if input_departement.get() == "departement":
        input_departement.configure(border_color="red")
        messagebox.showerror("","input is empty")
        return False
    else:
        input_departement.configure(border_color="")

    #ht v
    hours_valid = match(r"^[0-9]{2,}$",input_htravail.get())
    if not hours_valid:
        input_htravail.configure(border_color="red")
        messagebox.showerror("","hours travaill is not valid")
        return False
    else:
        if float(input_htravail.get()) <= 0:
            input_htravail.configure(border_color="red")
            messagebox.showerror("hours error", "hours travaill should be great than 0")
            return False
        else:
            input_htravail.configure(border_color="")

    return True

def addEmploy():
    if checkEmpty():
        try: 
            dt = data.insert(Employ(input_nom.get(), input_age.get(), input_departement.get(), int(input_htravail.get()), int(input_salair.get())),idSelected)
            if not dt:
                messagebox.showinfo("success","Employe has been added successfuly")
                clear(True)
            else:
                clear(True)
        except Exception as ex:
            messagebox.showerror("error", ex)
        set_from_csv()

def deletEmploy():
    if idSelected != 0 :
        sure = messagebox.askokcancel("Delete Employ", "are you sure?")
        if sure:
            data.delet(idSelected)
            set_from_csv()
            messagebox.showinfo("delete", "Employ has been deleted")
    else:
        messagebox.showwarning("wr", "please select Employe for deleting")
    clear(True)

def dellall():
    resp = messagebox.askokcancel("dellet all data", "are sure?")
    if resp:
        data.reset()
        set_from_csv()
        clear(True)
    else:
        return
    
def updateEmploy():
    if idSelected != 0:
        if checkEmpty():
            data.updateE(idSelected,input_nom.get(), input_age.get(), input_departement.get(), int(input_htravail.get()), int(input_salair.get()))
            set_from_csv()
            clear(True)
            messagebox.showinfo("succes", "updating has been successfuly")
    else:
        messagebox.showwarning("wr", "please select Employ befor updating!")
        
def set_from_csv():
    treev.delete(*treev.get_children())
    dt = data.getAll()
    for imp in dt:
        treev.insert('',END, values=imp)

def selection(event):
    global idSelected
    selected = treev.selection()
    if selected:
        ss = treev.item(selected)['values']
        clear()
        input_nom.insert(0,ss[1])
        input_age.insert(0,ss[2])
        input_salair.insert(0,ss[3])
        input_departement.set(ss[4])
        input_htravail.insert(0,ss[5])
        idSelected = ss[0]

def clear(s=False):
    global idSelected
    input_nom.delete(0,END)
    input_age.delete(0,END)
    input_salair.delete(0,END)
    input_htravail.delete(0,END)
    input_departement.set("departement")
    if s:
        treev.selection_remove(treev.focus())
        idSelected = 0

def serch_by():
    global v
    res = []
    if sear_input.get() == "":
        sear_input.configure(border_color="red")
        messagebox.showerror("error", "input is empty!")
    else:
        try:
            sear_input.configure(border_color="")
            value = sear_input.get(),sear_by_c.get()
            treev.delete(*treev.get_children())
            if value[1] == v[0]:
                res = data.search_by_id(int(value[0]))
            elif value[1] == v[1]:
                res = data.search_by_nom(value[0])
            elif value[1] == v[2]:
                res = data.search_by_dep(value[0])
            elif value[1] == v[3]:
                res = data.search_by_h(float(value[0]))
            elif value[1] == v[4]:
                res = data.search_by_s(float(value[0]))
            for d in res:
                treev.insert('',END, values=d)
        except Exception as ex:
            messagebox.showerror("error", ex)

root = CTk()
root.geometry("950x520")
root.config(bg="black")
root.resizable(False,False)


frameleft = CTkFrame(root, fg_color="black")
frameleft.grid(row=0, column=0, padx=5)
label_nom = CTkLabel(frameleft,text="nom", font=("Arial", 15, "bold"))
label_nom.grid(row=0,column=0, pady=20, padx=5)
input_nom = CTkEntry(frameleft, font=("Arial", 15, "bold"))
input_nom.grid(row=0,column=1, pady=20, padx=5)

label_age = CTkLabel(frameleft,text="age", font=("Arial", 15, "bold"))
label_age.grid(row=1,column=0, pady=20, padx=5)
input_age = CTkEntry(frameleft, font=("Arial", 15, "bold"))
input_age.grid(row=1,column=1, pady=20, padx=5)

label_salair = CTkLabel(frameleft,text="salaire", font=("Arial", 15, "bold"))
label_salair.grid(row=2,column=0, pady=20, padx=5)
input_salair = CTkEntry(frameleft, font=("Arial", 15, "bold"))
input_salair.grid(row=2,column=1, pady=20, padx=5)

values = ["web developpement", "UI/UX design", "Networks ingenieur", "Softwere ingenieur"]
label_departement = CTkLabel(frameleft,text="departement", font=("Arial", 15, "bold"))
label_departement.grid(row=3,column=0, pady=20, padx=5)
input_departement = CTkComboBox(frameleft, font=("Arial", 14, "bold"), values= values)
input_departement.set("departement")
input_departement.grid(row=3,column=1, pady=20, padx=5)

label_htaravail = CTkLabel(frameleft,text="hoursTravaill", font=("Arial", 15, "bold"))
label_htaravail.grid(row=4,column=0, pady=20, padx=5)
input_htravail = CTkEntry(frameleft, font=("Arial", 15, "bold"))
input_htravail.grid(row=4,column=1, pady=20, padx=5)

btn_reset = CTkButton(frameleft,text="unselect", command=lambda x = True: clear(x), corner_radius=50, hover_color="red")
btn_reset.grid(row=5,column=0, columnspan= 2)



frameright = CTkFrame(root)
frameright.grid(row=0, column=1)

sear_label = CTkLabel(frameright,font=("Arial", 13, "bold"), text="Search by:")
sear_label.grid(row=0,column=0,pady=5, padx=3)

sear_by_c = CTkComboBox(frameright, font=("Arial", 13, "bold"), values= ["id","nom","departement","hoursTravail","salaire"])
sear_by_c.grid(row=0,column=1, pady=5, padx=3)

sear_input = CTkEntry(frameright)
sear_input.grid(row=0,column=2, pady=5, padx=3)

sear_btn = CTkButton(frameright,text="search", command=serch_by)
sear_btn.grid(row=0, column = 3, pady=5, padx=3)

showall_btn = CTkButton(frameright,text="show all", command=set_from_csv)
showall_btn.grid(row=0, column = 4, pady=5, padx=3)



treev = ttk.Treeview(frameright, height=20)
treev.grid(row=1, column=0, columnspan=10)
columns = ("Id", "Nom", "Age", "Salair", "Departement", "HoursTravail")
treev['columns'] = columns
for i in columns:
    if i == "Id":
        treev.column(i, width=67)
    elif i == "Age":
        treev.column(i, width=67)
    elif i == "Departement":
        treev.column(i, width=135)
    else:
        treev.column(i, width=120)
for i in columns:
    treev.heading(i, text= i)

treev.config(show="headings")
set_from_csv()

style = ttk.Style()
style.configure("Treeview.Heading", font=("arial", 13, "bold"), background="#bfbfbf")
style.configure("Treeview", font=("arial", 10, "bold"))

framebottom = CTkFrame(root, fg_color="black")
framebottom.grid(row=1, column=0, columnspan=2)

btn_new = CTkButton(framebottom,text="new Employ", command=addEmploy)
btn_new.grid(row=0, column=0, padx=10, pady = 10)

btn_update = CTkButton(framebottom,text="update Employ", command=updateEmploy)
btn_update.grid(row=0, column=1, padx=10, pady = 10)

btn_delete = CTkButton(framebottom,text="delete Employ", command=deletEmploy, fg_color="red")
btn_delete.grid(row=0, column=2, padx=10, pady = 10)

btn_deletall = CTkButton(framebottom,text="delete All", command=dellall,fg_color="red")
btn_deletall.grid(row=0, column=3, padx=10, pady = 10)

btn_updateall = CTkButton(framebottom,text="exit", command=exit)
btn_updateall.grid(row=0, column=4, padx=10, pady = 10)

treev.bind("<ButtonRelease>", selection)
root.mainloop()