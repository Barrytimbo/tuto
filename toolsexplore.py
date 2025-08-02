
import phonenumbers 
import requests
import keyword
import inspect
import builtins
import importlib
import json
from bs4 import BeautifulSoup


moduleimportlib = dir(importlib)
moduleutil = importlib.util
web_scrap = dir(BeautifulSoup)

connect = input("connecte vous...")

def myinspect():
    mydict = {
        "age":12,
        "sport":"football",
        "prosionnal":"coder"
    }

    mylist = ["12", "salut", 12]

    return mydict, mylist


class Classinsp:
    name = 'Barri'
    age = 45


if " " in connect:
    name = input("password :")
    if "  " in name:
        print("bienveu :")

    else:
       print("votre ou password incorec :")


mytype = type(myinspect())

#print(json.dumps(web_scrap, indent=4))
