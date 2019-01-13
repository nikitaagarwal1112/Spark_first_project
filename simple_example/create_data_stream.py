'''
Objective   :   Create New Files for data stream
Dependency  :	os, time, random
@author     :	Nikita Agarwal
'''

from random import randint
import time
import os

##########################################################################################################
###################################### Description of  variables #########################################
##########################################################################################################

##  path               : The Workspace where train and test files are located and results will be stored
##  test_file_name     : The name of the test file. test.csv in this case

##########################################################################################################
##########################################################################################################
##########################################################################################################



path = "/home/nikita/test/"
test_file_name = 'test.csv'

a = 1
f = open(path+test_file_name, 'r')
lines = f.readlines()

if not os.path.exists(path+'stream'):
    os.makedirs(path+'stream')
    
for i in range(1,len(lines)):
    wf = open(path+'stream/data_point'+str(i)+'.txt', 'w')
    wf.write(','.join(lines[i].split(',')[1:]))
    wf.close()
    time.sleep(5)



