import numpy as np


def game_core(number):
    count = 0
    start = 0
    end = 101
    predict = end // 2
    while number != predict:
        count += 1
        if number > predict:
            start = predict
            predict += (end - predict) // 2
        elif number < predict:
            end = predict
            predict -= (predict - start) // 2

    return count

def score_game(game_core):
    """Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core)