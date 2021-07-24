def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

    # dictionary unpacking
d = {'name':'harshit','age':24}
func(**d)