from song import Song

import unittest

class TestSong(unittest.TestCase):
    def test_length(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        expected_result="3:44"
        self.assertEqual(s.length(),expected_result)
    def test_length_seconds(self):
        s=Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:1:10")
        expected_result=int("3670")
        self.assertEqual(s.length(seconds=True),expected_result)
    def test_length_mins(self):
        s=Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:1:10")
        expected_result=int("61")
        self.assertEqual(s.length(minutes=True),expected_result)
    def test_length_hours(self):
        s=Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="70:10")
        expected_result=int("1")
        self.assertEqual(s.length(hours=True),expected_result)



if __name__=='__main__':
     unittest.main()