def convert_prefix_ip():
    prefix = int(input("Enter prefix :"))
    mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF;

    print"%lu.%lu.%lu.%lu\n"% (mask >> 24, (mask >> 16) & 0xFF, (mask >> 8) & 0xFF, mask & 0xFF)

convert_prefix_ip()
