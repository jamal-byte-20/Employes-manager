from employ import Employ
import csv
from tkinter import messagebox

keys = ['id', 'nom', 'age', 'salaire', 'departement', 'hoursTravaill']

def getAll():
    lista_emp = []
    with open("employes.csv") as f:
          fscv = csv.reader(f)
          for em in fscv:
               if em != keys:
                    lista_emp.append(em)
    return lista_emp

def save(data):
     with open("employes.csv", "w") as f:
        fcsv = csv.writer(f)
        fcsv.writerow(keys)
        for i in data:
            fcsv.writerow(i)

def insert(em:Employ,idselect:int):
    data = getAll()
    isf = False
    for i in data:
            if int(i[0]) == idselect:
                del em
                messagebox.showerror("error", "this Employ is already fined")
                isf = True
    if isf is False:
         with open("employes.csv", "a") as f:
                    fcsv = csv.writer(f)
                    fcsv.writerow(([em.id,em.nom,em.age,em.salaire,em.departement,em.hoursTravaill]))
    return isf

def delet(id:int):
    isf = False
    data = getAll()
    for i in data:
        if int(i[0]) == id:
            isf = True
            print("trouve")
            data.remove(i)
        
    if not isf:
         messagebox.showerror("error", "this name is not defined")
    save(data)          

def reset():
    data = []
    with open("id.txt", "w") as f:
         f.write("")
    save(data)


def updateE(id,nom, age, dep, hrs, s):
    data = getAll()
    for i in data:
        if int(i[0]) == id:
            i[1] = nom
            i[2] = age
            i[3] = s
            i[4] = dep
            i[5] = hrs
    save(data)


def search_by_dep(dep:str):
    deps = []
    data = getAll()

    for i in data:
          if i[4].lower() == dep.lower():
               deps.append(i)

    return deps

def search_by_id(id:int):
    ids = []
    data = getAll()

    for i in data:
          if int(i[0]) == id:
               ids.append(i)

    return ids

def search_by_nom(nom:str):
    ids = []
    data = getAll()

    for i in data:
          if i[1].lower() == nom.lower():
               ids.append(i)

    return ids

def search_by_h(hours:float):
    ids = []
    data = getAll()

    for i in data:
          if float(i[5]) == hours:
               ids.append(i)

    return ids

def search_by_s(s:float):
    ids = []
    data = getAll()

    for i in data:
          if float(i[3]) == s:
               ids.append(i)

    return ids