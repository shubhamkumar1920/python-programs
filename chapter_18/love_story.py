with open('love_story.txt','r', encoding ='UTF-8') as f:
    print(f.encoding)
    data = f.read()
    print(data)