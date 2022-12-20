import wk

print(wk.read_file('read_file.txt'))
wk.write_file('save_file.txt', wk.read_file('read_file.txt'))