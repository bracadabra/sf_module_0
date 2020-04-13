import numpy as np


def game_core(number):
    """Guess a number with binary search

    Keyword arguments:
    number -- number to guess

    """
    
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
    """Launch game 1000 time to know how fast it guesses a number"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in {score} attempts")
    return score


# Launch
score_game(game_core)
