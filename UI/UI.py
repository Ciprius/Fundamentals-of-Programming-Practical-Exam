'''
Created on Jan 27, 2017

@author: Cipri
'''

class UI:
    
    def __init__(self,master,controller):
        self._master=master
        self._controler=controller

    
    def mainmenu(self):
        
        for i in self._master.get_list():
            print(i)
        while True:
            
            print("add- add new qestion")
            print("create- creat a new file")
            print("start- start a quiz")
            print("exit-end the program")
            comm=input("Give the command:")
            pos=comm.find(" ")
            if pos!=-1:
                com=comm[:pos]
                li=comm[pos+1:]
            else:
                com=comm
            #print(li)
            if com=='add':
                lista=li
                lista=lista.split(';')
                print(lista,len(lista))
                if len(lista)==7:
                    self.ADD(lista)
                else:
                    print("Wrong number of arguments!")
            if com=='create':
                lista=li
                lista=lista.split(';')
                if len(lista)==3:
                    self.Create(lista)
                else:
                    print("Wrong number of arguments!")
                    
            if com=='start':
                lista=li
                print(lista)
                #lista=lista.split(';')
                if len(lista)!=0:
                    self.Start(lista)
                else:
                    print("Wrong arguments!")
            if com=='exit':
                break
        
    def ADD(self,lista):
        '''
        This function adds a new element to the list
        '''
        arg=lista[0]
        while True:
            try:
                int(arg)
                lista[0]=arg
                break
            except ValueError:
                arg=input("Give an integer number")
        
        arg=lista[1]
        while True:
            if len(arg)==0:
                arg=input("Give a nonzero text")
            else:
                break
        self._controler.add(lista)
                
                
    def Create(self,lista):
        '''
        This function creates a new file which will contains the corresponding questions
        '''
        print(lista)
        
        if lista[0]=='easy' and int(lista[1])//2<=int(self._controler.geteasy()):
            self._controler.store_quiz(lista[2],lista[0],lista[1])

        elif lista[0]=='medium' and int(lista[1])//2<=int(self._controler.getmedium()):
            self._controler.store_quiz(lista[2],lista[0],lista[1])
        
        elif lista[0]=='hard' and int(lista[1])//2<=int(self._controler.gethard()):
            self._controler.store_quiz(lista[2],lista[0],lista[1])
        
        elif lista[0]!='easy' and lista[0]!='medium' and lista[0]!='hard':
            print("Wrong difficulty!")
        else:
            print("There is not enought questions!")
            
            
            
    def Start(self,lista):
        '''
        This funcion starts a file and the display the corresponding questions
        '''
        res=self._controler.startfile(lista)
        c=0
        t=0
        for i in res:
            print(i[1]," a)",i[2]," b)",i[3]," c)",i[4]," dif:",i[6])
            arg=input("Answer:")
            if arg==i[5] and i[6]=='easy':
                c=c+1
                t=t+1
            elif i[6]=='easy':
                t=t+1
            
            if arg==i[5] and i[6]=='medium':
                c=c+2
                t=t+2
            elif i[6]=='medium':
                t=t+2
            if arg==i[5] and i[6]=='hard':
                c=c+3
                t=t+3
            elif i[6]=='hard':
                t=t+3
        print(c," out of",t)  
                
        
        
        
            
