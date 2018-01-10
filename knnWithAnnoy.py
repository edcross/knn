#import h5py
import numpy as np
from annoy import AnnoyIndex
import random
import csv
import os,sys

#---/Split string by row/---

#features = []
features = ""
with open('tm.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\"')
    
    a = AnnoyIndex(2048)
    for row in readCSV:
        index = row[0].split(",")
       	#print (index[0] + "-" + index[1])
      
      
        indice = int(index[0])
        features = row[1].split(",")

        caracteristica = []
        for feature in features:
            caracteristica.append(float(feature))

        a.add_item(indice, caracteristica)
     
a.build(10)

a.save('test.ann')
print ("algo hizo")

'''
u = AnnoyIndex(2048)
u.load('test.ann') # super fast, will just mmap the file
print(u.get_nns_by_item(2, 2)) # will find the 1000 nearest neighbors
print(u.get_nns_by_vector([1.0, 0.5, 0.5], 10))
#---/end code/---
'''