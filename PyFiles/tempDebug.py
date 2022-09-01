# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:03:12 2022

@author: Momin-PC
"""

import pdb

def sum_values(a, b):
    return a + b

def test_function():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = sum_values(2, 3)
    print('The code is done!')
    return value 


test_function()


#testing & debugging exercise:1
import pdb
class Calculator:
    def addNum(num1 , num2):
        pdb.set_trace()
        print('Add Method has been called')
        value = num1 + num2
        print('Add Method has been operated')
        return value
    
    def subNum(num1 , num2):
        pdb.set_trace()
        print('Sub Method has been called')
        value = num1 - num2
        print('Sub Method has been operated')
        return value
    
    def mulNum(num1 , num2):
        pdb.set_trace()
        print('Mul Method has been called')
        value = num1 * num2
        print('Mul Method has been operated')
        return value
    
    def divNum(num1 , num2):
        pdb.set_trace()
        print('Div Method has been called')
        value = num1 / num2
        print('Div Method has been operated')
        return value
    
    def powNum(num1 , num2):
        pdb.set_trace()
        print('Pow Method has been called')
        value = num1 ** num2
        print('Div Method has been operated')
        return value
    
    def modNum(num1 , num2):
        pdb.set_trace()
        print('Mod Method has been called')
        value = num1 % num2
        print('Div Method has been operated')
        return value
x = 2
y = 3
return_add = Calculator.addNum(x,y)
return_sub = Calculator.subNum(x,y)
return_mul = Calculator.mulNum(x,y)
return_div = Calculator.divNum(x,y)
return_pow = Calculator.powNum(x,y)
return_mod = Calculator.modNum(x,y)
print('Results : ')
print('Addition : ',return_add)
print('Subtraction : ',return_sub)
print('Multiplication : ',return_mul)
print('Division  ',return_div)
print('Power : ',return_pow)
print('Modulus : ',return_mod)