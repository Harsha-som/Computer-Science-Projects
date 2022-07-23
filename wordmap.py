'''Harsha Somaya
11/3/2021
CS152
lab8
ask user to type something and have their response to the given key list be the value
change directory to project 8 and run py.wordmap.py to call
'''

def main():
    inputt=input("user give me sm")  #ask user string
    mapping={}
    words=["yes ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten"]
    for i in words:  #for element in words list
        response=input(i)  #ask user to gve response to element in list
        mapping[i]=response   #dictionary mapping[key-every word in list]=value (response user types)
    for key in mapping.keys():  #keys() method returns keys
        print("the key is", key, "and value is", mapping[key])  
main()

