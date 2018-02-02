""" This script demonstrates the use of a convolutional LSTM network.
This network is used to predict the next frame of an artificially
generated movie which contains moving squares.
"""
import re
import collections
import os
from tensorflow.python.client import device_lib

from os import listdir
from os.path import isfile, join
from keras.utils import np_utils
from tensorflow.python.client import device_lib
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import sys
import argparse
import resnet50
import h5py
from keras.optimizers import Nadam
from keras.optimizers import rmsprop

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Dataset Path")
parser.add_argument("save", help="Path to save the extracted Features")
args = parser.parse_args()

print 'Argumentos Recibidos'
print args.path
print args.save


os.environ["CUDA_VISIBLE_DEVICES"]=""
print device_lib.list_local_devices()


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def readDataset(path):
    #print "entre"
    path1 = path
    imgList = [join(path1, f) for f in listdir(path1) if isfile(join(path1, f)) and "png" in f ]
    imgList = natural_sort(imgList)
    print("Images: "+str(len(imgList)))

    return imgList

#carpeta con tu dataset
pathToTest = str(args.path)

# instancias la red (copiar lo que tienes)

model = resnet50.ResNet50()
optimize = rmsprop(lr=0.0001)


#model = ResNet50(weights='imagenet', include_top=False)
#model.load_weights("/home/ed/Desktop/knn-test/ep_22.hdf5")
model.load_weights("/home/rovit01/Escritorio/sequences_cat3/resnet50/Base/snapsep_194.hdf5")

#model.summary()

model.summary()
#model.layers.pop()
model.layers.pop()
model.outputs = [model.layers[-1].output]
# added this line in addition to zo7 solution
model.output_layers = [model.layers[-1]]
model.layers[-1].outbound_nodes = []
#model.summary()


model.compile(loss='categorical_crossentropy',
              optimizer=optimize, metrics=['accuracy'])

# devuelve lista de nombres de ficheros
datasetX = readDataset(pathToTest) #
print len(datasetX)
print "Extranting"

for i in range(0,len(datasetX)):
    img_path = datasetX[i] # leer image, preprocess, ...
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print preds.shape
    reshaped_features = preds.reshape(1, -1)
    #-----------------------
    print "Preds 1: "
    print preds
    print "\n"
    print "reshaped 2: "
    print reshaped_features
    #----------------------
    #path to save
    words = datasetX[i].split("/") 
    name= words[len(words)-1].split(".")[0]
    #filename = str(args.save) +"/"+name+'.txt'
    filename = str(args.save) +name+'.txt'
    print filename
    #print reshaped_features
    #np.savetxt(filename, reshaped_features, '%.12f\n')
    np.savetxt(filename, reshaped_features, '%.12f,')
    print 'Feature for ' +datasetX[i]+ 'saved.\n' 
