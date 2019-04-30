#Task 5
def deep_compare(obj1,obj2):
  for k,v in obj1.items():
        #print('k:',k,"v:",v)
        if k not in obj2:
            print('key',k,'does not exist in obj2')
            return False
        else:
            #print('out v',v)
            if isinstance(v,Iterable)==False or isinstance(v,str)==True:
                if obj1[k]!=obj2[k]:
                    print("-",k,":",obj1[k])
                    print("-",k,":",obj2[k])
                    return False
            elif isinstance(v,dict):
                deep_compare(obj1[k],obj2[k])
            elif isinstance(v, Iterable) and isinstance(v,dict)==False:#v=obj1[k]
                print(v,obj1[k],obj2[k])
                for el1 in obj1[k]:
                    print(el1)
                    if el1 not in obj2[k]:
                        print(el1,"not in obj2 in the value corresponding to key",k)
                        return False
                    if isinstance(el1,dict):
                        #deep_compare(el,key)
                        pass
        #         elif isinstance(el,Iterable) and isinstance(el,dict)==False:
        #             for element in el:
        #                 if isinstance(element,dict):
        #                     if deep_compare(element,key)!= None:
        #                         found_key=True
        #                         return deep_compare(element,key)
def deep_compare2(obj1, obj2):
   visited1=[]
   visited2=[]
   for k,v in obj1.items():
        #print('k:',k,"v:",v)
        if k not in obj2:
            print('key',k,'does not exist in obj2')
            return False
   else:
       for k,v in obj1.items():
            visited1.append(v)
            #print('k:',k,', visited: ',visited)
       for k,v in obj2.items():
            visited2.append(v)

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


def deep_compare_bfs(data, data2):
   visited=[]
   found_values = []
   visited2=[]
   found_values2 = []
   for k,v in data.items():        
        if isinstance(v,dict):
            visited.append(v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False and isinstance(v,str)==False:
            visited.append(v)
        else:
            visited.append(v)
        #print('k:',k,', visited: ',visited)
   print('k:',k,', visited: ',visited)
   for k,v in data2.items():        
        if isinstance(v,dict):
            visited2.append(v)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False and isinstance(v,str)==False:
            visited2.append(v)
        else:
            visited2.append(v)
   print('k:',k,', visited2: ',visited2)

   for el in visited:
        if isinstance(el,dict):
            #print("el in if : ",el)
            for k,v in el.items():
                 #print("k:",k,"v:",v)
                 if isinstance(v,dict):
                    #visited.remove(el)
                    visited.append(v)
                    #print('k:',k,'in',visited)
                 elif isinstance(v, Iterable)==True and isinstance(v,dict)==False :
                    for e in v:
                        if isinstance(e,dict):
                            #visited.remove(el)
                            visited.append(e)
                            #print('In',visited)
                 else:
                    visited.append(v)
                            

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
   for el in visited2:
        if isinstance(el,dict):
            #print("el in if : ",el)
            for k,v in el.items():
                 #print("k:",k,"v:",v)
                 if isinstance(v,dict):
                    #visited.remove(el)
                    visited2.append(v)
                    #print('k:',k,'in',visited)
                 elif isinstance(v, Iterable)==True and isinstance(v,dict)==False:
                    for e in v:
                        if isinstance(e,dict):
                            #visited.remove(el)
                            visited2.append(e)
                            #print('In',visited)
                 else:
                    visited2.append(v)
                            

        elif isinstance(el, Iterable) and isinstance(el,dict)==False:
            #print("el in elif: ",el)
            for e in el:
                if isinstance(e,dict):
                     #visited.remove(el)
                     visited2.append(e)
                     #print('In ELIF',visited)
                elif isinstance(e,Iterable) and isinstance(e,dict)==False:
                    for element in e:
                        if isinstance(element,dict):
                         #visited.remove(el)
                         visited2.append(element)
   print('visited:',visited)
   print('visited2:',visited2)
   return visited==visited2


 print('=======COMPARE========')
    data4={
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
    d1={'A':'aa','B':5,'C':{'C1':"cc"},'D':[1,2,{'D1':55}]}
    d2={'A':'aa','B':5,'C':{'C1':'cc'},'D':[1,2,{'D1':55}]}
    s1=[1,2,{'A':'aa'}]
    s2=[1,2,{'A':'aa'}]
    print(s1==s2)
    print(d1==d2)
    #print(deep_compare(d1,d2))
    print(d1)
    print(deep_compare_bfs(d1,d2))
    print(deep_find_bfs(d1,'D1'))
    #print(deep_compare(data2,data4))
