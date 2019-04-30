from collections.abc import Iterable

#Task1
def deep_find(data, key):
   for k,v in data.items():
        #print('k:',k,"v:",v)
        if k==key:
            found_key=True
            return v
        elif isinstance(v,dict):
            if deep_find(v,key)!= None:
                found_key=True
                return deep_find(v,key)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                if isinstance(el,dict):
                    if deep_find(el,key)!= None:
                        found_key=True
                        return deep_find(el,key)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            if deep_find(element,key)!= None:
                                found_key=True
                                return deep_find(element,key)

def deep_find_bfs(data, key):
   visited=[]
   for k,v in data.items():
        
        if k==key:
            find_el=True
            return v
        else:
            visited.append(v)
        #print('k:',k,', visited: ',visited)

   for el in visited:
        #print('IN FOR',visited)
        if isinstance(el,dict):
            #print("el in if : ",el)
            for k,v in el.items():
                 #print("k:",k,"v:",v)
                 if k==key:
                    find_el=True
                    return v
                 elif isinstance(v,dict):
                    #visited.remove(el)
                    visited.append(v)
                    #print('k:',k,'in',visited)
                 elif isinstance(v, Iterable)==True and isinstance(v,dict)==False:
                    for e in v:
                        if isinstance(e,dict):
                            #visited.remove(el)
                            visited.append(e)
                            #print('In',visited)
                            

        elif isinstance(el, Iterable) and isinstance(el,dict)==False:
            #print("el in elif: ",el)
            for e in el:
                if isinstance(e,dict):
                     #visited.remove(el)
                     visited.append(e)
                     #print('In ELIF',visited)
                elif isinstance(e,Iterable) and isinstance(e,dict)==False:
                    for element in e:
                        if isinstance(element,dict):
                         #visited.remove(el)
                         visited.append(element)

#Task 2
def deep_find_all_dfs(data, key):
   found_values = []
   for k,v in data.items():
        #print('k:',k,"v:",v)
        if k==key:
            found_values.append(v)
        elif isinstance(v,dict):
            if deep_find(v,key)!= None:
                found_values+=deep_find_all_dfs(v,key)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    if deep_find(el,key)!= None:
                         found_values+=deep_find_all_dfs(el,key)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            if deep_find(element,key)!= None:
                                 found_values+=deep_find_all_dfs(element,key)
   #print(found_values)
   return found_values


def deep_find_all_bfs(data, key):
   visited=[]
   found_values = []
   for k,v in data.items():
        
        if k==key:
            find_el=True
            #return v
            found_values.append(v)
            #print('found_values',found_values)
        elif isinstance(v,dict):
            visited.append(v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            visited.append(v)
        #print('k:',k,', visited: ',visited)

   for el in visited:
        if isinstance(el,dict):
            #print("el in if : ",el)
            for k,v in el.items():
                 #print("k:",k,"v:",v)
                 if k==key:
                    find_el=True
                    found_values.append(v)
                    #return v
                 elif isinstance(v,dict):
                    #visited.remove(el)
                    visited.append(v)
                    #print('k:',k,'in',visited)
                 elif isinstance(v, Iterable)==True and isinstance(v,dict)==False:
                    for e in v:
                        if isinstance(e,dict):
                            #visited.remove(el)
                            visited.append(e)
                            #print('In',visited)
                            

        elif isinstance(el, Iterable) and isinstance(el,dict)==False:
            #print("el in elif: ",el)
            for e in el:
                if isinstance(e,dict):
                     #visited.remove(el)
                     visited.append(e)
                     #print('In ELIF',visited)
                elif isinstance(e,Iterable) and isinstance(e,dict)==False:
                    for element in e:
                        if isinstance(element,dict):
                         #visited.remove(el)
                         visited.append(element)
   return found_values

#Task 3
def deep_update(data, key, val):
    for k,v in data.items():
        #print('k:',k,"v:",v)
        if k==key:
            data[k]=val
        elif isinstance(v,dict):
            deep_update(v,key,val)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                if isinstance(el,dict):               
                    deep_update(el,key,val)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):                       
                            deep_update(element,key,val)

#Task 4
def func(key):
    new_key=key+'s'
    return new_key

#In Python 3, d.items() is a view into the dictionary, like d.iteritems() in Python 2. To do this in Python 3, 
#instead use d.copy().items(). This will similarly allow us to iterate over a copy of the dictionary in order to
#avoid modifying the data structure we are iterating over. If I use only data.items() there are problems-the loop starts all over again
#because it has been modified
def deep_apply(func, data):
   for k,v in data.copy().items():
        #print('k:',k,"v:",v)
        #print('data1:',data)
        ks=func(k)
        if isinstance(v,Iterable)==False or isinstance(v,str)==True:
            #print('A k:',k)
            data[ks]=data.pop(k)
            #print('in A, data:',data)
        elif isinstance(v,dict):
            #print('B k:',k)
            d=deep_apply(func, v)
            data[ks]=d
            del data[k]
            #print('in B, data:',data)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            type_of_object=type(v)
            new_v=type_of_object()
            #print('C k:',k)
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    #print('CC k:',k)
                    d=deep_apply(func, el)
                    if isinstance(new_v,tuple):
                        l=list(new_v)
                        l.append(d)
                        new_v=tuple(l)
                    else:
                        new_v.append(d)

                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    type_of_object=type(v)
                    new_v=type_of_object()
                    #print('CCC k:',k)
                    for element in el:
                        if isinstance(element,dict):
                            d=deep_apply(func, element)
                            if isinstance(new_v,tuple):
                                l=list(new_v)
                                l.append(d)
                                new_v=tuple(l)
                            else:
                                new_v.append(d)
                        else:
                            if isinstance(new_v,tuple):
                                l=list(new_v)
                                l.append(element)
                                new_v=tuple(l)
                            else:
                                new_v.append(element)

                else:
                     if isinstance(new_v,tuple):
                        l=list(new_v)
                        l.append(el)
                        new_v=tuple(l)
                     else:
                        new_v.append(el)
            #print('new_v:',new_v,'v:',v)
            data[ks]=new_v
            del data[k]

   #print('data2: ',data)
   return data

