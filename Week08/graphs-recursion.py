find_el=False
def deep_find_bfs(data, key):
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
        print('k:',k,', FOUND: ',found)
   if find_el==False:
        for el in found:
            if isinstance(el,dict):
                if deep_find_bfs(el,key)!= None:
                        print('in')
                        return deep_find_bfs(el,key)

                elif isinstance(el, Iterable) and isinstance(el,dict)==False:
                    for e in el:
                        if isinstance(e,dict):
                            if deep_find_bfs(e,key)!= None:
                                return deep_find_bfs(e,key)






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
        print('k:',k,', FOUND: ',found)
   if find_el==False:
        for el in found:
            if isinstance(el,dict):
                # if deep_find_bfs(el,key)!= None:
                #         print('in')
                #         return deep_find_bfs(el,key)
                for k,v in el.items():
                     if k==key:
                        find_el=True
                        return v
                     elif isinstance(v,dict):
                        found.append(v)



            elif isinstance(el, Iterable) and isinstance(el,dict)==False:
                for e in el:
                    if isinstance(e,dict):
                        if deep_find_bfs(e,key)!= None:
                            return deep_find_bfs(e,key)
