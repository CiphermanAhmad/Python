# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import unittest 

def join_names(first, last):
    return ' '.join([first.capitalize(), last.capitalize()])


return_data =  join_names('ahmed', 'hadi')
print(return_data)


class TestStringMethods(unittest.TestCase):
    def test_is_capitalized(self):
        temp1, temp2 = return_data.split(' ')
        self.assertTrue(temp1.istitle())
        self.assertTrue(temp2.istitle())
    
    def test_length(self):
        self.assertTrue(len(return_data.split(' ')), 2)
    
    def test_split(self):
        self.assertEqual(type(return_data), str)

if __name__ == '__main__':
    unittest.main()
    
#testing & debugging exercise:1
class Calculator:
    def addNum(num1 , num2):
        return num1 + num2
    
    def subNum(num1 , num2):
        return num1 - num2
    
    def mulNum(num1 , num2):
        return num1 * num2
    
    def divNum(num1 , num2):
        return num1 / num2
    
    def powNum(num1 , num2):
        return num1 ** num2
    
    def modNum(num1 , num2):
        return num1 % num2
#Perfom Operations:
x = 2
y = 3
return_add = Calculator.addNum(x,y)
return_sub = Calculator.subNum(x,y)
return_mul = Calculator.mulNum(x,y)
return_div = Calculator.divNum(x,y)
return_pow = Calculator.powNum(x,y)
return_mod = Calculator.modNum(x,y)
#print Results:
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