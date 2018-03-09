'''
Created on Jan 27, 2017

@author: Cipri
'''

class Controller:
    def __init__(self,controller):
        self._controller=controller
        
    def add(self,lista):
        '''
        This function adds a new element to the list
        '''
        self._controller.add_question(lista)
        
    def geteasy(self):
        '''
        This function verify the number of easy questions
        output:the number of easy questions
        '''
        return self._controller.get_easy()
        
    def getmedium(self):
        '''
        This function verify the number of medium questions
        outout:the number of medium questions
        '''
        return self._controller.get_medium()
        
    def gethard(self):
        '''
        This function verify the number of hard questions
        outout:the number of hard questions
        '''
        return self._controller.get_hard()
        
    def store_quiz(self,filename,diff,amount):
        '''
        This function 
        '''
        self._controller.store_quizs(filename,diff,amount)
        
    def startfile(self,lista):
        return self._controller.start_file(lista)