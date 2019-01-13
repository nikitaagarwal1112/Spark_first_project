'''
Objective   :   Read Training data and train model
Dependency  :	os, numpy, xgboost, pyspark
@author     :	Nikita Agarwal
'''

import os
import numpy as np
import xgboost as xgb

##########################################################################################################
###################################### Description of  variables #########################################
##########################################################################################################

##  path               : The Workspace where train and test files are located and results will be stored
##  model_file_name    : The name of the model file. model.model in this case
##  train_file_name    : The name of the training file.

##########################################################################################################
##########################################################################################################
##########################################################################################################

path = "/home/nikita/test/"
os.chdir(path)

train_file_name = 'train.csv'
model_file_name = 'model.model'

# Read Train datafile
train =  np.genfromtxt(train_file_name, delimiter=',')[1:,1:]

#shuffle data before training
n = np.arange(train.shape[0])
np.random.seed(3)
np.random.shuffle(n)

#80-20 split for train and validation data
m = int(0.8*n.shape[0])

#create XGBoost DMatrix
dtrain = xgb.DMatrix(train[n[0:m],1:6], label=train[n[0:m],5])
dval = xgb.DMatrix(train[n[m:],1:6], label=train[n[m:],5])

#Specify parameters for training
param = {'max_depth':2, 'eta':1, 'verbosity':0, 'objective':'multi:softmax', 'num_class':np.unique(train[:,5]).shape[0]}
watchlist = [(dval, 'eval'), (dtrain, 'train')]

#train and save model
bst = xgb.train(param, dtrain, 10, watchlist)
bst.save_model(model_file_name)
