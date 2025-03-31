def name_diamond(name):
    for i  in range(0,len(name)+1):
        print(name[ :i])
    for i  in range(1,len(name)+1):
        print(" "*(i-1),name[i: ])
    
name=input("Bir kelime giriniz: ")
name_diamond(name)
#name_diamond("martynlesss")
