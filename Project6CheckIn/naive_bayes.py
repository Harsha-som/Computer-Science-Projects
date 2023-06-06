'''naive_bayes_multinomial.py
Naive Bayes classifier with Multinomial likelihood for discrete features
YOUR NAME HERE
CS 251/2: Data Analysis Visualization
Spring 2023
'''
import numpy as np


class NaiveBayes:
    '''Naive Bayes classifier using Multinomial likeilihoods (discrete data belonging to any
     number of classes)'''
    def __init__(self, num_classes):
        '''Naive Bayes constructor

        TODO:
        - Add instance variable for `num_classes`.
        - Add placeholder instance variables the class prior probabilities and class likelihoods (assigned to None).
        You may store the priors and likelihoods themselves or the logs of them. Be sure to use variable names that make
        clear your choice of which version you are maintaining.
        '''
        self.num_classes=num_classes

        # class_priors: ndarray. shape=(num_classes,).
        #   Probability that a training example belongs to each of the classes
        #   For spam filter: prob training example is spam or ham
        self.class_priors_=None

        # class_likelihoods: ndarray. shape=(num_classes, num_features).
        #   Probability that each word appears within class c
        self.class_likelihoods=None
    def get_priors(self):
        '''Returns the class priors (or log of class priors if storing that)'''
        return self.class_priors

    def get_likelihoods(self):
        '''Returns the class likelihoods (or log of class likelihoods if storing that)'''
        return self.class_likelihoods

    def train(self, data, y):
        '''Train the Naive Bayes classifier so that it records the "statistics" of the training set:
        class priors (i.e. how likely an email is in the training set to be spam or ham?) and the
        class likelihoods (the probability of a word appearing in each class — spam or ham)

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_samps,). Corresponding class of each data sample.

        TODO:
        - Compute the class priors and class likelihoods (i.e. your instance variables) that are needed for
        Bayes Rule. See equations in notebook.
        '''
        num_samps, num_features = data.shape
        #every column is a word, every cell is how many times this coulmn word appears in this row/email which is spam or ham
        priors = np.empty(self.num_classes)
        likelihoods = np.empty((self.num_classes, num_features))

        for c in range(self.num_classes): #for c in 0 1 2 3 
            # print(np.unique(y)[c]) #class value
            classs=np.unique(y)[c]
            classCount = sum(y == classs)
            # print(classCount)
            priors[c] = classCount / num_samps

            for i in range(num_features):
                # print(y==classs)
                #get index of trues, then get data at this index
                TrueFalseArray=y==classs
                temp=data[TrueFalseArray]
                # print(temp.shape)
                summ = np.sum(temp) #number of true instances, number of data points in this class
                # print(summ)
                Ncw = np.sum(temp[:, i])
                likelihoods[c][i] = (Ncw+1)/(summ+num_features)

        self.class_priors = priors
        self.class_likelihoods = likelihoods
    def predict(self, data):
        '''Combine the class likelihoods and priors to compute the posterior distribution. The
        predicted class for a test sample from `data` is the class that yields the highest posterior
        probability.

        Parameters:
        -----------
        data: ndarray. shape=(num_test_samps, num_features). Data to predict the class of
            Need not be the data used to train the network

        Returns:
        -----------
        ndarray of nonnegative ints. shape=(num_samps,). Predicted class of each test data sample.

        TODO:
        - For the test samples, we want to compute the log of the posterior by evaluating
        the the log of the right-hand side of Bayes Rule without the denominator (see notebook for
        equation). This can be done without loops.
        - Predict the class of each test sample according to the class that produces the largest
        log(posterior) probability (hint: this can also be done without loops).

        NOTE: Remember that you are computing the LOG of the posterior (see notebook for equation).
        NOTE: The argmax function could be useful here.
        '''
        num_test_samps, num_features = data.shape

        predicted_class = np.empty(num_test_samps)
        for i in range(num_test_samps):
            # print((np.log(self.class_likelihoods) @ data[i].T).shape)
            log_posteriors = np.log(self.class_priors) + np.log(self.class_likelihoods) @ data[i].T
            predicted_class[i] = np.argmax(log_posteriors)


        return predicted_class.astype(int)

    def accuracy(self, y, y_pred):
        '''Computes accuracy based on percent correct: Proportion of predicted class labels `y_pred`
        that match the true values `y`.

        Parameters:
        -----------
        y: ndarray. shape=(num_data_sams,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_sams,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        float. Between 0 and 1. Proportion correct classification.

        NOTE: Can be done without any loops
        '''
        assert len(y) == len(y_pred)
        diffs = y == y_pred #true false array 
        print(diffs)
        vals, counts = np.unique(diffs, return_counts=True)
        print("vals: " ,vals)
        print(counts)
        return counts[1]/ (np.sum(counts))

    def confusion_matrix(self, y, y_pred):
        '''Create a confusion matrix based on the ground truth class labels (`y`) and those predicted
        by the classifier (`y_pred`).

        Recall: the rows represent the "actual" ground truth labels, the columns represent the
        predicted labels.

        Parameters:
        -----------
        y: ndarray. shape=(num_data_samps,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_samps,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        ndarray. shape=(num_classes, num_classes).
            Confusion matrix
        '''
        confusion=np.empty((self.num_classes,self.num_classes))
        for i in range(len(y)): #for every data sample 
            confusion[y[i]][[y_pred[i]]]+=1

        return confusion.astype(int)
