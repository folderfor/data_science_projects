import numpy as np


def random_numer():
    return np.random.randint(1,101)


def random_predict(rnd_numb: int = 1, left: int = 1, right: int = 101, count=0) -> int:
    """Битовый поиск, только со случайными числами"""
    count += 1
    predict_numb = np.random.randint(left, right)
    if predict_numb < rnd_numb:
        left = predict_numb + 1
    elif predict_numb > rnd_numb:
        right = predict_numb
    elif predict_numb == rnd_numb:
        return count
    return random_predict(rnd_numb, left, right, count)


list_ = []
for _ in range(1000):
    list_.append(random_predict(random_numer()))

print(int(np.mean(list_)))


