def dbl_linear(n):
    u = [1]  # Initialize the sequence with the first element
    i, j = 0, 0  # Pointers to keep track of the next elements to be added

    for _ in range(n):
        # Get the next two elements to be added
        x2 = 2 * u[i] + 1
        x3 = 3 * u[j] + 1

        # Add the smaller of the two elements to the sequence, and increment the corresponding pointer
        if x2 <= x3:
            u.append(x2)
            i += 1
            if x3 == x2:
                j += 1  # Increment j as well if x3 is also in the sequence
        else:
            u.append(x3)
            j += 1
            if x2 == x3:
                i += 1  # Increment i as well if x2 is also in the sequence

    return u[n]