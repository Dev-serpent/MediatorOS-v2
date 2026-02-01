# Makefile for MediatorOS

# Programs
export PREFIX=$(HOME)/cross-compiler/opt
export TARGET=i686-elf
export PATH:=$(PREFIX)/bin:$(PATH)

ASM = nasm
CC = i686-elf-gcc
AR = i686-elf-ar
LD = i686-elf-ld

# Directories
BUILD_DIR = build
SRC_DIR = .
ISO_DIR = $(BUILD_DIR)/iso_root
MICROPYTHON_DIR = ../micropython/ports/mediator

# Source files
KERNEL_C = $(SRC_DIR)/kernel/kernel.c
KERNEL_ASM = $(SRC_DIR)/kernel/kernel.asm
LINKER_LD = $(SRC_DIR)/linker.ld
LIBC_C = $(wildcard $(SRC_DIR)/libc/*.c)
LIBC_OBJS = $(patsubst $(SRC_DIR)/libc/%.c, $(BUILD_DIR)/libc/%.o, $(LIBC_C))
LIBC_A = $(BUILD_DIR)/libc.a
MICROPYTHON_A = $(MICROPYTHON_DIR)/build/libmicropython.a

# Build files
KERNEL_O = $(BUILD_DIR)/kernel.o
KERNEL_ASM_O = $(BUILD_DIR)/kernel_asm.o
KERNEL_BIN = $(BUILD_DIR)/kernel.bin
ISO_FILE = mediator.iso

# Flags
CFLAGS = -m32 -ffreestanding -O2 -g -Wall -Wextra -I$(SRC_DIR)/libc/include -I../micropython
ASFLAGS = -f elf32
LDFLAGS = -m elf_i386 -T $(LINKER_LD)
ARFLAGS = rcs

.PHONY: all clean iso run

all: $(KERNEL_BIN)

$(MICROPYTHON_A):
	$(MAKE) -C $(MICROPYTHON_DIR)

$(KERNEL_BIN): $(KERNEL_ASM_O) $(KERNEL_O) $(LIBC_A) $(MICROPYTHON_A)
	$(LD) $(LDFLAGS) -o $@ $(KERNEL_ASM_O) $(KERNEL_O) $(LIBC_A) $(MICROPYTHON_A)

$(KERNEL_ASM_O): $(KERNEL_ASM)
	mkdir -p $(BUILD_DIR)
	$(ASM) $(ASFLAGS) -o $@ $<

$(KERNEL_O): $(KERNEL_C)
	mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -c -o $@ $<

$(LIBC_A): $(LIBC_OBJS)
	$(AR) $(ARFLAGS) $@ $^

$(BUILD_DIR)/libc/%.o: $(SRC_DIR)/libc/%.c
	mkdir -p $(BUILD_DIR)/libc
	$(CC) $(CFLAGS) -c -o $@ $<

iso: all
	mkdir -p $(ISO_DIR)/boot/grub
	cp $(KERNEL_BIN) $(ISO_DIR)/boot/
	cp $(SRC_DIR)/iso/boot/grub/grub.cfg $(ISO_DIR)/boot/grub/
	grub-mkrescue -o $(ISO_FILE) $(ISO_DIR)

run: iso
	qemu-system-x86_64 -cdrom $(ISO_FILE)

clean:
	rm -rf $(BUILD_DIR) $(ISO_FILE)
	$(MAKE) -C $(MICROPYTHON_DIR) clean