#Task6
def make_flat_lst(lst):
    flat_lst=[]
    for el in lst:
        if isinstance(el,list):
            flat_lst+=make_flat_lst(el)
        else:
            flat_lst.append(el)

    return flat_lst

def schema_validator(schema: list, data: dict):
   flat_lst=make_flat_lst(schema)
   found_keys=[]
   visited=[]
   for k,v in data.items():       
        found_keys.append(k)
        if isinstance(v,dict):
            visited.append(v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False and isinstance(v,str)==False:
            visited.append(v)
   #print('found_keys',found_keys,'visited:',visited)
   for el in visited:
        #print('el:',el,'visited:',visited)
        if isinstance(el,dict):
            #print("el in if : ",el)
            for k,v in el.items():
                 found_keys.append(k)
                 if isinstance(v,dict):
                    #visited.remove(el)
                    visited.append(v)
                    #print('k:',k,'in',visited)
                 elif isinstance(v, Iterable)==True and isinstance(v,dict)==False and isinstance(v,str)==False:
                    for e in v:
                        if isinstance(e,dict):
                            #visited.remove(el)
                            visited.append(e)
                            #print('In',visited) 
        elif isinstance(el, Iterable) and isinstance(el,dict)==False and isinstance(el,str)==False:
            #print("el in elif: ",el)
            for e in el:
                if isinstance(e,dict):
                     #visited.remove(el)
                     visited.append(e)
                     #print('In ELIF',visited)
                elif isinstance(e,Iterable) and isinstance(e,dict)==False:
                    for element in e:
                        if isinstance(element,dict):
                         #visited.remove(el)
                         visited.append(element)

   found_keys = list(dict.fromkeys(found_keys))#we remove the duplicates
   flat_lst = list(dict.fromkeys(flat_lst))#we remove the duplicates
   flat_lst_len=len(flat_lst)
   # print('!!! found_keys',found_keys)
   # print('schema:',flat_lst)
   if flat_lst_len!=len(found_keys):
        msg='Not equal number of elements'
        return (False,msg)
   else:
       for key in flat_lst:
            if key not in found_keys:
                return False       
       return True



def main():
    data={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'C2':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9}}),
          'F':6
          }
    data2={
            'A':{
                'X':{'C1':1000}
                },
            'B':[2,3],
            'C':{
                'C1':2,
                'C2':3,
                'C3':{
                    'C31':11,
                    'C32':[{'C32_INNER':111}]
                }            }
    }



    # print(data)
    # print('D4 in BFS')
    # print(deep_find_bfs(data,'D4'))
    # print('D4 in DFS')
    # print(deep_find(data,'D4'))

    # print('E2_inner in BFS')
    # print(deep_find_bfs(data,'E2_inner'))
    # print('E2_inner in DFS')
    # print(deep_find(data,'E2_inner'))

    # print('C1 in BFS')
    # print(deep_find_bfs(data,'C1'))
    # print('C1 in DFS')
    # print(deep_find(data,'C1'))

    # print('B1 in BFS')
    # print(deep_find_bfs(data,'B1'))
    # print('B1 in DFS')
    # print(deep_find(data,'B1'))

    # print('Z in BFS')
    # print(deep_find_bfs(data,'Z'))
    # print('Z in DFS')
    # print(deep_find(data,'Z'))


    print('================')
    print(data2)
    print('C1 in BFS')
    print(deep_find_bfs(data2,'C1'))
    print('C1 in DFS')
    print(deep_find(data2,'C1'))

    print('C32_INNER in BFS')
    print(deep_find_bfs(data2,'C32_INNER'))
    print('C32_INNER in DFS')
    print(deep_find(data2,'C32_INNER'))

    print('===========ALL=============')
    data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
    # print('all values of C1 using dfs')
    # print(deep_find_all_dfs(data2,'C1'))
    # print('all values of C1 using bfs')
    # print(deep_find_all_bfs(data2,'C1'))
    # print('all values of X in data3 using bfs')
    # print(deep_find_all_bfs(data3,'X'))


    # print('=======COMPARE========')
    # data4={
    #         'A':{
    #             'X':{'C1':1000}
    #             },
    #         'B':[2,3],
    #         'C':{
    #             'C1':2,
    #             'C2':3,
    #             'C3':{
    #                 'C31':11,
    #                 'C32':[{'C32_INNER':111}]
    #             }            }
    # }
    # d1={'A':'aa','B':5,'C':{'C1':"cc"},'D':[1,2,{'D1':55}]}
    # d2={'A':'aa','B':5,'C':{'C1':'cc'},'D':[1,2,{'D1':55}]}
    # s1=[1,2,{'A':'aa'}]
    # s2=[1,2,{'A':'aa'}]
    # print(s1==s2)
    # print(d1==d2)
    # #print(deep_compare(d1,d2))
    # print(d1)
    # print(deep_compare_bfs(d1,d2))
    # print(deep_find_bfs(d1,'D1'))
    # #print(deep_compare(data2,data4))





if __name__=='__main__':
    main()
    