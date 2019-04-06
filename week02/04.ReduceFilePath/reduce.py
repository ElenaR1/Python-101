def reduce_file_path(path):
    result=path
    dots='..'
    lst=[]
    for i in range(len(result)-1):
        if result[i]!=result[i+1] or result[i]!='/':
            lst=lst+[result[i]]
    #print(lst)
    lst=lst+[result[-1]]
    result=''.join(lst)

    while dots in result:
        position=result.rfind(dots)
        if position == 1:
            result = result[3:]
            #print(result)
            break
        result = result[:position-1] + result[(position+4):]
        #print(position,result[:position-1],"--",result[(position+4):],result)

        while True:
            #print(result[:position-1])
            result = result[:position-1]
            if result.endswith("/"):                
                break;
            position -=1

    result = result.replace("./","")

    if len(result)>1 and result[-1:]=="/":
        result = result[:-1]
    return result



print(reduce_file_path("/"))
print(reduce_file_path("/home//rositsazz/courses/./Programming-101-Python-2019/week02/../"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
