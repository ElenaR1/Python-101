import datetime
from collections import defaultdict
from itertools import combinations

def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str

def filter(file_name):
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    #print(array)
    #print('-------------')
    for i in range(len(array)):
        array[i]=remove_newline(array[i])
        array[i]=array[i].split(',')
    
    for el in array:
        for i in range(len(el)):
            if el[i]=='NULL':
                el[i]=str(datetime.date.today())
    #print('-------------')
    #print(array)
    #print('-------------')
    d = defaultdict(list)
    newdict = defaultdict(list)
    #we create a dictionary where the keys are the projects' ids
    for el in array[1:]:
        EmpID,ProjectID,DateFrom,DateTo=el[0],el[1],el[2],el[3]
        d[ProjectID].append([EmpID,DateFrom,DateTo])
    #print(d)
    for key,val in d.items():
        #we only look at projects with more than one employees involved
        if len(val) >= 2:
            #we find all possible combinations for the projects
            combins=combinations(val,2)
            for comb in combins:
                #print(comb)
                #map transforms the comb list by applying the lambda functio. By applying max we find the max starting date
                start = max(map(lambda x: x[1], comb))
                #print(list(map(lambda x: x[1], comb)), 'start: ',start)
                end = min(map(lambda x: x[2], comb))
                #print(list(map(lambda x: x[2], comb)), 'end: ',end)
                difference = datetime.datetime.strptime(end, '%Y-%m-%d') \
                        - datetime.datetime.strptime(start, '%Y-%m-%d')
                difference_between_dates = difference.days

                #we are only interested in the case whete two or more than two ppl have worked at the same time on the project
                if difference_between_dates > 0:
                    newdict[(comb[0][0],comb[1][0])].append(difference_between_dates)
                    print('employees:', comb[0][0], ' and ', comb[1][0],
                          'worked on project: ',
                          key, ' for ', difference_between_dates, 'days\n')
                else:
                    print('employees:', comb[0][0], ' and ', comb[1][0],
                          'have not worked together on project: '+ key+' \n')

    key_corresponding_to_max_val=max(newdict, key = newdict.get)
    print('Pair of employees that worked together for the longest time ' +  key_corresponding_to_max_val[0] +' and '+ key_corresponding_to_max_val[1] +
     '. They worked together for '+ str(max(newdict[key_corresponding_to_max_val])) + ' days.')


    



def main():
    filter('employees.txt')


if __name__=='__main__':
    main()
