import csv
import sys
import os

'''
with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'kame', 'last_name': 'hame'})

with open('names.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        print(row['first_name'], row['last_name'])
'''

#write file
'''
with open('beneficiary.csv', 'w') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['user_id', 'username'])
    newFileWriter.writerow([1, 'xyz'])
    newFileWriter.writerow([2, 'pqr'])
'''

'''
#-------/ read txt file /----------


total = len(sys.argv)
cmdargs = str(sys.argv)
print("The total numbers of args passed to the script: %d " % total)
print("Args list: %s " % cmdargs)
# Pharsing args one by one
print("Script name: %s" % str(sys.argv[0]))
print("First argument: %s" % str(sys.argv[1]))
#print("Second argument: %s" % str(sys.argv[2]))

#------/ end read txt file /----------
'''

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



'''

print "argumentos 1: "
print valores[0]
print "argumentos 2: "
print valores[1]

'''

#with open(str(sys.argv[1])) as f:
with open(argumentos[0]) as f:
    my_lines = f.readlines()
    
archivo = my_lines[0]
#print(archivo)
archivo = archivo.replace(",\n","")



#add row to filetra



with open('user.csv', 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([str(valores[1]),archivo])
  

#read file

with open('user.csv', 'r') as userFile:
    userFileReader = csv.reader(userFile)
    userFileReader = userFile
    for row in userFileReader:
        print row