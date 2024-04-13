def encrypt(s, n):
    if not s or n <= 0:
        return s
    for _ in range(n):
        s = s[1::2] + s[0::2]
    return s


def decrypt(s, n):
    if not s or n <= 0:
        return s
    for _ in range(n):
        half = len(s) // 2
        evens = s[:half]
        odds = s[half:]
        s = "".join(
            odds[i : i + 1] + evens[i : i + 1] for i in range(half + len(s) % 2)
        )
    return s
