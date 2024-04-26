import unittest
import tempfile
import os
from cmudict import dict_reader_tuple, dict_reader_dict, dict_invert

class TestDictFunctions(unittest.TestCase):

    def setUp(self):
        self.temp_files = []

    def tearDown(self):
        for tmp_file in self.temp_files:
            os.remove(tmp_file.name)

    def create_temp_file(self, content):
        tmp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        self.temp_files.append(tmp_file)
        with tmp_file as tmp:
            tmp.write(content)
        return tmp_file.name

    def test_dict_reader_tuple_empty_file(self):
        tmp_file = self.create_temp_file('')
        result = dict_reader_tuple(tmp_file)
        self.assertEqual(result, [])

    def test_dict_reader_tuple_single_word_multiple_pronunciations(self):
        content = 'NACHOS 2 N AE1 CH OW0 Z\nNACHOS 1 N AA1 CH OW0 Z'
        tmp_file = self.create_temp_file(content)
        result = dict_reader_tuple(tmp_file)
        expected = [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']), ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z'])]
        self.assertEqual(result, expected)

    def test_dict_reader_tuple_multiple_words_multiple_pronunciations(self):
        content = 'NACHOS 2 N AE1 CH OW0 Z\nSLAVUTA 1 SL A VU TA\nWATER 1 W A T E R'
        tmp_file = self.create_temp_file(content)
        result = dict_reader_tuple(tmp_file)
        expected = [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']), ('SLAVUTA', 1, ['SL', 'A', 'VU', 'TA']), ('WATER', 1, ['W', 'A', 'T', 'E', 'R'])]
        self.assertEqual(result, expected)

    def test_dict_reader_dict_empty_file(self):
        tmp_file = self.create_temp_file('')
        result = dict_reader_dict(tmp_file)
        self.assertEqual(result, {})

    def test_dict_reader_dict_single_word_multiple_pronunciations(self):
        content = 'NACHOS 2 N AE1 CH OW0 Z\nNACHOS 1 N AA1 CH OW0 Z'
        tmp_file = self.create_temp_file(content)
        result = dict_reader_dict(tmp_file)
        expected = {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z'), ('N', 'AA1', 'CH', 'OW0', 'Z')}}
        self.assertEqual(result, expected)

    def test_dict_reader_dict_multiple_words_multiple_pronunciations(self):
        content = 'NACHOS 2 N AE1 CH OW0 Z\nSLAVUTA 1 SL A VU TA\nWATER 1 W A T E R'
        tmp_file = self.create_temp_file(content)
        result = dict_reader_dict(tmp_file)
        expected = {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z')}, 'SLAVUTA': {('SL', 'A', 'VU', 'TA')}, 'WATER': {('W', 'A', 'T', 'E', 'R')}}
        self.assertEqual(result, expected)

    def test_dict_invert_empty_dict(self):
        result = dict_invert({})
        self.assertEqual(result, {})

    def test_dict_invert_single_word_single_pronunciation(self):
        input_dict = {'WATER': {('W', 'A', 'T', 'E', 'R')}}
        result = dict_invert(input_dict)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)

    def test_dict_invert_single_word_multiple_pronunciations(self):
        input_dict = {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z'), ('N', 'AA1', 'CH', 'OW0', 'Z')}}
        result = dict_invert(input_dict)
        expected = {2: {('NACHOS', ('N', 'AE1', 'CH', 'OW0', 'Z')), ('NACHOS', ('N', 'AA1', 'CH', 'OW0', 'Z'))}}
        self.assertEqual(result, expected)

    def test_dict_invert_multiple_words_multiple_pronunciations(self):
        input_dict = {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z')}, 'SLAVUTA': {('SL', 'A', 'VU', 'TA')}, 'WATER': {('W', 'A', 'T', 'E', 'R')}}
        result = dict_invert(input_dict)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R')), ('SLAVUTA', ('SL', 'A', 'VU', 'TA')), ('NACHOS', ('N', 'AE1', 'CH', 'OW0', 'Z'))}}
        self.assertEqual(result, expected)
    def test_dict_invert_list_input_empty(self):
        input_list = []
        result = dict_invert(input_list)
        self.assertEqual(result, {})

    def test_dict_invert_list_input_single_word_single_pronunciation(self):
        input_list = [('WATER', 1, ['W', 'A', 'T', 'E', 'R'])]
        result = dict_invert(input_list)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)

    def test_dict_invert_list_input_single_word_multiple_pronunciations(self):
        input_list = [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']), ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z'])]
        result = dict_invert(input_list)
        expected = {2: {('NACHOS', ('N', 'AE1', 'CH', 'OW0', 'Z')), ('NACHOS', ('N', 'AA1', 'CH', 'OW0', 'Z'))}}
        self.assertEqual(result, expected)

    def test_dict_invert_list_input_multiple_words_multiple_pronunciations(self):
        input_list = [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']), ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z']), ('SLAVUTA', 1, ['SL', 'A', 'VU', 'TA']), ('WATER', 1, ['W', 'A', 'T', 'E', 'R'])]
        result = dict_invert(input_list)
        expected = {2: {('NACHOS', ('N', 'AE1', 'CH', 'OW0', 'Z')), ('NACHOS', ('N', 'AA1', 'CH', 'OW0', 'Z'))}, 1: {('SLAVUTA', ('SL', 'A', 'VU', 'TA')), ('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
