def int32_to_ip(int32):
    return ".".join(str(int32 >> i & 255) for i in (24, 16, 8, 0))
