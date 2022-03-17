"""Игра угадай число
компьютер сам угадывает число меньше чем за 20 попыток
"""

import numpy as np

number = np.random.randint(1,101) #загадай число

print('Задуманное чиско: ', number)

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number = 1
    max_number = 100
    number_predict = max_number / 2
    
    while number != number_predict:
        count+=1
 
        if number > number_predict: 
            min_number = number_predict
            number_predict = (max_number + min_number)//2
        elif number < number_predict: 
            max_number = number_predict
            number_predict = (max_number + min_number)//2
        
    return(count)

print(f'Количество попыток: {random_predict()}')

