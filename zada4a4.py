# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран. 
# Пример: 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 

from random import randint 

def RandomNum(k): 
    result = '' 
    for i in range(k, -1, -1): 
        if i == 0: 
            result = result + str(randint(0, 100)) 

        else: 
            result = result + f'{randint(0, 100)} x^{i} + ' 
    return(result) 

k = int(input('Введите k: ')) 
result = RandomNum(k) 
print(result) 