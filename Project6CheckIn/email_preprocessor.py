'''email_preprocessor.py
Preprocess Enron email dataset into features for use in supervised learning algorithms
Harsha Somaya
CS 251/2 Data Analysis Visualization
Spring 2023
'''
import re
import os
import numpy as np
from pathlib import Path


def tokenize_words(text):
    '''Transforms an email into a list of words.

    Parameters:
    -----------
    text: str. Sentence of text.

    Returns:
    -----------
    Python list of str. Words in the sentence `text`.

    This method is pre-filled for you (shouldn't require modification).
    '''
    # Define words as lowercase text with at least one alphabetic letter
    pattern = re.compile(r'[A-Za-z]+[\w^\']*|[\w^\']*[A-Za-z]+[\w^\']*')
    return pattern.findall(text.lower())


def count_words(email_path='data/enron'):
    '''Determine the count of each word in the entire dataset (across all emails)

    Parameters:
    -----------
    email_path: str. Relative path to the email dataset base folder.

    Returns:
    -----------
    word_freq: Python dictionary. Maps words (keys) to their counts (values) across the dataset.
    num_emails: int. Total number of emails in the dataset.

    TODO:
    - Descend into the dataset base directory -> class folders -> individual emails.
    - Read each email file as a string.
    - Use the `tokenize_words` function above to chunk it into a list of words.
    - Update the counts of each word in the dictionary.

    Hints:
    - Check out Python functions in the os and os.path modules for walking the directory structure.
    '''
    dict={}
    NumberEmails=0
    # listOfEmailsName=[]
    with os.scandir(email_path) as entries:
        for entry in entries:
            print(entry.name)
            with os.scandir(f'{email_path}/{entry.name}') as files:
                for file in files:
                    NumberEmails+=1
                    print(file.name)
                    # listOfEmailsName.append(file)
                    path = Path(f'{email_path}/{entry.name}/{file.name}').read_text()
                    txt=tokenize_words(path)
                    for word in txt:
                        if word in dict:
                            dict[word]+=1
                        else:
                            dict[word]=1
    return dict, NumberEmails



def find_top_words(word_freq, num_features=200):
    '''Given the dictionary of the words that appear in the dataset and their respective counts,
    compile a list of the top `num_features` words and their respective counts.

    Parameters:
    -----------
    word_freq: Python dictionary. Maps words (keys) to their counts (values) across the dataset.
    num_features: int. Number of top words to select.

    Returns:
    -----------
    top_words: Python list. Top `num_features` words in high-to-low count order.
    counts: Python list. Counts of the `num_features` words in high-to-low count order.
    '''
    top_words=[]
    valuesList = list(word_freq.values())
    valuesList.sort(reverse=True)
    counts=valuesList[:num_features]
    for index in range(len(counts)):
        KeyList=list(word_freq.keys())
        top_words.append(KeyList[index])
    return top_words,valuesList
    






def make_feature_vectors(top_words, num_emails, email_path='data/enron'):
    '''Count the occurance of the top W (`num_features`) words in each individual email, turn into
    a feature vector of counts.

    Parameters:
    -----------
    top_words: Python list. Top `num_features` words in high-to-low count order.
    num_emails: int. Total number of emails in the dataset.
    email_path: str. Relative path to the email dataset base folder.

    Returns:
    -----------
    feats. ndarray. shape=(num_emails, num_features).
        Vector of word counts from the `top_words` list for each email.
    y. ndarray of nonnegative ints. shape=(num_emails,).
        Class index for each email (spam/ham)

    TODO:
    - Descend into the dataset base directory -> class folders -> individual emails.
    - Read each email file as a string.
    - Use `tokenize_words` to chunk it into a list of words.
    - Count the occurance of each word, ONLY THOSE THAT APPEAR IN `top_words`.

    HINTS:
    - Start with your code in `count_words` and modify as needed.
    '''
    # dict={}
    NumberEmails=0
    NumberSpamEmails=0
    NumberHamEmails=0
    features=np.empty((num_emails, len(top_words)))
    print(features.shape)

    
    # listOfEmailsName=[]
    with os.scandir(email_path) as entries:
        for entry in entries:
            print(entry.name)
            with os.scandir(f'{email_path}/{entry.name}') as files:
                for file in files:
                    # print(,NumberEmails)
                    NumberEmails+=1
                    print(file.name)
                    if entry.name=="spam":
                        NumberSpamEmails+=1
                    elif entry.name=="ham":
                        NumberHamEmails+=1
                    # listOfEmailsName.append(file)
                    path = Path(f'{email_path}/{entry.name}/{file.name}').read_text()
                    txt=tokenize_words(path)
                    print(txt)
                    for word in top_words:
                        # print(word)
                        if word in txt:
                            # print("herwwe")
                            features[NumberEmails-1][top_words.index(word)]=1
                        else:
                            # print("here")
                            features[NumberEmails-1][top_words.index(word)]=0
    z=np.tile(0,NumberSpamEmails)
    y=np.tile(1,NumberHamEmails)
    print(z,y)
    combined=np.hstack((z,y))
    print(features)

    return features,combined



