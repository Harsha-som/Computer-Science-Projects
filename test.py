def main():
    '''this parts gives dictionary'''
    f_1= open ('test2.txt', 'r')
    dict={}
    allLines=f_1.readlines()  #returns a list containing each line in the file as a list item.
    only_Bases_with_newLines=allLines[1::2] #gets the bases
    only_OTU_with_newLines=allLines[::2]
    int=0
    for line2 in only_OTU_with_newLines:
        dict[line2.strip()]=int
        int+=1
        for line in only_Bases_with_newLines:
           dict[line2.strip()]=line.strip()  #gets rid of new line
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
    # f_2= open ('table.from_biom.txt', 'r')
    # OTUIDS=[]
    # allLines=f_2.readlines()[2:] #eturns a list containing each line in the file as a list item.  #righ now gives line 3
    # for row in allLines:
    #     OTUIDS.append(row.split()[0])
    # print(OTUIDS)

    f_3= open ('testOTU2.txt', 'r')
    OTUIDS=[]
    allLines=f_3.readlines() #eturns a list containing each line in the file as a list item.  #righ now gives line 3
    for row in allLines:
        if not row.isspace():
            OTUIDS.append(row.strip())
    print(OTUIDS)

    '''make dictionary of ids (keys) and sequences (values). If dicitonary key key contains
    result ID, put ID and corresponding value into new file'''
    
    '''creates new file'''
    out=""
    for OTU in OTUIDS:
        if OTU in dict.keys():
            out+=">"+str(OTU)+'\n'
            out+=str(dict[OTU])+'\n'
    newfile=open("testfile.txt","a")
    newfile.write(out)
main()