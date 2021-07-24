# else and finally clause in exception handling
while True:
    try:
        number = int(input('enter a number:  '))
        break

    except ValueError:
        print("please type integer !!  s")
    except:
        print('unexcepted error !!!')
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks .....')