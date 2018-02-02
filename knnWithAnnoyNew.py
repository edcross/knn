#import h5py
import numpy as np
from annoy import AnnoyIndex
import random
import csv
import os,sys
import time
#---/Split string by row/---


#features = []
features = ""
#with open('Seq1-3_train_xx.csv') as csvfile:
    #readCSV = csv.reader(csvfile, delimiter='\"')

csvfile = open("Seq1-3_train_xx.csv","r")  
start = time.time()
a = AnnoyIndex(2048)
for line in csvfile:
    toks = line.split(",\"")
    idx = int(toks[0].split()[0])
    features = toks[1].split("\"")[0]
    #print (index[0] + "-" + index[1])
    
    
    #indice = int(index[0])
    #features = row[1].split(",")


    caracteristica = []
    for feature in features.split(", "):
        caracteristica.append(float(feature))

    #print(idx)
    #print(len(caracteristica))
    #exit(0)

    a.add_item(idx, caracteristica)
     
a.build(10)
print(time.time()-start)
a.save('Seq1_3time.ann')
print ("algo hizo")

'''
u = AnnoyIndex(2048)
u.load('test.ann') # super fast, will just mmap the file
print(u.get_nns_by_item(2, 2)) # will find the 1000 nearest neighbors
print(u.get_nns_by_vector([1.0, 0.5, 0.5], 10))
#---/end code/---
'''