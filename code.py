

# Harsha
# Fall 2021
# CS 152 Project 2
#

# any required import statements here

# main function here
def main():
    #maincode here
   ''' hitemp=200
    hidate= ""
    v=open("blend.csv", "r")
    k=v.readline()
    print(k)
    for k in v: 
        y=k.split (",")
        print(y)  
        temp=float(y[3]) 
        date=y[0]
        if temp>hitemp:
            hitemp=temp
            hidate=date
    print("Highest Temp: %.3f occurred on %s." % (hitemp, hidate))
    v.close()
main()'''
# only execute main if this file was executed
#if __name__ == "__main__": '''

#1 drill quizz boolean+conditonals
'''def alarm_clock (day, vaca):
    if 0<day<=5 and vaca==True:
        print("10:00")
    elif day==0 or 6 and vaca==True:
        print("off")
    elif 0<day<=5 and vaca==False:
        print("7:00")
    else:
         print("10:00")
alarm_clock(1, False)
alarm_clock(0,True) '''

#2
'''
def caught_speeding(speed,is_birthday):
    if is_birthday==True:
        speed=speed-5
    elif is_birthday==False:
        speed=speed
    if speed<=60:
        print(0)
    elif 61<=speed<=80:
        print(1) 
    elif speed>=81:
        print(2)
caught_speeding(85,True)
caught_speeding(60,False)
caught_speeding(65,True) '''

#3
'''
def date_fashion (you, date):
        if you <=2 or date<=2:
            print (0)
        elif you>=8 or date>=8:
            print(2)
        else:
            print(1)
date_fashion(5, 10)
date_fashion(5, 2)
date_fashion(8,2)   '''

#4
'''

def in1to10(n,outside_mode):
    if 1<=n<=10 and outside_mode==False:
        print (True)
    if outside_mode==True and n<=1 or n>=10:
        print (True)
in1to10 (5,False)
in1to10(11, True)
in1to10 (1,True) '''

#5 
'''
def  near_ten(num):
    if num % 10<=2:
        print(True)
    else:
        print(False)
near_ten(18)
near_ten(17)
near_ten(12) 
'''

#quiz #4
'''
def square_negative(num):
    if num>0:
        print(num)
    if num<0:
        print(num**2)
square_negative(-5)
square_negative(4)
square_negative(-1)
square_negative(5)   '''

#quiz 5
'''
def monkey_trouble(a_smile, b_smile):
    if a_smile==True and b_smile==True or a_smile==False and b_smile==False:
        print(True)
    else:
        print (False)
monkey_trouble(True,True)
monkey_trouble(False,False)
monkey_trouble(True,False)
'''
'''
var="NATIONAL GEOGRAPHIC NEWS"
var=var.lower()
print(var.capitalize())
hi="This IS HIGH with lower case and UPPERCASE"
print(hi.lower())
sentence ='Brandy stands and hands Randy sand.'
print(sentence. split())
print(sentence.replace("an","oo"))
print(sentence.count("a"))
print("stan" in sentence)    '''

'''def numberofdays(year):
    days=year*365
    print(days)
numberofdays(numberhere)'''

'''def calc_sum( vals ):
    #Returns the sum of the numbers in the list vals 
    #(which much contain only ints and/or floats).
    total = 0
    for i in list:
      total+=i
    return total  '''

'''def removeDuplicateCharacters (variable):
    newlist=list(variable)
    print(newlist)
    if newlist.count("")>1:
        newlist=newlist.replace ("",random.random)
        print(newlist)
removeDuplicateCharacters(variable)  '''

'''def isPalindrome (string):
    newstring=list(string)
    newstring1=newstring[::-1]
    print(newstring1)
    print(newstring.reverse())
    if newstring.reverse==newstring:
       return True
    else:
       return False 
isPalindrome("madam")    '''
'''def sqaures(list):
    for number in range(1,(list)+1,1):
        if number<1:
            print(["k"])
        else:
            print(number**2)
sqaures(-3)'''

'''def has23(data):
    x=False
    for i in range(len(data)-1):  
        if data[i]==2 and data[i+1]==3:
            x=True
    print(x)
has23([1,2,3,4,5])
has23([5,4,3,2,1])
has23([5,7,8,9,2,3,4,5]) '''

'''def pyramid(size):
    x="*"
    for i in range(0,size):
        print(x*(2*i+1))
pyramid(4) '''

'''def strig_bits(s):
    y=""
    for i in range(len(s)):
        if i%2==0:
            y+=(s[i])
    print(y)
strig_bits("Heeololeo") '''

'''def functionName ( list1, d, e=True):
    newList = []
    if e:
        newList = list1.append(d)
    else:
        newList = list1[:]
    list1.append(d)
    return newList, list1
print(functionName([1,2,3,4,5], d=6))'''

'''oldlist=[1,2,3,4,5,6]
newlist4=[]
v=int(len(oldlist)/2)
print(v)
newlist4.append(oldlist[2:-2])
print (newlist4) '''
'''A = [ 8, "T", "R", "K", 7  ]
B = [ "S", "K", 9, "T", "H" ]
C=[]
C.append((B[1:3])*4)
print(C)'''

