import json
import os
from typing import List

class Contat:
    def __init__(self, name, phone, email):
        self.number = phone
        self.email = email
        self.name = name
    
    def printSelf(self):
        print()
        print(f"Name: {self.name}")
        print(f"Phone: {self.number}")
        print(f"Email: {self.email}")

contats: List[Contat] = []
running = True
file_path = "contatos.json"

def objToClass(objs):
    for obj in objs:
        temp = Contat(obj['name'], obj['phone'], obj['email'])
        global contats
        contats.append(temp)


def load_contacts():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return [] 

def saveToFile():
    dictionary = []
    for x in contats:
        temp = {
            "name": x.name,
            "phone": x.number,
            "email": x.email
        }
        dictionary.append(temp)
    json_object = json.dumps(dictionary, indent=4)
        
    with open("contatos.json", "w") as outfile:
            outfile.write(json_object)

def showAllCont():
    for x in contats:
        x.printSelf()

def addCont():
    name = str(input("Name: "))
    phone = str(input("Phone: "))
    email = str(input("Email: "))
    
    temp = Contat(name, phone, email)
    temp.printSelf()
    global contats
    contats.append(temp)


def removeCont():
    name = str(input("Name: "))

    for x in contats:
        if x.name == name:
            contats.remove(x)


def searchCont():
    name = str(input("Name: "))

    for x in contats:
        if x.number == name:
            x.printSelf()

def updateCont():
    name = str(input("Name: "))

    newName = str(input("New name: "))
    newPhone = str(input("New phone: "))
    newEmail = str(input("New email: "))

    for x in contats:
        if x.name == name:
            x.name = newName
            x.email = newEmail
            x.number = newPhone


def menu():

    print("\n0 - Close")
    print("1 - Show all contacts")
    print("2 - Add a contact")
    print("3 - Remove a contact")
    print("4 - Search for a contact")
    print("5 - Update a contact")
    
    option = int(input("\nChoose an option: "))

    if option == 0:
        global running
        running = False

    elif option == 1:
        showAllCont()
    
    elif option == 2:
        addCont()

    elif option == 3:
        removeCont()

    elif option == 4:
        searchCont()
    
    elif option == 5:
        updateCont()

contatsObjs = load_contacts()
objToClass(contatsObjs)

while running:
    menu()

saveToFile()

