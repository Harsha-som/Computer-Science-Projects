'''kmeans.py
Performs K-Means clustering
Harsha Somaya
CS 251: Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt
# from palettable import cartocolors as cc
import palettable.cartocolors.qualitative as cq

from scipy.spatial import distance

class KMeans:
    def __init__(self, data=None):
        '''KMeans constructor

        (Should not require any changes)

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features)
        '''

        # k: int. Number of clusters
        self.k = None
        # centroids: ndarray. shape=(k, self.num_features)
        #   k cluster centers
        self.centroids = None
        # data_centroid_labels: ndarray of ints. shape=(self.num_samps,)
        #   Holds index of the assigned cluster of each data sample
        self.data_centroid_labels = None

        # inertia: float.
        #   Mean squared distance between each data sample and its assigned (nearest) centroid
        self.inertia = None

        # data: ndarray. shape=(num_samps, num_features)
        self.data = data
        # num_samps: int. Number of samples in the dataset
        self.num_samps = None
        # num_features: int. Number of features (variables) in the dataset
        self.num_features = None
        if data is not None:
            self.num_samps, self.num_features = data.shape

    def set_data(self, data):
        '''Replaces data instance variable with `data`.

        Reminder: Make sure to update the number of data samples and features!

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features)
        '''
        self.data=data
        self.num_features=data.shape[1]
        self.num_samps=data.shape[0]

    def get_data(self):
        '''Get a COPY of the data

        Returns:
        -----------
        ndarray. shape=(num_samps, num_features). COPY of the data
        '''
        return self.data.copy()


    def get_centroids(self):
        '''Get the K-means centroids

        (Should not require any changes)

        Returns:
        -----------
        ndarray. shape=(k, self.num_features).
        '''
        return self.centroids

    def get_data_centroid_labels(self):
        '''Get the data-to-cluster assignments

        (Should not require any changes)

        Returns:
        -----------
        ndarray of ints. shape=(self.num_samps,)
        '''
        return self.data_centroid_labels

    def dist_pt_to_pt(self, pt_1, pt_2):
        '''Compute the Euclidean distance between data samples `pt_1` and `pt_2`

        Parameters:
        -----------
        pt_1: ndarray. shape=(num_features,)
        pt_2: ndarray. shape=(num_features,)

        Returns:
        -----------
        float. Euclidean distance between `pt_1` and `pt_2`.

        NOTE: Implement without any for loops (you will thank yourself later since you will wait
        only a small fraction of the time for your code to stop running)
        '''
        subtracted = pt_1-pt_2
        return np.sqrt(np.dot(subtracted.T, subtracted))

    def dist_pt_to_centroids(self, pt, centroids):
        '''Compute the Euclidean distance between data sample `pt` and and all the cluster centroids
        self.centroids

        Parameters:
        -----------
        pt: ndarray. shape=(num_features,)
        centroids: ndarray. shape=(C, num_features)
            C centroids, where C is an int.

        Returns:
        -----------
        ndarray. shape=(C,).
            distance between pt and each of the C centroids in `centroids`.

        NOTE: Implement without any for loops (you will thank yourself later since you will wait
        only a small fraction of the time for your code to stop running)
        '''
        return distance.cdist(pt.reshape(1, pt.shape[0]), centroids)

    def initialize(self, k):
        '''Initializes K-means by setting the initial centroids (means) to K unique randomly
        selected data samples

        Parameters:
        -----------
        k: int. Number of clusters

        Returns:
        -----------
        ndarray. shape=(k, self.num_features). Initial centroids for the k clusters.

        NOTE: Can be implemented without any for loops
        '''
        randomIndex=np.random.choice(np.arange(self.num_samps), size=k, replace=False)
        return self.data[randomIndex,:]


        # centroids = np.array([self.data[x] for x in np.random.choice(np.arange(len(data)), size=k, replace=False)])


    def cluster(self, k=2, tol=1e-2, max_iter=1000, verbose=False):
        '''Performs K-means clustering on the data

        Parameters:
        -----------
        k: int. Number of clusters
        tol: float. Terminate K-means if the (absolute value of) the difference between all
        the centroid values from the previous and current time step < `tol`. aka centroids did nto rly ch
        max_iter: int. Make sure that K-means does not run more than `max_iter` iterations.
        verbose: boolean. Print out debug information if set to True.

        Returns:
        -----------
        self.inertia. float. Mean squared distance between each data sample and its cluster mean
        int. Number of iterations that K-means was run for

        TODO:
        - Initialize K-means variables
        - Do K-means as long as the max number of iterations is not met AND the absolute value of the
        difference between the previous and current centroid values is > `tol`
        - Set instance variables based on computed values.
        (All instance variables defined in constructor should be populated with meaningful values)
        - Print out total number of iterations K-means ran for
        '''
        self.k=k
        i=0
        oldcentroid=self.initialize(k)
        self.centroids=oldcentroid
        
        #Do K-means as long as the max number of iterations is not met AND the absolute value of the
        #difference between the previous and current centroid values is > `tol`
        while i<max_iter :
            if verbose:
                print("debug info here;")
                # print(self.centroids)
            self.data_centroid_labels = self.update_labels(self.centroids)
            # print(i, flush=True)
            self.centroids, centroid_dif = self.update_centroids(k, self.data_centroid_labels, self.centroids)
            self.data_centroid_labels = self.update_labels(self.centroids)
            self.inertia = self.compute_inertia()
            i += 1
            # print("dif is ",centroid_dif)
            # print("condition ", np.max(np.abs(centroid_dif)))
            if np.max(np.abs(centroid_dif)) < tol:
                break
        return self.inertia, i
            
    

    def cluster_batch(self, k=2, n_iter=1, verbose=False):
        '''Run K-means multiple times, each time with different initial conditions.
        Keeps track of K-means instance that generates lowest inertia. Sets the following instance
        variables based on the best K-mean run:
        - self.centroids
        - self.data_centroid_labels
        - self.inertia

        Parameters:
        -----------
        k: int. Number of clusters
        n_iter: int. Number of times to run K-means with the designated `k` value.
        verbose: boolean. Print out debug information if set to True.
        '''
        listOfLabels=[]
        listofCentroids=[]
        listOfInertia=[]

        if verbose:
            print("debug")
        iteration=0

        while iteration<n_iter:
            interia=self.cluster(k)[0]
            listOfInertia.append(interia)
            listOfLabels.append(self.get_data_centroid_labels())
            listofCentroids.append(self.get_centroids())
            iteration+=1

        min_inertia = min(listOfInertia)
        self.inertia=min_inertia
        # print(self.inertia)
        min_index = listOfInertia.index(min_inertia)
        self.centroids=listofCentroids[min_index]
        self.data_centroid_labels=listOfLabels[min_index]
        # self.plot_clusters()

        
   



    def update_labels(self, centroids):
        '''Assigns each data sample to the nearest centroid

        Parameters:
        -----------
        centroids: ndarray. shape=(k, self.num_features). Current centroids for the k clusters.

        Returns:
        -----------
        ndarray of ints. shape=(self.num_samps,). Holds index of the assigned cluster of each data
            sample. These should be ints (pay attention to/cast your dtypes accordingly).

        Example: If we have 3 clusters and we compute distances to data sample i: [0.1, 0.5, 0.05]
        labels[i] is 2. The entire labels array may look something like this: [0, 2, 1, 1, 0, ...]
        '''
        array=np.ones((self.num_samps),)
        # print(array.shape)
        for j, datum in enumerate(self.data):
                # find the index of the centroid with the smallest distance to this data point
                min_cluster_index = np.argmin(self.dist_pt_to_centroids(datum, centroids)) #should give index of lowest number in this array
                # add this data point to that centroid's cluster
                array[j]=(min_cluster_index)
        return array.astype(int)

    def update_centroids(self, k, data_centroid_labels, prev_centroids):
        '''Computes each of the K centroids (means) based on the data assigned to each cluster

        Parameters:
        -----------
        k: int. Number of clusters
        data_centroid_labels. ndarray of ints. shape=(self.num_samps,)
            Holds index of the assigned cluster of each data sample
        prev_centroids. ndarray. shape=(k, self.num_features)
            Holds centroids for each cluster computed on the PREVIOUS time step

        Returns:
        -----------
        new_centroids. ndarray. shape=(k, self.num_features).
            Centroids for each cluster computed on the CURRENT time step
        centroid_diff. ndarray. shape=(k, self.num_features).
            Difference between current and previous centroid values

        NOTE: Your implementation should handle the case when there are no samples assigned to a cluster —
        i.e. `data_centroid_labels` does not have a valid cluster index in it at all.
            For example, if `k`=3 and data_centroid_labels = [0, 1, 0, 0, 1], there are no samples assigned to cluster 2.
        In the case of each cluster without samples assigned to it, you should assign make its centroid a data sample
        randomly selected from the dataset.
        '''
        clusters=[]
        for i in range(k):
            clusters.append([])
        # print(data_centroid_labels.shape)
        for position in range(data_centroid_labels.shape[0]):
            # print(position) #0 to 29
            # print(data_centroid_labels[position]) #works
            clusters[data_centroid_labels[position]].append(self.data[position,:])
        # print(clusters) #should be working fine, at least in structuree
        newcentroids=np.ones((k,self.num_features))
        # array=np.array(clusters)
        # print(array)
        # print(newcentroids.shape)
        for i in range((k)):
            if np.any(data_centroid_labels == i):
                newcentroids[i]=np.mean(clusters[i], axis=0)
            else:
                newcentroids[i]= self.data[np.random.choice(np.arange(self.num_samps), size=1, replace=False)]

        return newcentroids, newcentroids-prev_centroids

      
    def compute_inertia(self):
        '''Mean squared distance between every data sample and its assigned (nearest) centroid

        Returns:
        -----------
        float. The average squared distance between every data sample and its assigned cluster centroid.
        '''
        sum = 0
        for index in range(len(self.data)):
            correspondingCentroid=self.centroids[self.data_centroid_labels[index]]
              
            # calculate the distance squared between each data point and its centroid
            sum += self.dist_pt_to_pt(self.data[index], correspondingCentroid)**2
        # average over the data
        inertia=sum /len(self.data)
        return inertia

    def plot_clusters(self):
        '''Creates a scatter plot of the data color-coded by cluster assignment.

        TODO:
        - Plot samples belonging to a cluster with the same color.
        - Plot the centroids in black with a different plot marker.
        - The default scatter plot color palette produces colors that may be difficult to discern
        (especially for those who are colorblind). Make sure you change your colors to be clearly
        differentiable.
            You should use a palette Colorbrewer2 palette. Pick one with a generous
            number of colors so that you don't run out if k is large (e.g. 10).
        '''
        fig, axes = plt.subplots(1, 1,facecolor="pink")
        cmap=cq.Prism_6.mpl_colormap
        
        axes.set_ylabel("y")
        # cmap=plt.colormaps["RdPu"]
        axes.set_xlabel("x")
        axes.set_title("Graph of cluster w/ y vs. x")
        # for i in range(self.k):

            # w1 = self.data[self.data_centroid_labels == 1]
            # w2 = self.data[self.data_centroid_labels == 2]
        axes.scatter(self.data[:, 0], self.data[:, 1], c=self.data_centroid_labels,cmap=cmap,marker='o', alpha=0.5)
        # axes.scatter(w1[:, 0], w1[:, 1],  marker='d', alpha=0.5, label='cluster 1')
        # axes.scatter(w2[:, 0], w2[:, 1],  marker='s', alpha=0.5, label='cluster 2')
        axes.scatter(self.centroids[:, 0], self.centroids[:, 1],marker="1", s=150, label='centroids', c="black")
        axes.axis('equal')
        axes.legend(shadow=True, loc='upper left',  prop={'size': 6})

    def elbow_plot(self, max_k, n_iter=1):
        '''Makes an elbow plot: cluster number (k) on x axis, inertia on y axis.

        Parameters:
        -----------
        max_k: int. Run k-means with k=1,2,...,max_k.
        N-iterations: int. Number of iterations with the given k

        TODO:
        - Run k-means with k=1,2,...,max_k, record the inertia.
        - Make the plot with appropriate x label, and y label, x tick marks.
        '''
        # we make an elbow plot
        inertia_by_k=np.ones((max_k, 2))
        # inertia_by_k = np.array(inertia_by_k)
        for i in range(max_k): 
            inertia_by_k[i,0]=i+1
            self.cluster_batch(i+1, n_iter)
            inertia_by_k[i,1]=self.compute_inertia()
        # print(inertia_by_k)

        fig = plt.figure(figsize=(6,4))
        ax1 = fig.add_subplot(111)
        ax1.plot(inertia_by_k[:, 0], inertia_by_k[:, 1])
        ax1.set_xlabel('k')
        ax1.set_ylabel('Inertia')
        ax1.set_title('Elbow Plot')
        xticks=range(1,max_k+1) #[1,6]
        ax1.set_xticks(xticks)
        plt.show()

    def replace_color_with_centroid(self):
        '''Replace each RGB pixel in self.data (flattened image) with the closest centroid value.
        Used with image compression after K-means is run on the image vector.

        Parameters:
        -----------
        None

        Returns:
        -----------
        None
        '''
        data = []
        for i in range(self.num_samps):
            # centroid = (self.centroids[self.data_centroid_labels[i]]).astype(int) #get ervery label, get the the centroid at this index, make that centroid be a integer 

            centroid = np.rint(self.centroids[self.data_centroid_labels[i]]).astype(int)
            data.append(centroid)
            # print(i)
        self.data=np.array(data)

        








        
        
