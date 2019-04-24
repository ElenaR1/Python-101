import unittest
from graphs import deep_find, deep_find_bfs,deep_update,deep_find_all_dfs,deep_find_all_bfs,func,deep_apply

class GraphsTest(unittest.TestCase):
    data={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'C2':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9}}),
          'F':6
          }
    data2={
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
    data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
    def test_DFS_deep_find_when_key_is_in_a_dict_inside_an_iterable(self):
        key_to_find='C1'
        expected_result=100
        self.assertEqual(deep_find(self.data,key_to_find), expected_result)
    def test_BFS_deep_find_bfs_when_key_is_in_a_dict_inside_an_iterable(self):
        key_to_find='C1'
        expected_result=4
        self.assertEqual(deep_find_bfs(self.data,key_to_find), expected_result)

    def test_DFS_deep_find_when_key_is_in_a_dict_inside_an_iterable2(self):
        key_to_find='B1'
        expected_result=10000
        self.assertEqual(deep_find(self.data,key_to_find), expected_result)
    def test_BFS_deep_find_bfs_when_key_is_in_a_dict_inside_an_iterable2(self):
        key_to_find='B1'
        expected_result=33
        self.assertEqual(deep_find_bfs(self.data,key_to_find), expected_result)

    def test_DFS_deep_find_when_key_is_in_a_dict_inside_an_iterable_which_is_inside_another_iterable(self):
        key_to_find='D4'
        expected_result=77
        self.assertEqual(deep_find(self.data,key_to_find), expected_result)
    def test_BFS_deep_find_bfs_when_key_is_in_a_dict_inside_an_iterable_which_is_inside_another_iterable(self):
        key_to_find='D4'
        expected_result=77
        self.assertEqual(deep_find_bfs(self.data,key_to_find), expected_result)

    def test_DFS_deep_find_when_key_is_in_a_dict_inside_another_dict(self):
        key_to_find='E2_inner'
        expected_result=9
        self.assertEqual(deep_find(self.data,key_to_find), expected_result)
    def test_BFS_deep_find_bfs_when_key_is_in_a_dict_inside_another_dict(self):
        key_to_find='E2_inner'
        expected_result=9
        self.assertEqual(deep_find_bfs(self.data,key_to_find), expected_result)

    def test_DFS_deep_find_when_key_is_absent(self):
        key_to_find='Z'
        expected_result=None
        self.assertEqual(deep_find(self.data,key_to_find), expected_result)
    def test_BFS_deep_find_bfs_when_key_is_test_DFS_deep_find_when_key_is_absent(self):
        key_to_find='Z'
        expected_result=None
        self.assertEqual(deep_find_bfs(self.data,key_to_find), expected_result)


    def test_deep_find_all_dfs_when_key_appears_more_than_once(self):
        key_to_find='C1'
        expected_result=[1000, 2]
        self.assertEqual(deep_find_all_dfs(self.data2,key_to_find), expected_result)

    def test_deep_find_all_dfs_when_key_is_absent(self):
        key_to_find='Z'
        expected_result=[]
        self.assertEqual(deep_find_all_dfs(self.data2,key_to_find), expected_result)

    def test_deep_find_all_bfs_when_key_appears_more_than_once(self):
        key_to_find='C1'
        expected_result=[2, 1000]
        self.assertEqual(deep_find_all_bfs(self.data2,key_to_find), expected_result)
    def test_deep_find_all_bfs_when_key_appears_more_than_once_in_more_cimplex_structure(self):
        data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
        key_to_find='X'
        expected_result=[5, [[1, 2, 3, {'B1': 10000}], {'C1': 100}], 55]
        self.assertEqual(deep_find_all_bfs(data3,key_to_find), expected_result)
    def test_deep_find_all_bfs_when_key_is_absent(self):
        key_to_find='Z'
        expected_result=[]
        self.assertEqual(deep_find_all_bfs(self.data2,key_to_find), expected_result)



    #Tests for Task3
    def test_data_after_deep_update(self):
        data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
        key_to_update='X'
        val=500
        expected_result={'A': [1, {'X': 500}, {'D4': 'oo'}], 'B': [2, 3, {'B1': 33}], 'C': {'C1': 4, 'X': 500}, 
        'D': [10, {'D1': 6, 'D2': 7}, [{'D3': 66}, {'D4': 77}]], 'E': ('e', {'E1': 8, 'E2': {'E2_inner': 9}, 'X': 500}), 'F': 6}
        deep_update(data3,key_to_update,val)
        self.assertEqual(data3, expected_result)
    def test_data_after_deep_update_of_a_key_with_different_type_of_values(self):
        data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }

        key_to_update='D4'
        val=500
        expected_result={'A': [1, {'X': [[1, 2, 3, {'B1': 10000}], {'C1': 100}]}, {'D4': 500}], 'B': [2, 3, {'B1': 33}],
         'C': {'C1': 4, 'X': 5}, 'D': [10, {'D1': 6, 'D2': 7}, [{'D3': 66}, {'D4': 500}]], 'E': ('e', {'E1': 8, 'E2': {'E2_inner': 9},
          'X': 55}), 'F': 6}
        deep_update(data3,key_to_update,val)
        self.assertEqual(data3, expected_result)
    def test_data_after_deep_update_of_a_key_that_is_absent(self):
        data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
        key_to_update='Z'
        val=500
        expected_result={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
        deep_update(data3,key_to_update,val)
        self.assertEqual(data3, expected_result)

    #Tests for Task4
    def test_data_after_deep_apply(self):
        data2={
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
        expected_result={'As': {'Xs': {'C1s': 1000}}, 'Bs': [2, 3], 'Cs': 
        {'C1s': 2, 'C2s': 3, 'C3s': {'C31s': 11, 'C32s': [{'C32_INNERs': 111}]}}}
        deep_apply(func,data2)
        self.assertEqual(data2, expected_result)
    def test_data_after_deep_apply_when_there_is_a_tuple(self):
        data3={'A':[1,{'X':[[1,2,3,{'B1':10000}],{'C1':100}]},{'D4':'oo'}],
          'B':[2,3,{'B1':33}],
          'C':{'C1':4, 'X':5},
          'D':[10,{'D1':6, 'D2':7}, [{'D3':66},{'D4':77}] ],
          'E':('e',{'E1':8,'E2':{'E2_inner': 9},'X':55}),
          'F':6
          }
        key_to_update='X'
        expected_result={'As': [1, {'Xs': [1, 2, 3, {'B1s': 10000}, {'C1s': 100}]}, {'D4s': 'oo'}], 'Bs': [2, 3, {'B1s': 33}],
         'Cs': {'C1s': 4, 'Xs': 5}, 'Ds': [{'D3s': 66}, {'D4s': 77}], 'Es': ('e', {'E1s': 8, 'E2s': {'E2_inners': 9}, 'Xs': 55}), 'Fs': 6}
        deep_apply(func,data3)
        self.assertEqual(data3, expected_result)



if __name__=='__main__':
     unittest.main()