import json
from xml.etree import ElementTree as ET
from collections import namedtuple
class Jsonable:
    def to_jason(self,indent=4):
        my_dict={}
        print(self.__dict__)
        my_dict["dict:"]=self.__dict__
        my_dict["type"]=self.__class__.__name__
        y=json.dumps(my_dict,indent=indent)
        return y


    @classmethod
    def from_json(cls,json_string):
        print('====')
        l=[]
        d=json.loads(json_string)
        # for key,val in my_dict.items():
        #     print("key: ",key,"val:",val)
        #     if isinstance(val,dict):
        #         for k,v in val.items():
        #             print(k,v)
        #             l.append(v)
        # print(l)
        # p=my_dict['type']()
        #print(d)
        # print(d['dict:'].keys(),*d['dict:'].values())
        panda = namedtuple(d['type'], d['dict:'].keys())(*d['dict:'].values())
        return panda


class Xmlable :
    def to_xml(self,indent=4):
        result=""
        result+="<"+str(self.__class__.__name__)+">"
        for d in self.__dict__:
            result+="<"+d+">"+str(self.__dict__[d])+"</"+d+">"
        result+="</"+str(self.__class__.__name__)+">"
        return result

    @classmethod
    def from_xml(cls,json_string):
        attributes=[]
        values=[]
        my_dict={}
        root = ET.fromstring(json_string)
        print(root.tag)
        for child in root:
            #print(child)
            #print(dir(child))
            print(child.tag, child.text)
            if child.text.isdigit():
                my_dict[child.tag]=int(child.text)
                continue
            if child.text=='True' or child.text=='False':
                my_dict[child.tag]=bool(child.text)
                continue
            my_dict[child.tag]=child.text
            # attributes.append(child.tag)
            # values.append(child.text)
        #print(my_dict)
        panda=namedtuple(root.tag,my_dict.keys())(*my_dict.values())
        return panda


class Panda(Jsonable, Xmlable):
    def __init__(self, name,age,eats_bamboo):
        self.name = name
        self.age=age
        self.eats_bamboo=eats_bamboo
    def __eq__(self,other):
        if self.name!=other.name or self.age!=other.age or self.eats_bamboo!=other.eats_bamboo:
            return False
        else:
            return True


def main():
    p=Panda("Torry",3,True)
    print('--------P1--------')
    print(p.to_jason())
    json_string=p.to_jason()
    p1=Panda.from_json(json_string)
    print(p1.name,p1.age,p1.eats_bamboo)
    assert p==p1
    print('--------P2--------')
    xml_string=p.to_xml()
    print(xml_string)
    p2=Panda.from_xml(xml_string)

    print(p2.name,p2.age,p2.eats_bamboo)
    print(p1==p2)
    assert p1==p2
    assert p==p2
if __name__=='__main__':
    main()