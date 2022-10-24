import numpy as np
import nltk
import csv

with open("test.csv", 'r') as news:
    reader = csv.reader(news)
    for row in reader:
        print(row)
