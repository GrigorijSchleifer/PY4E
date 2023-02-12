# where is vimrc for v

from ch07.ask_for_file import open_file, ask_for_filename

f_name = ask_for_filename()

with open(f_name, 'r') as f_r:
    text_to_write = open_file(f_r)
    with open('data/file_to_write.txt', 'w') as f_w:
        f_w.write(text_to_write)
    






# where is vimrc for v

from ch07.ask_for_file import open_file, ask_for_filename

f_name = ask_for_filename()

with open(f_name, 'r') as f_r:
    text_to_write = open_file(f_r)
    with open('data/file_to_write.txt', 'w') as f_w:
        f_w.write(text_to_write)
