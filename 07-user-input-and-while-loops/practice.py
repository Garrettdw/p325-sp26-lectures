a_value = input('Input an a value: ')
b_value = input('Input a b value: ')
c_value = input('Input a c value: ')

a = float(a_value)
b = float(b_value)
c = float(c_value)

from cmath import sqrt
quadratic_equation1 = (-b + sqrt(b*b - 4*a*c))/2*a
quadratic_equation2 = (-b - sqrt(b*b - 4*a*c))/2*a
print(f'{quadratic_equation1} \n{quadratic_equation2}')