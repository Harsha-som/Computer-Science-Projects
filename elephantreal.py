'''Harsha Somaya
10/20/2021
CS152
lab5
simulate elephnat population to make sure is wihtin carrying capacity
change directory to project 5 and run py elephant.py to call
'''
import stats
import random
import sys
IDXCalvingInterval = 0
IDXPercentdarted=1
IDXJuvenileAge=2
IDXMAximumAge=3
IDXProbabilityofCalfSurvival=4
IDXProbabilityofAdultSurvival=5
IDXProbabilityofSeniorSurviva=6
IDXCarryingCapacity=7
IDXNumberofYears=8
IDXGender=0
IDXAge=1
IDXMonthsPregnant=2
IDXMonthsContraceptiveRemaining=3
CalvingInterval=3.1 # assign each parameter from the table above to a variable with an informative name
PercentDarted=0.0
JuvenileAge=12
MaximumAge=60
ProbabilityofCalfSurvival=0.85
ProbabilityofAdultSurvival=0.996
ProbabilityofSeniorSurvival=0.20
CarryingCapacity=1000
NumberofYears=200
IDXtotalpop=0
parameters=[CalvingInterval,PercentDarted,JuvenileAge,MaximumAge,ProbabilityofCalfSurvival,ProbabilityofAdultSurvival, ProbabilityofSeniorSurvival, CarryingCapacity,NumberofYears] # make the parameter list out of the variables
def newElephant( parameters, age ):  #age=random.randint(1,parameters[IDXMAximumAge])
    '''generates elephant list with 4 elemnts, including population of pregnant elephants'''   
    elephant = [0,0,0,0]
    elephant[IDXGender]=random.choice(["f","m"]) #either a male or female for gender
    elephant[IDXAge]=age   #add age to argument
    if elephant[IDXGender]=="f":  #if female
        if elephant[IDXAge]>parameters[IDXJuvenileAge] and elephant[IDXAge]<=parameters[IDXMAximumAge]: #eligble females
            r=random.random()  #eleligble mothers if count this  #random deciaml from [0 to 1)
            if r<=1.0/parameters[IDXCalvingInterval]:  #less than prob, means not calved, survied
                elephant[IDXMonthsPregnant]=random.randint(1,22)  #eleigible females that are surving become pregant for x months
    return elephant  #return list with males and females and females that survived which are pregant 

def initPopulation(paramlist):  #paramlist is paramters again when called from main function
    '''return a list of list of the inital elephants'''
    newElephant2=[]
    for i in range(CarryingCapacity):  #for every number from 0 to 19, run 20 times
        newElephant2.append(newElephant(paramlist,random.randint(1,paramlist[IDXMAximumAge])))  #run in terms of paramlist as paramters list , shoudl give the same output as elephant from function 1 but age is randomly generated
    return newElephant2   #shoudl return a list with 20 numbers

def incrementAge(parameters,initpop):
    '''increases above list, the result of initpopulation, by 1 in second element '''
    for elephnat in range(len(initpop)):   #for elephant in range(20)- 0 to 19 times
        #print( "\n elephant list {0} is {1} and has {2} elements".format(elephnat, initpop[elephnat], len(initpop[elephnat])) )  #each elephant list (0 to 19) has len(initpop[0 to 19 index]
        initpop[elephnat][1] = initpop[elephnat][1] + 1
    #print(initpop, "is the above list but age increased by 1")
    return initpop   #initpop is now changed, so updated newElpahant2

def calcSurvival(parameters, population):   #whatever is the given population
    '''which elephants survive a year'''
    new_population=[]
    for i in population:  #for elephnag in given population
        if i[IDXAge]<=12: #juvenile
           if random.random()<ProbabilityofCalfSurvival:    #if less than chance of survival, meaning survives
               new_population.append(i) 
        if 60>=i[IDXAge]>12: #adult
           if random.random()<ProbabilityofAdultSurvival: #if less than chance of survival, meaning survives
               new_population.append(i)        
        if i[IDXAge]>MaximumAge: #senior
            if random.random()<ProbabilityofSeniorSurvival:
               new_population.append(i)  
    return new_population #returns a new list that only has those that survied

