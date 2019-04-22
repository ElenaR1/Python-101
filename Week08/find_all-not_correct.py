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
