import math

def dioph_solver(z_max):
    solutions = []
    total_solutions = 0
    max_z = 0
    for z in range(4, z_max + 1):
        y_max = math.floor(math.sqrt((z * z * z) / 3))
        for y in range(1, y_max + 1):
            x_squared = z ** 3 - 3 * y ** 2
            x = int(math.isqrt(x_squared))
            if x * x == x_squared and x > 0 and x * x + 3 * y * y == z * z * z:
                total_solutions += 1
                solutions.append([x, y, z])
                max_z = max(max_z, z)

    solutions = [s for s in solutions if s[2] == max_z]
    solutions.sort(key=lambda x: (x[0] + x[1] + x[2], -x[0]))
    return [total_solutions, solutions]