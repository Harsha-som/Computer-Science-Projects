'''Harsha Somaya
9/22/2021
CS152
lab3
compute sum, min/mas, mean,median, mode variance
change directory to project 3 and run to call'''



def sum(numbers):
    '''compute the sum of a list of numbers
    '''
    add=0.0
    for num in numbers:
        add+=num      #starts at zero, first number is add variable then, every elemnt added to previus elemnt and stroed in add
    return add


def mean(list):
    '''fives teh mean fo a list'''
    mean1=(sum(list)/len(list)) #recall sum divided by length of list
    return mean1   

def minmax(list):
    '''computates teh min/max of a list of data'''
    hi=-1000
    low=1000
    for elemment in list:     #go through every line in listmin
        if elemment>hi:        
            hi=elemment           #reassignment of variables so only one is chosen
        if elemment<low:
            low=elemment
    print("the maximum is {0}".format(hi))
    print("the minimum is {0}".format(low))
    return hi, low  #call function


def variance(list):
    '''function to calculate variance'''
    sum=0
    mean2=mean(list)
    for element in list:
        withoutsum=(element - mean2)**2
        sum+=withoutsum
    var=sum/(len(list)-1)
    return var

def median(list=[1,2,3,3,4,5]):
    '''finds median'''
    y=sorted(list)
    median=0
    if len(y)%2==0: #even 
        median=(y[int((len(y)/2))]+y[int((len(y)/2)-1)])/2
    else:
        median=y[int((len(y)-1)/2)]
    return median

def mode(data):
    count=0
    numberofmode=0
    x=[]
    y=[]
    data=list(data)
    for element in data:
        if data.count(element)>1 and element not in x:
           # count=data.count(element)
            #numberofmode=element
            x.append(data[element])
            for elment in x:
                if x.count([element])>x.count([elment+1]):
                    y.append(x[element])
                else:
                    print(x)
            print(y)




    return x
    
def test():
    '''test teh statstics'''
    mylist=[1,2,3,3,3,4,4,5]
    print(sum(mylist), "is the sum")
    print(mean(mylist),"is the mean")
    print(minmax(mylist))
    print(variance(mylist),"is the variance")
    print(median(mylist), "is the median")
    print(mode(mylist), "is the mode")
if __name__=="__main__":
    test()
 






