# Задайте натуральное число N. Напишите программу,  
# которая составит список простых делителей числа N. (1 - составное число) 

num = int(input("Введите натуральное число N: ")) 
list = []

while num != 1: 
    for i in range(2, num + 1): 
        if(num % i == 0): 
            list.append(i) 
            num = num // i 
print(list) 