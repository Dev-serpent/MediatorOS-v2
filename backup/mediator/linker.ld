/*
    linker.ld
*/
OUTPUT_FORMAT(elf32-i386)
ENTRY(start)

PHDRS
{
    text PT_LOAD FLAGS(5); /* R-X */
    data PT_LOAD FLAGS(6); /* RW- */
}

SECTIONS
{
    . = 1M;

    .text : {
        *(.text)
    } :text

    .rodata : {
        *(.rodata*)
    } :text

    .data : {
        *(.data)
    } :data

    .bss : {
        *(.bss)
    } :data
}