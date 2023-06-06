import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import scipy.linalg as sp_la

def getSummaryStatistics(data):
    print("min, max, mean, std per variable")
    return pd.DataFrame([data.min(axis=0), data.max(axis=0), data.mean(axis=0), data.std(axis=0)])

def getShapeType(data):
    print("shape")
    return (data.shape, data.dtype)
#fir, makeploy, r sqaured, predict

def msse(y, yhat):
    r = (np.square(y - yhat)).mean()
    return r



##coreelations
for i in range(len(columns)):
    print(columns[i], np.corrcoef(data[:, 0], data[:, i], rowvar=True)[0,1])

##split data 
data = data[data[:, 1].argsort()]
print(getSummaryStatistics(data))
print(getShapeType(data))

(train, test) = np.split(data, [int(len(data) / 10 * 8)])
print(train.shape, test.shape)


# x a matrix of multiple independent variables
# poly -> polys, a matrix of multiple polynomial degrees for each column in x in order
def makePoly(x, polys):
    # make an empty array of size A
    A = np.zeros([x.shape[0], np.sum(polys)+1])
    # left most column of 1s for the intercept
    # notice this is also a third way to get that leading column of ones!
    A[:, 0] = np.squeeze(x[:, 0]**0)
    k = 1
    # for each variable
    for (j, poly) in enumerate(polys):
        # for up to and including! poly
        for i in range(1, poly+1):
            A[:, k] = np.squeeze(x[:, j]**i)
            k += 1
    return A

def fit(data, independent, dependent, polys):
    # This is our independent variable, just one for now
    x = data[np.ix_(np.arange(data.shape[0]), independent)]

    # We add the polynomials, and a column of 1s for the intercept
    A = makePoly(x, polys)

    # This is the dependent variable 
    y = data[:, dependent]

    # This is the regression coefficients that were fit, plus some other results
    # We use _ when we don't want to remember something a function returns
    c, _, _, _ = sp_la.lstsq(A, y)
    return c

def predict(data, independent, polys, c):
    # These are our independent variable(s)
    x = data[np.ix_(np.arange(data.shape[0]), independent)]

    # We add the polynomials, and a column of 1s for the intercept
    A = makePoly(x, polys)

    return np.dot(A, c)

def rsquared(y, yhat):
    if len(y) != len(yhat):
        print("Need y and yhat to be the same length!")
        return 0
    return 1 - (((y - yhat)**2).sum() / ((y - y.mean())**2).sum())



from itertools import chain, combinations

def powerset(variables):
    return chain.from_iterable(combinations(variables, r) for r in range(len(variables)+1))

def msse(y, yhat):
    r = (np.square(y - yhat)).mean()
    return r

res = {}
for variableset in powerset(range(1, train.shape[1])):
    if len(variableset) > 0:
        # fit the multiple linear regression
        polys = [1 for x in range(len(variableset))]
        c = fit(train, list(variableset), 0, polys)
        # calculate MSSE and R^2
        res[variableset] = (msse(train[:, 0], predict(train, variableset, polys, c)), 
                            rsquared(test[:, 0], predict(test, variableset, polys, c)))



                            # x an array of multiple independent variables
# poly -> polys, an array of multiple polynomial degrees for each column in x in order
def makePoly(x, polys):
    # make an empty array of size A
    A = np.zeros([x.shape[0], np.sum(polys)+1])
    # left most column of 1s for the intercept
    A[:, 0] = np.squeeze(x[:, 0]**0)
    k = 1
    for (j, poly) in enumerate(polys):
        for i in range(1, poly+1):
            A[:, k] = np.squeeze(x[:, j]**i)
            k += 1
    return A

def fit_lr(data, independent, dependent, polys):
    # These are our independent variables
    x = data[np.ix_(np.arange(data.shape[0]), independent)] 
    # This is the dependent variable 
    y = data[:, dependent]
    A = makePoly(x, polys)
    c, _, _, _ = sp_la.lstsq(A, y)
    return c

def predict_lr(data, independent, polys, c):
    # These are our independent variable(s)
    x = data[np.ix_(np.arange(data.shape[0]), independent)]
    A = makePoly(x, polys)
    return np.dot(A, c)

def msse(y, yhat):
    r = ((y - yhat)**2).mean()
    return r

def rsquared(y, yhat):
    return 1 - (((y - yhat)**2).sum() / ((y - y.mean())**2).sum())



def fit_pca(data):
    # center
    centered_data = data - np.mean(data, axis=0)
    # covariance matrix
    covariance_matrix = (centered_data.T @ centered_data) / (data.shape[0] - 1)
    # plot covariance matrix
    fig = plt.figure(figsize=(12,12))
    seaborn.heatmap(pd.DataFrame(covariance_matrix), annot=False, cmap='PuOr')
    plt.show()
    # eigenvalues and eigenvectors, sorted
    (evals, evectors) = np.linalg.eig(covariance_matrix)
    order = np.argsort(evals)[::-1]
    eigenvals_sorted = evals[order]
    eigenvecs_sorted = evectors[:, order]
    print(eigenvals_sorted.shape, eigenvecs_sorted.shape)
    return np.mean(data, axis=0), eigenvals_sorted, eigenvecs_sorted

def variances(eigenvals_sorted, eigenvecs_sorted):
    # calculate proportional variances and cumulative sum
    sum = np.sum(eigenvals_sorted)
    proportional_variances = np.array([eigenvalue / sum for eigenvalue in eigenvals_sorted])
    cumulative_sum = np.cumsum(proportional_variances)
    # scree plot
    plt.figure(figsize=(6, 4))
    plt.bar(range(len(proportional_variances)), proportional_variances, alpha=0.5, align='center',
            label='Proportional variance')
    plt.ylabel('Proportional variance ratio')
    plt.xlabel('Ranked Principal Components')
    plt.title("Scree Graph")
    plt.legend(loc='best')
    plt.tight_layout()
    # elbow plot
    fig = plt.figure(figsize=(6,4))
    ax1 = fig.add_subplot(111)
    ax1.plot(cumulative_sum)
    ax1.set_ylim([0,1.0])
    ax1.set_xlabel('Number of Principal Components')
    ax1.set_ylabel('Cumulative explained variance')
    ax1.set_title('Elbow Plot')
    plt.show()

def project_pca(data, mean, eigenvecs_sorted, to_keep):
    centered_data = data - mean
    return centered_data@eigenvecs_sorted[:, :to_keep]

def reconstruct_pca(projected_data):
    return projected_data@v.T + np.mean(data, axis=0)
    