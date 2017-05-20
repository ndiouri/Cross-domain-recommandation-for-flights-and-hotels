# Import the pandas library.
import pandas
# Import matplotlib
import matplotlib.pyplot as plt
# Import the kmeans clustering model.
from sklearn.cluster import KMeans
# Import the PCA model.
from sklearn.decomposition import PCA

# Read in the data.
hotel = pandas.read_table("hotel_order_BJS.csv")

#Print the names of the columns in games.
print(hotel.columns)



"""
# Make a histogram of all price.
#working with missing data
plt.hist(HotelBJS["ciiamount"].dropna())

#plt.hist(HotelBJS["averecommendlevel"])

# Show the plot.
plt.show()



# Print the first row of all the flights with price = 0 .
# The .iloc method on dataframes allows us to index by position.
#print(HotelBJS[HotelBJS["price"] == 0].iloc[0])

# Remove any rows with price 0 .
#flights = HotelBJS[HotelBJS["price"] > 0]

# Initialize the model with 2 parameters -- number of clusters and random state.
kmeans_model = KMeans(n_clusters=5, random_state=1)
# Get only the numeric columns from games.
good_columns = HotelBJS.dropna()._get_numeric_data()
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
"""

      
