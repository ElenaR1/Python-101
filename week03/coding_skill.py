import json
import operator
import sys

def read_json():
    with open('data.json', 'r') as f:
        data = json.load(f)

    return data

def exists(el,arr):
    if arr==[]:
        return False
    for tpl in arr:
        if el == tpl[2]:
            return True
    return False

def coding_skills(my_dict):
    languages=[]
    languages_and_skills=[]
    final_languages_and_skills=[]
    for person in my_dict['people']:
        for i in range (len(person['skills'])):
            # print(person['skills'][i])
            #print(person['first_name'],person['last_name'],person['skills'][i]['name'],person['skills'][i]['level'])
            if person['skills'][i]['name'] not in languages:
                languages.append(person['skills'][i]['name'])
            languages_and_skills.append((person['first_name'],person['last_name'],person['skills'][i]['name'],person['skills'][i]['level']))
    # print(languages)
    # print(languages_and_skills)
    languages_and_skills.sort(key = operator.itemgetter(3))
    languages_and_skills.reverse()
    #print(languages_and_skills)
    for tpl in languages_and_skills:
        if exists(tpl[2],final_languages_and_skills)==False:
            final_languages_and_skills.append(tpl[:3])
    print('----------------')
    #print(final_languages_and_skills)
    for ind,el in enumerate(final_languages_and_skills):
        print(el[2],el[0],el[1])



def main():
    file=sys.argv[1]
    with open(file, 'r') as f:
        my_dict = json.load(f)
    coding_skills(my_dict)



if __name__=='__main__':
    main()