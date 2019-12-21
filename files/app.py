import pandas
import os
import time

while True:
    if(os.path.exists("files/temp_today.csv")):
        data = pandas.read_csv("files/temp_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10)