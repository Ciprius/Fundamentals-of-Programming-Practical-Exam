'''
Created on Jan 27, 2017

@author: Cipri
'''
class Repository:
    def __init__(self,filename):
        self._lista=[]
        self._filename=filename
        self._LoadFromfile(filename)
        
    def _LoadFromfile(self,filename):
        '''
        loads the list of operations from the file
        '''
        f=open(self._filename,"r")
        linie=f.readline().strip()
        while linie!='':
            arg=linie.split(";")
            #print(arg)
            idq=int(arg[0])
            t=idq,arg[1],arg[2],arg[3],arg[4],arg[5],arg[6]
            self._lista.append(list(t))
            linie=f.readline().strip()
        f.close()
        
    def get_list(self):
        return self._lista
    
    def get_easy(self):
        '''
        This function count the number of easy questions
        output:returns the number of easy questions
        '''
        c=0
        for i in self.get_list():
            if i[6]=='easy':
                c=c+1
        #print(c)
        return c
    
    def get_medium(self):
        '''
        This function count the number of medium questions
        output:returns the number of medium questions
        '''
        c=0
        for i in self.get_list():
            if i[6]=='medium':
                c=c+1
        return c
    
    def get_hard(self):
        '''
        This function count the number of hard questions
        output:returns the number of hard questions
        '''
        c=0
        for i in self.get_list():
            if i[6]=='hard':
                c=c+1
        return c    
    
    def store_quizs(self,filename,diff,amount):
        '''
        This function creates a new file which will contain the corresponding questions 
        input:filename-the name of the file, diff-the difficulty, amount-the amount of questions
        '''
        lista=[]
        c=0
        for i in self.get_list():
            if i[6]==diff and c!=int(amount)//2:
                lista.append(list(i))
                c=c+1
                
        #print("I")
        i=0
        c=len(lista)
        while c!=int(amount):
            #print(self._lista[i][6])
            if self._lista[i][6]!=diff:
                lista.append(list(self._lista[i]))
                c=c+1
            i=i+1
                
        #j="D:\Faculta\python projects\lexam"
        filename="D:\\Faculta\\python projects\\lexam"+"\\"+filename
        f=open(filename,'w')
        for i in lista:
            arg1=str(i[0])+";"+str(i[1])+";"+str(i[2])+";"+str(i[3])+";"+str(i[4])+";"+str(i[5])+";"+str(i[6])+"\n"
            f.write(arg1) 
        f.close()
        
    def start_file(self,filename):
        filename="D:\\Faculta\\python projects\\lexam"+"\\"+filename
        f=open(filename,'r')
        linie=f.readline().strip()
        arg1=[]
        while linie!='':
            arg=linie.split(";")
            #print(arg)
            idq=int(arg[0])
            t=idq,arg[1],arg[2],arg[3],arg[4],arg[5],arg[6]
            arg1.append(list(t))
            linie=f.readline().strip()
        f.close()
        return arg1
        

    def add_question(self,lista):
        '''
        This function adds a new element to the list
        '''
        self._lista.append(list(lista))
        self._storeTofile()
        
    def _storeTofile(self):
        '''
        Store to file a new list
        '''
        f=open(self._filename,"w")
        arg=self.get_list()
        for i in arg:
            arg1=str(i[0])+";"+str(i[1])+";"+str(i[2])+";"+str(i[3])+";"+str(i[4])+";"+str(i[5])+";"+str(i[6])+"\n"
            f.write(arg1)
        f.close()
        




        
        
        