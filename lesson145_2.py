def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

func('mohit',first_name='Shubham',last_name='Kumar')