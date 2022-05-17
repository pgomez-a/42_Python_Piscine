from sklearn.cluster import KMeans

class KmeansClustering(object):
    def __init__(self, max_iter = 20, ncentroid = 5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter   # number of max iterations to update the centroids
        self.centroids = []         # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        """
        self.kmeans = KMeans("random", self.ncentroid, self.max_iter)
        self.kmeans.fit(X)
        return

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        """
        self.predictions = self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        return self.centroids
