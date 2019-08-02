# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
        
class math_operation:
    def __init__(self):
        print ('Hi')
      
    def add(self, var1, var2):
        sum = var1 + var2
        return sum
        
    def sub(self, var1, var2):
        diff = var1 - var2
        return diff
        
    def mul(self, var1, var2):
        prod = var1 * var2
        return prod
        
    def div(self, var1, var2):
        quo = var1 / var2
        return quo
       
    
if __name__ == '__main__':
    
    var1 = int(input("enter:"))
    var2 = int(input("enter:"))
    
    operation = math_operation()
    print (operation.add(var1, var2))
    print (operation.sub(var1, var2))
    print (operation.mul(var1, var2))
    print ('%.2f' % operation.div(var1, var2))