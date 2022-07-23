'''Harsha Somaya
10/20/2021
CS152
lab6
automate the process and use a search method to find the optimal darting percentage given the simulation parameters.
change directory to project 6 and run py serach.py to call
'''
import random
def searchSortedList( mylist, value ):
    '''tells if found value in mylist and how much times the while loop ran'''
    done=False
    found=False
    count=0
    maxIdx=len(mylist)-1
    minIdx=0
    while done==False:
        count+=1
        testIndex=maxIdx+minIdx/2
        testIndex=int(testIndex)
        if mylist[testIndex]<value:  #if numer in middle is less than value
            minIdx=testIndex+1   #less than, which menas value is to the right, change start/minindex to test index+1 to indicate move right from testIndex
        elif mylist[testIndex]>value: ##if numer in middle is greater than value
            maxIdx=testIndex-1 #greather than, so value is to the left. Chnage maximum/end position to be more left, or testindex minus 1 for 1 to left of testindex
        else:
            done=True
            found=True
            if maxIdx<minIdx: #how is this possile? max indx went so left in became less than min index, stop
                done=True
                found=False
    return (found, "it took", count, "function runs to find the value")
         
def test():
    '''simply tests above function'''
    a = []
    for i in range(10000):  #every number from 0 to 9,9999, do it this much times
        a.append(random.randint(0,100000)) #add a random numer from 0 to 100,000 both inclusive 
        a.append(42)
        a.sort() #should have 10,000 42s plus 10,000 random numbers from 0 to 100,000
    print(len(a))#should be 10,000*2=20,000
    print(searchSortedList( a, 42 ))  
    '''it can take a different number of steps each time 
    program run because randint chnage so ordering of 42 relateive to teh 
    random numbers 
    in the sorted list will change every time, sp then the function looking for 
    42 will have to run different times to find the chnaging position of 42'''				
if __name__ == "__main__":
    '''call test'''
    test()
        
 