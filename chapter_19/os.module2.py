import os
import shutil
os.chdir(r'G:\python\chapter_19')
print(os.listdir())
fileiter = os.walk(r'G:\python\chapter_19')
for current_path,folder_names,file_names in fileiter:
    print(f'current path : {current_path}')
    print(f'folder names : {folder_names}')
    print(f'file names : {file_names}')

# os.makedirs('new/movies')
shutil.rmtree('songs')
shutil.copytree('new','documents/new')
shutil.copy('file.txt','documents/file.txt')
shutil.move('file.txt','new/file2.txt')
shutil.move('new','documents/new2')