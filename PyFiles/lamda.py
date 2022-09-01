def my_power_raiser(n):
  return lambda a : a ** n

square_it = my_power_raiser(2)
cube_it = my_power_raiser(3)
quad_it = my_power_raiser(4)

input_number = 3
print('Our input is:', input_number)
print('square_it function raises input by power 2: ', square_it(input_number))
print('cube_it   function raises input by power 3: ', cube_it(input_number))
print('quad_it   function raises input by power 4: ', quad_it(input_number))