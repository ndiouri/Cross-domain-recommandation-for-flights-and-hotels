# Import the pandas library.
import pandas
# Import matplotlib
import matplotlib.pyplot as plt
# Import the kmeans clustering model.
from sklearn.cluster import KMeans
# Import the PCA model.
from sklearn.decomposition import PCA

# Read in the data.
flightsSH = pandas.read_table("data_flight_BJS_18_num.csv")

"""
# Print the names of the columns in games.
print(flightsSH.columns) 

Index([u'uid', u'flightno', u'airline', u'dcity', u'acity', u'aport', u'dport',
       u'class', u'price', u'craftkind', u'takeofftime', u'arrivaltime',
       u'quantity'],
      dtype='object')
      
print(flightsSH.shape) 
 

"""

# Normalization of data - price

def normalization()
	for (flishtsSH["price"]< )
	for (flishsH 

# Make a histogram of all price.
#plt.hist(flightsSH["price"])
#plt.hist(flightsSH["quantity"])

# Show the plot.
#plt.show()

# Print the first row of all the flights with price = 0 .
# The .iloc method on dataframes allows us to index by position.
#print(flightsSH[flightsSH["price"] == 0].iloc[0])

# Remove any rows with price 0 .
#flights = flightsSH[flightsSH["price"] > 0]

# Initialize the model with 2 parameters -- number of clusters and random state.
kmeans_model = KMeans(n_clusters=5, random_state=1)
# Get only the numeric columns from games.
good_columns = flightsSH._get_numeric_data()
print good_columns.columns
# Fit the model using the good columns.
kmeans_model.fit(good_columns)
# Get the cluster assignments.
labels = kmeans_model.labels_

# Create a PCA model.
pca_2 = PCA(2)
# Fit the PCA model on the numeric columns from earlier.
plot_columns = pca_2.fit_transform(good_columns)
# Make a scatter plot of each game, shaded according to cluster assignment.
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
# Show the plot.
#plt.show()