"""Dict"""
def dict_reader_tuple(file_dict: str) -> list[tuple]:
    """
    Read dict and return a list of tuples.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as tmpfile:
    ...     _=tmpfile.write('NACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_tuple(tmpfile.name)
    [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z'])]
    """
    res = []
    with open(file_dict, 'r', encoding='utf-8') as file:
        dictionary = file.read().strip().split('\n')
        for line in dictionary:
            temp = line.split()
            word = temp[0]
            pronun_num = int(temp[1])
            phon = temp[2:]
            res.append((word, pronun_num, phon))
        return res

def dict_reader_dict(file_dict: str) -> dict:
    """
    Read dictionary from file and return a dictionary.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as tmpfile:
    ...     _=tmpfile.write('NACHOS 1 N AA1 CH OW0 Z\\nNACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_dict(tmpfile.name)['NACHOS'] \
== {('N', 'AE1', 'CH', 'OW0', 'Z'), ('N', 'AA1', 'CH', 'OW0', 'Z')}
    True
    """
    dictionary = {}
    with open(file_dict, 'r', encoding='utf-8') as file:
        diction = file.read().strip().split('\n')
        for line in diction:
            temp = line.split()
            word = temp[0]
            pronun_num = int(temp[1])
            phon = temp[2:]
            if pronun_num == 1:
                dictionary[word] = tuple(phon)
            elif pronun_num == 2:
                dictionary[word] = {dictionary[word], tuple(phon)}
            else:
                dictionary[word] = dictionary[word].union({tuple(phon)})
    return dictionary

def dict_invert(dct) -> dict:
    """
    Convert dictionary into a dict where keys are the numbers
    of pronunciations and the values are tuples containing words 
    with the specified number of pronunciations. Each tuple contains 
    the word itself and a tuple of phonemes.
    >>> dict_invert([("NACHOS", 2, ["N", "AE1", "CH", "OW0", "Z"])])
    {2: {('NACHOS', ('N', 'AE1', 'CH', 'OW0', 'Z'))}}
    """
    res = {}
    if isinstance(dct, list):
        for i in dct:
            word, n_pr, phon = i
            if n_pr in res:
                res[n_pr].add((word, tuple(phon)))
            else:
                res[n_pr] = {(word, tuple(phon))}
    return res

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
