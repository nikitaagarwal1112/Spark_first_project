'''
Objective   :   Read data stream using Spark and predict the class for data point
Dependency  :	os, numpy, xgboost, pyspark
@author     :	Nikita Agarwal
'''

import os
import numpy as np
import xgboost as xgb
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

##########################################################################################################
###################################### Description of  variables #########################################
##########################################################################################################

##  path               : The Workspace where train and test files are located and results will be stored
##  model_file_name    : The name of the model file. model.model in this case

##########################################################################################################
##########################################################################################################
##########################################################################################################

path = "/home/nikita/test/"

# makes prediction from given model and data vector 
def prediction(model, vector):    
    vector = vector.split(',')
    vector = np.array(vector)[np.newaxis,:]
    vector[vector==''] = np.NaN

    dvector = xgb.DMatrix(vector)
    pred  = model.predict(dvector)
    
    return pred
    
#stream data using spark and cal prediction function.
def stream(model):    
    sc = SparkContext(appName="TimeSeriesStreaming")
    ssc = StreamingContext(sc, 1)
    lines = ssc.textFileStream(path+'stream')
    vector = lines.flatMap(lambda line: prediction(model, line))
    vector.pprint()
    vector.saveAsTextFiles(path+'res/res')
    ssc.start()
    ssc.awaitTermination()
    
#load model
model_file_name = 'model.model'
model = xgb.Booster(model_file = path + model_file_name)

#create directory (is not there) where stream data will be stored.
if not os.path.exists(path+'stream'):
    os.makedirs(path+'stream')

#create result directory (if not there) where the result will be stored.
if not os.path.exists(path+'res'):
    os.makedirs(path+'res')
stream(model)

    
    
    
