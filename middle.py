def main():
    '''this parts gives dictionary from green genes'''
    f_1= open ('middlefile.txt', 'r')
    allLines=f_1.readlines()  #returns a list containing each line in the file as a list item.
    ony=allLines[2:21277] #gets the bases
    out=""
    for line in ony:
        out+=str(line)
    with open("middlenorefrencestwo.txt","w") as newfile:
        newfile.write(out)
main()