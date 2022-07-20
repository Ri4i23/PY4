# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 

from random import randint 

def AllElements(array): 
    for i in range(len(array)): 
        array[i] = randint(0, len(array)) 
    print(array) 

def OrderElem(arr): 
    num = [] 
    for i in range(len(arr)): 
        if arr.count(arr[i]) == 1: 
            num.append(arr[i]) 
    print(num) 

n = int(input('Введите размер последовательности: ')) 
numbers = [''] * n 
AllElements(numbers) 
OrderElem(numbers) 