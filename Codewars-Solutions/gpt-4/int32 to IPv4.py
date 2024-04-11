def int32_to_ip(int32):
    # Convert the int32 to a 32 bit binary string
    bin_str = format(int32, "032b")
    # Split the binary string into 4 octets
    octets = [bin_str[i : i + 8] for i in range(0, len(bin_str), 8)]
    # Convert each binary octet to decimal and join them with '.'
    return ".".join(str(int(octet, 2)) for octet in octets)
