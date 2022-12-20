import db_m
import logs
import dif_sel


def win_round() -> None:
    print('Вы выиграли! Приз в студию!')

    db_m.current_session_record += 1

    if db_m.current_session_record > db_m.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(db_m.current_session_record))
        db_m.record = db_m.current_session_record
        db_m.update_record()


def start_game() -> None:
    lives_count: int = 0
    if not logs.is_difficult_set:
        lives_count = logs.get_lives_count_by_difficult()
        logs.lives = lives_count
        logs.is_difficult_set = True
    else:
        lives_count = logs.lives
    current_word: str = db_m.get_random_word()
    locked_word: str = dif_sel.lock_word(current_word)

    while True:
        print(f'{locked_word} | {db_m.heart_symbol}x{lives_count}')
        player_answer: str = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            win_round()
            break
        elif player_answer in current_word:
            if player_answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = dif_sel.unlock_part_of_word(current_word, locked_word, player_answer)

            if db_m.locked_symbol not in locked_word:
                win_round()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lives_count -= 1

        if lives_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(db_m.record))
            break