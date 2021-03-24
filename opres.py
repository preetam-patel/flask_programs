from excepti import *
class Opera():

    def __init__(self,val_1,val_2):
        self.val_1=val_1
        self.val_2=val_2

    def add(self):
        result= self.val_1+self.val_2
        return result

    def sub(self):
        result= self.val_1-self.val_2
        return result

    def mul(self):
        result= self.val_1*self.val_2
        return result
    
    def div(self):
        result= self.val_1/self.val_2
        return result


