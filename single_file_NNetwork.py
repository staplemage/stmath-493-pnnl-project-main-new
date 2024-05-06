#Training the image classifier
import torch
import torchvision
import torchvision.transforms as transforms
from Bio.Seq import Seq
import os
import glob
import pathlib
import pickle
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def train_data():
    #Building training data
    strep_train = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\training data\\strep_train.txt', 'rb'))
    lacto_train = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\training data\\lacto_train.txt', 'rb'))
    bac_train = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\training data\\bac_train.txt', 'rb'))
    pseudo_train = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\training data\\pseudo_train.txt', 'rb'))

    strep_train = strep_train[:len(strep_train)//2]
    lacto_train = lacto_train[:len(lacto_train)//2]
    bac_train = bac_train[:len(bac_train)//2]
    pseudo_train = pseudo_train[:len(pseudo_train)//2]


    strep_train_array = np.asarray(strep_train)
    strep_train_array = np.reshape(strep_train_array, [len(strep_train_array), 1, 64, 64])
    # print(strep_train_array.shape)

    lacto_train_array = np.asarray(lacto_train)
    lacto_train_array = np.reshape(lacto_train_array, [len(lacto_train_array), 1, 64, 64])
    # print(lacto_train_array.shape)

    bac_train_array = np.asarray(bac_train)
    bac_train_array = np.reshape(bac_train_array, [len(bac_train_array), 1, 64, 64])
    # print(bac_train_array.shape)

    pseudo_train_array = np.asarray(pseudo_train)
    pseudo_train_array = np.reshape(pseudo_train_array, [len(pseudo_train_array), 1, 64, 64])
    # print(pseudo_train_array.shape)

    train_full_list = np.concatenate((strep_train_array, lacto_train_array, bac_train_array, pseudo_train_array))

    # print(train_full_list.shape)

    # print(strep_train_array[5])

    # print(train_full_list[5])

    label_bac = np.ones(len(bac_train_array)) * 1
    label_lacto = np.ones(len(lacto_train_array)) * 2
    label_pseudo = np.ones(len(pseudo_train_array)) * 3
    label_strep = np.ones(len(strep_train_array)) * 4

    train_label_list = np.concatenate((label_strep, label_lacto, label_bac, label_pseudo))

    # f = open("train_full_list.txt", "wb")
    # pickle.dump(train_full_list, f)
    # print("Done")
    # f.close()

    # f = open("train_label_list.txt", "wb")
    # pickle.dump(train_label_list, f)
    # print("Done")
    # f.close()

    # print(len(train_label_list))

def test_data():
    # Building testing data
    strep_test = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\testing data\\strep_test.txt', 'rb'))
    lacto_test = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\testing data\\lacto_test.txt', 'rb'))
    bac_test = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\testing data\\bac_test.txt', 'rb'))
    pseudo_test = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\testing data\\pseudo_test.txt', 'rb'))

    strep_test = strep_test[:len(strep_test)//2]
    lacto_test = lacto_test[:len(lacto_test)//2]
    bac_test = bac_test[:len(bac_test)//2]
    pseudo_test = pseudo_test[:len(pseudo_test)//2]

    strep_test_array = np.asarray(strep_test)
    strep_test_array = np.reshape(strep_test_array, [len(strep_test_array), 1, 64, 64])
    print(strep_test_array.shape)

    lacto_test_array = np.asarray(lacto_test)
    lacto_test_array = np.reshape(lacto_test_array, [len(lacto_test_array), 1, 64, 64])
    print(lacto_test_array.shape)

    bac_test_array = np.asarray(bac_test)
    bac_test_array = np.reshape(bac_test_array, [len(bac_test_array), 1, 64, 64])
    print(bac_test_array.shape)

    pseudo_test_array = np.asarray(pseudo_test)
    pseudo_test_array = np.reshape(pseudo_test_array, [len(pseudo_test_array), 1, 64, 64])
    print(pseudo_test_array.shape)

    test_full_list = np.concatenate((strep_test_array, lacto_test_array, bac_test_array, pseudo_test_array))

    print(test_full_list.shape)

    # print(strep_test_array[5])

    # print(test_full_list[5])

    label_bac = np.ones(len(bac_test_array)) * 1
    label_lacto = np.ones(len(lacto_test_array)) * 2
    label_pseudo = np.ones(len(pseudo_test_array)) * 3
    label_strep = np.ones(len(strep_test_array)) * 4

    test_label_list = np.concatenate((label_strep, label_lacto, label_bac, label_pseudo))

    # f = open("test_full_list.txt", "wb")
    # pickle.dump(test_full_list, f)
    # print("Done")
    # f.close()

    # f = open("test_label_list.txt", "wb")
    # pickle.dump(test_label_list, f)
    # print("Done")
    # f.close()

def import_all():
    train_full_list = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\train_final_data\\train_full_list.txt', 'rb'))
    train_label_list = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\train_final_data\\train_label_list.txt', 'rb'))
    test_full_list = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\test_final_data\\test_full_list.txt', 'rb'))
    test_label_list = pickle.load(open('C:\\Users\\patri\\Desktop\\pnnl single position here\\test_final_data\\test_label_list.txt', 'rb'))

import_all()

def build_train():
    # Building training dataset
    # use x_train and y_train as numpy array without further modification
    x_train = np.array(train_full_list)
    y_train = np.array(train_label_list)

    # convert to numpys to tensor
    tensor_x = torch.Tensor(x_train)
    tensor_y = torch.Tensor(y_train)
    # create the dataset
    trainset = TensorDataset(tensor_x,tensor_y) 
    # create your dataloader
    trainloader = DataLoader(trainset,batch_size=64, shuffle=True) 

    #check if you can get the desired things
    i1, l1 = next(iter(trainloader))
    print(i1.shape)   # torch.Size([64, 1, 64, 64]) 
    print(l1.shape)   # torch.Size([64]) 

build_train()

def build_test():
    # Building testing dataset

    # use x_train and y_train as numpy array without further modification
    x_test = np.array(test_full_list)
    y_test = np.array(test_label_list)

    # convert to numpys to tensor
    tensor_x1 = torch.Tensor(x_test)
    tensor_y1 = torch.Tensor(y_test)
    # create the dataset
    testset = TensorDataset(tensor_x1,tensor_y1) 
    # create your dataloader
    testloader = DataLoader(testset,batch_size=64, shuffle=True) 

    #check if you can get the desired things
    i2, l2 = next(iter(testloader))
    print(i2.shape)   # torch.Size([64, 1, 64, 64]) 
    print(l2.shape)   # torch.Size([64]) 

build_test()

#define batch size
batch_size = 64
#define classes
classes = tensor_y1

