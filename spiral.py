def spiral(m, n, a):
    '''k=starting row of the matrix
       m=ending row of matrix
       l=start column of the matrix
       n=last column of matrix'''
    k=0
    l=0
    while(k<m and l<n):
        for i in range(l,n):    #printing frst row of matrix 
            print(a[k][i],end=' ')
        k+=1
        for i in range(k,m):      #printing lst col of matrix
            print(a[i][n-1],end=' ')
        n-=1
        if(k<m):                     #printing last row of matrix
            for i in range(n-1,(l-1),-1):
                print(a[m-1][i],end=' ')
            m-=1
        if (l<n):                      #printing frst col of matrix
            for i in range(m-1,(k-1),-1):
                print(a[i][l],end=' ')
            l+=1
print("THE SPRIAL MATRIX IS:")
m=int(input("enter the rows: "))
n=int(input("enter the coloumns:"))
a=[]
for i in range(m):
    r=[int(x) for x in input(f'enter the rows{i+1}:').split()]
    a.append(r)
spiral(m,n,a)




