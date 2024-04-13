import math

def dioph_solver(z_max):
    max_z = 0
    solutions = []
    total_solutions = 0
    for z in range(1, z_max + 1):
        limit_y = math.floor(math.sqrt((z * z * z) / 3))
        for y in range(1, limit_y + 1):
            diff = z * z * z - 3 * y * y
            sqrt_diff = int(math.sqrt(diff))
            if sqrt_diff * sqrt_diff == diff:
                x = sqrt_diff
                if x > 0:
                    if z > max_z:
                        max_z = z
                        solutions = []
                    solutions.append([x, y, z])
                    total_solutions += 1

    # Sort solutions by x + y + z increasing, then by x decreasing
    sorted_solutions = sorted(solutions, key=lambda s: (sum(s), -s[0]))

    return [total_solutions, sorted_solutions]

# Test case
print(dioph_solver(66))  # Output: [43, [[256, 256, 64]]]