'''A = [ 8, "T", "R", "K", 7  ]
B = [ "S", "K", 9, "T", "H" ]
B[2]=8
B[4]="R"
print(B) '''

'''def oz2ml(oz):
    mili=oz*29.57353
    print( mili)
oz2ml(5)'''

'''def evenOdd(x):
    c=list(range(1,x+1))
    print(c)
    for i in c:
        if  i % 2==0:
            print(i, "is the even numbers")
        else:
            print(i, "are the odd numbers")
evenOdd(10) '''

'''def inBoth(item1,item2):
    c=item1+item2
    print(c)
inBoth([1,2,7,4,3],[4,5,6,1,2,3]) '''


# def dinner_calculator(meal_cost, drinks_cost):
#     discounteddrink=drinks_cost*.7
#     total=(meal_cost+discounteddrink)*1.15
#     print (total)
#     return total 
# dinner_calculator(12,4)

# def  longest_string(list):
#     answer=""
#     count=0
#     for i in range(len(list)):
#         if len(list[i])>count:
#             count=len(list[i])
#             answer=list[i]
#     print(answer)
#     return answer
# longest_string(list=["x"])

# def num_rushes(slope_height, rush_height_gain, back_sliding):
#     '''Herbert the Heffalump'''
#     current_height = 0
#     rushes = 0
#     while current_height < slope_height:
#         rushes+=1
#         current_height+=rush_height_gain
#         if current_height!=slope_height:
#             current_height-=back_sliding
#     print(rushes)
#     return rushes
# num_rushes(10, 10, 9)
# num_rushes(100, 10, 0)
# num_rushes(15, 10, 5)
# num_rushes(100, 15, 7)
# num_rushes(200, 16, 9)

# def num_rushes(slope_height, rush_height_gain, back_sliding):
#     '''Herbert the Heffalump'''
#     current_height = 0
#     rushes = 0
#     while current_height < slope_height:
#         rushes+=1
#         current_height+=rush_height_gain
#         rush_height_gain=rush_height_gain*.95
#         if current_height!=slope_height:
#             current_height-=back_sliding
#             back_sliding=back_sliding*.95
#     print(rushes)
#     return rushes
# num_rushes(10, 10, 9)
# num_rushes(100, 15, 7)

# class Robot():
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def getName(self):  #accessor method
#         return self.name
#     def getPosition(self):  #accessor method
#         return self.position
#     def move_to(self,x, y): # px and py are the new x,y values
#         self.move_to(x,y)# assign to x_old the current x position
#         return self.move_to
#     def introduction(self):  
#         return(self.name+ " is at "+str(self.position))
# Marvin = Robot("Marvin", (0,0))
# Angus = Robot("Angus",(19, -3))
# print(Marvin.introduction())
# print(Angus.introduction())
# print(Marvin.move_to(5, 11))
# print(Marvin.introduction())

# def is_palindrome(input):
#     # write your base case here
#     string=input.lower()
#     if len(string)==1 or len(input)==0:
#       return string[0]
#     # write your recursive case here
#     return is_palindrome(string[1:]) + string[0]  # the recursive call    #reverse("ello")+H = reverse(llo)+e +H=  reverse(lo)+l+e+h=reverse(o)+l+l+e+h=o+l+l+e+h
# def real(input):
#     lowerbackwards=is_palindrome(input)
#     if lowerbackwards==input.lower():
#        print(lowerbackwards,input,"are palindromes")
#     else:
#       print("not palindormes")
#     return lowerbackwards
# print(real('Hello'))
# print(real("hasrha"))

# # #Test Cases:
# # #print(is_palindrome(''))
# print(is_palindrome('e'))
# print(is_palindrome("jack"))

# def can_offer(fav_food, fridge_contents):
#     if fav_food in fridge_contents:  #i jave it
#         if fridge_contents[fav_food]>2:
#             return True
#         else:
#             return False
#     else: #i do not even have it
#         return False

# class Car:
#     def __init__(self,model,year,speed=0):
#         self.model=model
#         self.year=year
#         self.speed=speed
#     def accelerate (self):
#         self.speed=self.speed+5
#         return self.speed
#     def brake(self):
#         if self.speed==0:
#             return self.speed
#         else:
#             self.speed=self.speed-5
#     def honk_horn(self):
#         print (self.model,"goes 'beep beep' " )
#     def __str__(self):
#         return "{} {}, moving at {} km/h.".format(self.model, self.year, self.speed)
	
# my_car = Car("Toyota", 1999, 50)
# print(my_car)
import time
from turtle import *

# pensize(2)
# pencolor("orange")
# bgcolor("green")
# fillcolor("blue")
# hideturtle()

# def halfPetal():
#     forward(50)
#     left(30)
#     forward(75)
#     left(30)
#     forward(50)
#     left(120)

# def petal():
#     for i in range(2):
#         halfPetal()
# def flower(num, i=1):
#     if i==1:
#         begin_fill()
#         for i in range(num):
#             petal()
#             left(360/num)
#         end_fill()

# flower(4)
#time.sleep(2000000)
# from graphics import *
