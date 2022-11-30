bool = False
lives = int(0)

def lives_count_diff() -> int: #количество жизней зависит от сложности игры
    difficult = int(input('Выберите сложность: 1 - Легкая, 2 - Нормальная, 3 - Сложная '))
    if difficult == 1:
        return 10
    elif difficult == 2:
        return 3
    elif difficult == 3:
        return 2
    else:
        print('Ты не будешь играть')
        return lives_count_diff()