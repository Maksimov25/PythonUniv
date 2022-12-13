import random
def paradox(people, num_runs):
    count = 0 #счетчик совпадений
    for i in range(num_runs):
        bdays = []
        for p in range(people):
            bdays.append(random.randint(1, 364))
        if len(set(bdays)) != people: # проверка на совпадения
            count += 1
    return count/(num_runs/100)


print(paradox(60, 1000), '%')