def main():
    '''this parts gives dictionary from green genes'''
    f_1= open ('updatesgreengenes', 'r')
    dict={}
    allLines=f_1.readlines()  #returns a list containing each line in the file as a list item.
    only_Bases_with_newLines=allLines[1::2] #gets the bases
    only_OTU_with_newLines=allLines[::2] #gets the OTU  #even lines
    int=0
    for line2 in only_OTU_with_newLines:
        dict[line2.strip()]=int  #keys are OTUs,values dummy
        int+=1
        for line in only_Bases_with_newLines:
           dict[line2.strip()]=line.strip()  #gets rid of new line   #values replaced with sequnces #odd
    # print(dict)

    '''sequences in a list'''
    # f_1= open ('greengenes.txt', 'r')
    # result=[]
    # allLines=f_1.readlines()  #eturns a list containing each line in the file as a list item.
    # only_Bases_with_newLines=allLines[1::2] #gets the bases
    # for line in only_Bases_with_newLines:
    #     result.append(line.strip())  #gets rid of new line
    # print(result)

    '''getting OTU IDS'''
    f_2= open ('updatedOTU', 'r')
    OTUIDS=[]
    allLines=f_2.readlines()[2:] #eturns a list containing each line in the file as a list item.  
    for row in allLines:
        OTUIDS.append(row.split()[0])
    print(OTUIDS)

    # f_3= open ('testOTU2.txt', 'r')
    # OTUIDS=[]
    # allLines=f_3.readlines() #eturns a list containing each line in the file as a list item.  #righ now gives line 3
    # for row in allLines:
    #     OTUIDS.append(row.strip())
    # print(OTUIDS)

    '''make dictionary of ids (keys) and sequences (values). If dicitonary key key contains
    result ID, put ID and corresponding value into new file'''
    '''creates new file'''
    out=""
    for OTU in OTUIDS:
        if OTU in dict.keys():
            out+=">"+str(OTU)+'\n'
            out+=str(dict[OTU])+'\n'
    newfile=open("outputfile.txt","a")
    newfile.write(out)
main()