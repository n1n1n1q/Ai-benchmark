"""
Keyword processor
"""
def find_film_keywords(film_keywords: dict, film_name: str)-> set():
    """
    Returns list of keywords for a certain film.
    >>> keywords={'unwashed-dishes': ['Withnail & I (1987)'], 'civil-war-monument': ['Without Li\
mits (1998)'],'eugene-register-the-newspaper': ['Without Limits (1998)'], 'hayward-field': ['Wit\
hout Limits (1998)'], 'reference-to-jim-ryan': ['Without Limits (1998)'], 'reference-to-n-sync':\
['Without Me (2002) (V)'], 'compensating': ['Without a Compass (2015)'], 'mid-life-crisis': ['Wi\
thout a Compass (2015)'], 'airplane-highjacker': ['Without a Paddle (2004)'], 'canoe-christening\
': ['Without a Paddle (2004)'], 'drug-plantation': ['Without a Paddle (2004)'], 'four-wheeler-ex\
plosion': ['Without a Paddle (2004)']}
    >>> find_film_keywords(keywords,'Without a Paddle (2004)')==\
{'drug-plantation', 'canoe-christening', 'four-wheeler-explosion', 'airplane-highjacker'}
    True
    """
    return set(key for key in film_keywords if film_keywords[key].count(film_name))


def find_films_with_keywords(film_keywords: dict, num_of_films: int)-> list:
    """
    Returns descending list of {num_of_films} tuples (film name, amount of keywords) 
    >>> keywords={'unwashed-dishes': ['Withnail & I (1987)'], 'civil-war-monument': ['Without Li\
mits (1998)'],'eugene-register-the-newspaper': ['Without Limits (1998)'], 'hayward-field': ['Wit\
hout Limits (1998)'], 'reference-to-jim-ryan': ['Without Limits (1998)'], 'reference-to-n-sync':\
['Without Me (2002) (V)'], 'compensating': ['Without a Compass (2015)'], 'mid-life-crisis': ['Wi\
thout a Compass (2015)'], 'airplane-highjacker': ['Without a Paddle (2004)'], 'canoe-christening\
': ['Without a Paddle (2004)'], 'drug-plantation': ['Without a Paddle (2004)'], 'four-wheeler-ex\
plosion': ['Without a Paddle (2004)']}
    >>> find_films_with_keywords(keywords,2)
    [('Without Limits (1998)', 4), ('Without a Paddle (2004)', 4)]
    >>> find_films_with_keywords(keywords,0)
    []
    """
    temp={}
    for key in film_keywords:
        for keyword in film_keywords[key]:
            temp.setdefault(keyword,0)
            temp[keyword]+=1
    temp=sorted(temp.items(),key=lambda x:(-x[1],x[0]))
    return [(val) for key,val in enumerate(temp) if key<num_of_films]

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
