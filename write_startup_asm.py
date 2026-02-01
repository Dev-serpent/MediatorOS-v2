import os

assembly_content = """
; startup.asm for i686-elf MicroPython port

; Multiboot header for GRUB
MBOOT_PAGE_ALIGN    equ 1<<0
MBOOT_MEM_INFO      equ 1<<1
MBOOT_AOUT_KLUDGE   equ 1<<16
MBOOT_HEADER_MAGIC  equ 0x1BADB002
MBOOT_HEADER_FLAGS  equ MBOOT_PAGE_ALIGN | MBOOT_MEM_INFO | MBOOT_AOUT_KLUDGE
MBOOT_CHECKSUM      equ -(MBOOT_HEADER_MAGIC + MBOOT_HEADER_FLAGS)

section .multiboot
    dd MBOOT_HEADER_MAGIC
    dd MBOOT_HEADER_FLAGS
    dd MBOOT_CHECKSUM

    ; These are required but not used for now
    dd 0x0
    dd 0x0
    dd 0x0
    dd 0x0
    dd 0x0

; Entry point from GRUB (multiboot specification)
section .text
global start
extern mp_main ; MicroPython's main function

start:
    ; Disable interrupts
    cli

    ; Setup GDT (Global Descriptor Table) - simplified for bare minimum
    ; For a full OS, this would be more elaborate.
    lgdt [gdt_ptr]

    ; Enable protected mode
    mov eax, cr0
    or eax, 0x1
    mov cr0, eax

    ; Far jump to flush segment registers and enter protected mode
    jmp CODE_SEG:protected_mode_start

protected_mode_start:
    ; Setup segment registers
    mov ax, DATA_SEG
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax

    ; Setup stack
    mov esp, stack_top

    ; Clear BSS section
    ; The linker script will define _sbss and _ebss
    mov edi, _sbss
    mov ecx, _ebss
    sub ecx, edi
    shr ecx, 2            ; Divide by 4 for dword count
    xor eax, eax
    cld                   ; Clear direction flag for stosd
    rep stosd             ; Fill BSS with zeros

    ; Call MicroPython's main function
    call mp_main

    ; If mp_main returns, halt
    cli
    hlt

; Global Descriptor Table
section .data
gdt_start:
    ; Null descriptor
    dq 0x0

; Code Segment Descriptor
CODE_SEG equ gdt_code - gdt_start
gdt_code:
    dw 0xFFFF         ; Limit (bits 0-15)
    dw 0x0            ; Base (bits 0-15)
    db 0x0            ; Base (bits 16-23)
    db 10011010b      ; Access Byte (Present, Privl 0, Executable, Non-conforming, Read/Write, Accessed)
    db 11001111b      ; Flags (Granularity 4KB, 32-bit, Limit 16-19)
    db 0x0            ; Base (bits 24-31)

; Data Segment Descriptor
DATA_SEG equ gdt_data - gdt_start
gdt_data:
    dw 0xFFFF         ; Limit (bits 0-15)
    dw 0x0            ; Base (bits 0-15)
    db 0x0            ; Base (bits 16-23)
    db 10010010b      ; Access Byte (Present, Privl 0, R/W, Expand-down, Not accessed)
    db 11001111b      ; Flags (Granularity 4KB, 32-bit, Limit 16-19)
    db 0x0            ; Base (bits 24-31)

gdt_end:

gdt_ptr:
    dw gdt_end - gdt_start - 1 ; GDT Limit
    dd gdt_start               ; GDT Base

section .bss
    resb 8192 ; 8KB for initial stack
stack_top:
"

file_path = "/home/Dhruv/cross-compiler/micropython/ports/i686-elf/startup.asm"
temp_script_path = "/home/Dhruv/Documents/Projects/MediatorOS-0.12/write_startup_asm.py"

with open(temp_script_path, "w") as f:
    f.write(f"with open('{file_path}', 'w') as f:\n")
    f.write(f"    f.write({repr(assembly_content)})
")
