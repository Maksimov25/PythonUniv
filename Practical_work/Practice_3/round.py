import prog_sis as ps
import lives as l
import word_processor as wp


def win_round() -> None:
    print('Вы выиграли!')

    ps.current_session_record += 1

    if ps.current_session_record > ps.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(ps.current_session_record))
        ps.record = ps.current_session_record
        ps.update_record()


def start_game() -> None:
    lives_count: int = 0
    if not l.is_difficult_set:
        lives_count = l.get_lives_count_by_difficult()
        l.lives = lives_count
        l.is_difficult_set = True
    else:
        lives_count = l.lives
    current_word: str = ps.get_random_word()
    locked_word: str = wp.lock_word(current_word)

    while True:
        print(f'{locked_word} | {ps.heart_symbol}x{lives_count}')
        answer: str = input('Назовите букву или слово целиком: ')

        if answer == current_word:
            win_round()
            break
        elif answer in current_word:
            if answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = wp.unlock_part_of_word(current_word, locked_word, answer)

            if ps.locked_symbol not in locked_word:
                win_round()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lives_count -= 1

        if lives_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(ps.record))
            break