import csv
import sys
import os

#append row to file
archivo = ""
#NameFile = str(sys.argv)
line = str(sys.argv[1])
argumentos = line.split(';')
valores = ["",""]
i = 0

for arg in argumentos:
    
    #print arg
    valores[i]=str(arg)
    i = i + 1
    if i==2:
        i=0


#with open(str(sys.argv[1])) as f:
with open(valores[0]) as f:
    my_lines = f.readlines()
    
archivo = my_lines[0]
#print(archivo)
archivo = archivo.replace(",\n","")


#add row to filetra


with open('test.csv', 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([str(valores[1]),archivo])

print "|-----------/Listo/------------|"  

'''
#read file

with open('user.csv', 'r') as userFile:
    userFileReader = csv.reader(userFile)
    userFileReader = userFile
    for row in userFileReader:
        print row

'''
