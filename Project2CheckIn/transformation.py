'''transformation.py
Perform projections, translations, rotations, and scaling operations on Numpy ndarray data.
Harsha Somaya
CS 251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt
import palettable
import analysis
import data


class Transformation(analysis.Analysis):

    def __init__(self, orig_dataset, data=None):
        '''Constructor for a Transformation object

        Parameters:
        -----------
        orig_dataset: Data object. shape=(N, num_vars).
            Contains the original dataset (only containing all the numeric variables,
            `num_vars` in total).
        data: Data object (or None). shape=(N, num_proj_vars).
            Contains all the data samples as the original, but ONLY A SUBSET of the variables.
            (`num_proj_vars` in total). `num_proj_vars` <= `num_vars`

        TODO:
        - Pass `data` to the superclass constructor.
        - Create an instance variable for `orig_dataset`.
        '''
        super().__init__(data) #pass data into analysis constructor 
        self.orig_data = orig_dataset #Create an instance variable for `orig_dataset`
        
    def project(self, headers):
        '''Project the original dataset onto the list of data variables specified by `headers`,
        i.e. select a subset of the variables from the original dataset.
        In other words, your goal is to populate the instance variable `self.data`.

        Parameters:
        -----------
        headers: Python list of str. len(headers) = `num_proj_vars`, usually 1-3 (inclusive), but
            there could be more.
            A list of headers (strings) specifying the feature to be projected onto each axis.
            For example: if headers = ['hi', 'there', 'cs251'], then the data variables
                'hi' becomes the 'x' variable,
                'there' becomes the 'y' variable,
                'cs251' becomes the 'z' variable.
            The length of the list matches the number of dimensions onto which the dataset is
            projected — having 'y' and 'z' variables is optional.


        TODO:
        - Create a new `Data` object that you assign to `self.data` (project data onto the `headers`
        variables). Determine and fill in 'valid' values for all the `Data` constructor
        keyword arguments (except you dont need `filepath` because it is not relevant here).
        '''

        newData=self.orig_data.select_data(headers)
        header2col={}
        index=0
        for header in headers:
            header2col[header]=index
            index=index+1
        self.data=data.Data(headers=headers,data=newData,header2col=header2col)

    def get_data_homogeneous(self):
        '''Helper method to get a version of the projected data array with an added homogeneous
        coordinate. Useful for homogeneous transformations.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars+1). The projected data array with an added 'fake variable'
        column of ones on the right-hand side.
            For example: If we have the data SAMPLE (just one row) in the projected data array:
            [3.3, 5.0, 2.0], this sample would become [3.3, 5.0, 2.0, 1] in the returned array.

        NOTE:
        - Do NOT update self.data with the homogenous coordinate.
        '''
        return np.append(self.data.data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1)


    def translation_matrix(self, magnitudes):
        ''' Make an M-dimensional homogeneous transformation matrix for translation,
        where M is the number of features in the projected dataset.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Translate corresponding variables in `headers` (in the projected dataset) by these
            amounts.

        Returns:
        -----------
        ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The transformation matrix.

        NOTE: This method just creates the translation matrix. It does NOT actually PERFORM the
        translation!
        '''
        # we need to define a transformation matrix that will allow us to shift the price variable; this one will be the identity matrix with the translation specified in an extra last column
        translateTransform = np.eye(self.data.get_num_dims()+1) #get seocnd column
        headerIndexceList=self.data.get_header_indices(self.data.get_headers()) #0 for 
        for index in headerIndexceList: #[0, 1, 2]
            translateTransform[index,self.data.get_num_dims()]=magnitudes[index]
        return translateTransform
    
    def scale_matrix(self, magnitudes):
        '''Make an M-dimensional homogeneous scaling matrix for scaling, where M is the number of
        variables in the projected dataset.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The scaling matrix.

        NOTE: This method just creates the scaling matrix. It does NOT actually PERFORM the scaling!
        '''
        scaleTransform = np.zeros((self.data.get_num_dims()+1,self.data.get_num_dims()+1)) #get seocnd column
        headerIndexceList=self.data.get_header_indices(self.data.get_headers()) #0 for 
        for index in headerIndexceList: #[0, 1, 2]
            scaleTransform[index,index]=magnitudes[index]
        scaleTransform[-1,-1]=1
        return scaleTransform

    def translate(self, magnitudes):
        '''Translates the variables `headers` in projected dataset in corresponding amounts specified
        by `magnitudes`.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Translate corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The translated data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to translate the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        coordinate!
        '''
        # print(self.data.get_num_samples()) #150
        # print(np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T)
        homogenizedData = np.append(self.data.data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1)
        # print("homogenized data")
        # print(homogenizedData[:5],"\n")
        translation_matrix=self.translation_matrix(magnitudes)
        transformedData = (translation_matrix@homogenizedData.T).T 
        transformedData=transformedData  [:,:-1]   

        self.data=data.Data(headers=self.data.get_headers(),data=transformedData,header2col=self.data.get_mappings())
        # print(self.data.get_headers(),"\n",self.data.get_mappings())
        return transformedData 


    def scale(self, magnitudes):
        '''Scales the variables `headers` in projected dataset in corresponding amounts specified
        by `magnitudes`.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The scaled data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to scale the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        homogenous coordinate!
        '''
        # np.ones([self.data.get_num_samples(),1])

        scaling_matrix=self.scale_matrix(magnitudes)
        homogenizedData = np.append(self.data.data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1)
        print("scaling matrix:\n",scaling_matrix)
        # print("homogenizied data: \n",homogenizedData[:5],"\n")
        transformedData = (scaling_matrix@homogenizedData.T).T
        # print(transformedData[:5])
        self.data=data.Data(headers=self.data.get_headers(),data=transformedData[:,:-1],header2col=self.data.get_mappings())
        # print(self.data.get_headers(),"\n",self.data.get_mappings())
        return transformedData [:,:-1]

    def transform(self, C):
        '''Transforms the PROJECTED dataset by applying the homogeneous transformation matrix `C`.

        Parameters:
        -----------
        C: ndarray. shape=(num_proj_vars+1, num_proj_vars+1).
            A homogeneous transformation matrix.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The projected dataset after it has been transformed by `C`

        TODO:
        - Use matrix multiplication to apply the compound transformation matix `C` to the projected
        dataset.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        coordinate!
        '''
        self.data.data=np.append(self.data.data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1) #add homogenized coordinate 
        transformedData = (C@self.data.data.T).T
        self.data=data.Data(headers=self.data.get_headers(),data=transformedData[:,:-1],header2col=self.data.get_mappings())
        # print(self.data.data[:5,])
        return self.data.data


        

    def normalize_together(self):
        '''Normalize all variables in the projected dataset together by translating the global minimum
        (across all variables) to zero and scaling the global range (across all variables) to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        # subtract the global minimum from each datapoint
        magnitude_translate=[]
        #translateTransform=np.array(self.data.shape[0],self.data.shape[1])
       # for i in range(self.data.data.shape[1]): #withut the column of 1s, 3 for i in range 0 1 2
        magnitude_translate.append( -self.data.data.min()) #mqke the last column in translate tranoform first 3 rows be the global minimum of 0
        magnitude_translate=magnitude_translate*(self.data.data.shape[1])
        translation_matrix=self.translation_matrix(magnitude_translate)
        print("translation_matrix:\n",translation_matrix)

        # divide by the global range
        # scaleTransform = np.eye(self.data.dat.shape[1]) #
        sclae_magnitude=[]
        #for i in range(self.data.data.shape[1]):  #withut the column of 1s, 3 for i in range 0 1 2
        sclae_magnitude.append( 1/(self.data.data.max()-self.data.data.min())) #(0,0): (1,1): (2,2)
        sclae_magnitude=sclae_magnitude*(self.data.data.shape[1])

        scale_translate=self.scale_matrix(sclae_magnitude)

        print("scale_trnaofmration matrixe:")
        print(scale_translate)


        # when we do a series of transformations, first we multiply the smaller transformation matrices, and only at the end the result of that with the larger data matrix (more efficient!)
        transformMatrix = scale_translate@translation_matrix
        print("transformMatrix")
        print(transformMatrix)

        normalized= (self.transform(transformMatrix))
        self.data.data=normalized
        return self.data.data



    def normalize_separately(self):
        '''Normalize each variable separately by translating its local minimum to zero and scaling
        its local range to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        # subtract the global minimum from each datapoint
        magnitude_translate=[]
        #translateTransform=np.array(self.data.shape[0],self.data.shape[1])
        for i in range(self.data.data.shape[1]): #withut the column of 1s, 3 for i in range 0 1 2
            magnitude_translate.append( -self.data.data[:,i].min()) #mqke the last column in translate tranoform first 3 rows be the global minimum of 0
        translation_matrix=self.translation_matrix(magnitude_translate)
        print("translation_matrix:\n",translation_matrix)

        # divide by the global range
        # scaleTransform = np.eye(self.data.dat.shape[1]) #
        sclae_magnitude=[]
        for i in range(self.data.data.shape[1]):  #withut the column of 1s, 3 for i in range 0 1 2
            sclae_magnitude.append( 1/(self.data.data[:,i].max()-self.data.data[:,i].min())) #(0,0): (1,1): (2,2)

        scale_translate=self.scale_matrix(sclae_magnitude)

        print("scale_trnaofmration matrixe:")
        print(scale_translate)


        # when we do a series of transformations, first we multiply the smaller transformation matrices, and only at the end the result of that with the larger data matrix (more efficient!)
        transformMatrix = scale_translate@translation_matrix
        print("transformMatrix")
        print(transformMatrix)

        normalized= (self.transform(transformMatrix))
        self.data.data=normalized
        return self.data.data

    def rotation_matrix_3d(self, header, degrees):
        '''Make an 3-D homogeneous rotation matrix for rotating the projected data
        about the ONE axis/variable `header`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(4, 4). The 3D rotation matrix with homogenous coordinate.

        NOTE: This method just creates the rotation matrix. It does NOT actually PERFORM the rotation!
        '''
        mapping=self.data.get_mappings()
        indexOfHeader=mapping[header]
        rotateTransform = np.eye(4,4)

        if indexOfHeader==0:
            rotateTransform[1,1]=np.cos(np.radians(degrees))

            rotateTransform[1,2]=-np.sin(np.radians(degrees))
            rotateTransform[2,1]=np.sin(np.radians(degrees))

            rotateTransform[2,2]=np.cos(np.radians(degrees))

            return rotateTransform

        elif indexOfHeader==1:
            rotateTransform[0,0]=np.cos(np.radians(degrees))
            rotateTransform[0,2]=-np.sin(np.radians(degrees))
            rotateTransform[2,0]=-np.sin(np.radians(degrees))
            rotateTransform[2,2]=np.cos(np.radians(degrees))
            return rotateTransform
            
        elif indexOfHeader==2:
            rotateTransform[0,0]=np.cos(np.radians(degrees))
            rotateTransform[0,1]=-np.sin(np.radians(degrees))
            rotateTransform[1,0]=np.sin(np.radians(degrees))
            rotateTransform[1,1]=np.cos(np.radians(degrees))
            return rotateTransform
        
        else: 
            return 
        



    def rotate_3d(self, header, degrees):
        '''Rotates the projected data about the variable `header` by the angle (in degrees)
        `degrees`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The rotated data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to rotate the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        homogenous coordinate!
        '''
        rotation_matrix=self.rotation_matrix_3d(header,degrees)
        homogenizedData = np.append(self.data.data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1)
        # print("rotation matrix:\n",rotation_matrix)
        # print("homogenizied data: \n",homogenizedData[:5],"\n")
        transformedData = (rotation_matrix@homogenizedData.T).T
        # print(transformedData[:5])
        self.data=data.Data(headers=self.data.get_headers(),data=transformedData[:,:-1],header2col=self.data.get_mappings())
        # print(self.data.get_headers(),"\n",self.data.get_mappings())
        return self.data.data

    def scatter_color(self, ind_var, dep_var, c_var, title=None):
        '''Creates a 2D scatter plot with a color scale representing the 3rd dimension.

        Parameters:
        -----------
        ind_var: str. Header of the variable that will be plotted along the X axis.
        dep_var: Header of the variable that will be plotted along the Y axis.
        c_var: Header of the variable that will be plotted along the color axis.
            NOTE: Use a ColorBrewer color palette (e.g. from the `palettable` library).
        title: str or None. Optional title that will appear at the top of the figure.
        '''
        x=self.data.select_data([ind_var])
        y=self.data.select_data([dep_var])
        z = self.data.select_data([c_var])


        # plt.xticks(np.arange(0, 8, 1.0))  #DO LATER


        color_map = palettable.colorbrewer.sequential.Blues_9
        #z = self.data.select_data([c_var]).reshape(self.data.get_num_samples(),)
        # plt.scatter(x.reshape(self.data.get_num_samples(),), y.reshape(self.data.get_num_samples(),), c=z, s=75, cmap=color_map.mpl_colormap, edgecolor='black')
        
        fig, axis = plt.subplots()

        # Correctly use cmap: Credit to Zixuan Wang
        scatterd = axis.scatter(x, y, c=z, cmap=color_map.mpl_colormap, edgecolors='black')
        

        axis.set_xlabel(ind_var)
        axis.set_ylabel(dep_var)

        colorbar =fig.colorbar(scatterd)
        colorbar.set_label(c_var)
        plt.title(title)