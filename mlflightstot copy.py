import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error
from math import sqrt

header1 = [u'uid', u'flightno', u'airline', u'dcity', u'acity', u'aport', u'dport',
       u'class', u'price', u'craftkind', u'takeofftime', u'arrivaltime',
       u'quantity']



df = pd.read_csv('flights_without_header.csv', sep='\t', names=header1)


n_users = df.uid.unique().shape[0]
n_airline = df.airline.unique().shape[0]
n_dcity = df.dcity.unique().shape[0]
n_price = df.price.unique().shape[0]


print 'Number of users = ' + str(n_users) +' | Number of airlines = ' + str(n_airline) +' | Number of destination cities = ' + str(n_dcity)

#Create vector of airline numbers
airline_vector = np.zeros(n_airline)
for line in df.itertuples():
    airline_vector[line[3]-1] = int(line[3])
##print airline_vector

#Create vector of users id
usersId_vector = np.zeros(n_users)
for line in df.itertuples():
    usersId_vector[line[1]-1] = int(line[1])
##print usersId_vector

#Create user-airline matrix
user_airline_matrix = np.zeros((n_users, n_airline))
for line in df.itertuples():
    if ((line[3] == airline_vector[line[3]-1]) & (line[1] == usersId_vector[line[1]-1])):
        user_airline_matrix[int(line[1])-1, int(line[3])-1] = 1
    else:
        user_airline_matrix[int(line[1])-1, int(line[3])-1] = 0
print user_airline_matrix


