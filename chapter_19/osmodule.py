import os

# os.getcwd   #cwl-current working directory
os.chdir(r'F:\stuff\movies')
# print(os.getcwd())
# os.mkdir('movies')
# print(os.path.exists('movies'))
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')
# open('file.txt','a').close()
# os.mkdir(r'F:\stuff\movies')
# print(os.listdir(r'F:\stuff'))

for item in os.listdir(r'F:\stuff'):
    path  = os.path.join(r'F:\stuff',item)
    print(path)
