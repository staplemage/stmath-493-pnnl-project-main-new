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
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

def defTrainData():
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

  # print(len(train_label_list))

