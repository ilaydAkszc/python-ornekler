# function  shows how many hours employees work
def hours():
    #take a file name as input
    filename=input("Input file? ")
    file=open(filename)
    line=file.read().split("\n")
    days=0
    hours=0
    for i in range(0,len(line)):
        lines=line[i].split()
        for j in range(2,len(lines)):
            days+=1
            hours+=float(lines[j])
        print(lines[1]," ","(ID#",lines[0],")"," worked ",hours," hours ","(",(hours/days),"/day)")
        

#sample output
#Input file? hours.txt
#Amy   (ID# 123 )  worked  31.5  hours  ( 7.875 /day)
#Miles   (ID# 456 )  worked  68.5  hours  ( 7.611111111111111 /day)
#Jessie   (ID# 802 )  worked  70.0  hours  ( 7.0 /day)
#Vilde   (ID# 647 )  worked  88.0  hours  ( 6.769230769230769 /day)
