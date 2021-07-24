# case2:
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

func(first_name = 'harshit',last_name = 'vashistha')