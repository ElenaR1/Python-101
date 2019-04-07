from mixins import *

import unittest
class TestMixins(unittest.TestCase):
     def test_to_json(self):
        p=Panda("Torry",3,True)
        print(p.__dict__)
        all_user_data = p
        expected_result="""{
    "dict:": {
        "name": "Torry",
        "age": 3,
        "eats_bamboo": true
    },
    "type": "Panda"
}"""

        self.assertEqual(p.to_jason(),expected_result)


     def test_from_json(self):
        expected_result=Panda("Torry",3,True)
        json_string="""{
    "dict:": {
        "name": "Torry",
        "age": 3,
        "eats_bamboo": true
    },
    "type": "Panda"
}"""
        self.assertEqual(Panda.from_json(json_string),expected_result)

     def test_to_xml(self):
       p=Panda("Torry",3,True)
       expected_result="<Panda><name>Torry</name><age>3</age><eats_bamboo>True</eats_bamboo></Panda>"

       self.assertEqual(p.to_xml(),expected_result)

     def test_from_xml(self):
        expected_result=Panda("Torry",3,True)
        xml_string="<Panda><name>Torry</name><age>3</age><eats_bamboo>True</eats_bamboo></Panda>"
        self.assertEqual(Panda.from_xml(xml_string),expected_result)

if __name__=='__main__':
     unittest.main()