def dartElephants(parameters,new_pop):
    '''randomly dart female elehhants list'''
    for i in new_pop:   #for elephant considisting of 4 characteristics in new_pop
        if i[IDXGender]=="f" and i[IDXAge]<parameters[IDXMAximumAge] and i[IDXAge]>parameters[IDXJuvenileAge]:   #eligibel females
            if random.random()<parameters[IDXPercentdarted]:   #if less than prob darted, get darted, so 0 months pregant and 22 months of dart activacncy reaminig
                i[IDXMonthsPregnant]=0 #each elphants list has a number/index for months pregnant 
                i[IDXMonthsContraceptiveRemaining]=22
    return new_pop         #return elephants being darted in list, updated

def cullElephants(parameters, popover):
    '''returns a tuple contianing culled list, # of elephants culled'''
    numover=0
    if len(popover)>parameters[IDXCarryingCapacity]:
        numover=len(popover)-parameters[IDXCarryingCapacity]
        random.shuffle(popover)
    culled=popover[numover:]   #start to end, but start is after killing the elephants that are over carrying capacity
    return culled,numover  #culled is popver list modified, so return culled list and numoer integer

def controlPopulation(parameters, population):
    '''return new pop list dpeending if eleohants should be darted or culled and #culled as tuple'''
    if parameters[IDXPercentdarted]==0.0:    #if if percent darted ==0, which is true for parameters initally at top level function unless call at with different function
        newPOP,numCulled=cullElephants(parameters, population)   #cull them and return newPop and num culled
    else:
        newPOP=dartElephants(parameters, population)   #dart
        numCulled=0
    return (newPOP, numCulled)   #return updated parameters--newPop where the elephanst were culled or darted and num culled

def simulateMonth(parameters, population):
    '''returns population list with new claves being born inside a month'''
    for e in population:  #population is list of list, so this gives single elephnat with all of its multiole charcateristics
        gender=e[IDXGender]    #in each elephnat, gove me the gender, which is at a certain index inside each elpehnat elemnt
        age=e[IDXAge]  
        monthsPregnant=e[IDXMonthsPregnant]
        monthsContraceptive=e[IDXMonthsContraceptiveRemaining]
        if gender=="f" and parameters[IDXMAximumAge]>=age>=parameters[IDXJuvenileAge]:   #breedable females
            if monthsContraceptive>0:
                e[IDXMonthsContraceptiveRemaining]-=1  #change monthscontrecpetive to minus one because one month passed
            elif monthsPregnant>0:      
                if monthsPregnant>=22:  #done being pregnat, have baby now
                    population.append(newElephant(parameters,1))  #age is 1 because baby is now born, assume is 1 yr
                    e[IDXMonthsPregnant]=0  #had baby, so no longer pregnat 
                else:
                    e[IDXMonthsPregnant]+=1  #or continue being pregnant 
            else:
                if random.random()<1.0/((parameters[IDXCalvingInterval]*12)-22):
                    e[IDXMonthsPregnant]=1
    return population  #return updated population with months contraciptive reminaing decreasing per month, adding new babies, or continue being pregnat 

def simulateYear(parameters, population):
    '''stimulates a sample for  year, each time updating the population list'''
    population=calcSurvival(parameters, population)  #returns a new list that only has those that survied
    population2=incrementAge(parameters, population)    #now take the list iwth those that survuved and increase age by one
    for i in range(12):  #for every month from jan to december (0 to 11)
        population=simulateMonth(parameters, population2)    #stimulate month 12 times for a year, 
    return population

def calcResults(parameters,population,numberculled):
    '''outpits list with # of calves, juvenules, adult males/females, seniors, total population #m number culled'''
    numcalves=0
    numjuvenile=0
    numadultm=0
    numadultf=0
    numseniors=0
    list=[]
    for i in population:  #for every elphnat with charcateristics
        if parameters[IDXMAximumAge]>=i[IDXAge]>=parameters[IDXJuvenileAge]:  #adult
            if i[IDXGender]=="m": #male
                numadultm+=1
            elif i[IDXGender]=="f": #female
                numadultf+=1
        if 1<i[IDXAge]<parameters[IDXJuvenileAge]:
            numjuvenile+=1     #juvenile
        if i[IDXAge]>parameters[IDXMAximumAge]:
            numseniors+=1  #senior
        if i[IDXAge]==1:
            numcalves+=1
    size=len(population)
    list.append(size)
    list.append(numcalves)
    list.append(numjuvenile)
    list.append(numadultf)
    list.append(numadultm)
    list.append(numseniors)
    list.append(numberculled)
    #print("there are", numcalves, "calves,", numjuvenile, "juveniles,", numadultm, "adult males,", numadultf, "adult females," , numseniors, "seniors, the population size is", size, ",and the number of animals culled is ",numberculled)
    return list  #list only has calculated counts of each 

