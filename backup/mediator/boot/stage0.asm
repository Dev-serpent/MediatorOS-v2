; Stage 0 Bootloader for MediatorOS
[org 0x7c00]
bits 16

start:
    ; Setup segment registers
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7c00

    ; Print loading message
    mov si, loading_msg
    call print_string

    ; Load Stage 1 from disk
    mov ah, 0x02        ; BIOS read sector function
    mov al, 1           ; Number of sectors to read
    mov ch, 0           ; Cylinder index
    mov cl, 2           ; Sector number
    mov dh, 0           ; Head number
    mov bx, 0x8000      ; Buffer to load to
    int 0x13
    jc read_error

    ; Jump to Stage 1
    jmp 0x8000:0x0000

print_string:
    lodsb
    or al, al
    jz .done
    mov ah, 0x0e
    int 0x10
    jmp print_string
.done:
    ret

read_error:
    mov si, error_msg
    call print_string
    hlt

loading_msg db 'Loading MediatorOS...', 13, 10, 0
error_msg db 'Disk read error!', 13, 10, 0

times 510-($-$$) db 0
dw 0xaa55
