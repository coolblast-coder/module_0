import numpy as np
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")  #условие задания
   
def score_game(game_core): #Функция, которая воспроизводит game_core_v4 1000 раз и 
    #находит среднее количество попыток, за которые находится число
    count_ls = []
    # np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
def game_core_v4 (number):
    count = 1
    predict = 50  #Концепт решения состоит в том, что предикт = 50. Есть несколько степов, с разными величинами шага,
    #чтобы угадать число number
    while number != predict:
        
        if count == 1: #на первом шаге ход изменения предикшн - 25. Большое число, чтобы дальше можно было сужать область поиска
             if number > predict: 
                predict += 25
             elif number < predict: 
                predict -= 25

        if count == 2: #на данном шаге ход изменения предикшн - 15.
            if number > predict: 
                predict += 15
            elif number < predict: 
                predict -= 15

        if count == 3: #на данном шаге ход изменения предикшн - 10.
            if number > predict: 
                predict += 10
            elif number < predict: 
                predict -= 10

        if count == 4: #на данном шаге ход изменения предикшн - 5.
            if number > predict: 
                predict += 5
            elif number < predict: 
                predict -= 5

        if count > 5 or count == 5: #на данном шаге ход изменения предикшн - 1. Этот шаг последний и будет выполняться до
            #тех пор, пока число не найдется
            if number > predict: 
                predict += 1
            elif number < predict: 
                predict -= 1

        count += 1
    return(count)

score_game(game_core_v4)