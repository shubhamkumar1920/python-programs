# writer , Dictwriter
from csv import writer
with open('file3.csv','w',newline = '') as f:
    csv_writer = writer(f)
    # methods -writerow,writerows
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['mohit','INDIA'])
    csv_writer.writerow(['Harshit','INDIA'])

    csv_writer.writerows([['name','country'],['mohit','INDIA'],['Harshit','INDIA']])