def runSimulation(parameters):
    '''like a test run'''
    #N=parameters[IDXNumberofYears]
    popsize = parameters[IDXCarryingCapacity]
    population = initPopulation( parameters )   #give init population
    [population,numCulled] = controlPopulation( parameters,population )   #cut init population b/c dart or cull
    results = []
    for i in range(parameters[IDXNumberofYears]):  #for number of years
        population = simulateYear( parameters, population )   #stimulate a year for that population
        [population,numCulled] = controlPopulation( parameters,population)  #now control/cut them again, every time for each year  by culling or darting
        results.append( calcResults( parameters, population,numCulled ) )     #add to empty list the calcResults on the cut pop for every year
        #print("in the {0} year, the population is of {1} size". format(i+1, len(population)))
        if results[i][0]> 2 * popsize or results[i][0] == 0:  #if population is double carrying capcity or if population length is 0
            print( "Terminating early")    #if greater than 2x carrying capcity stop
            break # cancel early, out of control
    #print(results, "is the resultss")
    return results

# def test():
#     '''create test run simulaton by calling it and other functions'''
#     print(parameters[IDXMAximumAge]) # print the maximum age, 60
#     pop = []
#     for i in range(15):  #(0 to 14
#         pop.append( newElephant( parameters,random.randint(1,parameters[IDXMAximumAge])))
#     print(pop)  #print ist of list
#     for e in pop:  #print each list individually
#         print(e)
#     newelephant2=initPopulation(parameters)
#     print(newelephant2)
#     incrementAge(parameters,newelephant2)
#     runSimulation(parameters)
# if __name__ == "__main__":
#     test()

def main():
    '''create test run simulaton by calling it and other functions'''
    PercentDarted=float(sys.argv[1])
    results = []
    results=runSimulation(parameters)   #run the simulation (which already runs for a goven number of years) in terms of the init pop of 1 year old that has been cut
    length=[]
    calves=[]
    jevnile=[]
    adultf=[]
    adultm=[]
    seniors=[]
    cull1=[]
    for i in results:  #for element in reults, which is a list of list with teh calcResults
        length.append(i[0])
        calves.append(i[1])
        jevnile.append(i[2])
        adultf.append(i[3])
        adultm.append(i[4])
        seniors.append(i[5])
        cull1.append(i[6])
    print(stats.mean(length), "is the average population size")
    print(stats.mean(calves), "is the average number of calves")
    print(stats.mean(jevnile), "is the average number of juvniles")
    print(stats.mean(adultf), "is the average number of adult females")
    print(stats.mean(adultm), "is the average number of adult males")
    print(stats.mean(seniors), "is the average number of seniors")
    print(stats.mean(cull1), "is the average number of culled animals")


if __name__ == "__main__":
    '''call functions'''
    #test() 
    main()

def defaultParameters():
    '''set default parameters list'''
    calvint= 3.1
    probdart= 0.0
    juvage= 12
    maxage=60
    probcalfsurvival= 0.85
    probadultsurvival= 0.996
    probseniorsurvival= 0.2
    carryingcapacity= 1000
    nyears=200
    parameters=[]
    parameters.append(calvint)
    parameters.append(probdart)
    parameters.append(juvage)
    parameters.append(maxage)
    parameters.append(probcalfsurvival)
    parameters.append(probadultsurvival)
    parameters.append(probseniorsurvival)
    parameters.append(carryingcapacity)
    parameters.append(nyears)  #number of years
    return parameters

def elephantSim(PercentDarted,inputParameters=None):
    '''does an elephant simulation in terms of default parameters or not'''
    if inputParameters==None:
        parameters1=defaultParameters()
    else:
        parameters1=inputParameters
    parameters1[IDXPercentdarted]=PercentDarted #parametersh[1]
    results=runSimulation(parameters1)
    for i in range(4):
        results=results+runSimulation(parameters1) #in total, run simulation is run 5 times
    totalpop=0
    for i in results:  #every item in results, every year infor
       totalpop=totalpop+i[IDXtotalpop]
    mean=totalpop/len(results)
    print(mean)
    #print(parameters1[IDXCarryingCapacity])
    return int(parameters1[IDXCarryingCapacity]-mean)#tells how much the population is over



