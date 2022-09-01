#Decorators Practice
#WrapperFunction
def validateInput(func):
    def check(*args,**kargs):
        print("The method called is : ",func.__name__)
        #write on file : log
        returned_value = func(*args,**kargs)
        print('Execution of the method is completed')
        return returned_value
    return check

#WrappingFunctions
@validateInput
def productOp(x,y):
    return x * y
@validateInput    
def divOp(x,y):
    return x /y

#Work
x = 2
y = 3
print("Product of {} and {} is {}".format(x,y,productOp(x,y)))
print("DivisionProduct of {} and {} is {}".format(x,y,divOp(x,y)))
 