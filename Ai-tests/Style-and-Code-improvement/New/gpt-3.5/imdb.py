"""
Keyword processor
"""

from collections import Counter

def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    Returns set of keywords for a certain film.
    >>> keywords = {'unwashed-dishes': ['Withnail & I (1987)'],
    ...             'civil-war-monument': ['Without Limits (1998)'],
    ...             'eugene-register-the-newspaper': ['Without Limits (1998)'],
    ...             'hayward-field': ['Without Limits (1998)'],
    ...             'reference-to-jim-ryan': ['Without Limits (1998)'],
    ...             'reference-to-n-sync': ['Without Me (2002) (V)'],
    ...             'compensating': ['Without a Compass (2015)'],
    ...             'mid-life-crisis': ['Without a Compass (2015)'],
    ...             'airplane-highjacker': ['Without a Paddle (2004)'],
    ...             'canoe-christening': ['Without a Paddle (2004)'],
    ...             'drug-plantation': ['Without a Paddle (2004)'],
    ...             'four-wheeler-explosion': ['Without a Paddle (2004)']}
    >>> find_film_keywords(keywords, 'Without a Paddle (2004)') == \
        {'drug-plantation', 'canoe-christening', 'four-wheeler-explosion', 'airplane-highjacker'}
    True
    """
    return {keyword for keyword, films in film_keywords.items() if film_name in films}


def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list:
    """
    Returns descending list of {num_of_films} tuples (film name, amount of keywords)
    >>> keywords = {'unwashed-dishes': ['Withnail & I (1987)'],
    ...             'civil-war-monument': ['Without Limits (1998)'],
    ...             'eugene-register-the-newspaper': ['Without Limits (1998)'],
    ...             'hayward-field': ['Without Limits (1998)'],
    ...             'reference-to-jim-ryan': ['Without Limits (1998)'],
    ...             'reference-to-n-sync': ['Without Me (2002) (V)'],
    ...             'compensating': ['Without a Compass (2015)'],
    ...             'mid-life-crisis': ['Without a Compass (2015)'],
    ...             'airplane-highjacker': ['Without a Paddle (2004)'],
    ...             'canoe-christening': ['Without a Paddle (2004)'],
    ...             'drug-plantation': ['Without a Paddle (2004)'],
    ...             'four-wheeler-explosion': ['Without a Paddle (2004)']}
    >>> find_films_with_keywords(keywords, 2)
    [('Without Limits (1998)', 4), ('Without a Paddle (2004)', 4)]
    >>> find_films_with_keywords(keywords, 0)
    []
    """
    film_counts = Counter(film for films in film_keywords.values() for film in films)
    sorted_films = sorted(film_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_films[:num_of_films]

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
