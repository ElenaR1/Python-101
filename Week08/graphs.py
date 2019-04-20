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

def deep_find_bfs2(data, key):
   found=[]
   find_el=False
   #global find_el
   for k,v in data.items():
        
        if k==key:
            find_el=True
            return v
        elif isinstance(v,dict):
            found.append(v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            found.append(v)
        #print('k:',k,', FOUND: ',found)

   while find_el==False:
        for el in found:
            if isinstance(el,dict):
                #print("el in if : ",el)
                for k,v in el.items():
                     #print("k:",k,"v:",v)
                     if k==key:
                        find_el=True
                        return v
                     elif isinstance(v,dict):
                        #found.remove(el)
                        found.append(v)
                        #print('k:',k,'in',found)
                     elif isinstance(v, Iterable)==True and isinstance(v,dict)==False:
                        for e in v:
                            if isinstance(e,dict):
                                #found.remove(el)
                                found.append(e)
                                #print('In',found)
                                

            elif isinstance(el, Iterable) and isinstance(el,dict)==False:
                #print("el in elif: ",el)
                for e in el:
                    if isinstance(e,dict):
                         #found.remove(el)
                         found.append(e)
                         #print('In ELIF',found)
                    elif isinstance(e,Iterable) and isinstance(e,dict)==False:
                        for element in e:
                            if isinstance(element,dict):
                             #found.remove(el)
                             found.append(element)



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
    print(data)
    print('D4 in BFS')
    print(deep_find_bfs2(data,'D4'))
    print('D4 in DFS')
    print(deep_find(data,'D4'))

    print('E2_inner in BFS')
    print(deep_find_bfs2(data,'E2_inner'))
    print('E2_inner in DFS')
    print(deep_find(data,'E2_inner'))

    print('C1 in BFS')
    print(deep_find_bfs2(data,'C1'))
    print('C1 in DFS')
    print(deep_find(data,'C1'))

    print('B1 in BFS')
    print(deep_find_bfs2(data,'B1'))
    print('B1 in DFS')
    print(deep_find(data,'B1'))

    # print('Z in BFS')
    # print(deep_find_bfs2(data,'Z'))
    print('Z in DFS')
    print(deep_find(data,'Z'))


    print('================')
    print(data2)
    print('C1 in BFS')
    print(deep_find_bfs2(data2,'C1'))
    print('C1 in DFS')
    print(deep_find(data2,'C1'))

    print('C32_INNER in BFS')
    print(deep_find_bfs2(data2,'C32_INNER'))
    print('C32_INNER in DFS')
    print(deep_find(data2,'C32_INNER'))



if __name__=='__main__':
    main()
    