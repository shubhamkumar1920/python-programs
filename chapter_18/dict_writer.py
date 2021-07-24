from csv import DictWriter
with open('final.csv','w') as f:
    csv_writer = DictWriter(f,fieldnames = ['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow,writerows
    csv_writer.writerow({
        'firstname':'harshit',
        'lastname':'vashistha',
        'age':'500'
    })
    csv_writer.writerow({
        'firstname':'mohit',
        'lastname':'vashistha',
        'age':500
    })

    # writerows  ---> [dict,dict,dict]
    csv_writer.writerows([
        {'firstname':'harshit','lastname':'vashistha','age':500},
        {'firstname':'harshit','lastname':'vashistha','age':500},
        {'firstname':'harshit','lastname':'vashistha','age':500}


    ])