def a(d):
    f = open(d)
    a = f.readline()
    num_list = f.read().splitlines()
    num_list = [int(i) for i in num_list]
    return num_list
try:
    name = str(input('Введите имя файла: '))
    print(a(name))
except FileNotFoundError:
    print("Такого файла нет!")
    rezultat = False
except NameError:
    print("Такого имени нет!")
    rezultat = False
except ValueError:
    print("Значение в документе не соответсвует числу!")
    rezultat = False
except TypeError:
    print("Несовместимые аргументы!")
    rezultat  = False
except ZeroDivisionError:
    print('Неверные данные для итерации!!')
    rezultat  = False
except MemoryError:
    print("Недостаточно оперативной памяти!")
    rezultat  = False
except StopIteration:
    print("Неверные данные для итерации!*")
    rezultat  = False
except IndexError:
    print("Неверные данные для итерации!/")
    rezultat  = False
except:
    print("Fatality error!")
    rezultat  = False
else:
    print(a(name))
    rezultat = True