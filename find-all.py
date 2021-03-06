
#Task 2
found_values=[]
def deep_find_all(data, key):  
   for k,v in data.items():
        #print('k:',k,"v:",v)
        if k==key:
            found_key=True
            #found_values.append(v)
            #print('found; ',found_values)
            return v
            #return found_values
        elif isinstance(v,dict):
            if deep_find_all(v,key)!= None:
                        found_key=True
            #             found_values.append(v)
                        val_to_add=deep_find_all(v,key)
                        found_values.append(val_to_add)
        elif isinstance(v, Iterable) and isinstance(v,dict)==False:
            for el in v:
                #print('el:',el)
                if isinstance(el,dict):
                    if deep_find_all(el,key)!= None:
                        found_key=True
                    #     found_values.append(el)
                        val_to_add=deep_find_all(el,key)
                        found_values.append(val_to_add)
                elif isinstance(el,Iterable) and isinstance(el,dict)==False:
                    for element in el:
                        if isinstance(element,dict):
                            if deep_find_all(element,key)!= None:
                                found_key=True
                            #     found_values.append(element)
                                val_to_add=deep_find_all(element,key)
                                found_values.append(val_to_add)
   print('data:',data,'found_values:',found_values)
   #return found_values



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
