import random

number = random.randint(1,100)
userNumber = -1
counter = 0

while number != userNumber:
    try:
        userNumber = int(input('Я загадал число от 1 до 100. Угадайте его: '))
        if userNumber >  number:
            counter += 1
            print('Число должно быть меньше! Попробуйте еще раз!')
        elif userNumber < number:
            counter += 1
            print('Число должно быть больше! Попробуйте еще раз!')
        elif userNumber == number:
            counter += 1
            print(f'Верно! Вы угадали число с {counter} попыток!')
    except:
        print('Вы ввели не число! Попробуйте еще раз!')
