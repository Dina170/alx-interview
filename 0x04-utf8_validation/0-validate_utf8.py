"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    count = 0
    bin_data = [bin(d)[2:].zfill(8) for d in data]

    for d in bin_data:
        if count == 0:
            if d[:3] == '110':
                count = 1
            elif d[:4] == '1110':
                count = 2
            elif d[:5] == '11110':
                count = 3
            elif d[0] != '0':
                return False
        else:
            if d[:2] != '10':
                return False
            count = count - 1
    return count == 0
