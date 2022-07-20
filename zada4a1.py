# Вычислить число c заданной точностью d 
# Пример: 

# - при d = 3, π = 3.141 

from math import pi 

d =  int(input('Введите число с заданной точностью: ')) 
a = round(pi, d) 
print(a) 