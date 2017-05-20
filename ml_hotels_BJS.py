import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error
from math import sqrt

header2 = [u'orderdate', u'room', u'hotel', u'uid', u'customereval', u'custtype',
           u'ordpersons', u'ordroomnum', u'averecommendlevel', u'orddays',
           u'ciiamount']

dh = pd.read_table('hotel_order_BJS.csv', sep='\t',parse_dates=True, low_memory=False, names=header2, header=None, usecols=header2)


n_users2 = dh.uid.unique().shape[0]
n_hotels = dh.hotel.unique().shape[0]
n_ciiamount = dh.ciiamount.unique().shape[0]

print 'Number of hotels = ' + str(n_hotels) + ' Number of users = ' + str(n_users2)
#Number of hotels = 11640 Number of users = 8107

#print dh.loc[[1],['hotel']]


#uid_hotel = pd.Series(dh['hotel'])

# Create Matrix : Uid Hotel + Price Hotel
uidHotel_PriceHotel = np.zeros((n_hotels,2))

#dhotel_price = ( uidHotel_PriceHotel, index_col=False, usecols=['hotel','price'] )

for x in range(len(dh)):


for line in dh.iteritems():
    uidHotel_PriceHotel[int(line[3]-1),0]  = int(line[3])
    uidHotel_PriceHotel[line[11]-1,1] = line[11]


'''
#Create vector of users id
usersId_vect = np.zeros(n_users2)
for line in dh.itertuples():
    usersId_vect[int(line[4]-1)] = int(line[4])


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

'''



