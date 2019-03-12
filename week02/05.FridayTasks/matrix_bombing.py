import sys



def matrix_bombing_plan(m):
    N=len(m[0])
    M=len(m)
    my_dict=dict()
    for x in range(N):
        for y in range(M):
            if x==0 and y==0:
                new_m = list(map(list, m))
                #print(m[x][y],'----',m[x][y+1],m[x+1][y+1],m[x+1][y])
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x+1][y+1]-new_m[x][y]>0:
                    new_m[x+1][y+1]=new_m[x+1][y+1]-new_m[x][y]
                else:
                    new_m[x+1][y+1]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x+1][y]=0
                sum_mat=sum(map(sum, new_m))
                #print(new_m)
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if x==N-1 and y==N-1:
                #print(m[x][y],'----',m[x][y-1],m[x-1][y-1],m[x-1][y])
                new_m = list(map(list, m))
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x-1][y-1]-new_m[x][y]>0:
                    new_m[x-1][y-1]=new_m[x-1][y-1]-new_m[x][y]
                else:
                    new_m[x-1][y-1]=0
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if x==0 and y!=0 and y+1<M:
                #print(m[x][y],'----',m[x][y+1],m[x][y-1],m[x+1][y+1],m[x+1][y],m[x+1][y-1])
                new_m = list(map(list, m))
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x+1][y]=0
                if new_m[x+1][y+1]-new_m[x][y]>0:
                    new_m[x+1][y+1]=new_m[x+1][y+1]-new_m[x][y]
                else:
                    new_m[x+1][y+1]=0
                if new_m[x+1][y-1]-new_m[x][y]>0:
                    new_m[x+1][y-1]=new_m[x+1][y-1]-new_m[x][y]
                else:
                    new_m[x+1][y-1]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if x==0 and y!=0 and y+1>=M:
                #print(m[x][y],'----',m[x][y-1],m[x+1][y],m[x+1][y-1])
                new_m = list(map(list, m))
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x-1][y-1]=0
                if new_m[x+1][y-1]-new_m[x][y]>0:
                    new_m[x+1][y-1]=new_m[x+1][y-1]-new_m[x][y]
                else:
                    new_m[x+1][y-1]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if y==0 and x!=0 and x+1<N:
                #print(m[x][y],'----',m[x+1][y],m[x-1][y],m[x+1][y+1],m[x][y+1],m[x-1][y+1])
                new_m = list(map(list, m))
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x+1][y]=0
                if new_m[x+1][y+1]-new_m[x][y]>0:
                    new_m[x+1][y+1]=new_m[x+1][y+1]-new_m[x][y]
                else:
                    new_m[x+1][y+1]=0
                if new_m[x-1][y+1]-new_m[x][y]>0:
                    new_m[x-1][y+1]=nnew_m[x-1][y+1]-new_m[x][y]
                else:
                    new_m[x-1][y+1]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if y==0 and x!=0 and x+1>=N:
                #print(m[x][y],'----',m[x-1][y],m[x][y+1],m[x-1][y+1])
                new_m = list(map(list, m))
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x-1][y+1]-new_m[x][y]>0:
                    new_m[x-1][y+1]=new_m[x-1][y+1]-new_m[x][y]
                else:
                    new_m[x-1][y+1]=0
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if x==N-1 and y+1<M and y>0:
                #print(m[x][y],'----',m[x][y-1],m[x][y+1],m[x-1][y],m[x-1][y-1],m[x-1][y+1])
                new_m = list(map(list, m))
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                if new_m[x-1][y-1]-new_m[x][y]>0:
                    new_m[x-1][y-1]=new_m[x-1][y-1]-new_m[x][y]
                else:
                    new_m[x-1][y-1]=0
                if new_m[x-1][y+1]-new_m[x][y]>0:
                    new_m[x-1][y+1]=new_m[x-1][y+1]-new_m[x][y]
                else:
                    new_m[x-1][y+1]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if y==M-1 and x+1<N and x>0:
                #print(m[x][y],'----',m[x][y-1],m[x+1][y],m[x-1][y],m[x+1][y-1],m[x-1][y-1])
                new_m = list(map(list, m))
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x+1][y]=0
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                if new_m[x+1][y-1]-new_m[x][y]>0:
                    new_m[x+1][y-1]=new_m[x+1][y-1]-new_m[x][y]
                else:
                    new_m[x+1][y-1]=0
                if new_m[x-1][y-1]-new_m[x][y]>0:
                    new_m[x-1][y-1]=new_m[x-1][y-1]-new_m[x][y]
                else:
                    new_m[x-1][y-1]=0
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
            if x > 0 and x+1<N and y>0 and y+1< M :
                #print(m[x][y],'----',m[x-1][y],m[x+1][y],m[x][y-1],m[x][y+1],m[x-1][y-1],m[x+1][y+1],m[x-1][y+1],m[x+1][y-1])
                new_m = list(map(list, m))
                if new_m[x-1][y]-new_m[x][y]>0:
                    new_m[x-1][y]=new_m[x-1][y]-new_m[x][y]
                else:
                    new_m[x-1][y]=0
                if new_m[x+1][y]-new_m[x][y]>0:
                    new_m[x+1][y]=new_m[x+1][y]-new_m[x][y]
                else:
                    new_m[x+1][y]=0
                if new_m[x][y-1]-new_m[x][y]>0:
                    new_m[x][y-1]=new_m[x][y-1]-new_m[x][y]
                else:
                    new_m[x][y-1]=0
                if new_m[x][y+1]-new_m[x][y]>0:
                    new_m[x][y+1]=new_m[x][y+1]-new_m[x][y]
                else:
                    new_m[x][y+1]=0
                if new_m[x-1][y-1]-new_m[x][y]>0:
                    new_m[x-1][y-1]=new_m[x-1][y-1]-new_m[x][y]
                else:
                    new_m[x-1][y-1]=0
                if new_m[x+1][y+1]-new_m[x][y]>0:
                    new_m[x+1][y+1]=new_m[x+1][y+1]-new_m[x][y]
                else:
                    new_m[x+1][y+1]=0
                if new_m[x-1][y+1]-new_m[x][y]>0:
                    new_m[x-1][y+1]=new_m[x-1][y+1]-new_m[x][y]
                else:
                    new_m[x-1][y+1]=0
                if new_m[x+1][y-1]-new_m[x][y]>0:
                    new_m[x+1][y-1]=new_m[x+1][y-1]-new_m[x][y]
                else:
                    new_m[x+1][y-1]=0                
                sum_mat=sum(map(sum, new_m))               
                my_dict[(x,y)]=sum_mat
                #print(my_dict)
    print(my_dict)

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print("A =", A) 
# print("A[1] =", A[1])
# print("A[1][2] =", A[1][2])  
# print("A[0][-1] =", A[0][-1])#3

matrix_bombing_plan(A) # true -{(0, 0): 42, (0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15, (1, 2): 23, (2, 0): 29, (2, 1): 15, (2, 2): 26}

print('---------------------')
matrix_bombing_plan(B) # true - {(0, 0): 133, (0, 1): 127, (0, 2): 122, (0, 3): 125, (1, 0): 118, (1, 1): 101, (1, 2): 93, (1, 3): 106, (2, 0): 98, (2, 1): 69, (2, 2): 61, (2, 3): 86, (3, 0): 104, (3, 1): 79, (3, 2): 74, (3, 3): 98}


# released = {
#         "iphone" : 2007,
#         "iphone 3G" : 2008,
#         "iphone 3GS" : 2009,
#         "iphone 4" : 2010,
#         "iphone 4S" : 2011,
#         "iphone 5" : 2012
#     }
# print(released)
# #the syntax is: mydict[key] = "value"
# released["iphone 5S"] = 2013
# print (released)