#import h5py
import numpy as np
from annoy import AnnoyIndex
import random
import csv
import os,sys

#---/Split string by row/---

#features = []
features = ""
u = AnnoyIndex(2048)
u.load('test.ann')

with open('TestData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\"')
    
    for row in readCSV:
        index = row[0].split(",")
        categoria = index[1]
       	#print (index[0] + "-" + index[1])
            
        indice = int(index[0])
        features = row[1].split(",")

        caracteristica = []
        for feature in features:
            caracteristica.append(float(feature))

        print(indice)
        print("Cat: "+ categoria)
        print(u.get_nns_by_item(indice, 5)) # will find the 1000 nearest neighbors
        #print(features)
        print(u.get_nns_by_vector(caracteristica, 5))
    