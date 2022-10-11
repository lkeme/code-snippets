import os

'''
批量重命名 文件夹内重复部分文件名

[abc] 01.mp4 -> 01.mp4
[abc] 02.mp4 -> 02.mp4
[abc] 03.mp4 -> 03.mp4
[abc] 04.mp4 -> 04.mp4
'''

if __name__ == '__main__':
    src_words = '关键字'
    root_path = 'your paths'
    files = os.listdir(root_path)
    for file in files:
        if file in ['.', '..']:
            continue
        if src_words in file:
            new_name = file.replace(src_words, "")
            os.rename(f'{root_path}\\{file}', f'{root_path}\\{new_name}',)
            print(file, '->', new_name)
