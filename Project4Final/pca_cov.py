'''pca_cov.py
Performs principal component analysis using the covariance matrix approach
Harsha Somaya
CS 251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class PCA_COV:
    '''
    Perform and store principal component analysis results
    '''

    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: pandas DataFrame. shape=(num_samps, num_vars)
            Contains all the data samples and variables in a dataset.

        (No changes should be needed)
        '''
        self.data = data

        # vars: Python list. len(vars) = num_selected_vars
        #   String variable names selected from the DataFrame to run PCA on.
        #   num_selected_vars <= num_vars
        self.vars = None

        # A: ndarray. shape=(num_samps, num_selected_vars)
        #   Matrix of data selected for PCA
        self.A = None

        # normalized: boolean.
        #   Whether data matrix (A) is normalized by self.pca
        self.normalized = None

        # A_proj: ndarray. shape=(num_samps, num_pcs_to_keep)
        #   Matrix of PCA projected data
        self.A_proj = None

        # e_vals: ndarray. shape=(num_pcs,)
        #   Full set of eigenvalues (ordered large-to-small)
        self.e_vals = None
        # e_vecs: ndarray. shape=(num_selected_vars, num_pcs)
        #   Full set of eigenvectors, corresponding to eigenvalues ordered large-to-small
        self.e_vecs = None

        # prop_var: Python list. len(prop_var) = num_pcs
        #   Proportion variance accounted for by the PCs (ordered large-to-small)
        self.prop_var = None

        # cum_var: Python list. len(cum_var) = num_pcs
        #   Cumulative proportion variance accounted for by the PCs (ordered large-to-small)
        self.cum_var = None

    def get_prop_var(self):
        '''(No changes should be needed)'''
        return self.prop_var

    def get_cum_var(self):
        '''(No changes should be needed)'''
        return self.cum_var

    def get_eigenvalues(self):
        '''(No changes should be needed)'''
        return self.e_vals

    def get_eigenvectors(self):
        '''(No changes should be needed)'''
        return self.e_vecs

    def covariance_matrix(self, data):
        '''Computes the covariance matrix of `data`

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_vars)
            `data` is NOT centered coming in, you should do that here.

        Returns:
        -----------
        ndarray. shape=(num_vars, num_vars)
            The covariance matrix of centered `data`

        NOTE: You should do this wihout any loops
        NOTE: np.cov is off-limits here — compute it from "scratch"!
        '''
        # self.vars = data[0,:]
        # print(self.vars)
        # print("shape: ",data.shape)
        centered_data = data - np.mean(data, axis=0)
        covariance_matrix = (centered_data.T @ centered_data) / (data.shape[0] - 1)
        return covariance_matrix

    def compute_prop_var(self, e_vals):
        '''Computes the proportion variance accounted for by the principal components (PCs).
        #   Cumulative proportion variance accounted for by the PCs (ordered large-to-small)

        Parameters:
        -----------
        e_vals: ndarray. shape=(num_pcs,)

        Returns:
        -----------
        Python list. len = num_pcs
            Proportion variance accounted for by the PCs
        '''
        summ = np.sum(e_vals) #one number
        proportional_variances = np.array([eigenvalue / summ for eigenvalue in e_vals]) ##one for every variable
        self.cum_var = proportional_variances.tolist()
        return self.cum_var

    def compute_cum_var(self, prop_var):
        '''Computes the cumulative variance accounted for by the principal components (PCs).

        Parameters:
        -----------
        prop_var: Python list. len(prop_var) = num_pcs
            Proportion variance accounted for by the PCs, ordered largest-to-smallest
            [Output of self.compute_prop_var()]

        Returns:
        -----------
        Python list. len = num_pcs
            Cumulative variance accounted for by the PCs
        '''
        return np.cumsum(prop_var).tolist()


    def pca(self, vars, normalize=False):
        '''Performs PCA on the data variables `vars`

        Parameters:
        -----------
        vars: Python list of strings. len(vars) = num_selected_vars
            1+ variable names selected to perform PCA on.
            Variable names must match those used in the `self.data` DataFrame.
        normalize: boolean.
            If True, normalize each data variable so that the values range from 0 to 1.

        NOTE: Leverage other methods in this class as much as possible to do computations.

        TODO:
        - Select the relevant data (corresponding to `vars`) from the data pandas DataFrame
        then convert to numpy ndarray for forthcoming calculations.
        - If `normalize` is True, normalize the selected data so that each variable (column)
        ranges from 0 to 1 (i.e. normalize based on the dynamic range of each variable).
            - Before normalizing, create instance variables containing information that would be
            needed to "undo" or reverse the normalization on the selected data.
        - Make sure to compute everything needed to set all instance variables defined in constructor,
        except for self.A_proj (this will happen later).
        '''
        self.vars=vars
        selected_data=self.data[vars]
        numpy_array=selected_data.to_numpy() #use for undo nirmalizing 
        self.range=np.max(numpy_array,axis=0)-np.min(numpy_array,axis=0)
        self.min=np.min(numpy_array,axis=0)
        self.normalized=normalize
        if normalize:
            numpy_array=(numpy_array - np.min(numpy_array, axis=0)) / (np.max(numpy_array, axis=0) - np.min(numpy_array, axis=0))
        # self.data=numpy_array
        covariance_matrix=self.covariance_matrix(numpy_array)
        (self.e_vals, self.e_vecs) = np.linalg.eig(covariance_matrix)
        self.prop_var=self.compute_prop_var(self.e_vals)
        self.cum_var=self.compute_cum_var(self.prop_var)
        self.A=numpy_array

        return self.e_vals, self.e_vecs



    def elbow_plot(self, num_pcs_to_keep=None):
        '''Plots a curve of the cumulative variance accounted for by the top `num_pcs_to_keep` PCs.
        x axis corresponds to top PCs included (large-to-small order)
        y axis corresponds to proportion variance accounted for

        Parameters:
        -----------
        num_pcs_to_keep: int. Show the variance accounted for by this many top PCs.
            If num_pcs_to_keep is None, show variance accounted for by ALL the PCs (the default).

        NOTE: Make plot markers at each point. Enlarge them so that they look obvious.
        NOTE: Reminder to create useful x and y axis labels.
        NOTE: Don't write plt.show() in this method
        '''
        cumulaticevar=self.get_cum_var()
        fig = plt.figure(figsize=(6,6))
        # print("cumulative sum: ", self.cum_var)
        ax1 = fig.add_subplot(111)
        if num_pcs_to_keep is None:
            ax1.plot(self.cum_var)
        else:
            # centered_data_normalized = data - np.mean(data, axis=0)
            cumulaticevar = self.cum_var[:num_pcs_to_keep]
            # self.A@self.e_vecs[:, :num_pcs_to_keep]
        ax1.plot(cumulaticevar, marker=".", markersize=15)

        # plt.xticks(self.get_eigenvectors().shape[1]+10)
        ax1.set_ylim([0.4,1.0])
        ax1.set_xlabel('Number of Principal Components')
        ax1.set_ylabel('Cumulative explained variance')
        ax1.set_title('Elbow Plot')

    def pca_project(self, pcs_to_keep):
        '''Project the data onto `pcs_to_keep` PCs (not necessarily contiguous)

        Parameters:
        -----------
        pcs_to_keep: Python list of ints. len(pcs_to_keep) = num_pcs_to_keep
            Project the data onto these PCs.
            NOTE: This LIST contains indices of PCs to project the data onto, they are NOT necessarily
            contiguous.
            Example 1: [0, 2] would mean project on the 1st and 3rd largest PCs.
            Example 2: [0, 1] would mean project on the two largest PCs.

        Returns
        -----------
        pca_proj: ndarray. shape=(num_samps, num_pcs_to_keep).
            e.g. if pcs_to_keep = [0, 1],
            then pca_proj[:, 0] are x values, pca_proj[:, 1] are y values.

        NOTE: This method should set the variable `self.A_proj`
        '''
       
        vhat=(self.get_eigenvectors()[:,pcs_to_keep])
        
        
        self.A_proj=self.A@vhat 
    
        return self.A_proj


     


    def pca_then_project_back(self, top_k):
        '''Project the data into PCA space (on `top_k` PCs) then project it back to the data space

        Parameters:
        -----------
        top_k: int. Project the data onto this many top PCs.

        Returns:
        -----------
        ndarray. shape=(num_samps, num_selected_vars)

        TODO:
        - Project the data on the `top_k` PCs (assume PCA has already been performed).
        - Project this PCA-transformed data back to the original data space
        - If you normalized, remember to rescale the data projected back to the original data space.
        '''
        #pca_project(top)
        centered_data = self.A - np.mean(self.A, axis=0)
        print("centered_data.shape ",centered_data.shape)
        print("self.get_eigenvectors() shape ",self.get_eigenvectors().shape)

        PCAsToKeepList=[]
        for i in range(top_k+1):
            PCAsToKeepList.append(i)
        print(PCAsToKeepList)

        print(self.pca_project(PCAsToKeepList).shape)
        print(self.get_eigenvectors()[:,:top_k+1].T)
        projected=self.pca_project(PCAsToKeepList) @self.get_eigenvectors()[:,:top_k+1].T + np.mean(self.A, axis=0)
        if self.normalized:
            projected=projected*(self.range)+self.min
        return projected



