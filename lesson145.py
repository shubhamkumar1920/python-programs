# kwargs(keyword argumnets)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(first_name = 'harshit',last_name = 'vashistha')