def make_train_test_sets(features, y, test_prop=0.2, shuffle=True):
    '''Divide up the dataset `features` into subsets ("splits") for training and testing. The size
    of each split is determined by `test_prop`.

    Parameters:
    -----------
    features. ndarray. shape=(num_emails, num_features).
        Vector of word counts from the `top_words` list for each email.
    y. ndarray of nonnegative ints. shape=(num_emails,).
        Class index for each email (spam/ham)
    test_prop: float. Value between 0 and 1. What proportion of the dataset samples should we use
        for the test set? e.g. 0.2 means 20% of samples are used for the test set, the remaining
        80% are used in training.
    shuffle: boolean. Should we shuffle the data before splitting it into train/test sets?

    Returns:
    -----------
    x_train: ndarray. shape=(num_train_samps, num_features).
        Training dataset
    y_train: ndarray. shape=(num_train_samps,).
        Class values for the training set
    inds_train: ndarray. shape=(num_train_samps,).
        The index of each training set email in the original unshuffled dataset.
        For example: if we have originally N=5 emails in the dataset, their indices are
        [0, 1, 2, 3, 4]. Then we shuffle the data. The indices are now [4, 0, 3, 2, 1]
        let's say we put the 1st 3 samples in the training set and the remaining
        ones in the test set. inds_train = [4, 0, 3] and inds_test = [2, 1].
    x_test: ndarray. shape=(num_test_samps, num_features).
        Test dataset
    y_test:ndarray. shape=(num_test_samps,).
        Class values for the test set
    inds_test: ndarray. shape=(num_test_samps,).
        The index of each test set email in the original unshuffled dataset.
        For example: if we have originally N=5 emails in the dataset, their indices are
        [0, 1, 2, 3, 4]. Then we shuffle the data. The indices are now [4, 0, 3, 2, 1]
        let's say we put the 1st 3 samples in the training set and the remaining
        ones in the test set. inds_train = [4, 0, 3] and inds_test = [2, 1].
    '''
    inds = np.arange(y.size)
    if shuffle:
        features = features.copy()
        y = y.copy()

        inds = np.arange(y.size)
        np.random.shuffle(inds)
        features = features[inds]
        y = y[inds]

    # Your code here:
    num_test_emails = int(features.shape[0] * test_prop)
    num_train_emails = features.shape[0] - num_test_emails

    x_train = features[:num_train_emails,:]
    y_train = y[:num_train_emails]
    inds_train = inds[:num_train_emails]

    x_test = features[num_train_emails:]
    y_test = y[num_train_emails:]
    inds_test = inds[num_train_emails:]

    return x_train, y_train, inds_train, x_test, y_test, inds_test

    




def retrieve_emails(inds, email_path='data/enron'):
    '''Obtain the text of emails at the indices `inds` in the dataset.

    Parameters:
    -----------
    inds: ndarray of nonnegative ints. shape=(num_inds,).
        The number of ints is user-selected and indices are counted from 0 to num_emails-1
        (counting does NOT reset when switching to emails of another class).
    email_path: str. Relative path to the email dataset base folder.

    Returns:
    -----------
    Python list of str. len = num_inds = len(inds).
        Strings of entire raw emails at the indices in `inds`
    '''
    pass
