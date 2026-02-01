import os

linker_script_content = """
/* A custom linker script for i686-elf bare-metal */
ENTRY(start)

SECTIONS
{
    /* The start of the .text section is at 1MB, a common choice to avoid GRUB and BIOS areas */
    . = 0x100000;

    .text :
    {
        *(.multiboot)   /* Multiboot header */
        *(.text)        /* All code sections */
        *(.text.*)
        . = ALIGN(0x1000); /* Align to 4KB page boundary */
    }

    .rodata :
    {
        *(.rodata)      /* Read-only data */
        *(.rodata.*)
        . = ALIGN(0x1000);
    }

    .data :
    {
        *(.data)        /* Initialized data */
        *(.data.*)
        . = ALIGN(0x1000);
    }

    .bss :
    {
        *(.bss)         /* Uninitialized data */
        *(.bss.*)
        *(COMMON)
        . = ALIGN(0x1000);
    }

    /* Heap and stack can be placed here, though a full memory manager might allocate dynamically */
    . = ALIGN(0x1000);
    _end = .; /* Mark the end of the kernel */

    /* The .comment section (compiler info) */
    /DISCARD/ : { *(.comment) }
}
"""

file_path = "/home/Dhruv/cross-compiler/micropython/ports/i686-elf/i686-elf.ld"

with open(file_path, "w") as f:
    f.write(linker_script_content)

print(f"Successfully wrote linker script to {file_path}")
