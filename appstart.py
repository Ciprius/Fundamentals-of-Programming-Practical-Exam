'''
Created on Jan 27, 2017

@author: Cipri
'''
from Domain.Repository.Repository import Repository
from Domain.Controller.Controller import Controller
from Domain.UI.UI import UI

repo=Repository("D:\Faculta\python projects\lexam\master.txt")
cont=Controller(repo)



ui=UI(repo,cont)
ui.mainmenu()