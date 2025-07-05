'''n=int(input("enter the size"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()'''

'''n=int(input("enter the size"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()'''

'''n=int(input("enter the size"))
for i in range(n):
    for j in range(n):
        if  i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()'''

'''n=int(input("enter the size"))
for i in range(n):
    for j in range(n):
        if j==n-1 or i+j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()'''

n=int(input("enter the size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("❤️",end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n-1,0,-1): 
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("❤️",end=" ")
        else:
            print(" ", end=" ")
    print()