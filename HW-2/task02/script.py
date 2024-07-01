#!/usr/bin/env python3

import sys

arr = [0x68, 0x11, 0x42, 0x4c, 0x39, 3, 0x5a, 0x2a, 0, 0, 0x11, 0x53, 0x5d, 0x54, 0x41, 4, 0x1c, 0x3e, 0x24, 0x28, 0x26, 0xe, 0x3c, 0x4d, 0x18, 0x5c, 0x3e, 0x52, 0x51, 0x27, 0] # 0x270F

def isInvertable(i):
    try:
        pow(i, -1, 101)
        return True
    except Exception as e:
        return False

def handle0(pos):
    if(pos == len(arr) - 1):
        return 0
    # printable chars
    for i in range(33, 127):
        if(isInvertable(i)):
            return i
    return 0


def main():
    s = bytearray([0x68])
    prev = 0x68
    print("len(arr): ", len(arr) - 1)
    for i in range(1, len(arr)):
        print(i, '; (', prev, ' * x) mod 101 = ', arr[i], end='; ')
        if(prev % 101 == 0):
            prev = handle0(i)
        else:
            prev = (pow(prev, -1, 101) * arr[i]) % 101
            # if(prev == 0):
            #     prev = 101
        print('( ', s[-1], ' * ', chr(prev), ') mod 101 = ', arr[i])
        s.append(prev)
    sys.stdout.buffer.write(bytes(s))

if __name__=="__main__":
    main()

