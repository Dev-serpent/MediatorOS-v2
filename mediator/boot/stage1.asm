; Stage 1 Bootloader for MediatorOS
bits 16

start:
    ; Enable A20 line
    in al, 0x92
    or al, 2
    out 0x92, al

    ; Switch to protected mode
    lgdt [gdt_descriptor]
    mov eax, cr0
    or eax, 1
    mov cr0, eax
    jmp 0x08:protected_mode

bits 32
protected_mode:
    ; Setup segment registers for protected mode
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov esp, 0x90000

    ; Call the C kernel
    call 0x100000

    ; Hang
    cli
    hlt

gdt_start:
    ; Null descriptor
    dq 0
    ; Code segment
    dw 0xffff       ; limit
    dw 0            ; base
    db 0            ; base
    db 10011010b    ; access
    db 11001111b    ; granularity
    db 0            ; base
    ; Data segment
    dw 0xffff
    dw 0
    db 0
    db 10010010b
    db 11001111b
    db 0
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start
