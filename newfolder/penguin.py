'''Harsha Somaya
10/03/2021
CS152
lab4
conduct statistics on the penguin population and if they will go exinct in a given year
change directory to project 4 and run to call
'''
import sys
import random
import matplotlib.pyplot as plt 
def initPopulation (N,probFemale):
    '''makes list for of having a female or male'''
    population=[]
    for i in range(N):
        number=random.random()
        if number<probFemale:
            population.append("f")   #add female if condion satsified
        else:
            population.append("m")   #else add male
    return population 

def simulateYear(pop,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity):
    '''use this to stimule one year, normal or el nino and population outcome'''
    elNinoYear=False
    if random.random()<elNinoProb:
        elNinoYear=True
    newpop=[]
    for i in pop:
        if len(newpop)>maxCapacity:
            break
        if elNinoYear:
            if random.random()<elNinoRho:     #if number between [0,1) less than prameter defined, execute
                newpop.append(i)
        else:
            newpop.append(i)
            if random.random()<stdRho-1.0:
                if random.random()<probFemale:    
                    newpop.append("f")             #adds female if the random numbe is less than probfemale arugument
                else:
                    newpop.append("m")           #again adds male
    return newpop

def runSimulation(N,initPopSize,probFemale,elNinoProb,stdRho,elNinoRho,maxCapacity,minViable):
    '''sample simulation for penguin population'''
    population=initPopulation(initPopSize,probFemale)              #produces list from initPopulation above by calling it
    endDate=N                                                 
    for i in range(N):
        newPopulation=simulateYear(population,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity) 
        if len(newPopulation)>=minViable and "f" in newPopulation and "m" in newPopulation:
            population=newPopulation
        else:
            endDate=i       #records exinction year
            break
    return endDate

def test():
    '''test teh above functions'''
    popsize = 10
    probFemale = 0.5
    pop = initPopulation(popsize, probFemale)
    print( pop,":this is the sexes with a population of 10 penguins" )
    newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )    #idetnifies this is an el nino year population in line 65
    print( newpop )
    newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )   #idetnifies this is an standard year population in line 68
    print( newpop )
    print(runSimulation(201,50,.5,1.0/7.0,1.188,.41,2000,10),"is the year of extinction")
    return
if __name__ == "__main__":  #call the first function
    test()

def computeCEPD(result,numSim):
    '''cumulative extinction probability distribution (CEPD)'''
    list=[]
    for i in range(numSim):
        list.append(0)       #makes list of 0s
    for year in result:
        print(year)
        if year<numSim:
            for m in range(year,numSim):
                list[m]+=1
    for x in list:   # divide each CEPD elemnt by the length of the extinction year results list in line 84 
        x=x/len(result)
    print(list, "list")                 
    return list

    
def main(numSim,yearsetween):
    '''runs many simulations, produces graphs of CEPD vs. specified every 3,5,7 years'''
    N=201
    list=[]
    y=[]
    for i in range(numSim):
        list.append(runSimulation(201,50,.5,1.0/7.0,1.188,.41,2000,10))
        count=0
    if list[i]<N:
        count+=1
        print(count/numSim)
    CEPD1=computeCEPD(list,numSim)
    for i in range(0,len(CEPD1),10):   
        print(CEPD1[i])       #gives every 10th item in CEPD1
    for i in range(0,202,7):
        y.append(CEPD1[i]/1000)    #gives CEPD1 in correct format of deciamals
    plt.plot(yearsetween,y)   #creates graph
    plt.xlabel("every 7 years from 0 to 200 years")    #creates x axis
    plt.ylabel("CEPD")   #creates y label
    plt.show()
if __name__ == "__main__":  #call the main function
    if len(sys.argv)!=3:
        print("there should be 3 command line arguments which are 1st file name, 2nd number of simulations, and 3rd teh el nino years")
    else:
        main(int(sys.argv[1]),yearsetween=range(0,202,7))




