def count_patterns_from(firstPoint, length):

    # Mapping of points to their coordinates on a 3x3 grid

    point_pos = {

        'A': (0, 0), 'B': (0, 1), 'C': (0, 2),

        'D': (1, 0), 'E': (1, 1), 'F': (1, 2),

        'G': (2, 0), 'H': (2, 1), 'I': (2, 2)

    }

    

    # Points that require to cross over certain other points to be reached

    cross_over_points = {

        ('A', 'C'): 'B',

        ('C', 'A'): 'B',

        ('B', 'H'): 'E',

        ('H', 'B'): 'E',

        ('D', 'F'): 'E',

        ('F', 'D'): 'E',

        ('G', 'I'): 'H',

        ('I', 'G'): 'H',

        ('A', 'I'): 'E',

        ('I', 'A'): 'E',

        ('C', 'G'): 'E',

        ('G', 'C'): 'E',

        ('A', 'G'): 'D',

        ('G', 'A'): 'D',

        ('C', 'I'): 'F',

        ('I', 'C'): 'F'

    }



    # Recursive function to count patterns

    def search_patterns(visited, current_point, remaining_length):

        if remaining_length == 0:

            return 1

        count = 0

        for point in point_pos:

            if point not in visited:

                # Check if the point is directly reachable or if we need to cross over another point

                if (current_point, point) not in cross_over_points or cross_over_points[(current_point, point)] in visited:

                    count += search_patterns(visited | {point}, point, remaining_length - 1)

        return count



    # Initialize the pattern search from the starting point

    return search_patterns({firstPoint}, firstPoint, length - 1)
