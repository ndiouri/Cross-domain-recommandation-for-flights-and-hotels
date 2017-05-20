import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error
from math import sqrt

header2 = [u'hotel', u'city', u'location', u'zone', u'star', u'mgrgroup', u'brand',
       u'openyear', u'roomquantity', u'ratingoverall', u'ratingroom',
       u'ratingatmosphere', u'ratingservice', u'ratingcostbenefit',
       u'fromrailway', u'fromairport', u'fromcitycenter', u'fromrailway2',
       u'fromairport2', u'fromcitycenter2', u'lat', u'lon', u'diy_breakfast',
       u'west_breakfast', u'chi_breakfast']

dh = pd.read_table('hotel.csv', sep='\t', names=header2)

n_hotels = dh.hotel.unique().shape[0]


print 'Number of hotels = ' + str(n_hotels)

'''
#Create vector of users id
usersId_vector_Hotel = np.zeros(n_users2)
for line in dh.itertuples():
    usersId_vector_Hotel[line[4]-1] = int(line[4])
print usersId_vector_Hotel


# Print the first row of all the flights with price = 0 .
# The .iloc method on dataframes allows us to index by position.

# Create user-priceHotels matrix :
user_priceHotels = np.zeros((n_users2,3))

for line in dh.itertuples():
        if (line[11] < 1000):
           user_priceHotels[line[4]-1,0] += 1
        elif ( line[11] < 2000):
            user_priceHotels[line[4]-1,1] += 1
        else :
            user_priceHotels[line[4]-1,2] += 1

print user_priceHotels

'''