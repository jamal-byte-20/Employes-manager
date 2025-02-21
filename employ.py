
def getId():
    with open("id.txt") as f:
        return f.read()

class Employ():
    nbEmploye = 0
    def __init__(self, nom, age, departement, hoursTravaill, salair = 0):
        if getId() != "":
            Employ.nbEmploye = int(getId())
        else:
            Employ.nbEmploye = 0

        Employ.nbEmploye += 1
        with open("id.txt", "w") as f:
            f.write(str(Employ.nbEmploye))

        self.id = Employ.nbEmploye
        self.nom = nom
        self.age = age
        self.salaire = salair
        self.departement = departement
        self.hoursTravaill = hoursTravaill