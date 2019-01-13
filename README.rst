Time Series Classification using Spark and XGBoost
===================================================


Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for testing purposes.

Prerequisites
~~~~~~~~~~~~~

-  Python 2.7
	-  Numpy
	-  xgboost (pip install xgboost)
	-  pyspark (pip install pyspark)
-  Apache Spark (https://spark.apache.org/downloads.html)

The code is tested with Apache Spark 2.3.2

How to use
~~~~~~~~~~
For all files please mention the path variable which is location to workspace where train and test files are located.

Trained model has to be created first using training dataset and xgboost (train_model.py). The pre-trained model is provided as file ‘model.model’.

Run the spark streaming code (read_predict.py) 

Generate the data stream files (create_data_stream.py)

Code will generate two folders ‘stream’ and ‘res’ at the provided workspace.

Answers to Questions
--------------------
Briefly describe the conceptual approach you chose! What are the trade-offs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Given time series data in train.csv I have trained a model using xgboost. There are five unique classes and softmax loss is used for multiclass classification. 

What's the model performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The training error is 1.5% and validation error is 1.7%.

What's the runtime performance? What is the complexity? Where are the bottlenecks?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I have created a very simple model with maximum depth of 2. The biggest bottleneck is at while receiving the data stream. If the data is streaming in very slowly, the test-time performance will be low even if the model is very fast.

If you had more time, what improvements would you make, and in what order of priority?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Learn spark properly and have more control over data streaming and processing. I would also like to save all the results in one file instead of separate file for each instance.
2. Experiment with model training and check if all variables are needed for training.
3. If data were to be more complex I would like to experiment using RNN and LSTM for time-series data.


.. _Uncompressed Color Image Dataset: http://www.recod.ic.unicamp.br/~oikawa/datasets.html

