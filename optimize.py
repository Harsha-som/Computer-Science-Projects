'''Harsha Somaya
10/20/2021
CS152
lab5
optimize to a percent dart of .43 and then change percent dart and other parameters, show on graph
change directory to project 6 and run py optimize.py to call
'''
import sys
import elephant
import random
import matplotlib.pyplot as plt

def optimize( min, max, optfunc, parameters = None, tolerance =0.001, maxIterations = 20, verbose=False):
    '''Executes a search to bring the result of the function optfunc to zero.'''
    done=False
    while done==False:
        testValue=(max+min)/2  #.5
        if verbose==True:
            print(testValue)
        result=optfunc(testValue,parameters)  #.5-.73542618  testvalue-target
        if verbose==True:
            print(result)
        if result>0:  #if difference>0, too much to the irght, go left/lower, 
            max=testValue
        elif result<0: #if diffeence<0,too low, chnage min to be higher
            min=testValue   #min changed from 0 to .5
        else: #found target
            done=True
        if max-min<tolerance:   #acceptable range
            done=True
        maxIterations-=1    
        if maxIterations<=0:   #after completed 20 runs, stop so set done=0
            done=True
    return (testValue)        

 						
# a function that returns x - target
def target(x, pars): #current value, target
    '''test with .73542618 as the target'''
    return x - 0.73542618
# # Tests the binary search using a simple target function.
# # Try changing the tolerance to see how that affects the search.
def testTarget():
    '''tests the optimize function and call it'''
    res = optimize( 0.0, 1.0, target, tolerance = 0.01, verbose=True)   #0 is min, 1 is max
    print(res)
    return

def testelephantSim():
    '''run in terms of elephant sim to optimize'''
    optimization=optimize(0.0,0.5,elephant.elephantSim,verbose=True)  #do again but in terms of elephant population
    print(optimization)
    return

def evalParameterEffect( whichParameter, testmin, testmax, teststep, defaults=None, verbose=False ):
    '''Evaluates the effects of the selected parameter on the dart percentage'''
    if defaults==None:
        simParameters=elephant.defaultParameters()
    else:
        simParameters=defaults[:]
    results=[]
    yaxis=[]     #use to create plot
    xaxis=[]
    if verbose:
        print("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))   
    t=testmin
    while t<testmax:
        simParameters[whichParameter]=t   #assign t in terms of which Parameter
        PercentDarted=optimize(0,1,elephant.elephantSim,simParameters)  #run optimize function in terms of elephantSim
        results.append((t,PercentDarted))
        if verbose:
            print("%8.3f \t%8.3f" % (t, PercentDarted))
        t+=teststep
        yaxis.append(PercentDarted)    #add to y axis
        xaxis.append(t)
    if verbose:
        print("Terminating")
    plt.plot(xaxis,yaxis, "o")
    plt.title("max age verus percent dart")   #title
    plt.xlabel("percent darted")
    plt.ylabel("optimal percent darted")
    plt.show()   #actually shows plot
    return results 

if __name__ == "__main__":
    '''call function'''
    #testTarget()
    testelephantSim()
    evalParameterEffect( elephant.IDXMAximumAge, 56,66, 2, verbose=True )   #call function
   