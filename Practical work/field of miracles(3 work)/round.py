import d_manager as d_m
import difficult as d
import word_handler as w_h

def win_round() -> None:
    print('Вы выиграли! Приз в студию!')
    d_m.current_session_record += 1

    if d_m.current_session_record > d_m.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(d_m.current_session_record))
        d_m.record = d_m.current_session_record
        d_m.update_record()

def start_game() -> None:
    lives_count = int(0)
    if not d.is_difficult_set:
        lives_count = d.get_lives_count_by_difficult()
        d.lives = lives_count
        d.is_difficult_set = True
    else:
        lives_count = d.lives
    current_word: str = d_m.get_random_word()
    locked_word: str = w_h.lock_word(current_word)

    while True:
        print(f'{locked_word} {d_m.heart_symbol}x{lives_count}')
        player_answer: str = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            win_round()
            break
        elif player_answer in current_word:
            if player_answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = w_h.unlock_part_of_word(current_word, locked_word, player_answer)

            if d_m.locked_symbol not in locked_word:
                win_round()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lives_count -= 1

        if lives_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(d_m.record))
            break