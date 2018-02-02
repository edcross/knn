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
 

    csvfile = open("Seq1-3_train_xx.csv","r")
    
    for line in csvfile:
        toks = line.split(",\"")
        indice = int(toks[0].split()[0])
        categoria = toks[0].split()[1]

        if int(indice) == inde:
            cat = int(categoria)
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
total=int(0)
aciertos=int(0)
u = AnnoyIndex(2048)
u.load('Seq1_3.ann')
resultado = []
categoriaPred = int(0)


#with open('TestData.csv') as csvfile:
#with open('s4.csv') as csvfile:
#with open('s5.csv') as csvfile:     
try:   
    #readCSV = csv.reader(csvfile, delimiter='\"')
    print("Predicted,GT")
    csvfile = open("seq1-3_test_xx.csv","r")
    
    for line in csvfile:
        total += 1
        c = [0,0,0,0,0,0,0,0,0,0]
        contador = []
        toks = line.split(",\"")
        indice = int(toks[0].split()[0])
        features = toks[1].split("\"")[0]
        #index = row[0].split(",")
        categoria = toks[0].split()[1]
       	#print (index[0] + "-" + index[1])
            

        #features = row[1].split(",")
        

        caracteristica = []
        for feature in features.split(", "):
            caracteristica.append(float(feature))

          
        #print(u.get_nns_by_item(indice, 5)) # will find the 1000 nearest neighbors
        #print(features)
        resultado = u.get_nns_by_vector(caracteristica, 3)

        #print("vector: ")
        #print(resultado)
        
        #print(u.get_nns_by_vector(caracteristica, 5))
        for dato in resultado:
            
            categoriaPred = int(IndexFinding(dato))
            contador = MasVotado(int(categoriaPred - 1))
            #print(dato)
            #print(contador)
            #print("GT: "+ str(categoria))
            #print("Pred: "+ str(categoriaPred))
        
        winner = np.argmax(contador)
        predic = winner + 1
        #print (predic)
        #print (categoria)
        #print(str(total)+"-"+str(aciertos))
        if int(categoria) == int(predic):
            aciertos+=1

        print(str(int(winner+1))+","+str(categoria))    
        #print(contador)
        #print(str(total)+"-"+str(aciertos))

except Exception as e:
    print(e)
    print("Ta to flama killo")
    exit(0)
print("algo hizo killo")
print(float(total))
print(float(aciertos))        
print(float(float(aciertos)/float(total)))
