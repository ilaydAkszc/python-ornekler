
def dna_errors(s1,s2):
    error=0
    minln=min(len(s1),len(s2))
    ln=abs(len(s1)-len(s2))
    error+=ln
    for i in range(0,len(s1)):
        if s1[i]=="-":
            error+=1
            s1.strip(s1[i])
    for i in range(0,len(s2)):
        if s2[i]=="-":
            error+=1
            s2.strip(s2[i])
            
    for i in range(0,minln):
        if (s1[i]=="G") and ((s2[i]=="G") or (s2[i]=="A") or (s2[i]=="T")):
            error+=2
        elif  (s1[i]=="C") and ((s2[i]=="C") or (s2[i]=="A") or (s2[i]=="T")):
            error+=2
        elif (s1[i]=="A") and ((s2[i]=="G") or (s2[i]=="A") or (s2[i]=="C")):
            error+=2
        elif (s1[i]=="T") and ((s2[i]=="G") or (s2[i]=="C") or (s2[i]=="T")):
            error+=2
    return error

print(dna_errors("GGGA-GAATCTCTGGACT","CTCTACTTA-AGACCGGTACAGG"))
