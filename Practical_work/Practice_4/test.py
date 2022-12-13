def read_file() -> list[str]:

    with open('spis-input.txt', 'r', encoding='utf8') as sp1:
        z: any = str.maketrans('''!()-[]{};?@#$%:'"\,./^&amp;*_''', '                             ')
        r: list = sp1.read().lower().translate(z).split()
        return [i + '\n' for i in r]


def save_file(c: int, n: list):
    with open('spis-output.txt', 'w', encoding='utf8') as sp2:
        sp2.write(str(c) + '\n')
        sp2.writelines(n)


def start():
    inputs: list = sorted(set(read_file()))
    count: int = len(inputs)
    save_file(count, inputs)

    start()