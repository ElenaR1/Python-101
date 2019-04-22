from collections.abc import Iterable

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
                #print('el:',el)
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

found_values=[]
def deep_find_all(data, key):  
   for k,v in data.items():
        print('k:',k,"v:",v)
        if k==key:
            print('!!! EQUAL !!!','k:',k,"v:",v)
            found_key=True
            return v
        elif isinstance(v,dict):
            print('FER')
            if deep_find_all(v,key)!= None:
                print('fergre')
                print('A k:',k,"v:",v)
                found_key=True
    #             found_values.append(v)
                val_to_add=deep_find_all(v,key)
                print('A k:',k,"val_to_add:",val_to_add)
                found_values.append(val_to_add)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    if deep_find_all(el,key)!= None and isinstance(deep_find_all(el,key))!=list:
                        print('B k:',k,"v:",v)
                        found_key=True
                    #     found_values.append(el)
                        val_to_add=deep_find_all(el,key)
                        print('B k:',k,"val_to_add:",val_to_add)
                        found_values.append(val_to_add)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            print('C k:',k,"v:",v)
                            if deep_find_all(element,key)!= None  and isinstance(deep_find_all(el,key))!=list:
                                found_key=True
                            #     found_values.append(element)
                                val_to_add=deep_find_all(element,key)
                                print('C k:',k,"val_to_add:",val_to_add)
                                found_values.append(val_to_add)
   print('data:',data,'found_values:',found_values)
   #return found_values
   arr_of_found_values=found_values
   # for el in found_values:
   #      arr_of_found_values.append(el)
   # print('arr_of_found_values:',arr_of_found_values)
   # return arr_of_found_values



def deep_find_all2(data, key):  
   for k,v in data.items():
        #print('k:',k,"v:",v)
        if k==key:
            found_key=True
            yield v
        elif isinstance(v,dict):
            if deep_find_all2(v,key)!= None:
                        found_key=True
            #             found_values.append(v)
                        val= deep_find_all2(v,key)
                        yield val                       
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    if deep_find_all2(el,key)!= None:
                        found_key=True
                    #     found_values.append(el)
                        val= deep_find_all2(el,key)
                        yield val
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            if deep_find_all2(element,key)!= None:
                                found_key=True
                                val= deep_find_all2(element,key)
                                yield val


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

def deep_apply(func, data):
    new_dict=dict()
    for k,v in data.items():
        #print('k:',k,"v:",v)
        # if k==key:
        #     data[k]=val
        k=func(k)
        #print('k:',k,'v:',v)
        if isinstance(v,int):
            new_dict[k]=v
        if isinstance(v,dict):
            deep_apply(func,v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            #el_to_copy
            for el in v:
                if isinstance(el,dict):               
                    val=deep_apply(func,el)
                    print('B val:',val)
                    new_dict[k]=val
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):                       
                            val=deep_apply(func,element)
                            print('C val:',val)
                            new_dict[k]=val
        print('IN FOR new_dict:',new_dict)
    print('OUT OF  FOR new_dict:',new_dict)
    return new_dict


def deep_app(func, data):
   for k,v in data.items():
        #print('k:',k,"v:",v)
        ks=func(k)
        if isinstance(v,Iterable)==False:
            data[ks]=data.pop(k)
        elif isinstance(v,dict):
            # if deep_find(v,key)!= None:
            #             found_key=True
            deep_app(func, v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    # if deep_find(el,key)!= None:
                    #     found_key=True
                    deep_app(func, el)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            # if deep_find(element,key)!= None:
                            #     found_key=True
                            deep_app(func, element)

   print(data)


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

    # print('===========ALL=============')
    # print('C1')
    # print(deep_find_all(data2,'C1'))
    # print(len(data2))
    # print('--')
    # l=list(deep_find_all2(data2,'C1'))
    # for el in l:
    #     print(el)

    print('===========Apply=============')
    d={'a':1,'b':2,'c':3}
    for k, v in d.items():
        ks=func(k)
        d[ks]=d.pop(k)
        # del d[k]
    print(d)
    data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
    # print(data3)
    # print(deep_apply(func,data3))
    # print(data3)
    deep_app(func,data3)



if __name__=='__main__':
    main()
    
