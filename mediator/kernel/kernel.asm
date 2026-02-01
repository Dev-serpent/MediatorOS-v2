; Kernel entry point for MediatorOS
bits 32

section .text
    ; Multiboot header
    align 4
    dd 0x1BADB002            ; magic
    dd 0x00                  ; flags
    dd - (0x1BADB002 + 0x00) ; checksum

extern main
global start
start:
    call main
    hlt