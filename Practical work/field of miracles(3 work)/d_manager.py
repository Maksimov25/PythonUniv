import random

symbol: str = '\u25A0'

current_session_record: int = 0
record: int = 0

with open("record.db", encoding='UTF-8') as r:
    record = int(r.read())

words_list: list = []
with open('words.db', encoding='UTF-8') as wd:
    words_list = wd.read().splitlines()


def random_word() -> str: #случайное слово из базы данных слов, которое нужно угадать.
    word: str = random.choice(words_list)
    words_list.remove(word)
    return word

def record() -> None:#Функция обновляет значение рекорда за одну сессию.
    with open('record.db', encoding='UTF-8', mode='w') as r:
        r.write(str(record))