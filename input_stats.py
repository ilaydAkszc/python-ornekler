#it takes a file name as input
#calculates the number of characters in each line
def input_stats(file):
    longest=0
    total=0
    i=1
    f=open(file)
    lines=f.read().split("\n")
    for line in lines:
        print("Line ",i," has ",len(line)," chars")
        total+=len(line)
        i+=1
        if len(line)>longest:
            longest=len(line)
        
    print(len(lines)," lines longest = ",longest,", average = ",(total/len(lines)))   

#sample output
#Line  1  has  33  chars
#Line  2  has  32  chars
#Line  3  has  31  chars
#Line  4  has  28  chars
#Line  5  has  0  chars
#Line  6  has  31  chars
#Line  7  has  41  chars
#Line  8  has  31  chars
#Line  9  has  27  chars
#9  lines longest =  41 , average =  28.22222222222222
