set_of_complexities: bool = False
lives: int = 0

#количество жизней
def lives_count() -> int:
    difficult: int = int(input('Выберите сложность: 1 - Легкая, 2 - Нормальная, 3 - Сложная '))

    if difficult == 1:
        return 7
    elif difficult == 2:
        return 5
    elif difficult == 3:
        return 3
    else:
        return lives_count()