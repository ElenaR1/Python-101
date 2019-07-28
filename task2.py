import string
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import csv
import re


def filter(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    exclude = set(string.punctuation)
    numbers={'0':'zero','1':'one', '2':'two', '3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    f.close()
    #print(array)
    for i in range(len(array)):
        array[i]=array[i].split(',')
    #print('-------------')
    #print(array)

    # for i in range(len(array)):
    #     n=len(array[i])
    #     if n > 6:
    #         num_of_additional_cols= n -6        
    #         array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]

    for el in array:
        #print(el[1],el[4],el[5])
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='Language':
                if el[4]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False           

        if add_element==True:
            el[0]=''.join(ch for ch in el[0] if ch.isalnum() and ch not in exclude or ch==' ')#for the special characters

            el[7]=''.join(ch for ch in el[7] if ch.isalnum() and ch not in exclude or ch==' ')

            # el[7] = ''.join(ch for ch in el[7] if ch not in exclude)
            # el[7]=''.join(ch for ch in el[7] if ch.isalnum() or ch==' ')

            for ch in el[0]:
                if ch in numbers.keys():
                    el[0]=el[0].replace(ch,numbers[ch])
            for ch in el[7]:
                if ch in numbers.keys():
                    el[7]=el[7].replace(ch,numbers[ch])
            el[0]=el[0].lower()
            el[7]=el[7].lower()

            ps = PorterStemmer()         
            arr_of_snd_part=el[7].split()
            arr_of_snd_part=[ps.stem(word) for word in arr_of_snd_part]
            el[7]=' '.join(arr_of_snd_part)
            result_array[len(result_array):]=[[el[0],el[7]]]
        else:
            add_element=True


    l=len(result_array)

    # print(result_array[0:4])

    with open('transformed_records.csv', 'w',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(result_array)
    csvFile.close()

    print(l)
    # for i in range(0,4):
    #     print(result_array[i])
    #return result_array[0:4]


def main():
#     print('filter')
#     s = "ab1k0"
#     numbers={'0':'zero','1':'one', 2:'two', 3:'three'}
#     print('0' in numbers.keys(),numbers['0'])
#     for el in s:
#         if el in numbers.keys():
#             s=s.replace(el,numbers[el])
#             print(s)

    exclude = set(string.punctuation)
    # ss="hello? there A-Z-R_T(,**), world, welcome to python.this **should? the next line#followed- by@ an#other %million^ %%like $this."
    # ss = ''.join(ch for ch in ss if ch not in exclude)
    # print(ss)

    ps = PorterStemmer() 
  
    # a=['ukrnzerozerozerofourfourfourtwotwofour', 'postglacial permian stratigraphy and geography of southern and central africa boundary conditions for climatic modelling']
    # arr_a=a[1].split()
    # arr_a=[ps.stem(word) for word in arr_a]
    # print(arr_a)
    # a[1]=' '.join(arr_a)
    # print(a)
   

    filter('records.csv',Language='English')
    # exclude = set(string.punctuation)
    # s="embryo-like fossils early metazoans?"
    # s = ''.join(ch for ch in s if ch not in exclude)
    # print(s)

    # k='"A theropod–sauropod track assemblage from the ?Middle–Upper Jurassic Shedian Formation at Shuangbai'
    # print(k)
    
    # a=''.join(ch for ch in k if ch.isalnum() and ch not in exclude or ch==' ')
    # #a=''.join(ch for ch in k if ch not in exclude)
    # print(a)


if __name__=='__main__':
    main()
