#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
from sys import stdin


def print_statistics():
    """prints some statistics"""
    print(f"File size: {fileSize}")
    for k in sorted(status_codes.keys()):
        if status_codes[k] != 0:
            print(f"{k}: {status_codes[k]}")


if __name__ == "__main__":
    count = 0
    fileSize = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in stdin:
            try:
                data = line.split()
                fileSize += int(data[-1])
                status_code = data[-2]
                if status_code in status_codes.keys():
                    status_codes[status_code] += 1
            except:
                pass
            count += 1
            if count % 10 == 0:
                print_statistics()
        print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise
