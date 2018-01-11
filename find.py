#import h5py
import numpy as np
from annoy import AnnoyIndex
import random
import csv
import os,sys



#--------------

c = [0,0,0,0,0,0,0,0,0,0]

def IndexFinding(inde):  
    cat=int(0)
    with open('Index_Cat.csv') as csvfile:
        #readCSV = csv.reader(csvfile, delimiter='\"')
        readCSV = csv.reader(csvfile, delimiter=';')
        #readCSV = csv.reader(csvfile)
    
        for index in readCSV:
        
            if int(index[0]) == inde:
                cat = int(index[1])
       	        #print (index[0] + "-" + index[1]+"-" +str(inde))
                break
                                   
    return cat           

#--------------

def MasVotado(n):
    num = n+1
    if num == 1:
        c[n] = c[n] + 1
    else:
        if num  == 2:
            c[n] = c[n] + 1
        else:
            if num  == 3:
                c[n] = c[n-1] + 1
            else:
                if num == 4:
                    c[n] = c[n] + 1
                else:
                    if num == 5:
                        c[n] = c[n] + 1
                    else:
                        if num == 6:
                            c[n] = c[n] + 1
                        else:
                            if num == 7:
                                c[n] = c[n] + 1
                            else:
                                if num == 8:
                                        c[n] = c[n] + 1
                                else:
                                    if num == 9:
                                        c[n] = c[n] + 1
                                    else:
                                        if num == 10:
                                            c[n] = c[n] + 1
    return c

#---------------

#---/Split string by row/---

#features = []
features = ""
u = AnnoyIndex(2048)
u.load('test.ann')
resultado = []
categoriaPred = int(0)


with open('TestData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\"')
    
    
    for row in readCSV:
        c = [0,0,0,0,0,0,0,0,0,0]
        contador = []
        index = row[0].split(",")
        categoria = index[1]
       	#print (index[0] + "-" + index[1])
            
        indice = int(index[0])
        features = row[1].split(",")
        

        caracteristica = []
        for feature in features:
            caracteristica.append(float(feature))

          
        #print(u.get_nns_by_item(indice, 5)) # will find the 1000 nearest neighbors
        #print(features)
        resultado = u.get_nns_by_vector(caracteristica, 5)

        print("vector: ")
        print(resultado)

        #print(u.get_nns_by_vector(caracteristica, 5))
        for dato in resultado:
            
            categoriaPred = int(IndexFinding(dato))
            contador = MasVotado(int(categoriaPred - 1))
            print(dato)
            #print(contador)
            #print("GT: "+ str(categoria))
            #print("Pred: "+ str(categoriaPred))
        print("Pred: ")    
        winner = np.argmax(contador)
        print(winner)    
        print(contador)
    
