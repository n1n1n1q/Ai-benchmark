def dbl_linear(n):
    u = [1]  # Initialize the sequence with the first element
    i, j = 0, 0  # Pointers to keep track of the next elements to be added

    while len(u) <= n:
        x2 = 2 * u[i] + 1
        x3 = 3 * u[j] + 1

        if x2 <= x3:
            u.append(x2)
            i += 1
            if x2 == x3:
                j += 1
        else:
            u.append(x3)
            j += 1
            if x2 == x3:
                i += 1

    return u[n]
