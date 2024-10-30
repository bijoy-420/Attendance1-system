
from datetime import datetime
import csv



def csv_input(sub,name):
    dt = datetime.now().strftime('%y-%m-%d')
    std_data = [sub,name,dt]
    with open('std_data.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(std_data)

def csv_output():
    with open('std_data.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
while True:
    sub = input('Enter Your Subject ')
    name = input('Enter Your Name: (or type exit to quit) ')      
    if name=="exit":
        break     


    csv_input(sub,name)
    csv_output()
