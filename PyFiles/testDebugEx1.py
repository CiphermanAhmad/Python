# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:03:32 2022

@author: Momin-PC
"""

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

#Testing
import unittest
#test cases
class testCalculations(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(isinstance(return_add, int))
    def testSub(self):
        self.assertTrue(isinstance(return_sub, int))
    def testMul(self):
        self.assertTrue(isinstance(return_mul, int))
    def testDiv(self):
        self.assertTrue(isinstance(return_div, float))
    def testPow(self):
        self.assertTrue(isinstance(return_pow, int))
    def testMod(self):
        self.assertTrue(isinstance(return_mod, int))
#Exe Tests        
if __name__ == '__main__':
        unittest.main()
        
#Use case for fail
return_add = 2.3
return_sub =3.2
return_mul = '3'
return_div = 2
return_pow = "3"
return_mod = Calculator()

if __name__ == '__main__':
        unittest.main()        