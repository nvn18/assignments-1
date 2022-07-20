def flames(n1,n2):
    l1=[]
    l2=[]
    for i in n1:
        l1.append(i)
    for i in n2:
        l2.append(i)
    for i in l1:
        for j in l2:
            if i==j:
                l1.remove(i)
                l2.remove(j)
                break
    n=len(l1+l2)
    F=["friends",'lovers','affection','marriage','enemies','siblings']
    while len(F)>1:
        index = (n%len(F)-1)
        if index>=0:
            F_right=F[index+1:]
            F_left=F[:index]
            F=F_right+F_left
        else:
            F=F[:len(F)-1]
    print("realatioon ship stauts:",F[0])
    if F[0]=="marraige":
        print("euuu....kani kaniii")
    elif F[0]=='friends':
        print("em kaadu le orrukoo inka")
    elif F[0]=='lovers':
        print("ahaaa....mava euuu")
    elif F[0]=='affection':
        print("affecction le ganii chadvuko")
    elif F[0]=='enemies':
        print("jagartha ra bathiki untey repu kaaludam le")
    elif F[0]=="siblings":
        print("sare sare le enno enno anukuntam anii jargutayaa entii")
n1=input("enter your name").replace(' ','').upper()
n2=input("enter your crush name").replace(' ','').upper()
if n1==n2:
        print("nuvu single ra inka velli himalayas lo kalisi poo")
        exit(0)
flames(n1,n2)
 
