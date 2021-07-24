# reader, DP
# writer,Dictreaderim
from csv import DictReader , DictWriter
with open('file2.csv','r') as rf:
    with open('file4.csv','w',newline ='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_names','lastnames','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age = row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'firstname':fname.upper(),
                'lastname':lname.upper(),
                'age':age
            })