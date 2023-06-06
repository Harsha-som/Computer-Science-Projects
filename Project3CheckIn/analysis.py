'''analysis.py
Run statistical analyses and plot Numpy ndarray data
Harsha Somaya
CS 251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt


class Analysis:
    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data = data

        # Make plot font sizes legible
        plt.rcParams.update({'font.size': 18})

    def set_data(self, data):
        '''Method that re-assigns the instance variable `data` with the parameter.
        Convenience method to change the data used in an analysis without having to create a new
        Analysis object.

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data=data

    def min(self, headers, rows=[]):
        '''Computes the minimum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.
        (i.e. the minimum value in each of the selected columns)

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''   
        dataArray=self.data.select_data(headers,rows)
        return dataArray.min(axis=0)
        # else:
        #     onlycertainrows=np.take(self.data,  rows)
        #     return onlycertainrows[self.data.header2col[headers]].min(axis=0) #headers is a list with multiple keys so multiples values for their indicides, HELP 




    def max(self, headers, rows=[]):
        '''Computes the maximum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of max over, or over all indices
            if rows=[]

        Returns
        -----------
        maxs: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        dataArray=self.data.select_data(headers,rows)
        return dataArray.max(axis=0)

    def range(self, headers, rows=[]):
        '''Computes the range [min, max] for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min/max over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        dataArray=self.data.select_data(headers,rows)
        return dataArray.min(axis=0),dataArray.max(axis=0)
        

    def mean(self, headers, rows=[]):
        '''Computes the mean for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`).

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of mean over, or over all indices
            if rows=[]

        Returns
        -----------
        means: ndarray. shape=(len(headers),)
            Mean values for each of the selected header variables

        NOTE: You CANNOT use np.mean here!
        NOTE: There should be no loops in this method!
        '''               
        dataArray=self.data.select_data(headers,rows)

        if rows==[]:
            return dataArray.sum(axis=0)/dataArray.shape[0]

        else:
            return dataArray.sum(axis=0)/len(rows)

    def var(self, headers, rows=[]):
        '''Computes the variance for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of variance over, or over all indices
            if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Variance values for each of the selected header variables

        NOTE: You CANNOT use np.var or np.mean here!
        NOTE: There should be no loops in this method!
        '''
        mean=self.mean(headers,rows)
        dataArray=self.data.select_data(headers,rows)
        difference=dataArray-mean
        differenceSquared=np.square(difference)
        sum=differenceSquared.sum(axis=0)
        if rows==[]:                
            var=sum/(dataArray.shape[0]-1)

        else:
            var=sum/(len(rows)-1)
        
        return var

    def std(self, headers, rows=[]):
        '''Computes the standard deviation for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of standard deviation over,
            or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Standard deviation values for each of the selected header variables

        NOTE: You CANNOT use np.var, np.std, or np.mean here!
        NOTE: There should be no loops in this method!
        '''
        variance=self.var(headers,rows)
        return np.sqrt(variance)

    def show(self):
        '''Simple wrapper function for matplotlib's show function.

        (Does not require modification)
        '''
        plt.show()

    def scatter(self, ind_var, dep_var, title):
        '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and
        "y" variable in the dataset `dep_var`. Both `ind_var` and `dep_var` should be strings
        in `self.headers`.

        Parameters:
        -----------
        ind_var: str.
            Name of variable that is plotted along the x axis
        dep_var: str.
            Name of variable that is plotted along the y axis
        title: str.
            Title of the scatter plot

        Returns:
        -----------
        x. ndarray. shape=(num_data_samps,)
            The x values that appear in the scatter plot
        y. ndarray. shape=(num_data_samps,)
            The y values that appear in the scatter plot

        NOTE: Do not call plt.show() here.
        '''
        
        x=self.data.select_data([ind_var])
        y=self.data.select_data([dep_var])

        # mappings=self.data.get_mappings()
        # print(mappings)
        # x = self.data.data[:,mappings[ind_var]]
        # y = self.data.data[:,mappings[dep_var]]


        plt.scatter(x,y)
        plt.title(title)
        return x,y





    def pair_plot(self, data_vars, fig_sz=(12, 12), title=''):
        '''Create a pair plot: grid of scatter plots showing all combinations of variables in
        `data_vars` in the x and y axes.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)

        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots

        TODO:
        - Make the len(data_vars) x len(data_vars) grid of scatterplots
        - The y axis of the first column should be labeled with the appropriate variable being
        plotted there.
        - The x axis of the last row should be labeled with the appropriate variable being plotted
        there.
        - There should be no other axis or tick labels (it looks too cluttered otherwise!)

        Tip: Check out the sharex and sharey keyword arguments of plt.subplots.
        Because variables may have different ranges, pair plot columns usually share the same
        x axis and rows usually share the same y axis.
        '''                

 

        numberVariables=len(data_vars)

        data=self.data.select_data(data_vars)
        
        fig, axes = plt.subplots(numberVariables, numberVariables, sharex='col', sharey='row', figsize=fig_sz,facecolor="pink")
        fig.suptitle(title)
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axes.flat:
            ax.label_outer()
        for Index1 in range(numberVariables): # 0 1 2 3 
            for Index2 in range(numberVariables):
                axes[Index1, Index2].scatter(data[:,Index2], data[:,Index1]) 
                #axis 0,0 graph .scatter with data all rows, 0 column for x and all rows 0th column for y
                #axis 0,1 graph .scatter with data all rows, 0 column for x and all rows 1th column for y
                #axis 1,0 graph .scatter with data all rows, 1st column for x and all rows 0th column for y
                #axis 1,1 .scatter with data all rows, 1st column for x and all rows 1st column for y
                if Index1==numberVariables-1: #4-1=3, last graph for x
                    axes[Index1, Index2].set_xlabel(data_vars[Index2]) #set label for bottom graphs/rows
                if Index2==0: #top y columns, top 4 graphs #setlabel for top column
                    axes[Index1, Index2].set_ylabel(data_vars[Index1])
        return fig, axes               
        
    def linearregrrssion(self, data_vars, fig_sz=(12, 12), title="", backgroundcolor= "pink"):
        '''Create a linear regrrssion equation and add line to plot.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)
        backgroudn color= colr for entire figure 
        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots
        '''               
        numberVariables=len(data_vars)
        data=self.data.select_data(data_vars)
        fig, axes = plt.subplots(numberVariables, numberVariables, sharex='col', sharey='row', figsize=fig_sz,facecolor=backgroundcolor)
        fig.suptitle(title)
        plotnum=1
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axes.flat:
            ax.label_outer()
        for Index1 in range(numberVariables): # 0 1 2 3 
            for Index2 in range(numberVariables):
                axes[Index1, Index2].scatter(data[:,Index2], data[:,Index1]) 

                if Index1==numberVariables-1: #4-1=3, last graph for x
                    axes[Index1, Index2].set_xlabel(data_vars[Index2]) #set label for bottom graphs/rows
                if Index2==0: #top y columns, top 4 graphs #setlabel for top column
                    axes[Index1, Index2].set_ylabel(data_vars[Index1])
                b, a = np.polyfit(data[:,Index2], data[:,Index1], deg=1)
                print("the linear regression for the " + str(plotnum) + " plot is ", "y={0}x+{1}".format(b,a))
                # Create sequence of 100 numbers from 0 to 100 
                xseq = np.linspace(0, 10, num=30)
                # Plot regression line
                axes[Index1, Index2].plot(xseq, a + b * xseq, color="k", lw=2)
                plotnum=plotnum+1
        return fig, axes               
        
